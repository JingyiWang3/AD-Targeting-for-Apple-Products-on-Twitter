# Twitter 广告定向投放项目

## 简介
推特广告是扩展业务覆盖面的好方法，能有效地将内容投放到目标市场，获取流量。本项目通过精心策划，如选择正确的关键词、人群、用户感兴趣的广告文案、以及有影响力的广告推广人，来达到以最低的成本使用推特广告，“击中”最有购买可能的潜在客户，了解用户的需求，为用户体验优化提供方向的目标。


## 流程
![Image of Architecture](https://github.com/yh2866/AD-Targeting-for-Apple-Products-on-Twitter/blob/master/website/img/diagram2.png)

1. 通过 Twiiter API 抓取包含关键词 airpod 的数据，对数据进行简单的处理，存入MangoDB 中。
2. 数据分析流程

   * 使用用户个人描述及用户信息，建立用户画像（包含地域、活跃时间、客户端、用户职业、兴趣、受教育程度、是否结婚、有孩子等标签），定位对 airpod 感兴趣的受众。
   * 使用 LDA 算法分析推文主题，可以把这些主题大概理解为这是用户对 Airpods 最关注的点，作为广告核心话题。同时通过分析这些包含了主观情感色彩的推文来了解用户对产品的看法，为用户体验优化提供方向。
   * 通过构造社交网络，结合 PageRank 算法挖掘出有影响力的用户，作为广告推广人。
3. 使用 Flask 搭建网站，实现可视化。
  

## 不足

1. 清晰的效果统计工具，以及合理的结算方式。
2. 无法真正花钱在 Twitter 上打广告。


## 文件夹介绍
```data_collection```：获取数据代码

```data_processing```：数据清洗和数据分析代码，包含词云、LDA、情感分析、及PageRank 代码

```data_processing/main.ipynb``` 

```output```：数据分析中间结果图

```website```：网站搭建及可视化代码



## 快速开始

clone the git repository: 

`git clone: git@github.com/yh2866/AD-Targeting-for-Apple-Products-on-Twitter.git`

get into "website" folder:

`python3 app.py`

get into "website/s3" folder:

`python -m SimpleHTTPServer`

And then, the website is availble through: '0.0.0.0:5000'


## 网站内容
![Image of Architecture](https://github.com/yh2866/AD-Targeting-for-Apple-Products-on-Twitter/blob/master/website/img/main.png)

### Page of twitter and geometrical information:
![Image of Architecture](https://github.com/yh2866/AD-Targeting-for-Apple-Products-on-Twitter/blob/master/website/img/geo.png)

### Page of profile and sentimentation analysis:
![Image of Architecture](https://github.com/yh2866/AD-Targeting-for-Apple-Products-on-Twitter/blob/master/website/img/sen.png)

### Page of influencer analysis:
![Image of Architecture](https://github.com/yh2866/AD-Targeting-for-Apple-Products-on-Twitter/blob/master/website/img/influ.png)

### Page of result Ads:
![Image of Architecture](https://github.com/yh2866/AD-Targeting-for-Apple-Products-on-Twitter/blob/master/website/img/ad-banner.png)
![Image of Architecture](https://github.com/yh2866/AD-Targeting-for-Apple-Products-on-Twitter/blob/master/website/img/ad-airpod.png)


## 成员

|     姓名           |          邮件        | 
|  -------------------   |   ------------------| 
| Jingyi Wang            | jw3592@columbia.edu |
| Fangbing Liu           | fl2476@columbia.edu    |
| Yuanqing Hong        |  yh2866@columbia.edu   |
