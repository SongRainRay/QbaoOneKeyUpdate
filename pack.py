#coding:utf-8
'''这只是个打包用的代码，会被pack.bat文件调用，目的是把Qbao.py打包成exe文件，
供没装python的使用，打包用的库叫 py2exe'''
from distutils.core import setup
import py2exe
setup(console=["QBao.py"])