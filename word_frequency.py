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
#punctuation = punctuation_list.replace("", " ")
#print("replace", punctuation)
#punctuation = punctuation.split()
#print("split", punctuation)
# add the punctuation string items to the STOP_WORDS array
#STOP_WORDS = STOP_WORDS + punctuation
#print("This is STOP_WORDS:", STOP_WORDS)
# our function

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""

    with open(file) as file:
        words = file.read()
        
    words_dic = {}
    #print(words)

    words = words.lower() #make lowercase
    words = words.rstrip()
    words_2 = []
    #need to remove punctuation now
    for i in words:
        #print(i) #loop through by character
        if i in punctuation_list:
            words = words.replace(i, "")
    print(words)
    
    
    words = words.split(" ")
    print("after split:", words) 
    #print(type(words))
    
    #remove stop_words
    #print(words_copy)
    for i in STOP_WORDS:
        if i in words:
            words.remove(i)
    print("stopwords removed:", words)
    
    #This counts the frequency of the words and adds the key/value pairs to our dictionary
    #List comprehension?? - https://www.educative.io/edpresso/how-to-count-the-number-of-occurrences-of-a-list-item-in-python
    words_dic = (dict((x,words.count(x)) for x in set(words)))
    print("Here's the dictionary:", words_dic)
    
    #removes duplicate words, but how to make count? 
    #for i in words:
        #if i not in words_2:
                #words_2.append(i)
    #print("words_2", words_2)
        #for i in range(0, len(words2)):
        # count the frequency of each word(present in str2) in str and print
            #print(words2[i], ':', words2.count(words2[i]))
            #print(f"{len(lines)} lines in the file.") #can we change this to words?
    #print(type(words_2))   
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
