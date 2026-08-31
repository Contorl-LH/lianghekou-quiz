file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 在Supabase初始化代码之后，</script>之前添加init()调用
old_code = '''// 页面加载时初始化Supabase
if (typeof supabase !== 'undefined') {
  initSupabase();
}
</script>'''

new_code = '''// 页面加载时初始化Supabase
if (typeof supabase !== 'undefined') {
  initSupabase();
}

// 初始化题库
init();
</script>'''

if old_code in content:
    content = content.replace(old_code, new_code)
    print("init()调用已添加")
else:
    print("找不到要替换的内容")
    # 尝试查找其他位置
    idx = content.find('// 页面加载时初始化Supabase')
    if idx != -1:
        print(f"找到Supabase初始化代码在位置: {idx}")
        print(content[idx:idx+200])

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("修复完成")
