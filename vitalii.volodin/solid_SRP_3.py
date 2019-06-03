class Content:
    def __init__(self, text=None):
        """
        :param text: (str)
        """
        if text is None:
            self.text = ''
        else:
            self.text = text


class Reader:
    def __init__(self, content):
        self.content = content

    def get_content(self):
        return self.content.text


class TextEditor:
    def __init__(self, content):
        self.text = content.text

    def edit_content(self, words):
        """
        Function returns text without particular words
        :param words: (list) list of words
        """
        remove_words = [word for word in self.text.split() if word not in words]

        edited_text = ' '.join(remove_words)
        return edited_text


def main():
    text = Content('it provide the same functionality')
    reader = Reader(text)
    editor = TextEditor(text)

    print(reader.get_content())
    print(editor.edit_content(['it', 'the']))


if __name__ == '__main__':
    main()