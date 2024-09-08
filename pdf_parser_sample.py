# 这个脚本是我帮金融的同学写的，主要功能是从已有的财报中统计关键词。写好后我用pyinstaller生成exe文件，方便没有计算机基础的人运行。这里做个备份
import datetime
import jieba
import os
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator

path = 'data'
write_path = 'final_result.csv'

password = ''

if not os.path.exists(write_path):
    with open(write_path, 'a', encoding='UTF-8', errors='ignore') as wp:
        wp.write('股票代码,公司,年份,创新,创造,研发,变革,总字数\n')

start = datetime.datetime.now()

step=0
file_list = os.listdir(path)
for pdfs in file_list:
    step = step + 1
    print('Processing the ' + str(step) + 'th file in ' + str(len(file_list)) + ' files\n')
    if '英文版' in pdfs:
        continue
    word_cnt = 0
    chuangxin = 0
    yanfa = 0
    biange = 0
    chuangzao = 0

    PDF_path = os.path.join(path,pdfs)
    inform = pdfs.split('年年度报告')[0]
    year = inform[-4:]
    code = inform[0:6]
    company = inform[6:-4]
    if company[-1] == 'A' or company[-1] == 'B' or company[-1] == '：':
        company = company[0:-1]

    with open(PDF_path, 'rb')as fp:  # 以二进制读模式打开
        parser = PDFParser(fp)  # 用文件对象来创建一个pdf文档分析器
        document = PDFDocument(parser,password)  # 创建一个PDF文档

        # 创建一个pdf资源管理对象，存储共享资源
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        # 创建一个device对象
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # 创建一个解释对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        # 处理包含在文档中的每一页
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if isinstance(x, LTTextBox):
                    result = x.get_text().strip()
                    word_cnt = word_cnt + len(result)
                    word = jieba.cut(result)
                    for x in word:
                        if '创新' in x:
                            chuangxin = chuangxin + 2
                        elif '创造' in x:
                            chuangzao = chuangzao + 2
                        elif '研发' in x:
                            yanfa = yanfa + 2
                        elif '变革' in x:
                            biange = biange + 2

    with open(write_path, 'a', encoding='UTF-8', errors='ignore') as wp:
      wp.write(code + ',' + company + ',' + year + ',' + str(chuangxin) + ',' + str(chuangzao) + ',' + str(yanfa) + ',' + str(biange) + ',' + str(word_cnt) +'\n')

    end = datetime.datetime.now()
    print('Total time spent:')
    print(end - start)

 #   input('Press <Enter>')





