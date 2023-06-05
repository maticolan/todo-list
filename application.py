from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = []

@app.route('/', methods=['GET', 'POST'])
def todo_list():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
        return redirect('/')
    return render_template('todo.html', tasks=tasks)

@app.route('/complete', methods=['POST'])
def complete_task():
    task_index = int(request.form['task_index'])
    tasks[task_index] = f'<s>{tasks[task_index]}</s>'
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete_task():
    task_index = int(request.form['task_index'])
    del tasks[task_index]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
