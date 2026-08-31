file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 在renderPlanQuestion函数中添加更新planSkipBtn状态的代码
old_wrong_btn = '''  const wrongBtn = document.getElementById('planWrongBtn');
  const isWrong = wrongBook.includes(q.id);
  if (wrongBtn) {
    wrongBtn.classList.toggle('active', isWrong);
    wrongBtn.innerHTML = isWrong ? '❌ 已标记' : '❌ 标记错题';
  }

  // 设置底部导航按钮启用/禁用状态（基于筛选后的列表）'''

new_wrong_skip_btn = '''  const wrongBtn = document.getElementById('planWrongBtn');
  const isWrong = wrongBook.includes(q.id);
  if (wrongBtn) {
    wrongBtn.classList.toggle('active', isWrong);
    wrongBtn.innerHTML = isWrong ? '❌ 已标记' : '❌ 标记错题';
  }

  const skipBtn = document.getElementById('planSkipBtn');
  const isSkipped = skipBook.includes(q.id);
  if (skipBtn) {
    skipBtn.classList.toggle('active', isSkipped);
    skipBtn.innerHTML = isSkipped ? '✅ 恢复考题' : '🚫 不考题';
  }

  // 设置底部导航按钮启用/禁用状态（基于筛选后的列表）'''

if old_wrong_btn in content:
    content = content.replace(old_wrong_btn, new_wrong_skip_btn)
    print("renderPlanQuestion函数已添加更新planSkipBtn状态的代码")
else:
    print("找不到目标代码")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("修改完成")
