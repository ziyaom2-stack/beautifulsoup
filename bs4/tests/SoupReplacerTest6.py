from bs4 import BeautifulSoup
from bs4.SoupReplacer import SoupReplacer


def test_attrs_xformer_modify_links():
    """Test 4: Modify href attributes - convert http to https"""
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

    def make_https(tag):
        if tag.name == "a" and 'href' in tag.attrs:
            new_attrs = tag.attrs.copy()
            if new_attrs['href'].startswith('http://'):
                new_attrs['href'] = new_attrs['href'].replace('http://', 'https://')
            return new_attrs
        return tag.attrs

    replacer = SoupReplacer(attrs_xformer=make_https)
    soup = BeautifulSoup(xml_content, "lxml-xml", replacer=replacer)

    result_str = str(soup)


    assert 'http://example.com' not in result_str, "No http:// URLs should remain"
    print(result_str)


if __name__ == "__main__":
    test_attrs_xformer_modify_links()
    print("✅ Test 4 passed!")