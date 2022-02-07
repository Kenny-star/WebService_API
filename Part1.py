import flask
from flask import request, jsonify, abort

tasks = [
    {
        'id': 1,
        'title': u'Schedule Scrum Meeting',
        'description': u'Call group members to schedule the meeting',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    },
    {
        'id': 3,
        'title': u'Start Project',
        'description': u'Group meeting to discuss how to handle the new project.',
        'done': False
    }
]

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>The Title of the Page</h1><p>This is some text on the Web Page. \n </p>"


@app.route('/tasks/all', methods=['GET'])
def api_all():
    return jsonify(tasks)


@app.route('/tasks', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])

    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for t in tasks:
        if t['id'] == id:
            results.append(t)

    return jsonify(results)


@app.route('/addForm', methods=['GET', 'POST'])
def add_Form_Display():
    if request.method == 'POST':
        id_Get = request.form.get('id')
        title_Get = request.form.get('title')
        desc_Get = request.form.get('description')
        done_Get = request.form.get('done')

        tasks.append({'id':id_Get, 'description':desc_Get, 'done': done_Get, 'title': title_Get})

        return '''<h1>Id: {}</h1>
                  <h1>Title: {}</h1>
                  <h1>Description: {}</h1>
                  <h1>Done: {}</h1>
        '''.format(id_Get, title_Get, desc_Get, done_Get)

    return '''
    <form method="POST">
        <div><label>Input Id: <input type="text" name="id"></label></div>
        <div><label>Input Title: <input type="text" name="title"></label></div>
        <div><label>Input Description: <input type="text" name="description"></label></div>
        <div><label>Input Done: <input type="text" name="done"></label></div>
        <input type="submit" value="Submit">
    </form>'''


@app.route('/updateTask/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})


app.run()
