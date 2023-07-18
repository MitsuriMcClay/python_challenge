from flask import Flask, request

app = Flask('myfamily')

family = {'james': 38, 'mitsuri': 41}

@app.route('/')
def myapi():
    name = request.args.get('name')
    age = family[name]
    return  f'<h1>Hello {name}! you are {family[name]} years old.</h1>' #{'name': name, 'age': age}

app.run(host='0.0.0.0',port=900)