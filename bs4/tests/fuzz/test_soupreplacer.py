# test_soupreplacer.py
import pytest
from bs4 import BeautifulSoup
from bs4 import SoupReplacer


def test_tag_replacement():
    # 1. 创建一个简单 HTML
    html = "<div><oldtag>content</oldtag></div>"

    # 2. 创建一个 SoupReplacer 实例
    replacer = SoupReplacer(og_tag="oldtag", alt_tag="newtag")

    # 3. 使用 BeautifulSoup，并传入 replacer
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    # 4. 验证替换是否生效
    assert str(soup) == "<div><newtag>content</newtag></div>"
