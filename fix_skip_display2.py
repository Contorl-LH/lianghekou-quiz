file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 修改switchMode函数，直接设置skipMode的style.display
old_switch = '''  const skipMode = document.getElementById('skipMode');
  if (skipMode) skipMode.classList.toggle('active', mode === 'skip');'''

new_switch = '''  const skipMode = document.getElementById('skipMode');
  if (skipMode) {
    skipMode.classList.toggle('active', mode === 'skip');
    skipMode.style.display = mode === 'skip' ? 'block' : 'none';
  }'''

if old_switch in content:
    content = content.replace(old_switch, new_switch)
    print("switchMode函数已修改，直接设置skipMode的style.display")
else:
    print("找不到switchMode函数中的skipMode代码")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("修复完成")
