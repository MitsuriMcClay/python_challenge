#!/opt/homebrew/bin/python3
from flask import Flask, request



mitsuriapp=Flask("app")

Instruments = {
        'Guitar': {
            'Strings':6,
            'Genre': ['Blue Grass'],
        },
        'Banjo': {
            'Strings': 5,
            'Genre': ['Blue Grass']
        },
        'Cello': {
            'Strings':4,
            'Genre': ['Classic'],
            'Aliases': ['German Cello'],
        },
        'Violin': {
           'Strings': 4,
           'Genre': ['Classic','Blue Grass'],
           'Aliases': ['Fiddle']
        }
}

@mitsuriapp.route("/", methods=['GET','POST'])
def musicapp():
    if request.method == 'POST':
        somethingfromtheuser = request.json
        Instruments.update(somethingfromtheuser)
        return Instruments
    elif request.method == 'GET':
        # instrument_names = 'Cello-Banjo'
        instrument_names=request.args.get("instrument_name")
        # instrument_names = ['Cello', 'Banjo']
        instrument_names = instrument_names.split('-')
        # info_type = 'Genre'
        info_type = request.args.get("info_type")
        returnmessage = ''
        for instrument_name in instrument_names:
            if instrument_name == "" or info_type == "":
                return "Youare missing either Instrument name or info type which is Genre or the number of the strings."
            elif instrument_name == None or info_type == None:
                return "Request needs an argument to param \"instrument_name\""
            elif instrument_name not in Instruments.keys():
                return "<h1>No info about that instrument.</h1>"
            elif info_type not in Instruments[instrument_name].keys():
                return "You need to type Genre or Strings."
                # instrument_nameはinstrument_name=Cello-BanjoでいうCelloの部分。instrument_namesはリスト
            elif instrument_names == request.args.get("instrument_name").split('-'):         
                    if info_type == 'Genre':
                        genre = Instruments[instrument_name][info_type]
                        genre = ' and '.join(genre)
                        if 'Aliases' in Instruments[instrument_name].keys():
                            aliases = Instruments[instrument_name]['Aliases']
                            aliases = ', '.join(aliases)
                            returnmessage += f"{instrument_name}\'s genre is {genre}. And it's also known as {aliases}. "
                        else:
                            returnmessage += f"{instrument_name}\'s genre is {genre}. "
                    else:
                        info_type == 'Strings'
                        Strings = Instruments[instrument_name][info_type]
                        returnmessage += f"{instrument_name} has {Strings} strings. "
        return returnmessage

mitsuriapp.run(host="0.0.0.0", port=5050)

# http://127.0.0.1:5050/?instrument_name=Cello-Banjo&info_type=Genre

