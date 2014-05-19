@echo off
color 3E
mode con cols=26 lines=15
echo  -----------------------
echo         钱宝宝v1.1 
echo  -----------------------
echo *************************
echo        祝您财运亨通！
echo *************************
echo 欲知更多，请看 "说明.txt"
echo     正在读取钱宝数据

QBao.exe
echo  -----------------------
echo       正在打开文件

qbao.csv

puase