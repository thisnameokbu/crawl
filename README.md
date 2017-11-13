# crawl
下载后用IDE(如pycharm)打开，然后run 'spider_main'
如果没有输出，或者输出结果太少，可能情况如下：
	spider_main.py中root_url 可能已经改变了，百度百科对URL做了处理，原先的URL已经失效
	html_parser.py中links的re.compile内容变了，需要对页面重新分析，确定正则表达式
	
