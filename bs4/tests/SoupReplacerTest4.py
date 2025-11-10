from bs4 import BeautifulSoup
from bs4.SoupReplacer import SoupReplacer


def test_name_xformer_multiple_types():
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

    def transform_tags(tag):
        if tag.name == "b":
            return "strong"
        elif tag.name == "i":
            return "em"
        return tag.name

    replacer = SoupReplacer(name_xformer=transform_tags)
    soup = BeautifulSoup(html_content, "html.parser", replacer=replacer)

    result_str = str(soup)

    assert "<b>" not in result_str, "There should be no <b> tags left"
    assert "<i>" not in result_str, "There should be no <i> tags left"
    assert "<strong>" in result_str, "All <b> tags should be replaced with <strong>"
    assert "<em>" in result_str, "All <i> tags should be replaced with <em>"
    print(result_str)


if __name__ == "__main__":
    test_name_xformer_multiple_types()
    print("Test passed!")