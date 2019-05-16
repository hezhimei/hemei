# /usr/bin/env python
# coding:utf-8

import pytest

@pytest.fixture()
def login():
    print("登录了")