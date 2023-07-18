#!/opt/homebrew/bin/python3

#Japanese_name = {'Red': '赤', 'Blue': '青', 'Yellow': '黄色', 'Black': '黒'}
#Hex = {'Red': '#ff0000', 'Blue': '#0000ff', 'Yellow': '#ffff00', 'Black': '#000000'}
colors = {
    'Red': {
        'japanese_name': '赤',
        'hex': '#ff0000',
    },
    'Blue': {
        'japanese_name': '青',
        'hex': '#0000ff'
    }
}



color=input('Give a color name:').strip().lower().capitalize()
if color not in colors.keys():
    print("I don't know that color.")
    quit()
info_type=input('Give a type:').strip().lower()
if info_type not in colors[color].keys():
    print("I don't have that info.")
    quit()
result=colors[color][info_type]
print(f'Here is {color}\'s {info_type} :{result}')





'Give a key: Red'
'Give a type: japanese'
'赤'

'Give a key: Yellow'
'Give a type: hex'
'#ffff00'


