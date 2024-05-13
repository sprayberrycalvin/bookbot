def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(file_contents)}: words found in the document")
    print()
    print()      
    
    for key, value in sorted(letter_count(file_contents).items()):
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")

def word_count(words):
    return len(words.split())

def letter_count(words):
    letters = {}
    
    for letter in words:
        if letter.lower() not in letters.keys():
            letters[letter.lower()] = 1
        else:
            letters[letter.lower()] += 1

    return letters        

if __name__ == '__main__':
    main()