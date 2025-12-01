"""Tests for the replace functionality - Milestone 2"""

import pytest
from bs4 import BeautifulSoup
from bs4.SoupReplacer import SoupReplacer

#
class TestSoupReplacerMilestone2:

    def test_html_replacement(self):
        """Test basic tag replacement in HTML documents."""
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

        #replace row label with div label
        replacer = SoupReplacer("row", "div")
        soup = BeautifulSoup(html_content, "html.parser", replacer=replacer)
        result_str = str(soup)
        print(result_str)

        # Verify the replacement occurred
        assert "<row" not in result_str, "There should be no <row> tags left"
        assert "<div" in result_str, "All <row> tags should be replaced with <div>"

    def test_xml_replacement(self):
        """Test tag replacement in XML documents with lxml parser."""
        xml_content = """<?xml version="1.0" encoding="utf-8"?>
<root>
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
</root>"""

        #replace the row label with b label
        replacer = SoupReplacer("row", "b")
        soup = BeautifulSoup(xml_content, "lxml-xml", replacer=replacer)
        result_str = str(soup)
        print(result_str)

        # Verify the replacement occurred
        assert "<row" not in result_str, "There should be no <row> tags left"
        assert "<b" in result_str, "All <row> tags should be replaced with <b>"