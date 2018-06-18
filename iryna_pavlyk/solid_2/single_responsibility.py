"""
This module describes a homework related to SOLID.
"""
__author__ = "Iryna Pavlyk"
__email__ = "iruska.m1@ukr.net"

FILENAME = "text.txt"
my_text = [
    "My name is Ira.",
    "I have a petfff.",
    "It is a dog.",
    "Its name is Sparky."
]


class TextHandler:

    def write_to_file(self, data, filename):
        """
        This function writes text from `data` into file with `filename`.

        Args:
            filename (str) - name of file for writing.
            data (list, tuple) - lines of text which should be added into file.
        """
        try:
            with open(filename, 'w') as file:
                for row in data:
                    file.write(row + '\n')
        except (OSError, IOError):
            print("An Error has occurred!")


    def read_file(self, filename):
        """
        This function reads all the lines from the file with `filename`.

        Args:
            filename (str) - name of file for reading text.

        Returns:
            text - list of lines from the file.
        """
        try:
            with open(filename, 'r') as file:
                text = file.read()
                text = text.strip().split("\n")
                return text
        except (OSError, IOError):
            print("An Error has occurred!")

    def change_word(self, old_word, new_word, filename):
        """
        This function finds word and change it from an old value to
         a new value from `filename`.

        Args:
            old_word (str) - word from the text has to be changed.
            new_word(str) - new value of old_word after changing.

        Returns:
            list - list of lines from the file.
        """
        text = TextHandler.read_file(self, filename)
        for line in text:
            index = text.index(line)
            if old_word in line:
                line = line.replace(old_word, new_word)
                text[index] = line
        return TextHandler.write_to_file(self, text, filename)


if __name__ == '__main__':
    handler_1 = TextHandler()
    handler_1.write_to_file(my_text, FILENAME)
    print(handler_1.read_file(FILENAME))
    handler_1.change_word("dog", "cat", FILENAME)
    print(handler_1.read_file(FILENAME))
    handler_1.change_word("fff", "", FILENAME)
    print(handler_1.read_file(FILENAME))
