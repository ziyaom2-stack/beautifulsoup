"""Tests for SoupReplacer functionality - Milestone 3"""

import pytest
from bs4 import BeautifulSoup
from bs4.SoupReplacer import SoupReplacer


class TestSoupReplacerMilestone3:
    """Test cases for Milestone 3: SoupReplacer with transformer functions"""

    # shared HTML
    HTML_CONTENT = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Test Document</title>
</head>
<body>
  <div id="content" class="container">
    <section id="sec1" class="section">
      <h1>Section 1</h1>
      <p class="text">Text with <b>bold</b> and <i>italic</i> words.</p>
      <a href="http://example.com/page1">Link 1</a>
    </section>

    <section id="sec2" class="section">
      <h1>Section 2</h1>
      <p class="text">More <b>bold</b> and <i>italic</i> text here.</p>
      <a href="http://example.com/page2">Link 2</a>
    </section>

    <section id="sec3" class="section">
      <h1>Section 3</h1>
      <p class="text">Another <b>bold</b> and <i>italic</i> example.</p>
      <a href="https://secure.com/page3">Link 3</a>
    </section>
  </div>
</body>
</html>"""

    # shared XML
    XML_CONTENT = """<?xml version="1.0" encoding="utf-8"?>
<root>
  <document id="doc1" class="container">
    <section id="sec1" class="section">
      <title>Section 1</title>
      <paragraph class="text">Text with <bold>bold</bold> and <italic>italic</italic> words.</paragraph>
      <link href="http://example.com/page1">Link 1</link>
    </section>

    <section id="sec2" class="section">
      <title>Section 2</title>
      <paragraph class="text">More <bold>bold</bold> and <italic>italic</italic> text here.</paragraph>
      <link href="http://example.com/page2">Link 2</link>
    </section>

    <section id="sec3" class="section">
      <title>Section 3</title>
      <paragraph class="text">Another <bold>bold</bold> and <italic>italic</italic> example.</paragraph>
      <link href="https://secure.com/page3">Link 3</link>
    </section>
  </document>
</root>"""

    def test_name_xformer_html(self):
        """Test 1: name_xformer with HTML - transform b to strong, i to em"""

        replacer = SoupReplacer(
            name_xformer=lambda tag: "strong" if tag.name == "b"
            else "em" if tag.name == "i"
            else tag.name
        )
        soup = BeautifulSoup(self.HTML_CONTENT, "html.parser", replacer=replacer)
        result_str = str(soup)


        print("Test 1: name_xformer HTML (b->strong, i->em)")
        print("="*60)
        print(result_str)
        print("="*60)

        # Verify transformations
        assert "<b>" not in result_str, "No <b> tags should remain"
        assert "<i>" not in result_str, "No <i> tags should remain"
        assert "<strong>" in result_str, "Should have <strong> tags"
        assert "<em>" in result_str, "Should have <em> tags"

    def test_name_xformer_xml(self):
        """Test 2: name_xformer with XML - transform bold to strong, italic to em"""

        def transform_tags(tag):
            if tag.name == "bold":
                return "strong"
            elif tag.name == "italic":
                return "em"
            return tag.name

        replacer = SoupReplacer(name_xformer=transform_tags)
        soup = BeautifulSoup(self.XML_CONTENT, "lxml-xml", replacer=replacer)
        result_str = str(soup)


        print("Test 2: name_xformer XML (bold->strong, italic->em)")
        print("="*60)
        print(result_str)
        print("="*60)

        # Verify transformations
        assert "<bold>" not in result_str, "No <bold> tags should remain"
        assert "<italic>" not in result_str, "No <italic> tags should remain"
        assert "<strong>" in result_str, "Should have <strong> tags"
        assert "<em>" in result_str, "Should have <em> tags"

    def test_attrs_xformer_html(self):
        """Test 3: attrs_xformer with HTML - convert http to https"""

        def transform_attrs(tag):
            new_attrs = tag.attrs.copy() if tag.attrs else {}
            # Convert http to https in href attributes
            if tag.name == "a" and 'href' in new_attrs:
                if new_attrs['href'].startswith('http://'):
                    new_attrs['href'] = new_attrs['href'].replace('http://', 'https://')

            return new_attrs

        replacer = SoupReplacer(attrs_xformer=transform_attrs)
        soup = BeautifulSoup(self.HTML_CONTENT, "html.parser", replacer=replacer)
        result_str = str(soup)

        print("\n" + "="*60)
        print("Test 3: attrs_xformer HTML")
        print("="*60)
        print(result_str)
        print("="*60)

        # Verify transformations
        assert 'http://example.com' not in result_str, "No http:// URLs should remain"
        assert 'https://example.com/page1' in result_str, "URLs should be https"
        assert 'https://example.com/page2' in result_str, "URLs should be https"

    def test_attrs_xformer_xml(self):
        """Test 4: attrs_xformer with XML - convert http to https"""

        def transform_attrs(tag):
            new_attrs = tag.attrs.copy() if tag.attrs else {}
            # Convert http to https in href attributes
            if tag.name == "link" and 'href' in new_attrs:
                if new_attrs['href'].startswith('http://'):
                    new_attrs['href'] = new_attrs['href'].replace('http://', 'https://')

            return new_attrs

        replacer = SoupReplacer(attrs_xformer=transform_attrs)
        soup = BeautifulSoup(self.XML_CONTENT, "lxml-xml", replacer=replacer)
        result_str = str(soup)

        print("\n" + "="*60)
        print("Test 4: attrs_xformer XML")
        print("="*60)
        print(result_str)
        print("="*60)

        # Verify transformations
        assert 'http://example.com' not in result_str, "No http:// URLs should remain"
        assert 'https://example.com/page1' in result_str, "URLs should be https"
        assert 'https://example.com/page2' in result_str, "URLs should be https"

    def test_xformer_html(self):
        """Test 5: xformer with HTML - remove all class attributes"""

        def remove_class_attr(tag):
            if "class" in tag.attrs:
                del tag.attrs["class"]

        replacer = SoupReplacer(xformer=remove_class_attr)
        soup = BeautifulSoup(self.HTML_CONTENT, "html.parser", replacer=replacer)
        result_str = str(soup)

        print("\n" + "="*60)
        print("Test 5: xformer HTML - remove class attributes")
        print("="*60)
        print(result_str)
        print("="*60)

        # Verify transformations
        assert 'class="' not in result_str, "No class attributes should remain"


    def test_xformer_xml(self):
        """Test 6: xformer with XML - remove all class attributes"""

        def remove_class_attr(tag):
            if "class" in tag.attrs:
                del tag.attrs["class"]

        replacer = SoupReplacer(xformer=remove_class_attr)
        soup = BeautifulSoup(self.XML_CONTENT, "lxml-xml", replacer=replacer)
        result_str = str(soup)

        print("\n" + "="*60)
        print("Test 6: xformer XML - remove class attributes")
        print("="*60)
        print(result_str)
        print("="*60)

        # Verify transformations
        assert 'class="' not in result_str, "No class attributes should remain"
