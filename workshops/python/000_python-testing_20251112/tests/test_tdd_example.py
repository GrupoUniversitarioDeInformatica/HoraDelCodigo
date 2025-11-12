"""TDD Example - String Processor (for workshop demonstration)."""


# TDD Step 1: Write failing test first


def test_reverse_string():
    """Test string reversal - TDD Red phase."""
    from src.testing_workshop.string_processor import StringProcessor

    processor = StringProcessor()
    assert processor.reverse("hello") == "olleh"


def test_count_vowels():
    """Test vowel counting - TDD Red phase."""
    from src.testing_workshop.string_processor import StringProcessor

    processor = StringProcessor()
    assert processor.count_vowels("hello") == 2
    assert processor.count_vowels("xyz") == 0


def test_is_palindrome():
    """Test palindrome detection - TDD Red phase."""
    from src.testing_workshop.string_processor import StringProcessor

    processor = StringProcessor()
    assert processor.is_palindrome("racecar")
    assert not processor.is_palindrome("hello")


# Ping Pong Programming:
# Person A writes test, Person B makes it pass
# Person B writes next test, Person A makes it pass
