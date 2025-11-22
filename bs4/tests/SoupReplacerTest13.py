from bs4 import BeautifulSoup


def test_deep_html_structure():
    #test deep html content
    html_content = """<!DOCTYPE html>
<html>
<body>
    <div class="container">
        <article class="book">
            <h1>Learning XML</h1>
            <section class="chapter">
                <h2>Chapter 1: Introduction</h2>
                <div class="section">
                    <h3>1.1 What is XML?</h3>
                    <p>XML stands for eXtensible Markup Language.</p>
                </div>
            </section>
            <section class="chapter">
                <h2>Chapter 2: Syntax</h2>
                <div class="section">
                    <h3>2.1 Basic Rules</h3>
                    <p>XML documents must have a root element.</p>
                </div>
            </section>
        </article>
    </div>
</body>
</html>"""

    soup = BeautifulSoup(html_content, "html.parser")

    # get the outline
    print("✓ Document Outline:")
    outline = []
    for node in soup:
        if hasattr(node, 'name') and node.name in ['h1', 'h2', 'h3']:
            level = int(node.name[1])
            text = node.get_text().strip()
            outline.append((level, text))
            indent = "  " * (level - 1)
            print(f"{indent}{node.name.upper()}: {text}")

    assert len(outline) == 5, f"Should find 5 headings, found {len(outline)}"


    print("\nTest passed!")


if __name__ == "__main__":
    test_deep_html_structure()