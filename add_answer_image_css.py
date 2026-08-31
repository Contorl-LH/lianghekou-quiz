file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 在.answer-text样式后面添加答案图片组的样式
old_css = '''  /* 答案文字 */
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

new_css = '''  /* 答案文字 */
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
  }

  /* 答案图片组 */
  .answer-image-group {
    display: flex;
    flex-direction: column;
    gap: 16px;
    margin-top: 12px;
  }
  .answer-image-item {
    background: #f7fafc;
    border-radius: 12px;
    padding: 12px;
    border: 1px solid #e2e8f0;
  }
  .answer-image-label {
    display: inline-block;
    background: linear-gradient(135deg, #ed8936, #dd6b20);
    color: white;
    padding: 4px 10px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 10px;
  }
  .answer-image-item img {
    width: 100%;
    max-width: 100%;
    border-radius: 8px;
    cursor: pointer;
    display: block;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }'''

if old_css in content:
    content = content.replace(old_css, new_css)
    print("答案图片组CSS样式已添加")
else:
    print("找不到.answer-text样式")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("CSS修改完成")
