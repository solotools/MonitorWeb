# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 10:31
# @Author  : 李佳玮
# @Email   : lijiawei@symbio.com
# @File    : test.py
# @Software: PyCharm
import time
from pprint import pprint

import psutil
import os

# print(psutil.Process(11748).name())
# print(u'当前进程的内存使用：%.4f GB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024 / 1024) )
# print (u'电脑开机时间：{}'.format(time.strftime('%y-%m-%d %H:%M:%S', time.localtime(psutil.boot_time()))))

# print(len(psutil.Process(30128).open_files()))
from psutil._common import snicstats

# print(psutil.Process(30128).parents())
# print(psutil.Process(40448).children())
# print(psutil.Process(40448).cpu_percent(interval=1))
# # print(psutil.Process(11748).name())  # 进程名
# # print(psutil.Process(11748).exe())  # 进程的bin路径
# # print(psutil.Process(11748).cwd())
# print(psutil.Process(40448).status())  # 进程运行状态
# # print(psutil.Process(11748).create_time())  # 进程创建时间戳
# # print(psutil.Process(11748).cpu_times())  # 进程的cpu时间信息,包括user,system两个cpu信息
# print(u'%.4f' % psutil.Process(40448).memory_percent())  # 进程内存利用率
# # print(psutil.Process(11748).memory_info())  # 进程内存rss,vms信息
# print(psutil.Process(40448).io_counters())  # 进程io信息
# # print(psutil.Process(11748).connections())  # 返回进程列表
# # print(psutil.Process(11748).num_threads())  # 进程开启的线程数
# # print(psutil.net_io_counters(pernic=True))
# # print(psutil.Process(30128).memory_info())
# print(psutil.net_connections())
# print(u'%.4f MB' % (psutil.Process(40448).memory_info().rss / 1024 / 1024))
# print(u'%.4f MB' % (psutil.Process(40448).memory_info().vms / 1024 / 1024))

pprint(psutil.disk_usage("C:\\").percent)
pprint(psutil.users())