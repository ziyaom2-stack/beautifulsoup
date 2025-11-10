from bs4 import BeautifulSoup
from bs4.SoupReplacer import SoupReplacer


def test_combined_transformers():
    """Test 6: Use name_xformer and attrs_xformer together"""
    xml_content = """<?xml version="1.0" encoding="utf-8"?>
<root>
<row>
  <div id="book">
    <section id="chap1">
      <h1 id="title1">Chapter 1</h1>
      <p id="p1">Text with <b class="old">bold</b> word.</p>
    </section>

    <section id="chap2">
      <h1 id="title2">Chapter 2</h1>
      <p id="p2">More <b>bold</b> text.</p>
    </section>

    <section id="chap3">
      <h1 id="title3">Chapter 3</h1>
      <p id="p3">Another <b class="old">bold</b> example.</p>
    </section>
  </div>
</row>
</root>"""

    def change_name(tag):
        if tag.name == "b":
            return "strong"
        return tag.name

    def add_data_attr(tag):
        if tag.name in ["b", "strong"]:
            new_attrs = tag.attrs.copy() if tag.attrs else {}
            new_attrs['data-new'] = 'yes'
            return new_attrs
        return tag.attrs

    replacer = SoupReplacer(name_xformer=change_name, attrs_xformer=add_data_attr)
    soup = BeautifulSoup(xml_content, "lxml-xml", replacer=replacer)

    result_str = str(soup)

    assert "<b>" not in result_str and "<b " not in result_str, "No <b> tags should remain"
    assert result_str.count("<strong") == 3, "Should have 3 <strong> tags"
    assert result_str.count('data-new="yes"') == 3, "All <strong> tags should have data-new"

    print(result_str)


if __name__ == "__main__":
    test_combined_transformers()
    print("✅ Test 6 passed!")