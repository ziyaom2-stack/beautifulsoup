from bs4 import BeautifulSoup


def test_collect_all_links():
    #test get all links
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

    # get all a labels and links
    print("✓ Found all <a> tags with href attributes:")
    links = []
    for node in soup:
        if hasattr(node, 'name') and node.name == 'a':
            href = node.get('href')
            text = node.get_text().strip()
            links.append((href, text))
            print(f"  {href} - '{text}'")

    # 3 links
    assert len(links) == 3, f"Should find 3 links, found {len(links)}"



if __name__ == "__main__":
    test_collect_all_links()