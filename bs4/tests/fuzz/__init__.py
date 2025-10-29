import pytest
from bs4 import BeautifulSoup
from bs4 import SoupReplacer  # 替换成你放置 SoupReplacer 的路径


def test_tag_replacement():
    html = "<p>Hello <b>World</b></p>"
    replacer = SoupReplacer("b", "strong")  # <b> 替换成 <strong>

    soup = BeautifulSoup(html, replacer=replacer)

    # 验证替换是否成功
    strong_tag = soup.find("strong")
    assert strong_tag is not None, "替换后的 <strong> 标签没有找到"
    assert strong_tag.string == "World", "替换后的标签内容不正确"

    # 验证原标签不再存在
    b_tag = soup.find("b")
    assert b_tag is None, "<b> 标签应该被替换掉"

    # 打印 prettify 方便调试
    print(soup.prettify())


if __name__ == "__main__":
    pytest.main([__file__])
