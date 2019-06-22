###########################
########程序包导入##########
###########################
import pandas as pd 
import numpy as np 
import math
from matplotlib import pyplot as plt 
# 自己写的函数
from self_build_function import one_hot_point_comp, one_hot_point_econ, one_hot_point_health
from self_build_function import one_hot_point_dinner, one_hot_point_lunch, one_hot_point_morning
from self_build_function import one_hot_point_rain, one_hot_point_snack, willing_to_try
from self_build_function import one_hot_female, one_hot_male
# 解决图片显示汉字问题
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] 
mpl.rcParams['axes.unicode_minus'] = False
#########################################################
########################导入结束##########################
#########################################################


# 导入处理过的数据
df = pd.read_excel('work_data.xlsx', index_col = 0)
# 是否会点外卖人数对比
df['是否会点'].groupby(df['是否会点']).count()
# 柱状图
plt.bar(sorted(df['是否会点'].unique()), df['是否会点'].groupby(df['是否会点']).count())
plt.xlabel('是否会点外卖')
plt.ylabel('人数')
plt.show()
######################################################## 结束

# 将数据样本分为会点外卖和不会点外卖
not_order_df = df[df['是否会点'] == '否']
order_df = df[df['是否会点'] == '是']
##########################################################结束


#############################################################
# 基于不点外卖的人员属性分析，性别、年级以及原因，柱状图为输出结果#
#############################################################
not_order_df['性别'].groupby(not_order_df['性别']).count()
plt.bar(sorted(not_order_df['性别'].unique()), not_order_df['性别'].groupby(not_order_df['性别']).count())
plt.xlabel('性别')
plt.ylabel('人数')
plt.show()

not_order_df['年级'].groupby(not_order_df['年级']).count()
plt.bar(sorted(not_order_df['年级'].unique()), not_order_df['年级'].groupby(not_order_df['年级']).count())
plt.xlabel('年级')
plt.ylabel('人数')
plt.show()

# 将无用列去除，将原因热点化
not_order_df_2 = not_order_df[['是否会点', '不点原因', '性别', '年级']]
not_order_df_2['卫生原因'] = not_order_df_2['不点原因'].apply(one_hot_point_health)
not_order_df_2['经济原因'] = not_order_df_2['不点原因'].apply(one_hot_point_econ)
not_order_df_2['比较麻烦'] = not_order_df_2['不点原因'].apply(one_hot_point_comp)

# 根据性别分类原因，从比例上可以看出 女生的经济原因相较于男生略大
not_order_df_2.groupby(['性别']).sum().plot.bar()
plt.show()

# 根据年级分类原因。卫生原因会因年纪上升而减少。
not_order_df_2.groupby(['年级']).sum().plot.bar()
plt.show()
#####################################################################
##############################分析结束################################
#####################################################################

#############################################################
######################### 基于点外卖分析######################
#############################################################
# 去除无用列，将时段热点化。增加列，是否愿意尝试新品（无理由）
order_df = order_df.drop(['是否会点', '不点原因'], axis = 1)
order_df['早上'] = order_df['什么时段,时间点'].apply(one_hot_point_morning)
order_df['中午'] = order_df['什么时段,时间点'].apply(one_hot_point_lunch)
order_df['晚上'] = order_df['什么时段,时间点'].apply(one_hot_point_dinner)
order_df['夜宵'] = order_df['什么时段,时间点'].apply(one_hot_point_snack)
order_df['特殊天气'] = order_df['什么时段,时间点'].apply(one_hot_point_rain)
order_df['愿意尝试新品'] = order_df['是否愿意尝试新品'].apply(willing_to_try)
order_df_new = order_df.drop('什么时段,时间点', axis = 1)

# 愿意尝试新品的主要理由为新品的吸引力，其次为折扣力度
order_df_new[order_df_new['性别'] == '女']['是否愿意尝试新品'].groupby(order_df_new['是否愿意尝试新品']).count()
order_df_new[order_df_new['性别'] == '男']['是否愿意尝试新品'].groupby(order_df_new['是否愿意尝试新品']).count()

# 年级分布, 主要集中在大四以下
order_df_new['年级'].groupby(order_df_new['年级']).count().plot.bar()
plt.xlabel('年级')
plt.ylabel('人数')
plt.show()

# 点餐时间点,性别分布
order_time_df = order_df_new[['性别', '早上', '中午', '晚上', '夜宵', '特殊天气']]
order_time_df.groupby(order_time_df['性别']).sum().plot.bar()
plt.show()
# 女生主要集中在中午，男生中午晚上比例相近。早上最少

# 点餐时间, 年级分布
order_time_grade = order_df_new[['年级', '早上', '中午', '晚上', '夜宵', '特殊天气']]
order_time_grade.groupby(order_time_grade['年级']).sum().plot.bar()
plt.show()
# 各年级分布基本一致，都已午餐为主

# 服务要求，性别、年级分布
order_day_gender = order_df_new[['性别', '口味', '价格', '卫生安全', 
'产品包装', '产品更新速度', '售后服务', '配送员服务态度', '配送效率', '配送准时率']]
order_day_gender = order_day_gender.apply(pd.to_numeric, errors = 'ignore')
order_day_gender.groupby(order_day_gender['性别']).median().plot.bar()
plt.show()
# 中位数分布图，说明至少50%的人给了打了某项分数以及以上

# boxplot强调数据分布，绿线代表中位数，方框内代表50%的数据量集中的区间
order_day_grade = order_df_new[['年级', '口味', '价格', '卫生安全', '产品包装', 
'产品更新速度', '售后服务', '配送员服务态度', '配送效率', '配送准时率']]
order_day_grade = order_day_grade.apply(pd.to_numeric, errors = 'ignore')
order_day_grade.boxplot(by = '年级')
plt.show()

# 影响力，宣传对女生有较大的影响
order_influ_gender = order_df_new[['性别','宣传是否有影响']]
order_influ_gender['男'] = order_influ_gender['性别'].apply(one_hot_male)
order_influ_gender['女'] = order_influ_gender['性别'].apply(one_hot_female)
order_influ_gender = order_influ_gender.drop('性别', axis = 1)
order_influ_gender.groupby(order_influ_gender['宣传是否有影响']).sum().plot.bar()
plt.show()

# 宣传力对于女生单独分析
influ_df = order_df_new[(order_df_new['性别'] == '女')&(order_df_new['宣传是否有影响'] == '有影响')]
influ_df = influ_df[['朋友的推荐对我选择外卖的影响', '美食类公众号的影响', '商家分发的各式传单的影响', '商家的打折优惠活动对我选择外卖的影响', '商家是否提供赠品的影响','销量排行的影响', '美团等外卖平台首页推荐的影响', '美团等外卖平台客户评价的影响']]
influ_df.columns = ['朋友', '公众号', '传单', '优惠', '赠品', '销量排行', '首页推荐', '客户评价']
influ_df = influ_df.apply(pd.to_numeric, errors = 'ignore')
influ_df.boxplot()
plt.show()