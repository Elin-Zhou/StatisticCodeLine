# StatisticCodeLine
#统计代码行数
###用法

    #代码根路径
	path = "/yumei/code_new/"
    
	#参数为需要解析的文件拓展名
	statistic = Statistic(path, ".java", ".jsp")
	statistic.resolve()


目前仅支持 UTF-8 和 GBK编码