import sys
import os

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from bs4 import BeautifulSoup


def main():
    # get the file
    input_file = sys.argv[1]

    # read the file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # parse the file
    if input_file.endswith('.xml'):
        soup = BeautifulSoup(content, 'lxml-xml')
    else:
        soup = BeautifulSoup(content, 'html.parser')

    # iterate over all nodes
    for node in soup:
        print(node)


if __name__ == "__main__":
    main()