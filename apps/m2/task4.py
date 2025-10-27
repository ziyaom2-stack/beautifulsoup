import sys
from bs4 import BeautifulSoup,SoupStrainer
import time

def main():
    # get the file
    input_file = sys.argv[1]
    start_time=time.time();


    # read the file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    #only_id_tags
    only_id_tags=SoupStrainer(True,id=True)

    # deal with the file differently depending on xml or html
    if input_file.endswith('.xml'):
        soup = BeautifulSoup(content, 'lxml-xml', parse_only=only_id_tags)
    else:
        soup = BeautifulSoup(content, 'lxml', parse_only=only_id_tags)


    #print all tags
    for tag in soup.find_all(True, id=True):
        print(tag)

    end_time = time.time()
    print(f"Total time: {end_time - start_time:.2f} seconds")




if __name__ == "__main__":
    main()