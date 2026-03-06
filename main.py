# -*- coding: utf-8 -*-
import random
from generator import generate_names_batch

def save_names_to_file(names_list, filename="personal_info.txt"):
    """将生成的姓名列表保存到文件"""
    with open(filename, "w", encoding="utf-8") as f:
        for idx, item in enumerate(names_list, 1):
            f.write(f"{idx} {item}\n")
    return filename

if __name__ == "__main__":
    # ================= 可配置参数 =================
    target_count = 5000   # 生成数量
    name_length = 2       # 名字长度（1, 2, 或3, 默认为2）
    gender = None         # 性别倾向 ('male', 'female', 或 None)
    output_filename = "personal_info.txt"
    # ===========================================

    # 1. 生成姓名
    generated_names = generate_names_batch(target_count, name_length, gender)
    
    if not generated_names:
        print("❌ 未生成任何数据，请检查配置。")
        exit(1)

    # 2. 保存到文件
    filename = save_names_to_file(generated_names, output_filename)
    
    # 3. 打印统计信息
    print(f"\n✅ 姓名生成成功！文件：{filename}")
    print(f"📊 关键校验结果：")
#    print(f"   - 实际使用姓氏数量：{len(surnames)}个")
    print(f"   - 生成姓名总数：{len(generated_names)}个（全部为{name_length}字名）")
    print(f"   - 输出格式：序号. 姓名 性别 规范拼音 连写拼音 生日（如“1 王宇轩 男 Wang Yuxuan wangyuxuan 19950315”）")
    
    # 验证连写拼音唯一性
    unique_pinyins = set(item.split()[3] for item in generated_names)
    print(f"   - 连写拼音唯一性：{len(unique_pinyins)}个（与姓名数量一致：{len(unique_pinyins) == len(generated_names)}）")
    
    # 统计性别比例
    male_count = sum(1 for item in generated_names if item.split()[1] == '男')
    female_count = len(generated_names) - male_count
    total = len(generated_names)
    print(f"   - 性别比例：男 {male_count}个 ({male_count/total:.1%}), 女 {female_count}个 ({female_count/total:.1%})")
    
    # 随机抽取示例
    print(f"\n   - 随机抽取8个{name_length}字名示例：")
    sample_list = random.sample(generated_names, min(8, len(generated_names)))
    for i, sample in enumerate(sample_list, 1):
        # 格式化输出以便阅读
        parts = sample.split()
        # parts: [Name, Gender, StdPy, CombPy, Birthday]
        print(f"     {i}. {parts[0]} ({parts[1]}) | {parts[2]} | {parts[4]}")