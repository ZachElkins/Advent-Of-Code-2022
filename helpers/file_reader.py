import os

class FileReader:

    @staticmethod
    def read_lines(path=".", filename="input.txt"):
        lines = None
        with open(os.path.join(path, filename), 'r') as f:
            lines = [line.strip() for line in f]
        return lines

    @staticmethod
    def read_lines_raw(path=".", filename="input.txt"):
        lines = None
        with open(os.path.join(path, filename), 'r') as f:
            lines = [line for line in f]
        return lines

    @staticmethod
    def read_line(path=".", filename="input.txt"):
        return FileReader.read_lines(path, filename)[0]