import json
from os import abort, readlink
from difflib import get_close_matches
print("Welcome to the Dictionary World")

with open("data.json") as json_file:
    data=json.load(json_file)

turn_on=True




while turn_on:
    word=input("Enter the word to search:").lower()
    if word in data:
            print("....."+word+".....")
            for i,element in enumerate(data[word],1):
                print(i,element)

    else:
        word_check=str(get_close_matches(word,data.keys())[0])
        conditions=input("Did you mean:"+word_check+" yes or no:").lower()
        if conditions=="yes":
            if word_check in data:
                print("....."+word_check+".....")
                for i,element in enumerate(data[word_check],1):
                    print(i,element)
        else:
            print("Sorry the Word not found. Recheck the words.....!")


    

    

    

    









