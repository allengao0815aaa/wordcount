# wordcount

安装：

爬虫文件直接通过pycharm运行

wordcount在hadoop虚拟机上操作


通过BeautifulSoup爬取环球网英文版10000个新闻页面的文字内容，得到一个29.4MB的txt文件。 然后启动hadoop，并将txt文件上传到HDFS分布式文件系统中。最后运行mapreduce程序 wordcount进行统计，通过分布式的批量处理，比传统方式更快得处理得到每个单词出现的次数。
