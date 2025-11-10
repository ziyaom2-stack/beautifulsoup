import sys
import os
import time
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
from bs4.SoupReplacer import SoupReplacer
from bs4 import BeautifulSoup


def add_test_class(tag):
    if tag.name == "p":
        new_attrs = tag.attrs.copy() if tag.attrs else {}
        new_attrs['class'] = 'test'
        return new_attrs
    return tag.attrs

def main():
    # get the file
    input_file = sys.argv[1]


    # read the file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    start_time = time.time()



    replacer = SoupReplacer(attrs_xformer=add_test_class)

    # deal with the file differently depending on xml or html
    if input_file.endswith('.xml'):
        soup = BeautifulSoup(content, 'lxml-xml',replacer=replacer)  # XML
    else:
        soup = BeautifulSoup(content, 'lxml',replacer=replacer)  # HTML

    end_time = time.time()


    #write to the output file
    if input_file.endswith('.html'):
        output_file = input_file.replace('.html', '_addedclass.html')
    elif input_file.endswith('.xml'):
        output_file = input_file.replace('.xml', '_addedclass.xml')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print(f"output: {output_file}")

    print(f"Total time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()