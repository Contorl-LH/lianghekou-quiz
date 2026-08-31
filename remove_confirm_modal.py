file_path = r'C:\temp\deploy\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 删除confirmModal弹窗的HTML代码
old_modal_html = '''<div class="modal-overlay" id="confirmModal">
  <div class="modal-box">
    <h3 id="modalTitle">确认操作</h3>
    <p id="modalText">确定要执行此操作吗？</p>
    <div class="modal-buttons">
      <button class="cancel" onclick="closeModal()">取消</button>
      <button class="confirm" id="modalConfirm" onclick="confirmAction()">确定</button>
    </div>
  </div>
</div>'''

if old_modal_html in content:
    content = content.replace(old_modal_html, '')
    print("confirmModal弹窗HTML已删除")
else:
    print("找不到confirmModal弹窗HTML")

# 2. 将确认弹窗相关函数改为使用原生confirm()
old_modal_js = '''// ============ 确认弹窗 ============
let modalAction = null;
function clearWrongConfirm() {
  if (wrongBook.length === 0) { alert('错题本已是空的'); return; }
  document.getElementById('modalTitle').textContent = '清空错题本';
  document.getElementById('modalText').textContent = `确定要清空全部 ${wrongBook.length} 道错题吗？此操作不可恢复。`;
  modalAction = 'clearWrong';
  document.getElementById('confirmModal').classList.add('show');
}
function closeModal() {
  document.getElementById('confirmModal').classList.remove('show');
  modalAction = null;
}
function confirmAction() {
  if (modalAction === 'clearWrong') {
    wrongBook = [];
    saveWrong();
    updateActionButtons();
  } else if (modalAction === 'resetPlan') {
    planData = { started: false, startDate: null, currentDay: 0, completed: {} };
    savePlan();
    initPlanData();
    renderPlanOverview();
  }
  closeModal();
}'''

new_modal_js = '''// ============ 确认操作（使用原生confirm） ============
function clearWrongConfirm() {
  if (wrongBook.length === 0) { alert('错题本已是空的'); return; }
  if (confirm(`确定要清空全部 ${wrongBook.length} 道错题吗？此操作不可恢复。`)) {
    wrongBook = [];
    saveWrong();
    updateActionButtons();
    renderWrongList();
  }
}
function resetPlanConfirm() {
  if (confirm('确定要重置10天刷题计划吗？所有进度将被清除。')) {
    planData = { started: false, startDate: null, currentDay: 0, completed: {} };
    savePlan();
    initPlanData();
    renderPlanOverview();
  }
}'''

if old_modal_js in content:
    content = content.replace(old_modal_js, new_modal_js)
    print("确认弹窗相关函数已改为使用原生confirm()")
else:
    print("找不到确认弹窗相关函数")

# 3. 检查是否还有其他地方引用了resetPlanConfirm但没有定义
# 从之前的检查来看，resetPlanConfirm在第924行被调用，但在旧代码中没有定义resetPlanConfirm函数
# 它可能是在confirmAction中通过modalAction='resetPlan'来处理的
# 现在我已经添加了resetPlanConfirm函数的定义

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("修改完成")
