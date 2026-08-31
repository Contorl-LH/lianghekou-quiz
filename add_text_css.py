file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 在.answer-label样式后面添加.question-text和.answer-text的样式
old_css = '''  .answer-label {
    display: inline-block;
    background: linear-gradient(135deg, #4299e1, #2b6cb0);
    color: white;
    padding: 6px 14px;
    border-radius: 10px;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 12px;
    box-shadow: 0 2px 8px rgba(66, 153, 225, 0.3);
  }'''

new_css = '''  .answer-label {
    display: inline-block;
    background: linear-gradient(135deg, #4299e1, #2b6cb0);
    color: white;
    padding: 6px 14px;
    border-radius: 10px;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 12px;
    box-shadow: 0 2px 8px rgba(66, 153, 225, 0.3);
  }

  /* 题干文字 */
  .question-text {
    font-size: 16px;
    line-height: 1.8;
    color: #2d3748;
    margin-bottom: 16px;
    padding: 14px 16px;
    background: linear-gradient(135deg, #f7fafc, #edf2f7);
    border-radius: 12px;
    border-left: 4px solid #4299e1;
    white-space: pre-wrap;
    word-break: break-word;
  }

  /* 答案文字 */
  .answer-text {
    font-size: 15px;
    line-height: 1.8;
    color: #2d3748;
    margin-bottom: 12px;
    padding: 12px 14px;
    background: linear-gradient(135deg, #f0fff4, #c6f6d5);
    border-radius: 10px;
    border-left: 4px solid #48bb78;
    font-weight: 500;
    white-space: pre-wrap;
    word-break: break-word;
  }'''

if old_css in content:
    content = content.replace(old_css, new_css)
    print("CSS样式已添加，题干文字和答案文字样式已设置")
else:
    print("找不到.answer-label样式")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("CSS修改完成")
