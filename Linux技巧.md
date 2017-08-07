# Linux补充

1. ### Tab自动补全

2. 快捷键

   | 按键              | 作用                       |
   | --------------- | ------------------------ |
   | `Ctrl+d`        | 键盘输入结束或退出终端              |
   | `Ctrl+s`        | 暂停当前程序，暂停后按下任意键恢复运行      |
   | `Ctrl+z`        | 将当前程序放到后台运行，恢复到前台为命令`fg` |
   | `Ctrl+a`        | 将光标移至输入行头，相当于`Home`键     |
   | `Ctrl+e`        | 将光标移至输入行末，相当于`End`键      |
   | `Ctrl+k`        | 删除从光标所在位置到行末             |
   | `Alt+Backspace` | 向前删除一个单词                 |
   | `Shift+PgUp`    | 将终端显示向上滚动                |
   | `Shift+PgDn`    | 将终端显示向下滚动                |

3. Shell 常用通配符

   | 字符                      | 含义                              |
   | ----------------------- | ------------------------------- |
   | `*`                     | 匹配 0 或多个字符                      |
   | `?`                     | 匹配任意一个字符                        |
   | `[list]`                | 匹配 list 中的任意单一字符                |
   | `[!list]`               | 匹配 除list 中的任意单一字符以外的字符          |
   | `[c1-c2]`               | 匹配 c1-c2 中的任意单一字符 如：[0-9] [a-z] |
   | `{string1,string2,...}` | 匹配 string1 或 string2 (或更多)其一字符串 |
   | `{c1..c2}`              | 匹配 c1-c2 中全部字符 如{1..10}         |

4. 获取命令帮助

   ```
   man [num] <command_name>
   ```

   | 区段   | 说明                     |
   | ---- | ---------------------- |
   | 1    | 一般命令                   |
   | 2    | 系统调用                   |
   | 3    | 库函数，涵盖了C标准函数库          |
   | 4    | 特殊文件（通常是/dev中的设备）和驱动程序 |
   | 5    | 文件格式和约定                |
   | 6    | 游戏和屏保                  |
   | 7    | 杂项                     |
   | 8    | 系统管理命令和守护进程            |

   **NAME（名称）**

   > 该命令或函数的名称，接着是一行简介。

   **SYNOPSIS（概要）**

   > 对于命令，正式的描述它如何运行，以及需要什么样的命令行参数。对于函数，介绍函数所需的参数，以及哪个头文件包含该函数的定义。

   **DESCRIPTION（说明）**

   > 命令或函数功能的文本描述。

   **EXAMPLES（示例）**

   > 常用的一些示例。

   **SEE ALSO（参见）**

   > 相关命令或函数的列表。

5. 查看用户

   `who` 命令其它常用参数

   | 参数   | 说明                  |
   | ---- | ------------------- |
   | `-a` | 打印能打印的全部            |
   | `-d` | 打印死掉的进程             |
   | `-m` | 同`am i`,`mom likes` |
   | `-q` | 打印当前登录用户数及用户名       |
   | `-u` | 打印当前登录用户登录信息        |
   | `-r` | 打印运行等级              |

6. 创建用户

   ```
   sudo adduser <username>
   ```

7. 授予root权限

   ```
   su root  #切换到拥有root权限的用户
   sudo usermod -G sudo <username>   #授权
   groups <username>  #查看用户组
   ```

8. 删除用户

   ```
   sudo deluser <username> --remove-home
   ```

