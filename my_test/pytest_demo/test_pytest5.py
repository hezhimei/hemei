# /usr/bin/env python
# coding:utf-8

'''
用Pytest+Allure生成漂亮的HTML图形化测试报告
1,下载安装allure
2，安装Allure Pytest Adaptor：
    pip install pytest-allure-adaptor
    *注意，因为已经安装allure-pytest ，alluredir冲突会报错
    *解决办法：卸载allure-pytest
3.使用Allure Pytest Adaptor改造基于Pytest的测试用例
首先，conftest.py中可以通过allure.environment方法将测试环境的信息输出到报告中，
比如将测试时用的host和测试用的browser添加到测试报告中：
#!/usr/bin/env python
# coding=utf-8

import pytest
import allure
import yaml

@pytest.fixture(scope="session", autouse=True)
def env(request):
    """
    Parse env config info
    """
    root_dir = request.config.rootdir
    config_path = '{0}/config/env_config.yml'.format(root_dir)
    with open(config_path) as f:
        env_config = yaml.load(f) # 读取配置文件

    allure.environment(host=env_config['host']['domain']) # 测试报告中展示host
    allure.environment(browser=env_config['host']['browser']) # 测试报告中展示browser

    return env_config

接着，在测试脚本中，添加allure特性，直接看下面的脚本，我通过在脚本中添加注释的方式给大家
解释allure特性的用途。比如测试脚本是test_shopping_trolley.py：
#!/usr/bin/env python
# coding=utf-8

import pytest
import allure


@allure.feature('购物车功能')  # feature定义功能
class TestShoppingTrolley(object):
    @allure.story('加入购物车')  # story定义用户场景
    def test_add_shopping_trolley(self):
        login('刘春明', '密码')  # 调用“步骤函数”
        with allure.step("浏览商品"):  # 将一个测试用例分成几个步骤，将步骤打印到测试报告中，步骤2
            allure.attach('商品1', '刘春明')  # attach可以打印一些附加信息
            allure.attach('商品2', 'liuchunming')
        with allure.step("点击商品"):  # 将一个测试用例分成几个步骤，将步骤打印到测试报告中，步骤3
            pass
        with allure.step("校验结果"):
            allure.attach('期望结果', '添加购物车成功')
            allure.attach('实际结果', '添加购物车失败')
            assert 'success' == 'failed'

    @allure.story('修改购物车')
    def test_edit_shopping_trolley(self):
        pass

    @pytest.mark.skipif(reason='本次不执行')
    @allure.story('删除购物车')
    def test_delete_shopping_trolley(self):
        pass


@allure.step('用户登录')  # 还可以将一个函数作为一个步骤，调用此函数时，报告中输出一个步骤，步骤名字通常是函数名，我把这样的函数叫“步骤函数”
def login(user, pwd):
    print(user, pwd)

上面使用了Allure的几个特性：

@allure.feature # 用于定义被测试的功能，被测产品的需求点
@allure.story # 用于定义被测功能的用户场景，即子功能点
with allure.step # 用于将一个测试用例，分成几个步骤在报告中输出
allure.attach # 用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
@pytest.allure.step # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤

3、生成Allure测试报告
测试脚本中添加了Allure特性之后，在执行测试的时候需要先生成Allure报告所需要的测试结果数据。在
py.test执行测试的时候，指定–alluredir选项及测试数据保存的目录即可：

$ py.test test/ --alluredir ./result/

./result/中保存了本次测试的结果数据。另外，还可以执行指定features或者stories执行一部分
测试用例，比如执行‘购物车功能’下的‘加入购物车’子功能的测试用例：

$ py.test test/ --allure_features='购物车功能' --allure_stories='加入购物车'

3.1 命令行方式
3.1.1 安装命令行工具
首先需要安装命令行工具，如果是Mac电脑，推荐使用Homebrew安装。

$ brew install allure
1
3.1.2 生成测试报告
安装完成后，通过下面的命令将./result/目录下的测试数据生成测试报告：

$ allure generate ./result/ -o ./report/ --clean
1
这样在./report/目录下就生成了Allure的测试报告了。–clean目的是先清空测试报告目录，再生
成新的测试报告。

3.1.3 打开测试报告
通过下面的命令打开测试报告：

$ allure open -h 127.0.0.1 -p 8083 ./report/
1
本机的浏览器将打开http://127.0.0.1:8083/index.html网页，展示测试报告。

3.1.4 测试报告解读
打开生成的测试报告后，浏览器被自动调起，展示测试报告。下面我们分别看看测试报告的几个页面。

1，首页
首页中展示了本次测试的测试用例数量，成功用例、失败用例、跳过用例的比例，测试环境信
息，SUITES，FEATURES BY STORIES等基本信息，当与Jenkins做了持续置成后，TREND区
域还将显示，历次测试的通过情况。
首页的左边栏，还从不同的维度展示测试报告的其他信息，大家可以自己点进去看看。
2，Behaviors
接下来，我们点击一下FEATURES BY STORIES，将进入Behaviors页面，这个页面按照FEATURES
和 STORIES展示测试用例的执行结果：
从这个页面可以看到“购物车功能”这个FEATURES包含的三个STORIES的测试用例执行情况。
3，Suites
Allure测试报告将每一个测试脚本，作为一个Suite。在首页点击Suites区域下面的任何一条Suite，
都将进入Suites页面。
4，这个页面，将脚本的目录结果展示本次所有的测试用例执行情况。
测试用例页面
在Suites页面上点击任何一条测试用例，Suites页面的右侧将展示这条用例的详细执行情况。

'''

#生成allure报告
#pytest --alluredir ./test_report/ ./pytest_demo/

#生成测试报告
#allure generate ./ test_report / -o ./ report / --clean



