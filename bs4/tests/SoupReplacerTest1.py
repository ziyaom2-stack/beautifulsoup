from bs4 import BeautifulSoup
from bs4.SoupReplacer import SoupReplacer

def test_soupreplacer1():
    html_content = """<!doctype html>
<html lang="zh">
<head>
  <meta charset="utf-8" />
  <title>Tiny Test</title>
</head>
<row>
  <div id="book">
    <section id="chap1">
      <h1 id="title1">Chapter 1</h1>
      <p id="p1">This is the first chapter.</p>
    </section>

    <section id="chap2">
      <h1 id="title2">Chapter 2</h1>
      <p id="p2">This is the second chapter.</p>
    </section>

    <section id="chap3">
      <h1 id="title3">Chapter 3</h1>
      <p id="p3">This is the third chapter.</p>
    </section>
  </div>
</row>
</html>"""

    replacer = SoupReplacer("row", "b")
    soup = BeautifulSoup(html_content, "lxml", replacer=replacer)

    result_str = str(soup)

    # verify the result
    assert "<row" not in result_str, "There should be no <row> tags left"
    assert "<b" in result_str, "All <row> tags should be replaced with <b>"
    print(result_str)  # print the result

if __name__ == "__main__":
    test_soupreplacer1()
