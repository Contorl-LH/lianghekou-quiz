file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 修改filterByType函数，排除不考题
old_filter = '''function filterByType() {
  const type = document.getElementById('typeFilter').value;
  filteredQuestions = type ? allQuestions.filter(q => q.type === type) : [...allQuestions];
  currentIndex = 0;
  renderQuestion();
}'''

new_filter = '''function filterByType() {
  const type = document.getElementById('typeFilter').value;
  const activeQuestions = allQuestions.filter(q => !skipBook.includes(q.id)); // 排除不考题
  filteredQuestions = type ? activeQuestions.filter(q => q.type === type) : [...activeQuestions];
  currentIndex = 0;
  renderQuestion();
}'''

if old_filter in content:
    content = content.replace(old_filter, new_filter)
    print("filterByType函数已修改，排除不考题")
else:
    print("找不到filterByType函数")

# 2. 修改jumpToQuestion函数，排除不考题
old_jump = '''  let idx = filteredQuestions.findIndex(q => q.id === qid);
  if (idx < 0) {
    filteredQuestions = [...allQuestions];
    document.getElementById('typeFilter').value = '';
    idx = filteredQuestions.findIndex(q => q.id === qid);
  }'''

new_jump = '''  let idx = filteredQuestions.findIndex(q => q.id === qid);
  if (idx < 0) {
    filteredQuestions = allQuestions.filter(q => !skipBook.includes(q.id)); // 排除不考题
    document.getElementById('typeFilter').value = '';
    idx = filteredQuestions.findIndex(q => q.id === qid);
  }'''

if old_jump in content:
    content = content.replace(old_jump, new_jump)
    print("jumpToQuestion函数已修改，排除不考题")
else:
    print("找不到jumpToQuestion函数")

# 3. 检查shuffleQuestions函数是否也重新赋值了filteredQuestions
# 从之前的grep结果来看，第2192行是shuffleQuestions函数
# 让我检查一下

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("修复完成")
