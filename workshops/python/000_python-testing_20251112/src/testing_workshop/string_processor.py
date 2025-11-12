"""String processor for TDD demonstration."""


class StringProcessor:
    """String processing utilities - implement during TDD workshop."""

    def reverse(self, text: str) -> str:
        """Reverse a string - TDD Green phase implementation."""
        return text[::-1]

    def count_vowels(self, text: str) -> int:
        """Count vowels in text - TDD Green phase implementation."""
        vowels = "aeiouAEIOU"
        return sum(1 for char in text if char in vowels)

    def is_palindrome(self, text: str) -> bool:
        """Check if text is palindrome - TDD Green phase implementation."""
        clean_text = text.lower().replace(" ", "")
        return clean_text == clean_text[::-1]
