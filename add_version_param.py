file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 修改引用quiz_data_final.js的方式，添加版本号参数
old_script = '<script src="quiz_data_final.js"></script>'
new_script = '<script src="quiz_data_final.js?v=20260831"></script>'

if old_script in content:
    content = content.replace(old_script, new_script)
    print("quiz_data_final.js引用已添加版本号参数")
else:
    print("找不到quiz_data_final.js引用")
    # 尝试查找
    idx = content.find('quiz_data_final.js')
    if idx != -1:
        print(f"找到在位置: {idx}")
        print(content[idx-20:idx+50])

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("修改完成")
