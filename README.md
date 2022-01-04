### 关于

本软件是用python3.9.0编写和测试的，不过其他 Python 版本几乎可以在所有情况下使用。

本软件旨在监控一些特定界面是否出现想要的关键词或者消失了关键词，通过机器人自动化工作代替人工监控，节省人力。

### 开发环境搭建

#### 1.安装python环境

双击python-3.9.0.exe根据提示进行安装python环境

#### 2.安装python依赖包

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple playsound
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple selenium
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple tkinter
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller
```

#### 3.对程序进行exe打包

```
pyinstaller -F -w AutoRefresh.py --noconsole
```

#### 4.chromedriver下载

参考教程https://blog.csdn.net/lly1122334/article/details/106217320查看当前chrome版本号，根据版本号搜[谷歌浏览器驱动镜像](http://npm.taobao.org/mirrors/chromedriver/)，将下载的driver放到sup目录下。

#### 5.chrome浏览器安装

若无chrome浏览器，双击90.0.4430.212_chrome_installer_32.exe进行安装

### 使用

1.双击AutoRefresh.exe后，在网站地址框内输入网站地址后点击打开即可打开目标网站。

2.输入关键词，选择包含按钮，输入刷新频率（单位为秒），点击自动刷新后，即可监控当前网址界面是否包含该关键词，若包含即会响起音乐，若不包含即自动刷新，直到出现关键词为止，期间可以通过点击关闭刷新停止程序刷新功能。同理选择不包含按钮，即会在当前界面不出现关键词时响起音乐提示。

3.点击退出工具按钮即可退出工具。

![Snipaste_2022-01-04_20-59-03](https://user-images.githubusercontent.com/97103228/148068223-afca4008-6125-4e0a-8e1c-2d464c834c8d.jpg)

