from bs4 import BeautifulSoup
from bs4.SoupReplacer import SoupReplacer


def test_xformer_remove_attributes():
    """Test 5: Use xformer to remove class attributes"""
    xml_content = """<?xml version="1.0" encoding="utf-8"?>
<root>
<row>
  <div id="book">
    <section id="chap1" class="class">
      <h1 id="title1" class="class">Chapter 1</h1>
      <p id="p1" class="class">This is the first chapter.</p>
    </section>

    <section id="chap2" class="class">
      <h1 id="title2">Chapter 2</h1>
      <p id="p2" class="class">This is the second chapter.</p>
    </section>

    <section id="chap3" class="class" data-value="keep">
      <h1 id="title3" class="class">Chapter 3</h1>
      <p id="p3">This is the third chapter.</p>
    </section>
  </div>
</row>
</root>"""

    def remove_class_attr(tag):
        if "class" in tag.attrs:
            del tag.attrs["class"]

    replacer = SoupReplacer(xformer=remove_class_attr)
    soup = BeautifulSoup(xml_content, "lxml-xml", replacer=replacer)

    result_str = str(soup)

    assert 'class="class"' not in result_str, "No class attributes should remain"


    print(result_str)


if __name__ == "__main__":
    test_xformer_remove_attributes()
    print("✅ Test 5 passed!")