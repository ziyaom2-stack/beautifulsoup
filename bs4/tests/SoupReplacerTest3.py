from bs4 import BeautifulSoup
from bs4.SoupReplacer import SoupReplacer

def test_name_xformer_basic():
    html_content = """<!doctype html>
<html lang="zh">
<head>
  <meta charset="utf-8" />
  <title>Tiny Test</title>
</head>
<body>
  <div id="book">
    <section id="chap1">
      <h1 id="title1">Chapter 1</h1>
      <p id="p1">This is the <b>first</b> chapter.</p>
    </section>

    <section id="chap2">
      <h1 id="title2">Chapter 2</h1>
      <p id="p2">This is the <b>second</b> chapter.</p>
    </section>

    <section id="chap3">
      <h1 id="title3">Chapter 3</h1>
      <p id="p3">This is the <b>third</b> chapter.</p>
    </section>
  </div>
</body>
</html>"""

    replacer = SoupReplacer(name_xformer=lambda tag: "strong" if tag.name == "b" else tag.name)
    soup = BeautifulSoup(html_content, "html.parser", replacer=replacer)

    result_str = str(soup)

    assert "<b>" not in result_str, "There should be no <b> tags left"
    assert "<strong>" in result_str, "All <b> tags should be replaced with <strong>"
    assert result_str.count("<strong>") == 3, "Should have 3 <strong> tags"
    print(result_str)

if __name__ == "__main__":
    test_name_xformer_basic()
    print("Test passed!")