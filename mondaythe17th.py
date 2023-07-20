#!/opt/homebrew/bin/python3

from flask import Flask, request

app=Flask("app")

#instrument_names={"Guitar": 6, "Banjo": 5, "Cello": 4}

Instruments = {
        'Guitar': {
                'Strings':6,
                'Genre': 'Blue Grass'
        },
        'Banjo': {
                'Strings': 5,
                'Genre': 'Blue Grass'
        },
        'Cello': {
                'Strings':4,
                'Genre': 'Classic',
        }
}

@app.route("/")
def musicapp():
        info_key=request.args.get("instrument_name")
        info_type = request.args.get("info_type")
        if info_key == "" or info_type == "":
                return "Youare missing either Instrument name or info type which is Genre or the number of the strings."
        elif info_key == None or info_type == None:
                return "Request needs an argument to param \"instrument_name\""
        elif info_key or info_type not in Instruments.keys():
                return "<h1>No info about that instrument. Try either Guitar Banjo, or Cello.</h1>"
        elif info_key == request.args.get("instrument_name"):
               if info_type == 'Genre':
                       Genre = Instruments[info_key][info_type]
                       return f"{info_key}\'s Genre is {Genre}."
               else:
                       info_type == 'Strings'
                       Strings = Instruments[info_key][info_type]
                       return f"{info_key} has {Strings} strings."
app.run(host="0.0.0.0", port=5050)

