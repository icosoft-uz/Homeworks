class ReverseText:
    def __init__(self, original_text):
        self.original_text = original_text

    def restr(self):
        words = self.original_text.split()
        reversed_text = ' '.join(reversed(words))
        return reversed_text


def main():
    input_text = input("Enter text: ")

    reverse_text_instance = ReverseText(input_text)
    reversed_result = reverse_text_instance.restr()

    print("Original Text:", input_text)
    print("Reversed Text:", reversed_result)


if __name__ == "__main__":
    main()
