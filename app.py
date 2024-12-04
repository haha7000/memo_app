from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# 메모 저장 공간 (임시로 메모리 사용, 나중에 DB로 변경 가능)
memos = []

@app.route('/')
def index():
    return render_template('index.html', memos=memos)

@app.route('/add', methods=['POST'])
def add_memo():
    memo = request.form.get('memo')
    if memo:
        memos.append(memo)
    return redirect('/')

@app.route('/delete/<int:memo_index>')
def delete_memo(memo_index):
    if 0 <= memo_index < len(memos):
        memos.pop(memo_index)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
