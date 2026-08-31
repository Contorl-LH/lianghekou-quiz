file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 在导出按钮后面添加云端同步按钮
old_btn = '<button class="btn-success" onclick="openSyncModal(\'export\')">📤导出数据</button>'
new_btn = '''<button class="btn-success" onclick="openSyncModal('export')">📤导出数据</button>
  <button class="btn-secondary" onclick="openCloudSync()" style="background:linear-gradient(135deg,#667eea,#764ba2);color:white">☁️云端同步</button>'''

if old_btn in content:
    content = content.replace(old_btn, new_btn)
    print("云端同步按钮已添加")
else:
    print("找不到导出按钮")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("完成")
