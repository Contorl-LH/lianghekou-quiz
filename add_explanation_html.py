file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 修改普通答题部分的答案区域，添加讲解显示
old_answer = '''        <div class="answer-section" id="answerSection">
          <span class="answer-label">参考答案</span>
          <div class="answer-text" id="answerText"></div>
          <div class="answer-image-group">
            <div class="answer-image-item">
              <span class="answer-image-label">题目图片</span>
              <img id="qImg" src="" alt="题干" onclick="toggleZoom(this)">
            </div>
            <div class="answer-image-item">
              <span class="answer-image-label">答案图片</span>
              <img id="aImg" src="" alt="答案" onclick="toggleZoom(this)">
            </div>
          </div>
        </div>'''

new_answer = '''        <div class="answer-section" id="answerSection">
          <span class="answer-label">参考答案</span>
          <div class="answer-text" id="answerText"></div>
          <div class="explanation-section" id="explanationSection">
            <span class="explanation-label">📝 题目讲解</span>
            <div class="explanation-text" id="explanationText"></div>
          </div>
          <div class="answer-image-group">
            <div class="answer-image-item">
              <span class="answer-image-label">题目图片</span>
              <img id="qImg" src="" alt="题干" onclick="toggleZoom(this)">
            </div>
            <div class="answer-image-item">
              <span class="answer-image-label">答案图片</span>
              <img id="aImg" src="" alt="答案" onclick="toggleZoom(this)">
            </div>
          </div>
        </div>'''

if old_answer in content:
    content = content.replace(old_answer, new_answer)
    print("普通答题部分答案区域已添加讲解")
else:
    print("找不到普通答题部分答案区域")

# 修改计划答题部分的答案区域，添加讲解显示
old_plan_answer = '''          <div class="answer-section" id="planAnswerSection">
            <span class="answer-label">参考答案</span>
            <div class="answer-text" id="planAnswerText"></div>
            <div class="answer-image-group">
              <div class="answer-image-item">
                <span class="answer-image-label">题目图片</span>
                <img id="planQImg" src="" alt="题干" onclick="toggleZoom(this)">
              </div>
              <div class="answer-image-item">
                <span class="answer-image-label">答案图片</span>
                <img id="planAImg" src="" alt="答案" onclick="toggleZoom(this)">
              </div>
            </div>
          </div>'''

new_plan_answer = '''          <div class="answer-section" id="planAnswerSection">
            <span class="answer-label">参考答案</span>
            <div class="answer-text" id="planAnswerText"></div>
            <div class="explanation-section" id="planExplanationSection">
              <span class="explanation-label">📝 题目讲解</span>
              <div class="explanation-text" id="planExplanationText"></div>
            </div>
            <div class="answer-image-group">
              <div class="answer-image-item">
                <span class="answer-image-label">题目图片</span>
                <img id="planQImg" src="" alt="题干" onclick="toggleZoom(this)">
              </div>
              <div class="answer-image-item">
                <span class="answer-image-label">答案图片</span>
                <img id="planAImg" src="" alt="答案" onclick="toggleZoom(this)">
              </div>
            </div>
          </div>'''

if old_plan_answer in content:
    content = content.replace(old_plan_answer, new_plan_answer)
    print("计划答题部分答案区域已添加讲解")
else:
    print("找不到计划答题部分答案区域")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML修改完成")
