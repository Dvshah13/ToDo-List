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
    print request.args
    id = request.form.get('id')
    done = request.form.get('done')
    result = db.update('task', id = id, done = done )
    return jsonify(result)

@app.route('/mark_off_task')
def mark_tasks():
    results = db.query('select * from task where done = True').dictresult()
    return jsonify(results)

@app.route('/remove_completed', methods = ['POST'])
def remove_complete():
    print request.args
    id = request.form.get('id')
    result = db.delete('task', id = id)
    return jsonify(result);

if __name__ == '__main__':
    app.run(debug=True)