9. 文件权限

   我们之前已经很多次用到 `ls` 命令了，如你所见，我们用它来列出并显示当前目录下的文件，当然这是在不带任何参数的情况下，它能做的当然不止这么多，现在我们就要用它来查看文件权限。

   使用较长格式列出文件：

   ```
   $ ls -l

   ```

   ![img](https://dn-anything-about-doc.qbox.me/linux_base/3-8.png/logoblackfont)

   你可能除了知道最后面那一项是文件名之外，其它项就不太清楚了，那么到底是什么意思呢：

   ![img](https://dn-anything-about-doc.qbox.me/linux_base/3-9.png/logoblackfont)

   可能你还是不太明白，比如第一项文件类型和权限那一堆东西具体指什么，链接又是什么，何为最后修改时间，下面一一道来：

   ![img](https://dn-anything-about-doc.qbox.me/linux_base/3-10.png/logoblackfont)

   - 文件类型

   关于文件类型，这里有一点你必需时刻牢记 **Linux 里面一切皆文件**，正因为这一点才有了设备文件（ `/dev` 目录下有各种设备文件，大都跟具体的硬件设备相关）这一说。 `socket`：网络套接字，具体是什么，感兴趣的用户可以自己去了解或期待实验楼的后续相关课程。`pipe` 管道，这个东西很重要，我们以后将会讨论到，这里你先知道有它的存在即可。`软链接文件`：链接文件是分为两种的，另一种当然是“硬链接”（硬链接不常用，具体内容不作为本课程讨论重点，而软链接等同于 Windows 上的快捷方式,你记住这一点就够了）。

   - 文件权限

   读权限，表示你可以使用 `cat <file name>` 之类的命令来读取某个文件的内容；写权限，表示你可以编辑和修改某个文件；

   执行权限，通常指可以运行的二进制程序文件或者脚本文件，如同 Windows 上的 `exe` 后缀的文件，不过 Linux 上不是通过文件后缀名来区分文件的类型。你需要注意的一点是，**一个目录同时具有读权限和执行权限才可以打开并查看内部文件，而一个目录要有写权限才允许在其中创建其它文件**，这是因为目录文件实际保存着该目录里面的文件的列表等信息。

   所有者权限，这一点相信你应该明白了，至于所属用户组权限，是指你所在的用户组中的所有其它用户对于该文件的权限，比如，你有一个艾派德，那么这个用户组权限就决定了你的兄弟姐妹有没有权限使用它破坏它和占有它。

   - 链接数

   > 链接到该文件所在的 inode 结点的文件名数目（关于这个概念涉及到 Linux 文件系统的相关概念知识，不在本课程的讨论范围，感兴趣的用户可以自己去了解）。

   - 文件大小

   > 以 inode 结点大小为单位来表示的文件大小，你可以给 ls 加上 `-lh` 参数来更直观的查看文件的大小。

   明白了文件权限的一些概念，我们顺带补充一下关于 `ls` 命令的一些其它常用的用法：

   - 显示除了 `.`（当前目录）和 `..`（上一级目录）之外的所有文件，包括隐藏文件（Linux 下以 `.` 开头的文件为隐藏文件）。

   ```
   $ ls -A

   ```

   ![img](https://dn-anything-about-doc.qbox.me/linux_base/3-11.png/logoblackfont)

   当然，你可以同时使用 `-A` 和 `-l` 参数：

   ```
   $ ls -Al

   ```

   查看某一个目录的完整属性，而不是显示目录里面的文件属性：

   ```
   $ ls -dl <目录名>

   ```

   - 显示所有文件大小，并以普通人类能看懂的方式呈现：

   ```
   $ ls -AsSh

   ```

   其中小 s 为显示文件大小，大 S 为按文件大小排序，若需要知道如何按其它方式排序，请使用“man”命令查询。

10. 更改文件所有者

   ```
   sudo chown shiyanlou iphone6
   ```

11. 修改文件权限

    - 二进制数字表示

    ![img](https://dn-anything-about-doc.qbox.me/linux_base/3-14.png/logoblackfont)

    ```
    chmod 700 <filename>
    ```

    - 方式二：加减赋值操作

    完成上述相同的效果，你可以：

    ```
    chmod go-rw iphone6
    ```

    `g`、`o` 还有 `u` 分别表示 group、others 和 user，`+` 和 `-` 分别表示增加和去掉相应的权限

12. `adduser `和 `useradd `的区别

    答:useradd 只创建用户，创建完了用 passwd lilei 去设置新用户的密码。adduser 会创建用户，创建目录，创建密码（提示你设置），做这一系列的操作。其实 useradd、userdel 这类操作更像是一种命令，执行完了就返回。而 adduser 更像是一种程序，需要你输入、确定等一系列操作。

13. 文件目录

    ![img](https://dn-anything-about-doc.qbox.me/linux_base/4-1.png/logoblackfont)

14. 创建空白文件

    ```
    touch <filename>
    ```

15. 批量重命名

    ```
    # 使用通配符批量创建 5 个文件:
    $ touch file{1..5}.txt

    # 批量将这 5 个后缀为 .txt 的文本文件重命名为以 .c 为后缀的文件:
    $ rename 's/\.txt/\.c/' *.txt

    # 批量将这 5 个文件，文件名改为大写:
    $ rename 'y/a-z/A-Z/' *.c
    ```

16. 查看文件类型

    ```
    file <filename>
    ```

17. 添加自定义路径到"PATH"环境变量

    ```
    PATH=$PATH:/home/shiyanlou/mybin  #当前shell有效
    echo "PATH=$PATH:/home/shiyanlou/mybin" >> .zshrc  #添加至开启shell时启动
    source .zshrc  #让环境变量立即生效
    ```

18. 压缩打包

    * zip压缩打包过程

      ```
      $ zip -r -q -o shiyanlou.zip /home/shiyanlou
      $ du -h shiyanlou.zip
      $ file shiyanlou.zip
      ```

      上面命令将目录 /home/shiyanlou 打包成一个文件，并查看了打包后文件的大小和类型。第一行命令中，`-r` 参数表示递归打包包含子目录的全部内容，`-q` 参数表示为安静模式，即不向屏幕输出信息，`-o`，表示输出文件，需在其后紧跟打包输出文件名。后面使用 `du` 命令查看打包后文件的大小（后面会具体说明该命令）。

      - 设置压缩级别为 9 和 1（9 最大，1 最小），重新打包：

      ```
      $ zip -r -9 -q -o shiyanlou_9.zip /home/shiyanlou -x ~/*.zip
      $ zip -r -1 -q -o shiyanlou_1.zip /home/shiyanlou -x ~/*.zip
      ```

      这里添加了一个参数用于设置压缩级别 `-[1-9]`，1 表示最快压缩但体积大，9 表示体积最小但耗时最久。最后那个 `-x` 是为了排除我们上一次创建的 zip 文件，否则又会被打包进这一次的压缩文件中，**注意：这里只能使用绝对路径，否则不起作用**。

      - 创建加密 zip 包

        $ zip -r -e -o shiyanlou_encryption.zip /home/shiyanlou

      - Windows 兼容处理

        $ zip -r -l -o shiyanlou.zip /home/shiyanlou

    * zip解压

      ```
      $ unzip shiyanlou.zip
      $ unzip -q shiyanlou.zip -d ziptest
      $ unzip -l shiyanlou.zip
      unzip -O GBK 中文压缩文件.zip
      ```

    * rar打包

      - 安装 `rar` 和 `unrar` 工具：

      ```
      $ sudo apt-get update
      $ sudo apt-get install rar unrar

      ```

      - 从指定文件或目录创建压缩包或添加文件到压缩包：

      ```
      $ rm *.zip
      $ rar a shiyanlou.rar .

      ```

      上面的命令使用 `a` 参数添加一个目录 `～` 到一个归档文件中，如果该文件不存在就会自动创建。

      **注意：rar 的命令参数没有 -，如果加上会报错。**

      - 从指定压缩包文件中删除某个文件：

      ```
      $ rar d shiyanlou.rar .zshrc

      ```

      - 查看不解压文件：

      ```
      $ rar l shiyanlou.rar

      ```

      - 使用 `unrar` 解压 `rar` 文件

      全路径解压：

      ```
      $ unrar x shiyanlou.rar

      ```

      去掉路径解压：

      ```
      $ mkdir tmp
      $ unrar e shiyanlou.rar tmp/

      ```

      **rar 命令参数非常多，上面只涉及了一些基本操作。**

    * tar打包

      在 Linux 上面更常用的是 `tar` 工具，tar 原本只是一个打包工具，只是同时还是实现了对 7z、gzip、xz、bzip2 等工具的支持，这些压缩工具本身只能实现对文件或目录（单独压缩目录中的文件）的压缩，没有实现对文件的打包压缩，所以我们也无需再单独去学习其他几个工具，tar 的解压和压缩都是同一个命令，只需参数不同，使用比较方便。

      下面先掌握 `tar` 命令一些基本的使用方式，即不进行压缩只是进行打包（创建归档文件）和解包的操作。

      - 创建一个 tar 包：

      ```
      $ tar -cf shiyanlou.tar ~

      ```

      ![img](https://dn-anything-about-doc.qbox.me/linux_base/6-4.png)

      上面命令中，`-c` 表示创建一个 tar 包文件，`-f` 用于指定创建的文件名，注意文件名必须紧跟在 `-f` 参数之后，比如不能写成 `tar -fc shiyanlou.tar`，可以写成 `tar -f shiyanlou.tar -c ~`。你还可以加上 `-v` 参数以可视的的方式输出打包的文件。上面会自动去掉表示绝对路径的 `/`，你也可以使用 `-P` 保留绝对路径符。

      - 解包一个文件（`-x` 参数）到指定路径的**已存在**目录（`-C` 参数）：

      ```
      $ mkdir tardir
      $ tar -xf shiyanlou.tar -C tardir

      ```

      - 只查看不解包文件 `-t` 参数：

      ```
      $ tar -tf shiyanlou.tar

      ```

      - 保留文件属性和跟随链接（符号链接或软链接），有时候我们使用 tar 备份文件当你在其他主机还原时希望保留文件的属性（`-p` 参数）和备份链接指向的源文件而不是链接本身（`-h` 参数）：

      ```
      $ tar -cphf etc.tar /etc

      ```

      对于创建不同的压缩格式的文件，对于 tar 来说是相当简单的，需要的只是换一个参数，这里我们就以使用 `gzip`工具创建 `*.tar.gz` 文件为例来说明。

      - 我们只需要在创建 tar 文件的基础上添加 `-z` 参数，使用 `gzip` 来压缩文件：

      ```
      $ tar -czf shiyanlou.tar.gz ~

      ```

      - 解压 `*.tar.gz` 文件：

      ```
      $ tar -xzf shiyanlou.tar.gz

      ```

      ![img](https://dn-anything-about-doc.qbox.me/linux_base/6-5.png/logoblackfont)

      现在我们要使用其它的压缩工具创建或解压相应文件只需要更改一个参数即可：

      | 压缩文件格式     | 参数   |
      | ---------- | ---- |
      | `*.tar.gz` | `-z` |
      | `*.tar.xz` | `-J` |
      | `*tar.bz2` | `-j` |

      > tar 命令的参数很多，不过常用的就是上述这些，需要了解更多你可以查看 man 手册获取帮助。
      >
      > 常用命令：
      >
      > - zip：
      >   - 打包 ：zip something.zip something （目录请加 -r 参数）
      >   - 解包：unzip something
      >   - 指定路径：-d 参数
      > - tar：
      >   - 打包：tar -zcvf something.tar something
      >   - 解包：tar -zxvf something.tar
      >   - 指定路径：-C 参数

19. 定时任务

    ```
    #启动(默认会自动开启)
    sudo cron -f &
    #添加任务
    crontab -e
    #添加命令文件
    * * * * * command
    */5 * * * * /home/dmtsai/test.sh  #每5分钟执行一次test.sh
    #查看是否在执行
    pgrep cron
    #查看任务列表
    crontab -l
    #移除任务(注意:这里是移除所有任务,若想移除单个,需要crontab -e编辑文件)
    crontab -r
    ```

    ```
    # Example of job definition:
    # .---------------- minute (0 - 59)
    # |  .------------- hour (0 - 23)
    # |  |  .---------- day of month (1 - 31)
    # |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
    # |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
    # |  |  |  |  |
    # *  *  *  *  * user-name command to be executed

    ```

    | 特殊字符   | 代表意義                                     |
    | ------ | ---------------------------------------- |
    | *(星號)  | 代表任何時刻都接受的意思！舉例來說，範例一內那個日、月、週都是 * ， 就代表著『不論何月、何日的禮拜幾的 12:00 都執行後續指令』的意思！ |
    | ,(逗號)  | 代表分隔時段的意思。舉例來說，如果要下達的工作是 3:00 與 6:00 時，就會是：0 3,6 * * * command時間參數還是有五欄，不過第二欄是 3,6 ，代表 3 與 6 都適用！ |
    | -(減號)  | 代表一段時間範圍內，舉例來說， 8 點到 12 點之間的每小時的 20 分都進行一項工作：20 8-12 * * * command仔細看到第二欄變成 8-12 喔！代表 8,9,10,11,12 都適用的意思！ |
    | /n(斜線) | 那個 n 代表數字，亦即是『每隔 n 單位間隔』的意思，例如每五分鐘進行一次，則：*/5 * * * * command很簡單吧！用 * 與 /5 來搭配，也可以寫成 0-59/5 ，相同意思！ |

    | 代表意義 | 分鐘   | 小時   | 日期   | 月份   | 週    | 指令    |
    | ---- | ---- | ---- | ---- | ---- | ---- | ----- |
    | 數字範圍 | 0-59 | 0-23 | 1-31 | 1-12 | 0-7  | 呀就指令啊 |

20. 执行多条命令

    ```
    $ sudo apt-get update;sudo apt-get install some-tool;some-tool
    ```

    ​
