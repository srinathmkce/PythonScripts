__author__ = 'user'

import urllib

def read_text() :
    quotes = open("/home/user/PycharmProjects/profanityEditor/data.txt")
    contents_of_file = quotes.read()
    quotes.close()
    check_for_profanity(contents_of_file)

def check_for_profanity(text_to_check) :
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
    output = connection.read()
    if "true" in output :
        print("Alert !!! It has Curse Word ")
    else :
        print("Doesnt Have Curse Word. Good To Go !!!")
    connection.close()

read_text()