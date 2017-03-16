from __future__ import print_function
import urllib
def read_text():
    """
    Read all lines from text file, then submit to profanity check website
    """
    quotes = open("movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    """
    Use the web api to check curse word, print out the result
    """
    webapi = "http://www.purgomalum.com/service/containsprofanity?text="
    connection = urllib.urlopen(webapi + text_to_check)
    output = connection.read()
    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")

read_text()
