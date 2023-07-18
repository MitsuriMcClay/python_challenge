#!/opt/homebrew/bin/python3
from flask import Flask, request

myapp=Flask("myapp")

ages={"Mits": 41, "James": 38, "Zai": 9, "Kaizo": 6}
mid_names={"Mits": "Ikeda", "James": "Devin", "Zai": "Carter", "Kaizo": "Michael"}

@myapp.route("/")
def myappsaturday():
    info_key=request.args.get("info_key")
    info_type=request.args.get("info_type")
    if info_type == "fam_age":
        age=ages[info_key]
        return f"{info_key}\'s age is {age}."
    else: 
        #info_type == "middle_name"
        middle_name=mid_names[info_key]
        return f"{info_key}\'s Middle name is {middle_name}."

myapp.run(host="0.0.0.0", port=5001)
