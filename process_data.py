import lyricsgenius
import glob
import subprocess
import os
import nltk
from nltk.tokenize import SyllableTokenizer
from nltk import word_tokenize

token = "66WN3L4XNqytxNDsgfEXKf7mwr3PhvPrteDKu6_DKZztGhK4zVVIfElQY9k2t54S"
genius = lyricsgenius.Genius(token)
genius.verbose = False
genius.remove_section_headers = True
genius.skip_non_songs = True

'''
From genius api grabs a certain number of Juice WRLD lyrics 

input: int or None 
'''

def get_lyrics(number_of_songs):
    try:
        songs  = (genius.search_artist("Juice WRLD", max_songs = number_of_songs, )).songs
        ctr = 1 
        for song in songs:
            with open("./data/" + str(ctr)+ ".txt","w") as f:
                f.write(song.lyrics)
                ctr+=1
    except:
        print("Some Random Error")

'''
Preoprocesses ./data/ using ucto tokenizer, tokenizes into syllables
From ./data/ -> ./proc_data/
'''
def ucto_pre_processing():

    files = glob.glob("./data/*.txt")
    
    for f in files:
        startFile = "data/" + os.path.basename(f)
        endFile = "proc_data/" + os.path.basename(f)
        subprocess.call(["ucto", "-L", "eng", startFile, endFile])

