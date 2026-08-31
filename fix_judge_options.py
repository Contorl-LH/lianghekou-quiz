file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 修改renderQuestion函数，让判断题也显示选项
old_code = '''  const optsDiv = document.getElementById('answerOptions');
  optsDiv.innerHTML = '';
  if (q.type === 'A' && q.o) {
    Object.keys(q.o).sort().forEach(key => {
      const btn = document.createElement('button');
      btn.className = 'option-btn';
      btn.dataset.opt = key;
      btn.innerHTML = `<span class="opt-letter">${key}</span><span>${q.o[key]}</span>`;
      btn.onclick = () => selectOption(key);
      optsDiv.appendChild(btn);
    });
  }'''

new_code = '''  const optsDiv = document.getElementById('answerOptions');
  optsDiv.innerHTML = '';
  if ((q.type === 'A' || q.type === 'B') && q.o) {
    Object.keys(q.o).sort().forEach(key => {
      const btn = document.createElement('button');
      btn.className = 'option-btn';
      btn.dataset.opt = key;
      if (q.type === 'B') {
        btn.innerHTML = `<span class="opt-letter">${key === '正确' ? '✓' : '✗'}</span><span>${q.o[key]}</span>`;
      } else {
        btn.innerHTML = `<span class="opt-letter">${key}</span><span>${q.o[key]}</span>`;
      }
      btn.onclick = () => selectOption(key);
      optsDiv.appendChild(btn);
    });
  }'''

if old_code in content:
    content = content.replace(old_code, new_code)
    print("renderQuestion函数已修改，判断题现在显示选项")
else:
    print("找不到要替换的代码")
    # 尝试查找类似的代码
    idx = content.find("if (q.type === 'A' && q.o)")
    if idx != -1:
        print(f"找到代码在位置: {idx}")
        print(content[idx:idx+300])

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("修改完成")
