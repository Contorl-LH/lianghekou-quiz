file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 修改filterByType函数，筛选后自动跳转到第一道未做题目
old_filter = '''function filterByType() {
  const type = document.getElementById('typeFilter').value;
  const activeQuestions = allQuestions.filter(q => !skipBook.includes(q.id)); // 排除不考题
  filteredQuestions = type ? activeQuestions.filter(q => q.type === type) : [...activeQuestions];
  currentIndex = 0;
  renderQuestion();
}'''

new_filter = '''function filterByType() {
  const type = document.getElementById('typeFilter').value;
  const activeQuestions = allQuestions.filter(q => !skipBook.includes(q.id)); // 排除不考题
  filteredQuestions = type ? activeQuestions.filter(q => q.type === type) : [...activeQuestions];
  
  // 自动跳转到第一道未做的题目
  let firstUndoneIndex = 0;
  for (let i = 0; i < filteredQuestions.length; i++) {
    if (!isQuestionDone(filteredQuestions[i].id)) {
      firstUndoneIndex = i;
      break;
    }
  }
  currentIndex = firstUndoneIndex;
  renderQuestion();
}'''

if old_filter in content:
    content = content.replace(old_filter, new_filter)
    print("filterByType函数已修改，筛选后自动跳转到第一道未做题目")
else:
    print("找不到filterByType函数")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("修改完成")
