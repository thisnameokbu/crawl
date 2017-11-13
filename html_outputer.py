#coding:utf8
class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)


    def output_html(self):
        fout = open('output.html', 'w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<head><meta charset='utf-8'></head>")
        fout.write("<table width='80%' border='3px solid #000' style='word-break:break-all'>")

        for data in self.datas:
            fout.write("<tr>")

            fout.write("<td width='10%'>")
            fout.write("%s" % data['url'])
            fout.write("</td>")

            fout.write("<td width='10%'>")
            fout.write("%s" % data['title'])
            fout.write("</td>")
            fout.write("<td>%s</td>" % data['summary'])

            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()