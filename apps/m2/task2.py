import sys
from bs4 import BeautifulSoup,SoupStrainer
import time

def main():
    # get the file
    input_file = sys.argv[1]
    start_time = time.time();

    # read the file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # deal with the file differently depending on xml or html
    if input_file.endswith('.xml'):
        a_tags=SoupStrainer('a')
        soup = BeautifulSoup(content, 'lxml-xml',parse_only=a_tags)  # XML
    else:
        a_tags = SoupStrainer('a')
        soup = BeautifulSoup(content, 'lxml',parse_only=a_tags)  # HTML


    #print all <a> tags
    links = soup.find_all('a')
    for link in links:
        print(link)

    end_time = time.time()
    print(f"Total time: {end_time - start_time:.2f} seconds")




if __name__ == "__main__":
    main()