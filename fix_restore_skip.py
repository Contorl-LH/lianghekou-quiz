file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 修改restoreSkipQuestion函数，恢复后重新过滤filteredQuestions
old_restore = '''function restoreSkipQuestion(qid) {
  const idx = skipBook.indexOf(qid);
  if (idx > -1) {
    skipBook.splice(idx, 1);
    saveSkip();
    renderSkipList();
  }
}'''

new_restore = '''function restoreSkipQuestion(qid) {
  const idx = skipBook.indexOf(qid);
  if (idx > -1) {
    skipBook.splice(idx, 1);
    saveSkip();
    // 重新过滤filteredQuestions，将恢复的题目加回来
    const typeFilter = document.getElementById('typeFilter').value;
    let activeQuestions = allQuestions.filter(x => !skipBook.includes(x.id));
    if (typeFilter) activeQuestions = activeQuestions.filter(x => x.type === typeFilter);
    filteredQuestions = activeQuestions;
    updateStats();
    renderSkipList();
  }
}'''

if old_restore in content:
    content = content.replace(old_restore, new_restore)
    print("restoreSkipQuestion函数已修改，恢复后重新过滤filteredQuestions")
else:
    print("找不到restoreSkipQuestion函数")

# 2. 修改clearAllSkipConfirm函数，清空后重新过滤filteredQuestions
old_clear = '''function clearAllSkipConfirm() {
  if (confirm('确定要清空所有不考题吗？')) {
    skipBook = [];
    saveSkip();
    renderSkipList();
  }
}'''

new_clear = '''function clearAllSkipConfirm() {
  if (confirm('确定要清空所有不考题吗？')) {
    skipBook = [];
    saveSkip();
    // 重新过滤filteredQuestions，将所有恢复的题目加回来
    const typeFilter = document.getElementById('typeFilter').value;
    let activeQuestions = allQuestions.filter(x => !skipBook.includes(x.id));
    if (typeFilter) activeQuestions = activeQuestions.filter(x => x.type === typeFilter);
    filteredQuestions = activeQuestions;
    updateStats();
    renderSkipList();
  }
}'''

if old_clear in content:
    content = content.replace(old_clear, new_clear)
    print("clearAllSkipConfirm函数已修改，清空后重新过滤filteredQuestions")
else:
    print("找不到clearAllSkipConfirm函数")

# 3. 修改jumpToQuestion函数，恢复后重新过滤filteredQuestions
old_jump = '''function jumpToQuestion(qid) {
  const idx = allQuestions.findIndex(q => q.id === qid);
  if (idx > -1) {
    // 先从skip中恢复
    const skipIdx = skipBook.indexOf(qid);
    if (skipIdx > -1) {
      skipBook.splice(skipIdx, 1);
      saveSkip();
    }
    currentIndex = idx;
    switchMode('quiz');
    renderQuestion();
  }
}'''

new_jump = '''function jumpToQuestion(qid) {
  const idx = allQuestions.findIndex(q => q.id === qid);
  if (idx > -1) {
    // 先从skip中恢复
    const skipIdx = skipBook.indexOf(qid);
    if (skipIdx > -1) {
      skipBook.splice(skipIdx, 1);
      saveSkip();
    }
    // 重新过滤filteredQuestions，将恢复的题目加回来
    const typeFilter = document.getElementById('typeFilter').value;
    let activeQuestions = allQuestions.filter(x => !skipBook.includes(x.id));
    if (typeFilter) activeQuestions = activeQuestions.filter(x => x.type === typeFilter);
    filteredQuestions = activeQuestions;
    // 跳转到恢复的题目
    const newIdx = filteredQuestions.findIndex(x => x.id === qid);
    currentIndex = newIdx >= 0 ? newIdx : 0;
    updateStats();
    switchMode('quiz');
    renderQuestion();
  }
}'''

if old_jump in content:
    content = content.replace(old_jump, new_jump)
    print("jumpToQuestion函数已修改，恢复后重新过滤filteredQuestions")
else:
    print("找不到jumpToQuestion函数")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("所有修改完成")
