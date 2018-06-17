class TextWorkflow:
    def write_file(self, file_name, input):
        with open(file_name, 'w') as _file:
            return _file.write(input)
    def read_file(self, file_name):
        with open(file_name, 'r') as _file:
            return _file.read()
    def is_word_in_text(self, file_text, word):
        if word in file_text:
            return True
        return False
    def delete_word(self, file_text, word):
        updated_text = file_text.replace(word, "")
        return updated_text

text = TextWorkflow()
text.write_file("test_file.txt", "This is test input")
content = text.read_file("test_file.txt")
print(content)
is_in_text = text.is_word_in_text(content, "test")
if is_in_text:
    print(text.delete_word(content, " test"))
