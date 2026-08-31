file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 修改普通答题部分的答案区域，移除答案图片
old_answer = '''          <div class="answer-image-group">
            <div class="answer-image-item">
              <span class="answer-image-label">题目图片</span>
              <img id="qImg" src="" alt="题干" onclick="toggleZoom(this)">
            </div>
            <div class="answer-image-item">
              <span class="answer-image-label">答案图片</span>
              <img id="aImg" src="" alt="答案" onclick="toggleZoom(this)">
            </div>
          </div>'''

new_answer = '''          <div class="answer-image-group">
            <div class="answer-image-item">
              <span class="answer-image-label">题目图片</span>
              <img id="qImg" src="" alt="题干" onclick="toggleZoom(this)">
            </div>
          </div>'''

if old_answer in content:
    content = content.replace(old_answer, new_answer)
    print("普通答题部分答案图片已移除")
else:
    print("找不到普通答题部分答案图片")

# 修改计划答题部分的答案区域，移除答案图片
old_plan_answer = '''            <div class="answer-image-group">
              <div class="answer-image-item">
                <span class="answer-image-label">题目图片</span>
                <img id="planQImg" src="" alt="题干" onclick="toggleZoom(this)">
              </div>
              <div class="answer-image-item">
                <span class="answer-image-label">答案图片</span>
                <img id="planAImg" src="" alt="答案" onclick="toggleZoom(this)">
              </div>
            </div>'''

new_plan_answer = '''            <div class="answer-image-group">
              <div class="answer-image-item">
                <span class="answer-image-label">题目图片</span>
                <img id="planQImg" src="" alt="题干" onclick="toggleZoom(this)">
              </div>
            </div>'''

if old_plan_answer in content:
    content = content.replace(old_plan_answer, new_plan_answer)
    print("计划答题部分答案图片已移除")
else:
    print("找不到计划答题部分答案图片")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML修改完成")
