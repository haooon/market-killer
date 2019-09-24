from src.sysComponents.main.main import Main
import requests
import time

if __name__ == '__main__':
    header_pool = [
        "_ntes_nnid=1176171809d66c4ca967762dc9767fb9,1566534179292; _ntes_nuid=1176171809d66c4ca967762dc9767fb9; csrf_token=3e353cd8de55920d5f6005d53881765ab26de2a9; game=csgo; _ga=GA1.2.951113250.1569231272; _gid=GA1.2.1683707879.1569231272; NTES_YD_SESS=OQVgNd6Mt5.1MqGz2DEUf0Ldhgi9RcmOYbWHodsYKKMg2xCyAo0JcpVV.lDKRhk7DrHCtzo4uK4xB326q63sEcbL7LES4JkWta0Z.L9rM.XzwNM2RGAM9rlVo77bEC6rTkrguyMmWeS4NvDTSsINzGyILAULBkyPQgqzJS24m44uoWycQR18iJ5qNINiFeOtaxxm81Zyi2wJaIo13im6jo0y5jHc0XGk_hoUb0_zccZqn; S_INFO=1569231332|0|3&80##|17719495332; P_INFO=17719495332|1569231332|1|netease_buff|00&99|bej&1569210568&netease_buff#bej&null#10#0#0|&0|null|17719495332; session=1-pvcz9m5FwuvwYJEvVKIX0SvjMdfxhGUt5KahxhXONttm2043296940; Locale-Supported=zh-Hans; _gat_gtag_UA_109989484_1=1",
        "_ga=GA1.2.1549448114.1565356207; _ntes_nnid=dd304631d7902d3bad049873a6270018,1566042562983; _ntes_nuid=dd304631d7902d3bad049873a6270018; csrf_token=6ad711bfb7082004872317bc396d13b5a4336c4a; game=csgo; _gid=GA1.2.393649929.1569057473; Locale-Supported=zh-Hans; _gat_gtag_UA_109989484_1=1; NTES_YD_SESS=t6fg6GSwvnZleW7tJK.1XIDJ5Gntd6iVKDHBL.vWUH.6uWdmu57zsxdx.dDQHJSXgy0Xm3LN91zkjgfKPBPEapXNnGoEBu2tHaSF5X6QdHfyct_D62uui9aDqxdnNwf9NF3DhMg_Yjx0wHWVw3MASLKMr4E5hf1O9aS_RUHVMkJKmkLZftakSfJkq9995yUbYLGv9SY5YuAMh80NwC0VqjiQEXK4KY_7wELk9K0qXx7jb; S_INFO=1569146666|0|3&80##|15510592723; P_INFO=15510592723|1569146666|1|netease_buff|00&99|bej&1567432959&netease_buff#bej&null#10#0#0|&0|null|15510592723; session=1-TdwJJmnPZQZHY31B_HnidGb_tcetUfw88zN0Vznft5Pa2043074918"
    ]

    url = 'https://buff.163.com/api/market/goods?game=csgo&page_num=' + "130" + '&sort_by=price.desc&_=' + str(
        int(round(time.time() * 1000)))
    r = requests.get(url, headers={"Cookie":header_pool[0], "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}, verify=True)
    print(r.content)
    Main().init()
    while True:
        pass