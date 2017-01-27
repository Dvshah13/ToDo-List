from flask import Flask, jsonify, request
import pg

app = Flask('todo-list')
db = pg.DB(host="localhost", user="postgres", passwd="rockets", dbname="todo_list_db")

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/tasks')
def list_tasks():
    results = db.query('select * from task order by id').dictresult()
    return jsonify(results)

@app.route('/add_task', methods=['POST'])
def add_task():
    description = request.form.get('task')
    print description
    result = db.insert('task', description=description)
    return jsonify(result)

@app.route('/mark_task', methods=['POST'])
def mark_task():
    print request.form;
    task_id = int(request.form.get('id'))
    is_task_done = request.form.get('done')

    results = db.update(
        'task', {
            'id': task_id,
            'done': is_task_done
        }
    )

    return jsonify(results)

@app.route('/remove_task/<task_id>', methods=['POST'])
def remove_task(task_id):
    print task_id
    db.delete(
        'task',
            {
                'id': task_id
            }
    );
    return "Testing"

if __name__ == '__main__':
    app.run(debug=True)
