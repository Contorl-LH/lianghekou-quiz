file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 修改toggleSkipMark函数，标记后重新过滤filteredQuestions
old_toggle = '''function toggleSkipMark() {
  const q = filteredQuestions[currentIndex];
  const idx = skipBook.indexOf(q.id);
  if (idx > -1) {
    skipBook.splice(idx, 1);
  } else {
    skipBook.push(q.id);
  }
  saveSkip();
  updateSkipButton();
  // 如果标记为不考题，自动跳转到下一题
  if (idx === -1 && currentIndex < filteredQuestions.length - 1) {
    setTimeout(() => nextQuestion(), 300);
  }
}'''

new_toggle = '''function toggleSkipMark() {
  const q = filteredQuestions[currentIndex];
  const wasSkipped = skipBook.includes(q.id);
  
  if (wasSkipped) {
    // 恢复考题：从skipBook中移除
    const idx = skipBook.indexOf(q.id);
    if (idx > -1) skipBook.splice(idx, 1);
  } else {
    // 标记为不考题：添加到skipBook
    skipBook.push(q.id);
  }
  saveSkip();
  
  // 重新过滤filteredQuestions，排除不考题
  const currentQid = q.id;
  const typeFilter = document.getElementById('typeFilter').value;
  let activeQuestions = allQuestions.filter(x => !skipBook.includes(x.id));
  if (typeFilter) activeQuestions = activeQuestions.filter(x => x.type === typeFilter);
  filteredQuestions = activeQuestions;
  
  // 调整currentIndex
  if (wasSkipped) {
    // 恢复后，跳转到恢复的题目
    const newIdx = filteredQuestions.findIndex(x => x.id === currentQid);
    currentIndex = newIdx >= 0 ? newIdx : 0;
  } else {
    // 标记为不考题后，跳转到下一题
    if (currentIndex >= filteredQuestions.length) {
      currentIndex = filteredQuestions.length - 1;
    }
    if (currentIndex < 0) currentIndex = 0;
  }
  
  renderQuestion();
  updateStats();
}'''

if old_toggle in content:
    content = content.replace(old_toggle, new_toggle)
    print("toggleSkipMark函数已修改，标记后重新过滤filteredQuestions")
else:
    print("找不到toggleSkipMark函数")

# 检查是否有updateStats函数，如果没有就添加
if 'function updateStats' not in content:
    # 在toggleSkipMark函数后面添加updateStats函数
    old_update = '''function updateSkipButton() {'''
    new_update = '''function updateStats() {
  const activeCount = allQuestions.filter(q => !skipBook.includes(q.id)).length;
  document.getElementById('stats').textContent = `共 ${activeCount} 题`;
}

function updateSkipButton() {'''
    if old_update in content:
        content = content.replace(old_update, new_update)
        print("已添加updateStats函数")
    else:
        print("找不到updateSkipButton函数")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("修改完成")
