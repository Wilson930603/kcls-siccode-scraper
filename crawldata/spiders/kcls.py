import scrapy,json,re,os,platform,requests
from crawldata.functions import *
from datetime import datetime
from twocaptcha import TwoCaptcha

class CrawlerSpider(scrapy.Spider):
    name = 'kcls'
    DATE_CRAWL=datetime.now().strftime('%Y-%m-%d')
    #custom_settings={'LOG_FILE':'./log/'+name+'_'+DATE_CRAWL+'.log'}
    if platform.system()=='Linux':
        URL='file:////' + os.getcwd()+'/scrapy.cfg'
    else:
        URL='file:///' + os.getcwd()+'/scrapy.cfg'
    conn=None
    username='0061142980'
    password='1770'
    api_key='d368d93ac4830dc4a52b5351a7b92626'
    cookies = {'f5avrbbbbbbbbbbbbbbbb': 'DFLBGJIPDMMKAELCJNMCDFOEALMGFJJOONEINAMAMAGMKGIJLEEIMIMOEBNLJIEIMPDDLMCOMOIDDELBJPCAFAFFPBIALGPHPFKKJBOIHEIBLAKPNKCBOGIGNDMHLBIL','f5avrbbbbbbbbbbbbbbbb': 'PGEPCABFMMJBANOOIBMNEKGFKIGJOACKJNIPGNBEBJPJKPMLCNOKAPBJJBHAFGFGONPAAAGMIPMDMMLFFGMHBDMLICPADHEGFFFENBEGADMKDIFIOKMAGICKEHMJOCKI','ASP.NET_SessionId': 'mtyuowbzev2btijfmkbea41u','BIGipServerrefusa_https': '2639964352.47873.0000','TS0180d824': '01065b9f502d33d1bed07bfdfb467b30a3b8b6ac3a1b7fbaf10b2f806fd91139e9e287ea308f7b534cc90ccb2244e9020c79211abc','.ASPXAUTH': 'C5F6546E417B5D56A1EBC78B5CA2016404BF398551DE7CA6C5A1258F4F5EEFB857C7267272E7301D336EB1A89996C7C04F1991107BF2CBAAD025377D87318AE76DB483997360DE7AB6BD13F70134A7F11D918CD5707946E3BC3142EA9FB7FAD0AD03AA28DB422DE659F0E6B0B376AAC03C6D70C8C8D27389C7E9BC90CE6F207EB7675B261CFA7534D03FD2C80AE6F7C9B54BF3CD2B7482FCB895E6B4E286EA64F479157715FD37E840F9324D5249CEBC0892D3E13E3555D0D307056215AE44A2484A0737FDA7763C97C36D3B1C0DABDF7D172E49736CEC65CDEEF226C5D427EA00413842107C8EC9BA564938E87783947A771BA0BC292B3BE19849AD26F3A6A289DD8F24D86152D629FE971101E1F0062E7AFAF684B257AA89ED3377E032AF6B7511B23AF6ADDCB7513B2C56428CA90FA2B645839C6BDB46B3EB389EDF8038ADB0C4BE4034BE8F762FFB73C99313018DA74956D0FBD9DA31F982D7B82474229EE96844A499B720096D0D776765842AE1127D295D39E1E73D2152FC23043B0888FC3C31890D02DBF6E0BF51FC8581C06A971C80DC798FF080301B5C1924DD8F4B3AD2E9C0F860AA50FA462AC692F58D70D0B849F905467881B9E7BC95CA2E516ACACA1D54B718387FFEBEA5B34EF0B118B33127101FBEA886C2D48482C37A2EF47C32F1ABD2E4A5D03AEA26BEF9544AF7E1305C924F5B54E465E2D49F8CC5053FFA7C6882EC264D6D','UserAuthenticated': 'true','f5avrbbbbbbbbbbbbbbbb': 'AGBPMJCKMOEDHNGLIILMIJDHIBBBMJLBDLHLIOJAOIMPHIGCBKPNGAHONIMDNOPPJBKMNMIJOMIDJDNMIGNEPAMIBNCAHFAILLHDBNHFJDAAMHNCGILAPGJJGBDEPCAC','CurrentUser': '49244','TS01d981e1': '01065b9f509e32a79c2a3fe45750bf509c9ea7a7043b9c54493c541f7eec21954cf9238f4b926e5919fa327dc82c776460f45a85b7','ai_user': 's4CF4UW0cVVcVZOGXpnI04^|2023-08-07T06:15:49.143Z','ai_session': '4RLejuli51HfCrtwgWyOFy^|1691388953257^|1691395632530','_ga_Q1M017Q8EN': 'GS1.1.1691394312.2.1.1691395630.0.0.0','_ga': 'GA1.2.816852953.1691388954','_gid': 'GA1.2.1694472666.1691388954','ln_or': 'eyIyOTcyNjYiOiJkIn0^%^3D','_ga_X3GK0V6EYP': 'GS1.2.1691394321.2.1.1691395632.0.0.0','__utma': '72359952.816852953.1691388954.1691388955.1691394315.2','__utmc': '72359952','__utmz': '72359952.1691388955.1.1.utmcsr=(direct)^|utmccn=(direct)^|utmcmd=(none)','TS0180d824_77': '08cfd42f6fab280099824592fcf161346a7cd2c52956f490514c62b2a22c65497b77140297b3f1745124bf35628075970852a2e15d824000b3301663babd1d1f0c285ae9d520d7ec6f5db0cab866e1c4d5a0d7862634a58acf95ac652b4aa40071e5c057a19659a9df27d457636ae8509a74b1941584b92c','__hstc': '68387854.49a612d62533a360c2b0e752794f7624.1691388955522.1691388955522.1691394323472.2','hubspotutk': '49a612d62533a360c2b0e752794f7624','__hssrc': '1','ASP.NET_SessionID': '','__utmb': '72359952.13.10.1691394315','__hssc': '68387854.12.1691394323472','__utmt': '1','_gat_UA-891084-7': '1'}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language': 'en-GB,en;q=0.5','Connection': 'keep-alive','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1'}
    TYPE=None
    ID=None
    URLS={'NAICS':'https://www.referenceusa.com/UsBusiness/Data/NaicsKeywordSearch','SIC':'https://www.referenceusa.com/UsBusiness/Data/TryHarderSicLookup'}
    def __init__(self, type=None,code=None, **kwargs):
        if type:
            self.TYPE=type
        if code:
            self.ID=code
        super().__init__(**kwargs)
    # hcaptcha
    def hcaptcha(self,sitekey, url):
        try:
            solver = TwoCaptcha(self.api_key)
            result = solver.hcaptcha(sitekey=sitekey, url=url)
        except Exception as e:
            print(e)
            result = ""
        return result
    def start_requests(self):
        if self.TYPE and self.ID:
            print(self.TYPE,self.ID)
            CODES=[self.ID]
            yield scrapy.Request('https://www.referenceusa.com/UsBusiness/Search/Custom/',callback=self.parse_search,dont_filter=True,cookies=self.cookies,headers=self.headers,meta={'CODES':CODES})
    def parse_search(self, response):
        CODES=response.meta['CODES']
        CODE=str(response.url).split('/')[-1]
        print('CODE:',CODE)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language': 'en-GB,en;q=0.5','Content-Type': 'application/x-www-form-urlencoded','Connection': 'keep-alive','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1'}
        data = 'barcode='+self.username+'&password='+self.password+'&url=https^%^3A^%^2F^%^2Fwww.referenceusa.com&qurl='
        response = requests.post('https://evgcatalog.kcls.org/eg/opac/ezproxy/login?url=https://www.referenceusa.com',headers=headers,data=data)
        response=requests.get('https://www.referenceusa.com/Home/Home')
        self.cookies.update(response.cookies.get_dict())
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'en-GB,en;q=0.5','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest','Origin': 'https://www.referenceusa.com','Connection': 'keep-alive','Referer': 'https://www.referenceusa.com/UsBusiness/Search/Custom/'+CODE,'Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin'}
        if self.TYPE=='NAICS':
            data_post = {'VerifiedRecord': 'V','PrimarySic': '','PrimarySicLookup': '','Sic': '','SicLookup': '','Naics': '','NaicsLookup': ','.join(CODES),'PrimaryNaicsLookup': '','postbackType': 'viewresults'}
        elif self.TYPE=='SIC':
            data_post = {'VerifiedRecord': 'V','PrimarySic': '','PrimarySicLookup': '','Sic': '','SicLookup': ','.join(CODES),'Naics': '','NaicsLookup': '','PrimaryNaicsLookup': '','postbackType': 'viewresults'}
        elif self.TYPE=='PNAICS':
            data_post = {'VerifiedRecord': 'V','PrimarySic': '','PrimarySicLookup': '','Sic': '','SicLookup': '','Naics': '','NaicsLookup': '','PrimaryNaicsLookup': ','.join(CODES),'postbackType': 'viewresults'}
        else:
            data_post = {'VerifiedRecord': 'V','PrimarySic': '','PrimarySicLookup': ','.join(CODES),'Sic': '','SicLookup': '','Naics': '','NaicsLookup': '','PrimaryNaicsLookup': '','postbackType': 'viewresults'}
        response = requests.post('https://www.referenceusa.com/UsBusiness/Search/NewCustomSearchRequest/'+CODE,cookies=self.cookies,headers=headers,data=data_post)
        try:
            Data=json.loads(response.text)
            print(Data)
            TOTAL=int(Data['data']['totalCount']/250)
            if TOTAL<Data['data']['totalCount']:
                TOTAL+=1
            if Data['data']['totalCount']<=250:
                data_post = {'format': 'CSV','detailLevel': 'detail','filterCustom': '','purchaseId': '','customFields': 'BusinessName,ParentCompanyName,FirstNameMatch,LastNameMatch,Address,City,State,Zip,LegalName,VerifiedRecord'}
                response = requests.post('https://www.referenceusa.com/UsBusiness/Download/DownloadData/'+CODE,cookies=self.cookies,headers=headers,data=data_post)
                f=open(self.name+'_'+self.ID+'_1.csv','w',encoding='utf-8-sig',newline='').write(response.text)
            else:
                RUN=True
                Data_list=[]
                page=0
                No=int(page/10)+1
                while RUN:
                    file_name='./Data/'+self.TYPE+'_'+self.ID+'_'+str(No)+'.csv'
                    if not os.path.exists(file_name):
                        print('File_No:',No,'/',TOTAL,'Crawling page:',page)
                        data_post = {'requestKey': CODE,'sort': '','direction': 'Ascending','pageIndex': str(page),'optionalColumn': ''}
                        response = requests.post('https://www.referenceusa.com/UsBusiness/Result/Page', cookies=self.cookies, headers=headers, data=data_post)
                        if "'sitekey'" in response.text:
                            CHK=False
                            RUN=0
                            while CHK==False and RUN<10:
                                RUN+=1
                                print('Passing captcha time ',RUN)
                                sitekey=((str(response.text).split("'sitekey'")[1].split(',')[0]).strip()).replace("'","").replace(":","").strip()
                                print(sitekey)
                                url_cpt='https://www.referenceusa.com/UsBusiness/Result/'+CODE
                                answer = self.hcaptcha(sitekey, url_cpt)
                                if answer:
                                    # print("Token:", answer["code"])
                                    json_data={'requestKey': CODE, 'answer': answer["code"], 'pageType': 'Result' }
                                    res=requests.post('https://www.referenceusa.com/UsBusiness/Result/CheckCaptcha',json=json_data,cookies=self.cookies)
                                    CK=res.cookies.get_dict()
                                    self.cookies.update(CK)
                                    data_post = {'requestKey': CODE,'sort': '','direction': 'Ascending','pageIndex': str(page),'optionalColumn': ''}
                                    response = requests.post('https://www.referenceusa.com/UsBusiness/Result/Page', cookies=self.cookies, headers=headers, data=data_post)
                                    if not "'sitekey'" in response.text:
                                        CHK=True
                                        print("Solved hcaptcha successfully.")
                                else:
                                    print("Failed")
                        HTML=scrapy.Selector(text=response.text)
                        Data_page=HTML.xpath('//input[@data-recordid]/@data-recordid').getall()
                        Data_list+=Data_page
                        print('rows:',len(Data_page),'=>',len(Data_list))
                        data_post = {'requestKey': CODE,'ids': Data_list,'tag': 'true'}
                        response = requests.post('https://www.referenceusa.com/UsBusiness/Result/UpdateTaggedRecords',cookies=self.cookies,headers=headers,data=data_post)
                        if len(Data_list)>=250:
                            print('Write data:',file_name)
                            data_post = {'requestKey': CODE}
                            response = requests.post('https://www.referenceusa.com/UsBusiness/Result/HasSelectedRecords',cookies=self.cookies,headers=headers,data=data_post)
                            data_post = {'format': 'CSV','detailLevel': 'detail','filterCustom': '','purchaseId': '','customFields': 'BusinessName,ParentCompanyName,FirstNameMatch,LastNameMatch,Address,City,State,Zip,LegalName,VerifiedRecord'}
                            response = requests.post('https://www.referenceusa.com/UsBusiness/Download/DownloadData/'+CODE,cookies=self.cookies,headers=headers,data=data_post)
                            open(file_name,'w',encoding='utf-8-sig',newline='').write(response.text)
                            No+=1
                            data_post = {'requestKey': CODE,'ids': Data_list,'tag': 'false'}
                            response = requests.post('https://www.referenceusa.com/UsBusiness/Result/UpdateTaggedRecords',cookies=self.cookies,headers=headers,data=data_post)
                            Data_list=[]
                        if len(Data_page)>=25:
                            page+=1
                        else:
                            RUN=False
                            if len(Data_list)>0 and No >= TOTAL:
                                print('Write data:',file_name)
                                data_post = {'requestKey': CODE}
                                response = requests.post('https://www.referenceusa.com/UsBusiness/Result/HasSelectedRecords',cookies=self.cookies,headers=headers,data=data_post)
                                data_post = {'format': 'CSV','detailLevel': 'detail','filterCustom': '','purchaseId': '','customFields': 'BusinessName,ParentCompanyName,FirstNameMatch,LastNameMatch,Address,City,State,Zip,LegalName,VerifiedRecord'}
                                response = requests.post('https://www.referenceusa.com/UsBusiness/Download/DownloadData/'+CODE,cookies=self.cookies,headers=headers,data=data_post)
                                open(file_name,'w',encoding='utf-8-sig',newline='').write(response.text)
                    else:
                        print('Existed:',file_name)
                        page+=10
                        No+=1
        except:
            print(response.text)
