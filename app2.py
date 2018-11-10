import json
from difflib import get_close_matches

data = json.load(open("dictionary.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return(data[w])
    elif w.upper() in data:
        return data[w.upper()]
    elif w.title() in data:
        return data[w.title()]
    elif len(get_close_matches(w, data.keys() , cutoff=0.8)) > 0:
        x = input("Do you mean %s instead ? Enter Yes[y] or No[n] : " % (get_close_matches(w, data.keys() , cutoff=0.8)[0]).upper())
        if x == 'y':
            return data[get_close_matches(w, data.keys() , cutoff=0.8)[0]]
        elif x =='n':
            return "The word doesn't exist. Please Double check it !"
        else:
            return "Invalid input !"
    else:
        return "The word doesn't exist. Please Double check it !"

word = input("Enter word : ")

output  = translate(word)
if type(output) == 'list':
    for i in output:
        print(i)
else:
    print(output)

#python
