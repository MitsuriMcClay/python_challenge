#!/opt/homebrew/bin/python3

print('好きな数字を文字列にして入力して下さい。何桁でもOK!')
number_dict = {'one': '1',
               'two': '2',
               'three': '3',
               'four': '4',
               'five': '5',
               'six': '6',
               'seven': '7',
               'eight': '8',
               'nine': '9',
               'zero': '0',}

test_string = input()

print("入力した文字列：" +test_string)

result_number = ''.join(number_dict[a] for a in test_string.split())

print(result_number)
