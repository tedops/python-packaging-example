import argparse

class WordPrinter(object):
    def __init__(self, args):
        self.args = args


    def ensure_necessary_args_exist(self):
        if self.args.word:
            return True

        return False


    def run(self):
        if self.ensure_necessary_args_exist():
            print("The word you entered is: {0}".format(self.args.word))
        else:
            print("No word entered")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--word", help="Word to print")
    args = parser.parse_args()
    wp = WordPrinter(args)
    wp.run()
