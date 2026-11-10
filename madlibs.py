"""
Mad libs.py
Runs a madlibs game where the user can select a story and fill in the blanks with their own words.
With the output being 80 characters wide, the user can select a story and fill in the blanks with their own words.


AUTHOR: Madison Hood
"""

import random


Sample_stories = [
    "A. If you give a...",
    "B. Halloween Fun",
    "C. Banky's Sticky Situation",
    "D. Random Story",
]


def words_list():
    """Making sure that the story is 80 characters wide"""
    return [
        "noun",
        "plural noun",
        "will, be , or have",
        "biting, flying or cooking",
        "generous, short or fuzzy",
        "pinky toe, eyelid, or elbow",
        "zebra, giraffe, or elephant",
        "pizza, sushi, or ice cream",
    ]


words = []
try:
    with open("words.txt", "r") as f:
        words = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    pass  # If the file doesn't exist, we just use the default words_list
return words


def generate_word_for_blanks():
    """When there is no input from the user, the function generates a random filler word"""
    return random.choice(words_list())


def check_blanks(story):
    """Checking if the story has any blanks"""
    return "<blank>" in story


def prompt_user_for_words():
    """Prompting the user for words to fill in the blanks"""
    return input("Please enter a word to fill in the blank: ")


def play_mad_libs():
    """Main function to play the Madlibs game"""
    story = random.choice(Sample_stories)
    while check_blanks(story):
        word = prompt_user_for_words()
        story = story.replace("<blank>", word, 1)
    print(story)


def check_input(word):
    """Checking if the input is valid"""
    return word in Sample_stories


def display_menu():
    """Displaying the menu for the user to select a story"""
    print("Welcome to Mad libs!")
    print("Please select a story:")
    for i, story in enumerate(Sample_stories):
        print(f"{i + 1}. {story}")
    selection = input("Enter the number of the story you want to play: ")
    if check_input(selection):
        return Sample_stories[int(selection) - 1]
    else:
        print("Invalid selection. Please try again.")
        return display_menu()


def get_random_story():
    """ ""Generating a possible random story for choice D."""
    return random.choice(Sample_stories)


def get_user_input():
    """Gets input from user to keep everything organized."""
    return input("Please select a story (A, B, C, D): ")


def get_story(selection):
    """Gathering the user's story and keeping the format of the story."""
    if selection == "A":
        return Sample_stories[0]
    elif selection == "B":
        return Sample_stories[1]
    elif selection == "C":
        return Sample_stories[2]
    elif selection == "D":
        return get_random_story()
    else:
        print("Invalid selection. Please try again.")
        return get_user_input()


def ask_play_again():
    """Once the game is over, ask if the user would like to play again."""
    return input("Would you like to play again? (yes/no): ").lower() == "yes"


def main():
    """Main function to run the Mad libs game."""
    while True:
        selection = get_user_input()
        story = get_story(selection)
        print(story)
        if not ask_play_again():
            break


if __name__ == "__main__":
    main()
