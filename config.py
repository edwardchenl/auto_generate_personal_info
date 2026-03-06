# -*- coding: utf-8 -*-  # 声明编码格式，解决中文识别问题

# ---------------------- 1. 预设：100个常见姓氏-拼音映射表 ----------------------
surname_pinyin_map = {
    "李": "Li", "王": "Wang", "张": "Zhang", "刘": "Liu", "陈": "Chen",
    "杨": "Yang", "赵": "Zhao", "黄": "Huang", "周": "Zhou", "吴": "Wu",
    "徐": "Xu", "孙": "Sun", "马": "Ma", "朱": "Zhu", "胡": "Hu",
    "林": "Lin", "郭": "Guo", "何": "He", "高": "Gao", "罗": "Luo",
    "郑": "Zheng", "梁": "Liang", "谢": "Xie", "宋": "Song", "唐": "Tang",
    "许": "Xu", "韩": "Han", "冯": "Feng", "邓": "Deng", "曹": "Cao",
    "彭": "Peng", "薛": "Xue", "肖": "Xiao", "田": "Tian", "董": "Dong",
    "潘": "Pan", "袁": "Yuan", "蔡": "Cai", "蒋": "Jiang", "余": "Yu",
    "于": "Yu", "杜": "Du", "叶": "Ye", "程": "Cheng", "魏": "Wei",
    "苏": "Su", "吕": "Lv", "丁": "Ding", "任": "Ren", "卢": "Lu",
    "姚": "Yao", "沈": "Shen", "钟": "Zhong", "姜": "Jiang", "崔": "Cui",
    "谭": "Tan", "陆": "Lu", "汪": "Wang", "范": "Fan", "金": "Jin",
    "石": "Shi", "廖": "Liao", "贾": "Jia", "夏": "Xia", "韦": "Wei",
    "傅": "Fu", "方": "Fang", "白": "Bai", "邹": "Zou", "孟": "Meng",
    "熊": "Xiong", "秦": "Qin", "邱": "Qiu", "江": "Jiang", "尹": "Yin",
    "闫": "Yan", "段": "Duan", "雷": "Lei", "侯": "Hou", "龙": "Long",
    "史": "Shi", "陶": "Tao", "黎": "Li", "贺": "He", "顾": "Gu",
    "毛": "Mao", "郝": "Hao", "龚": "Gong", "邵": "Shao", "万": "Wan",
    "钱": "Qian", "严": "Yan", "武": "Wu", "孔": "Kong", "向": "Xiang",
    "常": "Chang", "汤": "Tang", "温": "Wen", "康": "Kang", "施": "Shi",
    "牛": "Niu", "洪": "Hong", "喻": "Yu", "庞": "Pang", "樊": "Fan",
    "兰": "Lan", "殷": "Yin", "翟": "Zhai", "安": "An", "颜": "Yan"
}

# 提取100个姓氏列表
surnames = list(surname_pinyin_map.keys())

# ---------------------- 2. 预设：分性别名字用字-拼音映射表 ----------------------
# 男性倾向名字用字
male_chars = {
    "轩": "Xuan", "宇": "Yu", "哲": "Zhe", "豪": "Hao", "辰": "Chen",
    "睿": "Rui", "泽": "Ze", "思": "Si", "浩": "Hao", "明": "Ming",
    "言": "Yan", "墨": "Mo", "恒": "Heng", "谦": "Qian", "熙": "Xi",
    "博": "Bo", "文": "Wen", "俊": "Jun", "诚": "Cheng", "嘉": "Jia",
    "子": "Zi", "凡": "Fan", "安": "An", "阳": "Yang", "星": "Xing",
    "旭": "Xu", "晨": "Chen", "朗": "Lang", "杰": "Jie", "涛": "Tao",
    "超": "Chao", "强": "Qiang", "伟": "Wei", "刚": "Gang", "勇": "Yong",
    "毅": "Yi", "信": "Xin", "友": "You", "智": "Zhi", "礼": "Li",
    "义": "Yi", "德": "De", "昌": "Chang", "宁": "Ning", "平": "Ping",
    "昊": "Hao", "皓": "Hao", "弘": "Hong", "宏": "Hong", "景": "Jing",
    "靖": "Jing", "然": "Ran", "霖": "Lin", "彤": "Tong", "峻": "Jun",
    "凯": "Kai", "航": "Hang", "洋": "Yang", "烁": "Shuo", "翊": "Yi",
    "麒": "Qi", "麟": "Lin", "潇": "Xiao", "钒": "Fan", "烨": "Ye"
}

# 女性倾向名字用字
female_chars = {
    "涵": "Han", "瑶": "Yao", "妍": "Yan", "若": "Ruo", "欣": "Xin",
    "梓": "Zi", "瑾": "Jin", "萌": "Meng", "琪": "Qi", "曦": "Xi",
    "语": "Yu", "桐": "Tong", "怡": "Yi", "萱": "Xuan", "诺": "Nuo",
    "亦": "Yi", "悦": "Yue", "玥": "Yue", "昕": "Xin", "雯": "Wen",
    "雅": "Ya", "诗": "Shi", "梦": "Meng", "琦": "Qi", "琳": "Lin",
    "玲": "Ling", "菲": "Fei", "芳": "Fang", "友": "You", "善": "Shan",
    "仁": "Ren", "慧": "Hui", "福": "Fu", "禄": "Lu", "寿": "Shou",
    "喜": "Xi", "顺": "Shun", "睦": "Mu", "静": "Jing", "柔": "Rou",
    "婉": "Wan", "淑": "Shu", "秀": "Xiu", "丽": "Li", "沁": "Qin",
    "芮": "Rui", "珂": "Ke", "诺": "Nuo", "涵": "Han", "垚": "Yao"
}

# 中性名字用字（男女通用）
neutral_chars = {
    "思": "Si", "明": "Ming", "嘉": "Jia", "子": "Zi", "凡": "Fan",
    "安": "An", "星": "Xing", "晨": "Chen", "宁": "Ning", "平": "Ping",
    "然": "Ran", "霖": "Lin", "彤": "Tong", "文": "Wen", "博": "Bo"
}

# 合并所有字符，供外部调用
all_chars = {**male_chars, **female_chars, **neutral_chars}