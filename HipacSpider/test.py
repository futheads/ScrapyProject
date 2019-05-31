import requests

if __name__ == '__main__':
    url = 'https://api.hipac.cn/process/prod/1.0.2/mall.item.searchItemListWithFlashBuyAct.pc/?' \
                  'appKey=1300&os=Chrome&t=1553848122455&sign=bd80c6d8138d464bf36b6e7bef78f7de' \
                  '&data={"pageNo":1,"pageSize":20,"sortType":"3","itemSearchTypes":"","searchSource":"cate"}'
    headers = dict()
    headers[
        "Cookie"] = "acw_tc=2f624a3515525447331993547e61488470c932a13415163c14a7d1b308a802; uid=3a174da55e814f19a088f57b53cf611a; df=1f3fe8ed63ad88558e8c516f85b26a20-1697ae097cd_tongdun; yduss_production=M6zhthVOv904OhWpFYuNLJjk-Pp6ZAbwDQscSIN_eNs0uBdq5o8JkDS3WvOXPhvo18IPHuUW43slhaE5RMC2AgbP_iNT01tYb18w-3HPAAmxS2mbySuIPJTKR9uQ721q_A1xvprE73TuqUOEegTrRzX9leKeNvEMeoxvjJ3Z7U26ELiggXYM-W3KPBWGO9rptue_RgeeGwYlL37ZfLxDmr0cNrtMc_w_4JicN7nWstAcTYjIcMoPN-tP5QLWu5aouv_9XEvFmk6zB4CAq78q2kMm5jVvbS3VlUxaFzf1qxKY4O3edYxG1BkSMpM9alFpyM78kIX8kohBc6LHhmg7FxLNYDe9qTx9aXcCKFrTBB0l4AbjiqQXQ4xO65pu7cm5iI6MTbWhD0EpUOhjYKWPa9USed1ZWxbsCED5qYIrSqGFqa8oBAjyLxRUD00IIXCsJfg1zZ8WAPjT0fP0m2Mq3PxlC2UzrWoq-rFmQQw0FJfcfSJ1pzCo0iR1-zGodoSYrUqO8jGkJ76wKyTbdAyhLXJBb4wHr-L1bzksaLJYD4Uj9oqYjEtyg-JYPjQiLkcm3sJzIOYiU6g.; hipac.cn_USERID=3a174da55e814f19a088f57b53cf611a; hipac.cn_LASTLOGINTIME=1553848111526; hipac.cnuser_uuid=ebce1d6a-a47c-4016-90e6-b00d028da5cc; SERVERID=703df12c9070c5b89b89c38696dbd8d2|1553852284|1553848070"
    headers[
        "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    headers["Host"] = "api.hipac.cn"
    print(requests.get(url, headers=headers).json())
