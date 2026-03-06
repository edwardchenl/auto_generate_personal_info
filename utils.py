# -*- coding: utf-8 -*-  # 声明编码格式，解决中文识别问题
import random
from datetime import datetime, timedelta
from config import surname_pinyin_map, male_chars, female_chars, neutral_chars

# ---------------------- 生成随机生日函数 ----------------------
def generate_birthday():
    """生成1990-2010年之间的随机生日，格式为YYYYMMDD"""
    # 设置起始日期和结束日期
    start_date = datetime(1990, 1, 1)
    end_date = datetime(2010, 12, 31)
    
    # 计算两个日期之间的天数差
    delta = end_date - start_date
    days_delta = random.randint(0, delta.days)
    
    # 生成随机日期
    random_date = start_date + timedelta(days=days_delta)
    
    # 格式化为YYYY-MM-DD
    return random_date.strftime("%Y%m%d")

# ---------------------- 姓名转拼音函数 ----------------------
def get_name_pinyin(full_name):
    """
    基于预设映射表生成两种拼音格式：
    1. 规范格式：姓氏拼音首字母大写 + 名字拼音首字母大写（如“李悦阳”→“Li Yueyang”）
    2. 连写格式：全部小写连在一起（如“李悦阳”→“liyueyang”）
    """
    if not full_name:
        raise ValueError("Name cannot be empty")
        
    # 拆分姓氏和名字
    surname = full_name[0]
    given_name = full_name[1:]
    
    # 从预设表获取姓氏拼音
    if surname not in surname_pinyin_map:
        raise KeyError(f"Surname '{surname}' not found in map")
    
    surname_py = surname_pinyin_map[surname]
    surname_py_lower = surname_py.lower()
    
    # 构建临时映射表以查找名字拼音
    all_char_map = {**male_chars, **female_chars, **neutral_chars}
    
    given_name_py_list = []
    for char in given_name:
        if char not in all_char_map:
            raise KeyError(f"Character '{char}' not found in map")
        given_name_py_list.append(all_char_map[char])
    
    # 处理名字拼音格式
    # 规范格式：每个字首字母大写，其余小写，然后拼接（注意：原逻辑是将所有字的拼音连起来作为一个整体处理大小写）
    # 原代码逻辑：given_name_py = ''.join([py[0] + py[1:].lower() for py in given_name_py_list])
    # 这意味着 "Wang" + "Xuan" -> "Wangxuan" (如果名字是两个字)。 
    # 让我们严格遵循原代码逻辑：
    given_name_py = ''.join([py[0] + py[1:].lower() for py in given_name_py_list])
    given_name_py_lower = ''.join([py.lower() for py in given_name_py_list])
    
    # 组合两种格式的拼音
    standard_py = f"{surname_py} {given_name_py}"
    combined_py = f"{surname_py_lower}{given_name_py_lower}"
    
    return standard_py, combined_py