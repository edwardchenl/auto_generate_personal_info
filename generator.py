# -*- coding: utf-8 -*-
import random
from config import surnames, male_chars, female_chars, neutral_chars
from utils import generate_birthday, get_name_pinyin

# ---------------------- 生成姓名函数（支持控制名字长度和性别倾向） ----------------------
def generate_single_name(name_length=2, gender=None):
    """
    生成单个指定长度和性别倾向的姓名
    
    参数:
    name_length: 名字长度（1, 2, 或3），默认为2
    gender: 性别倾向（'male', 'female' 或 None），None表示无特定倾向

    返回:
    tuple: (全名, 性别标签)
    """

    # 随机选择姓氏
    surname = random.choice(surnames)
    
    # 根据性别选择不同的字符集
    if gender == 'male':
        char_set = {**male_chars,** neutral_chars}  # 男性+中性字
        gender_label = '男'
    elif gender == 'female':
        char_set = {**female_chars,** neutral_chars}  # 女性+中性字
        gender_label = '女'
    else:
        # 无特定性别倾向，随机选择性别和对应字符集
        if random.random() < 0.5:
            char_set = {**male_chars,** neutral_chars}
            gender_label = '男'
        else:
            char_set = {**female_chars,** neutral_chars}
            gender_label = '女'
    
    chars = list(char_set.keys())
    
    # 生成指定长度的名字，避免连续重复字
    name_chars = []
    prev_char = None
    for _ in range(name_length):
        # 随机选择一个字符，避免与前一个字符相同
        char = random.choice(chars)
        while char == prev_char:
            char = random.choice(chars)
        name_chars.append(char)
        prev_char = char
    
    # 组合成全名
    full_name = surname + ''.join(name_chars)

    return full_name, gender_label

# ---------------------- 批量生成姓名主程序 ----------------------
def generate_names_batch(target_count=5000, name_length=2, gender=None):
    """
    批量生成指定数量、长度和性别倾向的姓名
    
    参数:
    target_count: 生成数量
    name_length: 名字长度（1, 2, 或3）
    gender: 性别倾向（'male', 'female' 或 None）

    返回:
    list: 排序后的生成结果列表
    """
    generated_names_with_pinyin = set()  # 存储"姓名 性别 规范拼音 连写拼音 生日"
    used_combined_pinyins = set()  # 用于确保连写拼音不重复
    
    print(f"正在生成{target_count}个{name_length}字名...")
    
    safety_counter = 0
    max_safety_attempts = target_count * 10 # 防止死循环
    
    while len(generated_names_with_pinyin) < target_count:
        safety_counter += 1
        if safety_counter > max_safety_attempts:
            print("警告：达到最大尝试次数，可能无法生成更多不重复的名字。")
            break
            
        # 生成姓名和性别标签
        full_name, gender_label = generate_single_name(name_length, gender)
        
        # 生成两种格式的拼音
        try:
            standard_pinyin, combined_pinyin = get_name_pinyin(full_name)
        except KeyError as e:
            # 理论上不会发生，因为字符集来自config
            print(f"警告：字符{e}未在拼音映射表中找到，已跳过")
            continue
        
        # 生成随机生日
        birthday = generate_birthday()
        
        # 检查连写拼音是否已使用，确保不重复
        if combined_pinyin not in used_combined_pinyins:
            name_with_py = f"{full_name} {gender_label} {standard_pinyin} {combined_pinyin} {birthday}"
            generated_names_with_pinyin.add(name_with_py)
            used_combined_pinyins.add(combined_pinyin)
            
            # 显示进度
            if len(generated_names_with_pinyin) % 500 == 0:
                print(f"已生成{len(generated_names_with_pinyin)}/{target_count}个{name_length}字名")
    
    return sorted(generated_names_with_pinyin, key=lambda x: x.split()[2])