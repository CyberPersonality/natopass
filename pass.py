def nato_translator(text):
    nato_map = {
        'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
        'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
        'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
        'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 'Y': 'Yankee',
        'Z': 'Zulu',
        '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
        '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine',
        '.': 'Dot', ',': 'Comma', '?': 'QuestionMark', '!': 'ExclamationMark',
        '@': 'AtSign', '#': 'Hash', '$': 'Dollar', '%': 'Percent', '^': 'Caret',
        '&': 'And', '*': 'Star', '(': 'OpenParenthesis', ')': 'CloseParenthesis',
        '-': 'Hyphen', '_': 'Underscore', '=': 'Equals', '+': 'Plus', '/': 'Slash',
        '\\': 'Backslash', '[': 'OpenBracket', ']': 'CloseBracket', '{': 'OpenBrace',
        '}': 'CloseBrace', ';': 'Semicolon', ':': 'Colon', "'": 'Apostrophe',
        '"': 'Quote', '<': 'LessThan', '>': 'GreaterThan', ' ': 'Space'
    }

    translated_parts = []
    for char in text.upper():
        if char in nato_map:
            translated_parts.append(nato_map[char])
        else:
            translated_parts.append(f"<{char}>")

    return ''.join(translated_parts)

if __name__ == "__main__":
    print("--- NATO Phonetic Alphabet Translator ---")
    print("Enter text to translate. Press Enter to confirm.")
    print("Type 'exit' to quit.")
    print("-----------------------------------------")

    while True:
        user_input = input("Your text: ")

        if user_input.lower() == 'exit':
            print("Exiting program.")
            break

        if not user_input.strip():
            print("No input provided. Please enter text or 'exit'.")
            continue

        translated_output = nato_translator(user_input)
        print(f"\nTranslated to NATO Phonetic:\n{translated_output}\n")