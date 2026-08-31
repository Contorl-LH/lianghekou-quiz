file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 在togglePlanWrongMark函数后面添加togglePlanSkipMark函数
old_plan_wrong = '''function togglePlanWrongMark() {
  const qid = planDays[planCurrentDay][planQuizIndex];
  const idx = wrongBook.indexOf(qid);
  if (idx >= 0) wrongBook.splice(idx, 1);
  else wrongBook.push(qid);
  saveWrong();
  updateBadges();
  renderPlanQuestion();
}'''

new_plan_wrong_skip = '''function togglePlanWrongMark() {
  const qid = planDays[planCurrentDay][planQuizIndex];
  const idx = wrongBook.indexOf(qid);
  if (idx >= 0) wrongBook.splice(idx, 1);
  else wrongBook.push(qid);
  saveWrong();
  updateBadges();
  renderPlanQuestion();
}

function togglePlanSkipMark() {
  const dayIds = planDays[planCurrentDay];
  const qid = dayIds[planQuizIndex];
  const wasSkipped = skipBook.includes(qid);
  
  if (wasSkipped) {
    // 恢复考题
    const idx = skipBook.indexOf(qid);
    if (idx > -1) skipBook.splice(idx, 1);
  } else {
    // 标记为不考题
    skipBook.push(qid);
  }
  saveSkip();
  updateBadges();
  
  // 从当天的题目列表中移除/恢复不考题
  if (!wasSkipped) {
    // 标记为不考题：从当天列表中移除
    const dayIdx = dayIds.indexOf(qid);
    if (dayIdx > -1) dayIds.splice(dayIdx, 1);
    // 调整当前索引
    if (planQuizIndex >= dayIds.length) planQuizIndex = dayIds.length - 1;
    if (planQuizIndex < 0) planQuizIndex = 0;
  }
  
  renderPlanQuestion();
  updateStats();
}'''

if old_plan_wrong in content:
    content = content.replace(old_plan_wrong, new_plan_wrong_skip)
    print("已添加togglePlanSkipMark函数")
else:
    print("找不到togglePlanWrongMark函数")

# 检查renderPlanQuestion函数，确保它更新了不考题按钮状态
# 让我先找到renderPlanQuestion函数

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("修改完成")
