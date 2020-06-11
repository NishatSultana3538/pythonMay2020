import os
import shutil
from os import path


def main():
    # make a duplicate of an existence file
    if path.exists("abc.txt"):
        # get the path to the file in the current directory
        src = path.realpath("abc.txt")

    # rename the original file
    os.rename('abc.txt', 'pythonTest.text')


if __name__ == "__main__":
    main()
