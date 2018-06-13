filename = "srp.txt"
new_file = "prs.txt"
word = "spot"
data = [
    "Two assure edward whence the was.",
    "Who worthy yet ten boy denote wonder.",
    "Weeks views her sight old tears sorry.",
    "Additions can suspected its concealed put furnished.",
    "Met the why particular devonshire decisively considered partiality.",
    "Certain it waiting no entered is.",
    "Passed her indeed uneasy shy polite appear denied.",
    "Oh less girl no walk.",
    "At he spot with five of view."
]


class File(object):

    def __init__(self, file, data):
        """
        :param self.file: filename
        :param self.data: data to be stored into a file
        :return: stored file with data
        """
        self.file = file
        self.data = data

    def store_text(self):
        """
        Function which stored data into the file

        """
        try:
            with open(self.file, 'w') as f:
                for d in self.data:
                    if '\n' in d:
                        f.write(d)
                    else:
                        f.write(d + '\n')
                return self.file
        except(IOError, RuntimeError):
            return []


class WorkWIthFile(File):

    def __init__(self, file, word, new_file=None):
        """
        :param self.file: filename
        :param self.new_file:
        :param self.word: specific word
        :return: stored file or new file which doesn't contains specific word
        """
        self.file = file
        self.word = word
        self.new_file = new_file

    def lookup_word_in_text(self):
        """
        LookUp function which find the specific word in the text

        """
        try:
            with open(self.file, 'r') as f:
                list_of_lines = f.readlines()
                for line in list_of_lines:
                    founded_word_index = line.find(self.word)
                    if founded_word_index != -1:
                        return line[founded_word_index
                                    :founded_word_index+len(self.word)]
                else:
                    raise Exception(mssg="The specific word is not found")
        except(IOError, RuntimeError):
            return []

    def delete_word_in_text(self):
        """
        Function which delete specific word from the text

        """
        try:
            with open(self.file, 'r') as f:
                list_of_lines = f.readlines()
                new_list_of_lines = []
                for line in list_of_lines:
                    founded_word_index = line.find(self.word)
                    if founded_word_index != -1:
                        new_line = line.replace(
                            line[founded_word_index:
                                 founded_word_index+len(self.word) + 1], '')
                        new_list_of_lines.append(new_line)
                    else:
                        new_list_of_lines.append(line)
                else:
                    raise Exception(mssg="The specific word is not found")
        except(IOError, RuntimeError):
            return []

        if new_file is not None:
            File(self.new_file, new_list_of_lines).store_text()
        else:
            File(self.file, new_list_of_lines).store_text()
        return


if __name__ == "__main__":
    st = File(filename, data).store_text()
    b = WorkWIthFile(st, word, new_file)
    b.lookup_word_in_text()
    b.delete_word_in_text()
