# coding:utf8
from test import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()#URL管理器
        self.downloader = html_downloader.HtmlDownLoader()#下载器
        self.parser = html_parser.HtmlParser()#解析器
        self.outputer = html_outputer.HtmlOutputer()#应用

    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d:%s"%(count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 5:
                    break
                count = count + 1
            except Exception as e:
                print(e)

        self.outputer.output_html()






#if __name__ == "main":
root_url = "http://baike.baidu.com/item/Python"
obj_spider = SpiderMain()
obj_spider.craw(root_url)


