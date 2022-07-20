from flask import Flask,jsonify,request

app = Flask(__name__)
data = [
    {
        'id' : 1,
        'contact' : '9987644456',
        'name' : 'Raju',
        'done' : False
    },
    {
        'id' : 2,
        'contact' : '9876543222',
        'name' : 'rahul',
        'done' : False
    }
]
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/add-data',methods = ['POST'])
def add_contact():
    if not request.json:
        return jsonify({
            'status' : 'error',
            'message' : 'Please provide the data'
        },400)
    contact = {
        'id' : data[-1]['id'] + 1,
        'name' : request.json['name'],
        'conatct' : request.json.get('contact',''),
        'done' : False
    }
    data.append(contact)
    return jsonify({
        'status' : 'Success',
        'message' : 'Contact added successfully!'
    })

@app.route('/get-data')
def get_tasks():
    return jsonify({
        'data' : data
    })

if(__name__ == '__main__'):
    app.run(debug= True)