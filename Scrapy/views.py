from django.shortcuts import render, redirect, HttpResponse
from .forms import ScrapForm
import time, os, json, re
from django.views.decorators.csrf import csrf_exempt

print(os.listdir(os.getcwd()))

def findUrls(strings):
    try:
        res =  "".join(strings.split())
        res =  res.replace(",", "")
        res = strings.replace("http", ",http")
        res = res.split(",")
        res = " ".join(res).split()
        return  res
    except:
        res = "".join(strings.split())
        res = strings.replace("http", ",http")
        res = res.split(",")
        res = " ".join(res).split()
        return res


def welcome(request):
    return HttpResponse("welcome to scrapy application | for scrapy goto /scrapy")

def Scrapy(request):
    student = ScrapForm()
    return render(request, "form.html",{'form':student})

items = []
def collect_items(item, response, spider):
    items.append(item)

@csrf_exempt
def dataScraping(request):
    eachUrls = []
    if request.method == 'POST':
        form = ScrapForm(request.POST)
        urls = form.data['UrlsName']
        eachUrls = findUrls(urls)
        for x in eachUrls:
            link = x
            path = os.getcwd()
            os.chdir(path + "/UrlScraper")
            cmd = 'scrapy crawl scraperBot -a start_url="{}" -t json -o outputfile.json'.format(link)
            r = os.system(cmd)
            os.chdir("../")

        try:
            path = os.getcwd()
            print("pth==", path)
            os.chdir(path + "/UrlScraper")
            print("-=0ok", os.getcwd())
            newpth = path+"/UrlScraper"
            x = open(newpth + "/outputfile.json", "r")
            x = x.read()
            if len(x) > 5:
                x = x.replace('][', ',')
                f = open(newpth + "/FinalOp.json", "w")
                f.write(x)
                f.close()
                with open(newpth + '/FinalOp.json') as f:
                    data = json.load(f)
                os.remove(newpth + "/outputfile.json")
                os.remove(newpth + "/FinalOp.json")
                os.chdir("../")
                print(os.listdir(os.getcwd()))

                return HttpResponse(json.dumps(data))
            else:
                return HttpResponse(json.dumps({"Status":"UrlErr"}))
        except:
            return ({"Status": "UrlErr"})
    else:
        return HttpResponse({"Status": "RequestErr"})