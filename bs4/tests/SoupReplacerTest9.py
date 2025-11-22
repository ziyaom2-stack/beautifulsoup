from bs4 import BeautifulSoup


def test_iteration_basic():
   #test the basic iteration function
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

    soup = BeautifulSoup(html_content, "html.parser")

    # test node
    all_nodes = list(soup)
    assert len(all_nodes) > 0, "Should be able to iterate over soup"
    print(f"✓ Total nodes: {len(all_nodes)}")

    # test b labels
    print("\n✓ Found <b> tags:")
    b_tags = [node for node in soup if hasattr(node, 'name') and node.name == 'b']
    for tag in b_tags:
        print(f"  {tag}")
    assert len(b_tags) == 3, f"Should have 3 <b> tags, found {len(b_tags)}"

    # test node with id
    print("\n✓ Found nodes with id attribute:")
    nodes_with_id = [node for node in soup if hasattr(node, 'get') and node.get('id')]
    for node in nodes_with_id:
        print(f"  {node}")
    assert len(nodes_with_id) >= 9, f"Should have at least 9 nodes with id, found {len(nodes_with_id)}"




if __name__ == "__main__":
    test_iteration_basic()