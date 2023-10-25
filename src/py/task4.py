def match_string(sentence, word):
    index = sentence.find(word)
    return index


def main():
    sentence = input("Enter a sentence: ")
    word = input("Enter a word: ")

    index = match_string(sentence, word)

    if index is not None:
        print(f"The word '{word}' matches the sentence at index {index}.")
    else:
        print("No match found.")


if __name__ == "__main__":
    main()
