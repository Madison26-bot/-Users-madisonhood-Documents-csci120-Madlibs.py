"""Mad libs.test.py
AUTHOR: Madison Hood
"""

import unittest
from Madlibs import (
    sample_stories,
    check_input,
    display_menu,
    play_mad_libs,
    words_list,
    generate_word_for_blanks,
    check_blanks,
    prompt_user_for_words,
    get_random_story,
    get_user_input,
    get_story,
    select_story_letter,
)


def test_select_story_letter():
    # test that the user can input a lowercase letter and it will still be accepted
    assert select_story_letter("a") == "A. If you give a..."
    assert select_story_letter("b") == "B. Halloween Fun"
    assert select_story_letter("c") == "C. Banky's Sticky Situation"
    assert select_story_letter("d") == "D. Random Story"

    # test that the user can input an uppercase letter and it will be accepted
    assert select_story_letter("A") == "A. If you give a..."
    assert select_story_letter("B") == "B. Halloween Fun"
    assert select_story_letter("C") == "C. Banky's Sticky Situation"
    assert select_story_letter("D") == "D. Random Story"

    # test for all invalid inputs
    assert (
        select_story_letter("e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z")
        == "Invalid input. Please select a story by entering the corresponding letter (A-D)."
    )
    assert (
        select_story_letter("1, 2, 3, 4, 5, 6, 7, 8, 9, 0")
        == "Invalid input. Please select a story by entering the corresponding letter (A-D)."
    )
    assert (
        select_story_letter("!@#$%^&*()_+-=~`")
        == "Invalid input. Please select a story by entering the corresponding letter (A-D)."
    )
    assert (
        select_story_letter("")
        == "Invalid input. Please select a story by entering the corresponding letter (A-D)."
    )


if __name__ == "__main__":
    unittest.main()
    print("All tests passed!")
