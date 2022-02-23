from string import punctuation


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
#don't change anything above this
#import the python string library so we can get a list of punctuation 
import string
punctuation_list = string.punctuation
#print(punctuation)
punctuation = punctuation_list.replace("", " ")
#print("replace", punctuation)
punctuation = punctuation.split()
#print("split", punctuation)
# add the punctuation string items to the STOP_WORDS array
STOP_WORDS = STOP_WORDS + punctuation
#print("This is STOP_WORDS:", STOP_WORDS)
# our function

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""

    with open(file) as file:
        words = file.read()
        words2 = []
        #print(words)
    
        words = words.lower() #make lowercase
        words = words.split(" ")
        print("after split:", words) 
        #remove stop_words
        for i in STOP_WORDS:
            if i in words:
                words = words.remove(i)
        print("here it is with punctuation removed", words, "well rats that doesn't exactly work")
        
        for i in words:
            if i not in words2:
                    words2 = words2.append(i)
        print(words2)
        #for i in range(0, len(words2)):
        # count the frequency of each word(present in str2) in str and print
            #print(words2[i], ':', words2.count(words2[i]))
            #print(f"{len(lines)} lines in the file.") #can we change this to words?
        #for stopword in STOP_WORDS:
         #   words.replace(stopword, "")
        #print(words)
#word_count_dic = {}    
#words = file() #can we change this to words?
#def count_words(string):
        
        
        
        
        

# don't change anything below this
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
