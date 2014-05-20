#coding:utf-8
import urllib,urllib2,re,codecs
from string import punctuation
from operator import itemgetter

url = "http://www.qianbao666.com"
one_page = "/ntask/home.html?co=0&po=0&ti=0&re=0&mr=0&mrb=&mre=&ty=11&p="
detail="http://www.qianbao666.com/ntask/loadAdvTaskInfo.html"
suffix = []
allItems = []

def getData(url):
    response = urllib2.urlopen(url)
    data = response.read().decode('utf-8')
    return data

def postData(url,para):
    sendData = urllib.urlencode(para)
    request = urllib2.Request(url,sendData)
    response = urllib2.urlopen(request)
    data = response.read().decode('utf-8')
    return data

def crawl():
    data = getData(url+one_page+'1')
    page = int(re.findall('var totalPage = (\d*?)\;',data)[0]) #页数
    #print 'total page is:',page
    for i in range(1,page+1):
        data = getData(url+one_page+str(i))
        suffix.extend(re.findall('<a href="(.*?)" title="点击查看任务详情">'.decode('utf-8'),data))
    #print suffix
    for i in range(len(suffix)):
        if suffix[i].startswith('/task'): #老版本任务
            #print suffix[i]
            data = getData(url+suffix[i])
            taskName = re.findall('ellipsis;" title="(.*?)"',data)[0]
            margins = int(re.findall('<span class="textTitle titleRwbzj"></span><span class="money2">(\d*?)</span>',data)[0])
            totalReward = int(re.findall('<span class="textTitle titleRwsy"></span><span class="money">(\d*?)</span>',data)[0])
            totalNum = int(re.findall('<span class="textTitle titleGgts"></span><span class="money2">(\d*?)</span>',data)[0])
            oneDayNum = int(re.findall('<span class="textTitle titleGgsx"></span><span class="money2">(\d*?)</span>',data)[0])
            totalDays = totalNum/oneDayNum
            keyNum = 10000.0*totalReward/totalDays/margins
            item = [suffix[i],taskName,margins,totalReward,totalDays,keyNum,' ',url+suffix[i]]
            if re.findall(u'任务时长：(.*?)。',data) == []:
                item.insert(7,' ')
            else:
                isVideo = re.findall(u'任务时长：(.*?)。',data)[0]
                item.insert(7,u'视频时长：'+isVideo)
            allItems.append(item)
            '''for key in item:
                print key'''
        else: #新版本任务
            #print suffix[i]
            taskId = re.findall('\d+',suffix[i])[0]
            info = {'taskId':taskId}
            data = postData(detail,info)
            taskName = re.findall('"taskName":"(.*?)"',data)[0]
            margins = int( str(re.findall('"margins":"(.*?)"',data)[0]).translate(None, punctuation))
            totalReward = int( str(re.findall('"totalReward":"(.*?)"',data)[0]).translate(None, punctuation))
            totalNum = int( str(re.findall('"totalNum":(\d*?),',data)[0]).translate(None, punctuation))
            oneDayNum = int( str(re.findall('"oneDayNum":(\d*?),',data)[0]).translate(None, punctuation))
            totalDays = totalNum/oneDayNum
            keyNum = 10000.0*totalReward/totalDays/margins
            item = [suffix[i],taskName,margins,totalReward,totalDays,keyNum,url+suffix[i]]
            limitDay = re.findall(',"limitDay":(\d*?),',data)[0]
            limitNum = re.findall(',"limitNum":(\d*?)}',data)[0]

            if limitDay =='0':#无限制
                item.insert(6,' ')
            else:#有限制
                constraint = u'每'+limitDay+u'天限领'+limitNum+u'次'
                item.insert(6,constraint)
            if re.findall(u'任务时长：(.*?)。',data) == []:
                item.insert(7,' ')
            else:
                isVideo = re.findall(u'任务时长：(.*?)。',data)[0]
                item.insert(7,u'视频时长：'+isVideo)
            allItems.append(item)
    return allItems

def generateCSV():
    sortedItem = sorted(crawl(), key=itemgetter(5,2),reverse=True)
    header_format = '%-s,%-s,%-s,%-s,%-s,%-s,%-s,%-s\n'
    header = (u'任务名'.encode('utf-8'),u'保证金/钱宝币'.encode('utf-8'),u'总收益/钱宝币'.encode('utf-8'),u'总天数'.encode('utf-8') \
                      ,u'日万份收益/元'.encode('utf-8'),u'限制'.encode('utf-8'),u'备注'.encode('utf-8'),u'链接'.encode('utf-8'))
    item_format = '%-s,%-d,%-d,%-d,%-.3f,%-s,%-s,%-s\n'
    with open('qbao.csv', 'w') as f:
        f.write(codecs.BOM_UTF8)
        f.write(header_format % header)
        for item in sortedItem:
            itemk = (item[1].encode('utf-8'),item[2],item[3],item[4],item[5],item[6].encode('utf-8')\
                            ,item[7].encode('utf-8'),item[8].encode('utf-8'))
            f.write(item_format % itemk)
    print '        All Done'

if __name__ == '__main__':
    generateCSV()