file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 修改普通答题部分的HTML，添加题干文字和答案文字
old_html = '''      <div class="card-body">
        <img id="qImg" src="" alt="题干" onclick="toggleZoom(this)">
        <div class="answer-options" id="answerOptions"></div>
        <div class="result-tip" id="resultTip"></div>
        <div class="action-row">
          <button class="action-btn done-mark" id="doneBtn" onclick="toggleDoneMark()">✅ 标记已做</button>
          <button class="action-btn fav" id="favBtn" onclick="toggleFavorite()">⭐ 收藏</button>
          <button class="action-btn wrong-mark" id="wrongBtn" onclick="toggleWrongMark()">❌ 标记错题</button>
        </div>
        <div class="answer-section" id="answerSection">
          <span class="answer-label">参考答案</span>
          <img id="aImg" src="" alt="答案" onclick="toggleZoom(this)">
        </div>
      </div>'''

new_html = '''      <div class="card-body">
        <div class="question-text" id="questionText"></div>
        <img id="qImg" src="" alt="题干" onclick="toggleZoom(this)">
        <div class="answer-options" id="answerOptions"></div>
        <div class="result-tip" id="resultTip"></div>
        <div class="action-row">
          <button class="action-btn done-mark" id="doneBtn" onclick="toggleDoneMark()">✅ 标记已做</button>
          <button class="action-btn fav" id="favBtn" onclick="toggleFavorite()">⭐ 收藏</button>
          <button class="action-btn wrong-mark" id="wrongBtn" onclick="toggleWrongMark()">❌ 标记错题</button>
        </div>
        <div class="answer-section" id="answerSection">
          <span class="answer-label">参考答案</span>
          <div class="answer-text" id="answerText"></div>
          <img id="aImg" src="" alt="答案" onclick="toggleZoom(this)">
        </div>
      </div>'''

if old_html in content:
    content = content.replace(old_html, new_html)
    print("普通答题部分HTML已修改，添加了题干文字和答案文字")
else:
    print("找不到普通答题部分HTML")

# 修改计划答题部分的HTML，添加题干文字和答案文字
old_plan_html = '''        <div class="card-body">
          <img id="planQImg" src="" alt="题干" onclick="toggleZoom(this)">
          <div class="answer-options" id="planAnswerOptions"></div>
          <div class="result-tip" id="planResultTip"></div>
          <div class="action-row">
            <button class="action-btn done-mark" id="planDoneBtn" onclick="togglePlanDone()">✅ 标记已做</button>
            <button class="action-btn fav" id="planFavBtn" onclick="togglePlanFavorite()">⭐ 收藏</button>
            <button class="action-btn wrong-mark" id="planWrongBtn" onclick="togglePlanWrongMark()">❌ 标记错题</button>
          </div>
          <div class="answer-section" id="planAnswerSection">
            <span class="answer-label">参考答案</span>
            <img id="planAImg" src="" alt="答案" onclick="toggleZoom(this)">
          </div>
        </div>'''

new_plan_html = '''        <div class="card-body">
          <div class="question-text" id="planQuestionText"></div>
          <img id="planQImg" src="" alt="题干" onclick="toggleZoom(this)">
          <div class="answer-options" id="planAnswerOptions"></div>
          <div class="result-tip" id="planResultTip"></div>
          <div class="action-row">
            <button class="action-btn done-mark" id="planDoneBtn" onclick="togglePlanDone()">✅ 标记已做</button>
            <button class="action-btn fav" id="planFavBtn" onclick="togglePlanFavorite()">⭐ 收藏</button>
            <button class="action-btn wrong-mark" id="planWrongBtn" onclick="togglePlanWrongMark()">❌ 标记错题</button>
          </div>
          <div class="answer-section" id="planAnswerSection">
            <span class="answer-label">参考答案</span>
            <div class="answer-text" id="planAnswerText"></div>
            <img id="planAImg" src="" alt="答案" onclick="toggleZoom(this)">
          </div>
        </div>'''

if old_plan_html in content:
    content = content.replace(old_plan_html, new_plan_html)
    print("计划答题部分HTML已修改，添加了题干文字和答案文字")
else:
    print("找不到计划答题部分HTML")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML修改完成")
