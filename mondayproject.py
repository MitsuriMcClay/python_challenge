from flask import Flask, request

color = { 'Red': '赤', 'Blue': '青', 'Yellow': '黄色', 'Black': '黒'}
hex = {'Red': '#ff0000', 'Blue': '#0000ff', 'Yellow': '#ffff00', 'Black': '#000000'}

mycolorapp=Flask("mycolorapp")

@mycolorapp.route("/")
def colorapp():
    info_key=request.args.get("info_key")
    info_type=request.args.get("info_type")
    if info_type=='color':
        japanese_color=color[info_key]
        return f'Japanese name for the color is {japanese_color}'
    elif info_type=='hex':
        hex_num=hex[info_key]
        return f'The hex number for that color is {hex_num}'
         
mycolorapp.run(host="0.0.0.0", port=5001)

