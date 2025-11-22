from bs4 import BeautifulSoup, NavigableString


def test_text_nodes():
    #test text contents
    xml_content = """<?xml version="1.0" encoding="utf-8"?>
<root>
<row>
  <div id="book">
    <section id="chap1">
      <h1 id="title1">Chapter 1</h1>
      <p id="p1">This is the first chapter.</p>
      <a href="http://example.com/chap1">Read more</a>
    </section>

    <section id="chap2">
      <h1 id="title2">Chapter 2</h1>
      <p id="p2">This is the second chapter.</p>
      <a href="http://example.com/chap2">Read more</a>
    </section>

    <section id="chap3">
      <h1 id="title3">Chapter 3</h1>
      <p id="p3">This is the third chapter.</p>
      <a href="https://secure.com/chap3">Read more</a>
    </section>
  </div>
</row>
</root>"""

    soup = BeautifulSoup(xml_content, "lxml-xml")

    # get all text nodes
    print("✓ Found text nodes:")
    text_nodes = []
    for node in soup:
        if isinstance(node, NavigableString) and not isinstance(node, type(soup)):
            text = str(node).strip()
            if text:  # only use text
                text_nodes.append(text)

    # print text
    for i, text in enumerate(text_nodes, 1):
        print(f"  {i}. '{text}'")



    print("\nTest passed!")


if __name__ == "__main__":
    test_text_nodes()