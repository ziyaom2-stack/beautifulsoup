from bs4 import BeautifulSoup
from bs4.SoupReplacer import SoupReplacer


def test_attrs_xformer_add_class():
    """Test 3: Add class attribute to all <p> tags"""
    html_content = """<!doctype html>
<html lang="zh">
<head>
  <meta charset="utf-8" />
  <title>Multiple Tag Types Test</title>
</head>
<body>
  <div id="content">
    <section id="sec1">
      <h1>Section 1</h1>
      <p>Text with <b>bold</b> and <i>italic</i> words.</p>
    </section>

    <section id="sec2">
      <h1>Section 2</h1>
      <p>More <b>bold</b> and <i>italic</i> text here.</p>
    </section>

    <section id="sec3">
      <h1>Section 3</h1>
      <p>Another <b>bold</b> and <i>italic</i> example.</p>
    </section>
  </div>
</body>
</html>"""

    def add_test_class(tag):
        if tag.name == "p":
            new_attrs = tag.attrs.copy() if tag.attrs else {}
            new_attrs['class'] = 'test'
            return new_attrs
        return tag.attrs

    replacer = SoupReplacer(attrs_xformer=add_test_class)
    soup = BeautifulSoup(html_content, "html.parser", replacer=replacer)

    result_str = str(soup)
    paragraphs = soup.find_all('p')
    for p in paragraphs:
        assert 'class' in p.attrs, "Each <p> should have class attribute"
        assert p.attrs['class'] == 'test', "Class should be 'test'"

    assert 'class="test"' in result_str, "Result should contain class='test'"
    print(result_str)


if __name__ == "__main__":
    test_attrs_xformer_add_class()
    print("✅ Test 3 passed!")