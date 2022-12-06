import os

class FileReader:

    @staticmethod
    def read_lines(path=".", filename="input.txt"):
        lines = None
        with open(os.path.join(path, filename), 'r') as f:
            lines = [line.strip() for line in f]