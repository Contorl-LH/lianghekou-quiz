file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 在Supabase代码结束后，HTML注释前添加</script>
old_text = '''// 页面加载时初始化Supabase
if (typeof supabase !== 'undefined') {
  initSupabase();
}




<!-- 确认操作弹窗 -->'''

new_text = '''// 页面加载时初始化Supabase
if (typeof supabase !== 'undefined') {
  initSupabase();
}
</script>

<!-- 确认操作弹窗 -->'''

if old_text in content:
    content = content.replace(old_text, new_text)
    print("</script>标签已添加")
else:
    print("找不到要替换的内容")
    # 尝试查找其他位置
    idx = content.find('<!-- 确认操作弹窗 -->')
    if idx != -1:
        print(f"确认操作弹窗在位置: {idx}")
        print(content[idx-100:idx+50])

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("修复完成")
