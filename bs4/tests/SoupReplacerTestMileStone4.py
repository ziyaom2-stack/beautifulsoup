"""Tests for BeautifulSoup Iterable functionality - Milestone 4"""

import pytest
from bs4 import BeautifulSoup, NavigableString


class TestBeautifulSoupIterable:
    """Test cases for Milestone 4: Making BeautifulSoup iterable"""

    def test_iteration_basic(self):
        """Test 1: Basic iteration over soup object"""
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

        print("\n" + "="*60)
        print("Test 1: Basic iteration")
        print("="*60)

        # Test finding specific tags using iteration
        print("\n✓ Found <b> tags:")
        b_tags = [node for node in soup if hasattr(node, 'name') and node.name == 'b']
        for tag in b_tags:
            print(f"  {tag}")
        assert len(b_tags) == 3, f"Should have 3 <b> tags, found {len(b_tags)}"

        # Test finding nodes with id attribute
        print("\n✓ Found nodes with id attribute:")
        #ensure have the get method(not text)
        nodes_with_id = [node for node in soup if hasattr(node, 'get') and node.get('id')]
        for node in nodes_with_id:
            print(f"  {node.name}: id='{node.get('id')}'")

    def test_nested_structure(self):
        """Test 2: Iteration over deeply nested XML structure"""
        xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<root>
<library>
    <book title="Learning XML" author="John Doe">
        <chapter number="1" title="Introduction to XML">
            <section number="1.1" title="What is XML?">
                <paragraph number="1">
                    <sentence>XML stands for eXtensible Markup Language.</sentence>
                    <sentence>It is used to store and transport data.</sentence>
                </paragraph>
                <paragraph number="2">
                    <sentence>XML is both human-readable and machine-readable.</sentence>
                </paragraph>
            </section>
        </chapter>
    </book>
</library>
</root>"""

        soup = BeautifulSoup(xml_content, "lxml-xml")

        print("\n" + "="*60)
        print("Test 2: Nested structure iteration")
        print("="*60)

        # Find all sentence tags using iteration
        print("\n Found all <sentence> tags:")
        sentence_tags = [node for node in soup if hasattr(node, 'name') and node.name == 'sentence']
        for tag in sentence_tags:
            print(f"  {tag.get_text().strip()}")
        assert len(sentence_tags) == 3, f"Should find 3 <sentence> tags, found {len(sentence_tags)}"

        # Find all paragraph tags
        print("\n✓ Found all <paragraph> tags:")
        paragraph_tags = [node for node in soup if hasattr(node, 'name') and node.name == 'paragraph']
        for tag in paragraph_tags:
            print(f"  Paragraph number={tag.get('number')}")
        assert len(paragraph_tags) == 2, f"Should find 2 <paragraph> tags, found {len(paragraph_tags)}"

    def test_text_nodes(self):
        """Test 3: Iteration including text nodes"""
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

        print("\n" + "="*60)
        print("Test 3: Text nodes iteration")
        print("="*60)

        # Get text nodes
        text_nodes = [node for node in soup if hasattr(node, 'name')]
        for tag in text_nodes:
            print(f"  {tag.get_text().strip()}")
        assert len(text_nodes)!=0,f"Should find text tags"


    def test_collect_all_links(self):
        """Test 4: Practical use case - collect all links"""
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

        print("\n" + "="*60)
        print("Test 4: Collect all links")
        print("="*60)

        # Get all <a> tags and their links
        print("✓ Found all <a> tags with href attributes:")
        links = []
        for node in soup:
            if hasattr(node, 'name') and node.name == 'a':
                href = node.get('href')
                text = node.get_text().strip()
                links.append((href, text))
                print(f"  {href} - '{text}'")

        # Should find 3 links
        assert len(links) == 3, f"Should find 3 links, found {len(links)}"

    def test_deep_html_structure(self):
        """Test 5: Iteration over deep HTML structure - document outline"""
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

        print("\n" + "="*60)
        print("Test 5: Deep HTML structure - document outline")
        print("="*60)

        # Get document outline using iteration
        print("✓ Document Outline:")
        outline = []
        for node in soup:
            if hasattr(node, 'name') and node.name in ['h1', 'h2', 'h3']:
                level = int(node.name[1])       #control the indentation
                text = node.get_text().strip()
                outline.append((level, text))
                indent = "  " * (level - 1)
                print(f"{indent}{node.name.upper()}: {text}")

        assert len(outline) == 5, f"Should find 5 headings, found {len(outline)}"