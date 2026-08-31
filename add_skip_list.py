file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 在10天计划模式之前插入不考题列表
old_plan = '''  <!-- 10天计划模式 -->
  <div class="plan-mode" id="planMode">'''

new_skip = '''  <!-- 不考题列表 -->
  <div class="list-mode" id="skipMode" style="display:none">
    <div class="list-header">
      <h2>🚫 不考题</h2>
      <p style="color:#666;font-size:14px">已标记为不考的题目，不会出现在答题和10天计划中</p>
      <button class="btn-danger" onclick="clearAllSkipConfirm()">清空不考题</button>
    </div>
    <div class="list-filter">
      <button class="type-filter-btn active" data-type="all" onclick="setSkipFilter('all')">全部</button>
      <button class="type-filter-btn" data-type="A" onclick="setSkipFilter('A')">选择</button>
      <button class="type-filter-btn" data-type="B" onclick="setSkipFilter('B')">判断</button>
      <button class="type-filter-btn" data-type="C" onclick="setSkipFilter('C')">简答</button>
      <button class="type-filter-btn" data-type="D" onclick="setSkipFilter('D')">计算</button>
      <button class="type-filter-btn" data-type="E" onclick="setSkipFilter('E')">绘图</button>
      <button class="type-filter-btn" data-type="F" onclick="setSkipFilter('F')">论述</button>
    </div>
    <div class="question-list" id="skipList"></div>
  </div>

  <!-- 10天计划模式 -->
  <div class="plan-mode" id="planMode">'''

if old_plan in content:
    content = content.replace(old_plan, new_skip)
    print("不考题列表页面已添加")
else:
    print("找不到10天计划模式开始位置")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML修改完成")
