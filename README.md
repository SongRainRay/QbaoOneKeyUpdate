钱宝宝v1.1
========

####源码说明：


>主程序只有一个:QBao.py ,所以只要搭建了python环境和相应的库，理论上就能直接运行，并生成一个csv文件。
>其他文件（pack.bat,pack.py,files_to_dist/info.txt,files_to_dist/click_me.bat）都是为了
>把QBao.py打包成exe文件并且让使用方便才加上去的如果你想将py文件打包，
>给没装python的windows电脑用，那么打包是最好的方法。

####具体步骤如下：


    1.确保QBao.py在您的环境中运行良好，并能生成csv文件

    2.双击pack.bat，跳出cmd的黑框框，它会帮你调用pack.py文件，pack.py执行打包命令，将QBao.py打包成exe。
      此时会跳出一堆东西，不一会儿，打包结束，按任意键退出

    3.你会发现此时多了两个文件夹build和dist，其中build文件夹可以直接删除，但是dist里面的都得保留

    4.你会发现QBao.exe已经存在于dist文件夹下面了，而且还有其他文件，注意，这个文件夹里面的文件都得保留

    5.files_to_dist文件夹下的两个文件此时可以复制到build文件夹里面，此时click_me.bat就会直接调用QBao.exe，
      并且在生成csv文件之后直接打开该csv

    6.如果你想要把文件复制给没安装python环境的电脑使用，那么做完以上5步，然后把dist发给他们，这样就能运行了



####可能遇到的问题：

1.打开的csv文件乱码：这是编码问题，请[点击这里](http://jingyan.baidu.com/article/adc81513510098f722bf7365.html)
    
