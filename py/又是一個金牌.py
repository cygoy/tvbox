# -*- coding: utf-8 -*-
# by @嗷呜
import json
import sys
import threading
import uuid
import requests
sys.path.append('..')
from base.spider import Spider
import time
from Crypto.Hash import MD5, SHA1

class Spider(Spider):
    '''
    配置示例：
    {
        "key": "xxxx",
        "name": "xxxx",
        "type": 3,
        "api": ".所在路径/金牌.py",
        "searchable": 1,
        "quickSearch": 1,
        "filterable": 1,
        "changeable": 1,
        "ext": {
            "site": "https://www.jiabaide.cn,域名2,域名3"
        }
    },
    '''
    def init(self, extend=""):
        if extend:
            hosts=json.loads(extend)['site']
        self.host = self.host_late(hosts)
        pass

    def getName(self):
        pass

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def destroy(self):
        pass

    def homeContent(self, filter):
        return {
            'class': [{'type_id': '1', 'type_name': '电影'},
          {'type_id': '2', 'type_name': '电视剧'},
          {'type_id': '3', 'type_name': '综艺'},
          {'type_id': '4', 'type_name': '动漫'}],
            'filters': {
    '1': [
        {'key': 'type',
         'name': '类型',
         'value': [{'n': '全部', 'v': ''},
                   {'n': '喜剧', 'v': '/type/22'},
                   {'n': '动作', 'v': '/type/23'},
                   {'n': '科幻', 'v': '/type/30'},
                   {'n': '爱情', 'v': '/type/26'},
                   {'n': '悬疑', 'v': '/type/27'},
                   {'n': '奇幻', 'v': '/type/87'},
                   {'n': '剧情', 'v': '/type/37'},
                   {'n': '恐怖', 'v': '/type/36'},
                   {'n': '犯罪', 'v': '/type/35'},
                   {'n': '动画', 'v': '/type/33'},
                   {'n': '惊悚', 'v': '/type/34'},
                   {'n': '战争', 'v': '/type/25'},
                   {'n': '冒险', 'v': '/type/31'},
                   {'n': '灾难', 'v': '/type/81'},
                   {'n': '伦理', 'v': '/type/83'},
                   {'n': '其他', 'v': '/type/43'}]},
        {'key': 'area',
         'name': '地区',
         'value': [{'n': '全部', 'v': ''},
                   {'n': '中国大陆', 'v': '/area/中国大陆'},
                   {'n': '中国香港', 'v': '/area/中国香港'},
                   {'n': '中国台湾', 'v': '/area/中国台湾'},
                   {'n': '美国', 'v': '/area/美国'},
                   {'n': '日本', 'v': '/area/日本'},
                   {'n': '韩国', 'v': '/area/韩国'},
                   {'n': '印度', 'v': '/area/印度'},
                   {'n': '泰国', 'v': '/area/泰国'},
                   {'n': '其他', 'v': '/area/其他'}]},
        {'key': 'year',
         'name': '年份',
         'value': [{'n': '全部', 'v': ''},
                   {'n': '2024', 'v': '/year/2024'},
                   {'n': '2023', 'v': '/year/2023'},
                   {'n': '2022', 'v': '/year/2022'},
                   {'n': '2021', 'v': '/year/2021'},
                   {'n': '2020', 'v': '/year/2020'},
                   {'n': '2019', 'v': '/year/2019'},
                   {'n': '2018', 'v': '/year/2018'},
                   {'n': '2017', 'v': '/year/2017'},
                   {'n': '2016', 'v': '/year/2016'},
                   {'n': '2015', 'v': '/year/2015'},
                   {'n': '2014', 'v': '/year/2014'},
                   {'n': '2013', 'v': '/year/2013'},
                   {'n': '2012', 'v': '/year/2012'},
                   {'n': '2011', 'v': '/year/2011'},
                   {'n': '2010', 'v': '/year/2010'},
                   {'n': '2009~2000', 'v': '/year/2009~2000'}]},
        {'key': 'lang',
         'name': '语言',
         'value': [{'n': '全部', 'v': ''},
                   {'n': '国语', 'v': '/lang/国语'},
                   {'n': '英语', 'v': '/lang/英语'},
                   {'n': '粤语', 'v': '/lang/粤语'},
                   {'n': '韩语', 'v': '/lang/韩语'},
                   {'n': '日语', 'v': '/lang/日语'},
                   {'n': '其他', 'v': '/lang/其他'}]},
        {'key': 'by',
         'name': '排序',
         'value': [{'n': '上映时间', 'v': '/sortType/1/sortOrder/0'},
                   {'n': '人气高低', 'v': '/sortType/3/sortOrder/0'},
                   {'n': '评分高低', 'v': '/sortType/4/sortOrder/0'}]}
    ],
    '2': [
        {'key': 'type',
         'name': '类型',
         'value': [{'n': '全部', 'v': ''},
                   {'n': '国产剧', 'v': '/type/14'},
                   {'n': '欧美剧', 'v': '/type/15'},
                   {'n': '港台剧', 'v': '/type/16'},
                   {'n': '日韩剧', 'v': '/type/62'},
                   {'n': '其他剧', 'v': '/type/68'}]},
        {'key': 'class',
         'name': '剧情',
         'value': [{'n': '全部', 'v': ''},
                   {'n': '古装', 'v': '/class/古装'},
                   {'n': '战争', 'v': '/class/战争'},
                   {'n': '喜剧', 'v': '/class/喜剧'},
                   {'n': '家庭', 'v': '/class/家庭'},
                   {'n': '犯罪', 'v': '/class/犯罪'},
                   {'n': '动作', 'v': '/class/动作'},
                   {'n': '奇幻', 'v': '/class/奇幻'},
                   {'n': '剧情', 'v': '/class/剧情'},
                   {'n': '历史', 'v': '/class/历史'},
                   {'n': '短片', 'v': '/class/短片'}]},
        {'key': 'area',
         'name': '地区',
         'value': [{'n': '全部', 'v': ''},
                   {'n': '中国大陆', 'v': '/area/中国大陆'},
                   {'n': '中国香港', 'v': '/area/中国香港'},
                   {'n': '中国台湾', 'v': '/area/中国台湾'},
                   {'n': '日本', 'v': '/area/日本'},
                   {'n': '韩国', 'v': '/area/韩国'},
                   {'n': '美国', 'v': '/area/美国'},
                   {'n': '泰国', 'v': '/area/泰国'},
                   {'n': '其他', 'v': '/area/其他'}]},
        {'key': 'year',
         'name': '时间',
         'value': [{'n': '全部', 'v': ''},
                   {'n': '2024', 'v': '/year/2024'},
                   {'n': '2023', 'v': '/year/2023'},
                   {'n': '2022', 'v': '/year/2022'},
                   {'n': '2021', 'v': '/year/2021'},
                   {'n': '2020', 'v': '/year/2020'},
                   {'n': '2019', 'v': '/year/2019'},
                   {'n': '2018', 'v': '/year/2018'},
                   {'n': '2017', 'v': '/year/2017'},
                   {'n': '2016', 'v': '/year/2016'},
                   {'n': '2015', 'v': '/year/2015'},
                   {'n': '2014', 'v': '/year/2014'},
                   {'n': '2013', 'v': '/year/2013'},
                   {'n': '2012', 'v': '/year/2012'},
                   {'n': '2011', 'v': '/year/2011'},
                   {'n': '2010', 'v': '/year/2010'}]},
        {'key': 'lang',
         'name': '语言',
         'value': [{'n': '全部', 'v': ''},
                   {'n': '普通话', 'v': '/lang/普通话'},
                   {'n': '英语', 'v': '/lang/英语'},
                   {'n': '粤语', 'v': '/lang/粤语'},
                   {'n': '韩语', 'v': '/lang/韩语'},
                   {'n': '日语', 'v': '/lang/日语'},
                   {'n': '泰语', 'v': '/lang/泰语'},
                   {'n': '其他', 'v': '/lang/其他'}, ]},
        {'key': 'by',
         'name': '排序',
         'value': [{'n': '最近更新', 'v': '/sortType/1/sortOrder/0'},
                   {'n': '添加时间', 'v': '/sortType/2/sortOrder/0'},
                   {'n': '人气高低', 'v': '/sortType/3/sortOrder/0'},
                   {'n': '评分高低', 'v': '/sortType/4/sortOrder/0'}]}
    ],
    '3': [
        {'key': 'type',
         'name': '类型',
         'value': [{'n': '全部', 'v': ''},
                   {'n': '国产综艺', 'v': '/type/69'},
                   {'n': '港台综艺', 'v': '/type/70'},
                   {'n': '日韩综艺', 'v': '/type/72'},
                   {'n': '欧美综艺', 'v': '/type/73'}]},
        {'key': 'class',
         'name': '剧情',
         'value': [{'n': '全部', 'v': ''},
                   {'n': '真人秀', 'v': '/class/真人秀'},
                   {'n': '音乐', 'v': '/class/音乐'},
                   {'n': '脱口秀', 'v': '/class/脱口秀'}]},
        {'key': 'area',
         'name': '地区',
         'value': [{'n': '全部', 'v': ''},
                   {'n': '中国大陆', 'v': '/area/中国大陆'},
                   {'n': '中国香港', 'v': '/area/中国香港'},
                   {'n': '中国台湾', 'v': '/area/中国台湾'},
                   {'n': '日本', 'v': '/area/日本'},
                   {'n': '韩国', 'v': '/area/韩国'},
                   {'n': '美国', 'v': '/area/美国'},
                   {'n': '其他', 'v': '/area/其他'}]},
        {'key': 'year',
         'name': '时间',
         'value': [{'n': '全部', 'v': ''},
                   {'n': '2024', 'v': '/year/2024'},
                   {'n': '2023', 'v': '/year/2023'},
                   {'n': '2022', 'v': '/year/2022'},
                   {'n': '2021', 'v': '/year/2021'},
                   {'n': '2020', 'v': '/year/2020'}]},
        {'key': 'lang',
         'name': '语言',
         'value': [{'n': '全部', 'v': ''},
                   {'n': '国语', 'v': '/lang/国语'},
                   {'n': '英语', 'v': '/lang/英语'},
                   {'n': '粤语', 'v': '/lang/粤语'},
                   {'n': '韩语', 'v': '/lang/韩语'},
                   {'n': '日语', 'v': '/lang/日语'},
                   {'n': '其他', 'v': '/lang/其他'}, ]},
        {'key': 'by',
         'name': '排序',
         'value': [{'n': '最近更新', 'v': '/sortType/1/sortOrder/0'},
                   {'n': '添加时间', 'v': '/sortType/2/sortOrder/0'},
                   {'n': '人气高低', 'v': '/sortType/3/sortOrder/0'},
                   {'n': '评分高低', 'v': '/sortType/4/sortOrder/0'}]}
    ],
    '4': [
        {'key': 'type',
         'name': '类型',
         'value': [{'n': '全部', 'v': ''},
                   {'n': '国产动漫', 'v': '/type/75'},
                   {'n': '日韩动漫', 'v': '/type/76'},
                   {'n': '欧美动漫', 'v': '/type/77'}]},
        {'key': 'class',
         'name': '剧情',
         'value': [{'n': '全部', 'v': ''},
                   {'n': '喜剧', 'v': '/class/喜剧'},
                   {'n': '科幻', 'v': '/class/科幻'},
                   {'n': '热血', 'v': '/class/热血'},
                   {'n': '冒险', 'v': '/class/冒险'},
                   {'n': '动作', 'v': '/class/动作'},
                   {'n': '运动', 'v': '/class/运动'},
                   {'n': '战争', 'v': '/class/战争'},
                   {'n': '儿童', 'v': '/class/儿童'}]},
        {'key': 'area',
         'name': '地区',
         'value': [{'n': '全部', 'v': ''},
                   {'n': '中国大陆', 'v': '/area/中国大陆'},
                   {'n': '日本', 'v': '/area/日本'},
                   {'n': '美国', 'v': '/area/美国'},
                   {'n': '其他', 'v': '/area/其他'}]},
        {'key': 'year',
         'name': '时间',
         'value': [{'n': '全部', 'v': ''},
                   {'n': '2024', 'v': '/year/2024'},
                   {'n': '2023', 'v': '/year/2023'},
                   {'n': '2022', 'v': '/year/2022'},
                   {'n': '2021', 'v': '/year/2021'},
                   {'n': '2020', 'v': '/year/2020'},
                   {'n': '2019', 'v': '/year/2019'},
                   {'n': '2018', 'v': '/year/2018'},
                   {'n': '2017', 'v': '/year/2017'},
                   {'n': '2016', 'v': '/year/2016'},
                   {'n': '2015', 'v': '/year/2015'},
                   {'n': '2014', 'v': '/year/2014'},
                   {'n': '2013', 'v': '/year/2013'},
                   {'n': '2012', 'v': '/year/2012'},
                   {'n': '2011', 'v': '/year/2011'},
                   {'n': '2010', 'v': '/year/2010'}]},
        {'key': 'lang',
         'name': '语言',
         'value': [{'n': '全部', 'v': ''},
                   {'n': '国语', 'v': '/lang/国语'},
                   {'n': '英语', 'v': '/lang/英语'},
                   {'n': '日语', 'v': '/lang/日语'},
                   {'n': '其他', 'v': '/lang/其他'}]},
        {'key': 'by',
         'name': '排序',
         'value': [{'n': '最近更新', 'v': '/sortType/1/sortOrder/0'},
                   {'n': '添加时间', 'v': '/sortType/2/sortOrder/0'},
                   {'n': '人气高低', 'v': '/sortType/3/sortOrder/0'},
                   {'n': '评分高低', 'v': '/sortType/4/sortOrder/0'}]}
    ]
}
        }

    def homeVideoContent(self):
        data1 = self.fetch(f"{self.host}/api/mw-movie/anonymous/v1/home/all/list", headers=self.getheaders()).json()
        data2=self.fetch(f"{self.host}/api/mw-movie/anonymous/home/hotSearch",headers=self.getheaders()).json()
        data=[]
        for i in data1['data'].values():
            data.extend(i['list'])
        data.extend(data2['data'])
        vods=self.getvod(data)
        return {'list':vods}

    def categoryContent(self, tid, pg, filter, extend):

        params = {
          "area": extend.get('area', ''),
          "filterStatus": "1",
          "lang": extend.get('lang', ''),
          "pageNum": pg,
          "pageSize": "30",
          "sort": extend.get('sort', '1'),
          "sortBy": "1",
          "type": extend.get('type', ''),
          "type1": tid,
          "v_class": extend.get('v_class', ''),
          "year": extend.get('year', '')
        }
        data = self.fetch(f"{self.host}/api/mw-movie/anonymous/video/list?{self.js(params)}", headers=self.getheaders(params)).json()
        result = {}
        result['list'] = self.getvod(data['data']['list'])
        result['page'] = pg
        result['pagecount'] = 9999
        result['limit'] = 90
        result['total'] = 999999
        return result

    def detailContent(self, ids):
        data=self.fetch(f"{self.host}/api/mw-movie/anonymous/video/detail?id={ids[0]}",headers=self.getheaders({'id':ids[0]})).json()
        vod=self.getvod([data['data']])[0]
        vod['vod_play_from']='老王有金牌'
        vod['vod_play_url'] = '#'.join(
            f"{i['name'] if len(vod['episodelist']) > 1 else vod['vod_name']}${ids[0]}@@{i['nid']}" for i in
            vod['episodelist'])
        vod.pop('episodelist', None)
        return {'list':[vod]}

    def searchContent(self, key, quick, pg="1"):
        params = {
          "keyword": key,
          "pageNum": pg,
          "pageSize": "8",
          "sourceCode": "1"
        }
        data=self.fetch(f"{self.host}/api/mw-movie/anonymous/video/searchByWord?{self.js(params)}",headers=self.getheaders(params)).json()
        vods=self.getvod(data['data']['result']['list'])
        return {'list':vods,'page':pg}

    def playerContent(self, flag, id, vipFlags):
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.61 Chrome/126.0.6478.61 Not/A)Brand/8  Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'DNT': '1',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'Origin': self.host,
            'Referer': f'{self.host}/'
        }
        ids=id.split('@@')
        pdata = self.fetch(f"{self.host}/api/mw-movie/anonymous/v2/video/episode/url?clientType=1&id={ids[0]}&nid={ids[1]}",headers=self.getheaders({'clientType':'1','id': ids[0], 'nid': ids[1]})).json()
        vlist=[]
        for i in pdata['data']['list']:vlist.extend([i['resolutionName'],i['url']])
        return {'parse':0,'url':vlist,'header':self.header}

    def localProxy(self, param):
        pass

    def host_late(self, url_list):
        if isinstance(url_list, str):
            urls = [u.strip() for u in url_list.split(',')]
        else:
            urls = url_list
        if len(urls) <= 1:
            return urls[0] if urls else ''

        results = {}
        threads = []

        def test_host(url):
            try:
                start_time = time.time()
                response = requests.head(url, timeout=1.0, allow_redirects=False)
                delay = (time.time() - start_time) * 1000
                results[url] = delay
            except Exception as e:
                results[url] = float('inf')
        for url in urls:
            t = threading.Thread(target=test_host, args=(url,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        return min(results.items(), key=lambda x: x[1])[0]

    def md5(self, sign_key):
        md5_hash = MD5.new()
        md5_hash.update(sign_key.encode('utf-8'))
        md5_result = md5_hash.hexdigest()
        return md5_result

    def js(self, param):
        return '&'.join(f"{k}={v}" for k, v in param.items())

    def getheaders(self, param=None):
        if param is None:param = {}
        t=str(int(time.time()*1000))
        param['key']='cb808529bae6b6be45ecfab29a4889bc'
        param['t']=t
        sha1_hash = SHA1.new()
        sha1_hash.update(self.md5(self.js(param)).encode('utf-8'))
        sign = sha1_hash.hexdigest()
        deviceid = str(uuid.uuid4())
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.61 Chrome/126.0.6478.61 Not/A)Brand/8  Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'sign': sign,
            't': t,
            'deviceid':deviceid
        }
        return headers

    def convert_field_name(self, field):
        field = field.lower()
        if field.startswith('vod') and len(field) > 3:
            field = field.replace('vod', 'vod_')
        if field.startswith('type') and len(field) > 4:
            field = field.replace('type', 'type_')
        return field

    def getvod(self, array):
        return [{self.convert_field_name(k): v for k, v in item.items()} for item in array]

