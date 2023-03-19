#### &#x20;一、页面分析

*   主url =  <https://desk.zol.com.cn>

    *   请求方式： get
    *   请求头

        *   user-agent\:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.43
        *   referer:<https://cn.bing.com/>
        *   cookie\:ip\_ck=48GJ5v7yj7QuNDY4MTQ1LjE2Njg1ODM3ODQ%3D; lv=1679208689; vn=11; Hm\_lvt\_ae5edc2bc4fc71370807f6187f0a2dd0=1678281601,1679208689; Hm\_lpvt\_ae5edc2bc4fc71370807f6187f0a2dd0=1679208695; questionnaire\_pv=1679184002
    *   响应头

        *   content-type\:text/html; charset=GBK
    *   获取到壁纸分类, 选择需求

        *   [风景](https://desk.zol.com.cn/fengjing/)[动漫](https://desk.zol.com.cn/dongman/)[美女](https://desk.zol.com.cn/meinv/)[创意](https://desk.zol.com.cn/chuangyi/)[卡通](https://desk.zol.com.cn/katong/)[汽车](https://desk.zol.com.cn/qiche/)[游戏](https://desk.zol.com.cn/youxi/)[可爱](https://desk.zol.com.cn/keai/)[建筑](https://desk.zol.com.cn/jianzhu/)[静物](https://desk.zol.com.cn/jingwu/)[动物](https://desk.zol.com.cn/dongwu/)[植物](https://desk.zol.com.cn/zhiwu/)[体育](https://desk.zol.com.cn/tiyu/)[车模](https://desk.zol.com.cn/chemo/)[背景](https://desk.zol.com.cn/beijing/)[手抄报](https://desk.zol.com.cn/shouchaobao/)[模特](https://desk.zol.com.cn/model/)[节日](https://desk.zol.com.cn/jieri/)[美食](https://desk.zol.com.cn/meishi/)[星座](https://desk.zol.com.cn/xingzuo/)[品牌](https://desk.zol.com.cn/pinpai/)[其他](https://desk.zol.com.cn/qita/)
        *   xpath解析：//\*\[@id="main"]/dl\[1]/dd/a\[position()>1]/@href
*   壁纸分类url = <https://desk.zol.com.cn/fengjing/>

    *   请求方式： get
    *   请求头：

        *   referer:<https://desk.zol.com.cn/>
        *   cookie\:ip\_ck=48GJ5v7yj7QuNDY4MTQ1LjE2Njg1ODM3ODQ%3D; lv=1679208689; vn=11; Hm\_lvt\_ae5edc2bc4fc71370807f6187f0a2dd0=1678281601,1679208689; Hm\_lpvt\_ae5edc2bc4fc71370807f6187f0a2dd0=1679208865; questionnaire\_pv=1679184003
    *   响应头：

        *   content-type\:text/html
    *   解析出详情页 - 选择多少页数据
        *   url = /html/body/div\[5]/div\[1]/ul\[1]/li\[position()>2]/a/@href
*   详情页url = <https://desk.zol.com.cn/bizhi/10055_120350_2.html>

    *   请求方式：get
    *   请求头：
        *   referer:<https://desk.zol.com.cn/bizhi/10055_120350_2.html>
    *   响应头：

        *   content-type\:text/html; charset=GBK
    *   解析得到每一张图片url ： //\*\[@id="showImg"]/li/a/@href : 每一页详情页url
        *   解析图片下载地址 : //a\[@id="1680x1050"]/@href
    *   解析到图片名字: /html/body/div\[3]/h3//text()
*   图片下载地址url = <https://desk.zol.com.cn/showpic/1680x1050_120300_111.html>

    *   请求方式: get
    *   响应头: content-type\:text/html
    *   解析得到图片下载地址: //img/@src

