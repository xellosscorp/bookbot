from collections import Counter

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_num_words(text)
    print(f"{num_words} are in Frankenstein.")
    char_counts = count_char_occurrences(text)
    #sorted_char_counts = alphabetize_char_counts(char_counts)
    sorted_char_counts = sort_by_count_desc(char_counts)
    print("Character Counts (Alphabetized):")
    for char, count in sorted_char_counts.items():
        if not char.isspace():
            print(f"Character '{char}': {count}")

def sort_by_count_desc(char_counts):
    """Sorts character counts in descending order of count."""
    return dict(sorted(char_counts.items(), key=lambda item: item[1], reverse=True))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_num_words(text):
    words = text.split()
    return len(words)

def count_char_occurrences(text):
    """Counts occurrences of each character in the text (case-insensitive)."""
    text = text.lower()  # Convert text to lowercase
    return Counter(text)

def alphabetize_char_counts(char_counts):
    """Alphabetizes the character counts dictionary."""
    return dict(sorted(char_counts.items()))

if __name__ == "__main__":
    main()