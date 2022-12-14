import re

def display_count(dictionary):
    """
    Custom print function.

    :param dictionary: Dictionary with the information of the counted words.
    """
    print()
    if not dictionary:
        print("No words where entered")
        print()
    for key in dictionary:
        if key:
            time_times = "time" if dictionary[key] == 1 else "times"
            print(f"---> The word \"{key}\" appears in the input sentence {dictionary[key]} {time_times}")
            print()

def word_counter(phrase):
    """
    This function takes a string entered by the user, breaks it into words, and counts the number of repeated words in it.
    Additionally calls the function 'display_count()' to display the collected information on the screen.

    :param phrase: user-entered phrase.
    """
    list_of_phrases = phrase.split()
    counted_words = {}

    for word in list_of_phrases:
        word = re.sub('[^A-Za-z0-9]+', '', word).lower() # removes special characters such as uppercase characters, commas, or question marks
        if word:
            if word not in counted_words:
                counted_words[word] = 1
            else:
                counted_words[word] += 1

    return counted_words

#---------- Main section -------------------------------------------------------
if __name__ == "__main__":
    counted_words = word_counter(input("\nInsert your phrase: "))
    display_count(counted_words)
