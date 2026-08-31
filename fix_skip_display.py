file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 移除skipMode元素的内联样式display:none
old_skip = '''  <!-- 不考题列表 -->
  <div class="list-mode" id="skipMode" style="display:none">'''

new_skip = '''  <!-- 不考题列表 -->
  <div class="list-mode" id="skipMode">'''

if old_skip in content:
    content = content.replace(old_skip, new_skip)
    print("skipMode元素的内联样式已移除")
else:
    print("找不到skipMode元素")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("修复完成")
