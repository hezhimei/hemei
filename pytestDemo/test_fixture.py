# /usr/bin/env python
# coding:utf-8

import pytest


@pytest.fixture(scope="module", autouse=True)
def open_browser():
    print("\n打开浏览器，打开百度首页")

    yield

    print("执行teardown")
    print("最后关闭浏览器")

def test_sousuo(login):
    print("case1:登录后执行搜索")

def test_chakan():
    print("case2:不登录就查看")

def test_cart(login):
    print("case3:登录，加购物车")

if __name__ == '__main__':
    if __name__ == '__main__':
        pytest.main(['-s', 'test_fixture.py'])
