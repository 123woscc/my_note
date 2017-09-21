#百度云离线VPS下载器

### 1.安装LAMP 

一键安装地址:[秋水逸冰LAMP脚本](lamp.sh/install.html)

### 2.安装h5ai文件管理系统

下载h5ai然后解压:[官网](https://larsjung.de/h5ai/)

```shell
cd /data/www/default
wget https://release.larsjung.de/h5ai/h5ai-0.28.1.zip
apt-get install unzip 
unzip h5ai*.zip
```

配置h5ai

```shell
cd _h5ai
chmod 666 private/cache 
chmod 666 public/cache
Movie thumbs视频预览,执行:
apt-get install libav-tools
PDF thumbsPDF预览,执行:
apt-get install aptitude
aptitude install imagemagick
Shell zipzip预览,执行:
apt-get install zip
```

配置Apache文件

```
vi /usr/local/apache/conf/extra/httpd-vhosts.conf

修改配置文件,增加一行
DirectoryIndex index.html index.php /_h5ai/public/index.php
删除default文件夹中的index文件
重启Apache
/etc/init.d/httpd (start|stop|restart|status)
```

### 3.百度云配置

####a.安装百度云脚本

1. 安装编译依赖

```
apt update
apt install build-essential dh-autoreconf dpkg-dev libssl-dev libcurl4-openssl-dev
```

2. 获取源代码

```
git clone https://github.com/GangZhuo/BaiduPCS.git

```

3. 构建打包

```
cd BaiduPCS
dpkg-buildpackage -us -uc -i -b
```

4. 安装

```
cd ..
sudo apt install ./baidupcs_*.deb
```

#### b.配置百度云

```
baidupcs set --max_thread=100
pcs set --captcha_file=/data/www/default/captcha.gif
```

#### c.登录百度云

```
baidupcs login
```

#### d.下载文件

````
浏览目录
baidupcs ls
切换目录
baidupcs cd <dir>
下载文件
baidupcs d '百度云文件的路径' '保存到本地的文件名'
````

### 4.Linux提速技巧

TCP_BBR一键安装脚本:https://doub.io/wlzy-16/



### *参考

[百度云网盘不限速 命令行下载工具 —— BaiduPCS 使用教程](https://doub.io/wlzy-35/)

[GitHub:BaiduPCS](https://github.com/GangZhuo/BaiduPCS)

[搭建h5ai文件服务器/个人下载站/以及参数设置功能开启](https://ipe6.com/?p=354)