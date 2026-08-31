file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 添加不考题按钮的CSS样式
old_css = '''  .action-btn.wrong-mark {
    background: linear-gradient(135deg, #f56565, #c53030);
    color: white;
  }'''

new_css = '''  .action-btn.wrong-mark {
    background: linear-gradient(135deg, #f56565, #c53030);
    color: white;
  }
  .action-btn.skip-mark {
    background: linear-gradient(135deg, #9f7aea, #805ad5);
    color: white;
  }'''

if old_css in content:
    content = content.replace(old_css, new_css)
    print("不考题按钮CSS样式已添加")
else:
    print("找不到wrong-mark CSS样式")

# 确保10天计划也排除不考题
# 查找buildPlan函数
old_build = '''function buildPlan() {
  // 将所有题目按题型分组
  const byType = {};
  allQuestions.forEach(q => {
    if (!byType[q.type]) byType[q.type] = [];
    byType[q.type].push(q.id);
  });'''

new_build = '''function buildPlan() {
  // 将所有题目按题型分组（排除不考题）
  const byType = {};
  allQuestions.forEach(q => {
    if (skipBook.includes(q.id)) return; // 排除不考题
    if (!byType[q.type]) byType[q.type] = [];
    byType[q.type].push(q.id);
  });'''

if old_build in content:
    content = content.replace(old_build, new_build)
    print("10天计划已排除不考题")
else:
    print("找不到buildPlan函数")

# 确保统计题目数量时排除不考题
old_stats = '''  document.getElementById('stats').textContent = `共 ${allQuestions.length} 题`;'''

new_stats = '''  const activeCount = allQuestions.filter(q => !skipBook.includes(q.id)).length;
  document.getElementById('stats').textContent = `共 ${activeCount} 题`;'''

if old_stats in content:
    content = content.replace(old_stats, new_stats)
    print("题目统计已排除不考题")
else:
    print("找不到题目统计代码")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("修改完成")
