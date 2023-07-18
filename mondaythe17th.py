#!/opt/homebrew/bin/python3

from flask import Flask, request

app=Flask("app")

instrument_names={"Guitar": 6, "Banjo": 5}

@app.route("/")

def musicapp():
        info_key=request.args.get("instrument_name")
        if info_key == "":
                return "Wrong info_key! Start over!"
        elif info_key == None:
                return "Request needs an argument to param \"instrument_name\""
        elif info_key == request.args.get("instrument_name"):
               result=instrument_names[info_key]
               return f"{info_key} has {result} strings."

app.run(host="0.0.0.0", port=5050)
