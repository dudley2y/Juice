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
def pre_processing():

    files = glob.glob("./data/*.txt")
    
    for f in files:
        startFile = "data/" + os.path.basename(f)
        endFile = "proc_data/" + os.path.basename(f)
        subprocess.call(["ucto", "-L", "eng", startFile, endFile])
'''
def pre_processing():

    files = glob.glob("./data/*.txt")

    for f in files:

        file_content = open(f).read()
        
        SSP = SyllableTokenizer()
        tokens = [SSP.tokenize(token) for token in word_tokenize(file_content)]
    
        with open("processed_data/" + os.path.basename(f),"w") as endFile:
            endFile.write(str(tokens))

        print(str(f) + " Done")
pre_processing()

