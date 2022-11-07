import pytest
from src.word_counter import word_counter, display_count

# ------------ Testing main logical function ---------------------------------------------
@pytest.mark.parametrize(
    ['phrase', 'output'],
    [
        ("Hi, how are you?", {"hi": 1, "how": 1, "are": 1, "you": 1}),
        ("Hi, ho(w a,re you?", {"hi": 1, "how": 1, "are": 1, "you": 1}),
        ("hi, how how how?", {"hi": 1, "how": 3}),
        ("", {}),
        ("Hi,", {"hi": 1}),
        ("you are how hi, how are you you", {"you": 3, "are": 2, "how": 2, "hi": 1}),
        ("Here is my secret. It is quite simple. One sees clearly only with the heart. What is essential is invisible to the eye.", {"here": 1, "is": 4, "my": 1, "secret": 1, "it": 1, "quite": 1, "simple": 1, "one": 1, "sees": 1, "clearly": 1, "only": 1, "with": 1, "the": 2, "heart": 1, "what": 1, "essential": 1, "invisible": 1, "to": 1, "eye": 1}),
        ("...........", {}),
        ("Hi, how are you?", {"hi": 1, "how": 1, "are": 1, "you": 1}),
        ("Testing dictionaries with pytest it's really fun ...", {"testing": 1, "dictionaries": 1, "with": 1, "pytest": 1, "its": 1, "really": 1, "fun": 1}),
    ]
)
def test_word_counter(phrase, output):
    """
    :param phrase: a string to be processed
    :param output: a dictionary listing avery single word in the phrase as a key, and the number of times (int) this phrase appears as a value
    """
    assert word_counter(phrase) == output
