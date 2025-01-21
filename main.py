def count_words(text):
    return len(text.split())

def count_chars(text):
    char_counts = {}
    for c in 'abcdefghijklmnopqrstuvwxyz':
        char_counts[c] = 0         
    lowertext = text.lower()
    for c in lowertext:  
        if c in char_counts:
            char_counts[c] +=  1
           # else:
           #     char_counts[c] = 1
    return char_counts
    
def read_file(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def print_char_counts(dict):
    for e in dict:
        print(f"The 'e.key' character was found e.value times")

def main():
    fpath = "books/frankenstein.txt"
    contents = read_file(fpath)
    print(count_chars(contents))


main()

