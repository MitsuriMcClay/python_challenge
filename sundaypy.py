#!/opt/homebrew/bin/python3
from flask import Flask, request, Response

family = {'james': '38', 'mitsuri': '41'}
jobs = {'james': 'manager', 'mitsuri': 'systems engineer'}

myapp=Flask("myapp")

form = '''
<style>
.banana {
 color: red;
 font-family: Arial;
 font-size: 30px;
}
</style>

<form>
<input class="banana" name=family_name></input>
<input type=submit></input>
</form>

<p>This is a paragraph</p>
<p class="banana"> This is the banana paragraph (it has a class called banana)</p>
'''

@myapp.route("/")
def mitsapproject():
    if 'family_name' not in request.args:
        return form
    elif request.args.get('family_name') == '':
        return 'Error: please enter something.'
    else:
        name=request.args.get('family_name')
        age=family[name]
        job=jobs[name]
        return f'{name}\'s job is {job}. {name}\'s age is{age}'

myapp.run(host="0.0.0.0", port=5001)

