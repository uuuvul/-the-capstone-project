def one_hot_point_health(value):
    if '卫生方面' in value:
        return 1
    else:
        return 0

def one_hot_point_econ(value):
    if '经济方面' in value:
        return 1
    else:
        return 0

def one_hot_point_comp(value):
    if '麻烦' in value:
        return 1
    else:
        return 0

def one_hot_point_morning(value):
    if '早上' in value:
        return 1
    else:
        return 0

def one_hot_point_lunch(value):
    if '中午' in value:
        return 1
    else:
        return 0

def one_hot_point_dinner(value):
    if '晚上' in value:
        return 1
    else:
        return 0

def one_hot_point_snack(value):
    if '夜宵' in value:
        return 1
    else:
        return 0

def one_hot_point_rain(value):
    if '天气' in value:
        return 1
    else:
        return 0

def willing_to_try(value):
    if '不' in value:
        return 0
    else:
        return 1

def one_hot_male(value):
    if value == '男':
        return 1
    else:
        return 0

def one_hot_female(value):
    if value == '女':
        return 1
    else:
        return 0