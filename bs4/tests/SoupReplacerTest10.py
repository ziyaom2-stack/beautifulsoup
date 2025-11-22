from bs4 import BeautifulSoup, SoupReplacer


def test_nested_structure():
    #test nested structure
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<root>
<library>
    <book title="Learning XML" author="John Doe">
        <chapter number="1" title="Introduction to XML">
            <section number="1.1" title="What is XML?">
                <paragraph number="1">
                    <sentence>XML stands for eXtensible Markup Language.</sentence>
                    <sentence>It is used to store and transport data.</sentence>
                </paragraph>
                <paragraph number="2">
                    <sentence>XML is both human-readable and machine-readable.</sentence>
                </paragraph>
            </section>
        </chapter>
    </book>
</library>
</root>"""


    soup = BeautifulSoup(xml_content, "lxml-xml")

    print("=== Verification with find_all ===")
    sentences_findall = soup.find_all('sentence')
    print(f"find_all found {len(sentences_findall)} sentence tags")

    # find all sentence
    print("\n✓ Found all <sentence> tags:")
    sentence_tags = [node for node in soup if hasattr(node, 'name') and node.name == 'sentence']
    for tag in sentence_tags:
        print(f"  {tag}")
    assert len(sentence_tags) == 3, f"Should find 3 <sentence> tags, found {len(sentence_tags)}"

    # find all paragraph
    print("\n✓ Found all <paragraph> tags:")
    paragraph_tags = [node for node in soup if hasattr(node, 'name') and node.name == 'paragraph']
    for tag in paragraph_tags:
        print(f"  {tag}")
    assert len(paragraph_tags) == 2, f"Should find 2 <paragraph> tags, found {len(paragraph_tags)}"

    # find deep attributes
    print("\n✓ Found <book> tag with attributes:")
    book_tags = [node for node in soup if hasattr(node, 'name') and node.name == 'book']
    for tag in book_tags:
        print(f"  title: {tag.get('title')}")
        print(f"  author: {tag.get('author')}")
    assert len(book_tags) == 1, "Should find 1 <book> tag"

    print("\nTest passed!")


if __name__ == "__main__":
    test_nested_structure()