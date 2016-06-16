#coding:utf8
'''
@author: chin
@date: 2016年6月16日
'''

from utils.fpm import FpGrowthMethod

fpgrowth_method = FpGrowthMethod()

# fpgrowth_method.load_data_from_file(filename = "../data/test-1.txt")
# fpgrowth_method.gen_frequent(min_supp=3)


fpgrowth_method.load_data_from_file(filename = "../../srcdata/design/plugin_no.txt")
fpgrowth_method.gen_frequent(min_supp=100)

print len(fpgrowth_method.frequent_list)
print len(fpgrowth_method.support_dict)

# fpgrowth_method.show_frequent()
# print fpgrowth_method.frequent_list
# print fpgrowth_method.support_dict
# 
fpgrowth_method.gen_associated_rules(min_conf=0.7)
fpgrowth_method.show_rules()