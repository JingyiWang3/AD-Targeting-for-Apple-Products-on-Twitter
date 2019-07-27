# Twitter 广告定向投放项目

## 简介
推特广告是扩展业务覆盖面的好方法，能有效地将内容投放到目标市场，获取流量。本项目通过精心策划，如选择正确的关键词、人群、用户感兴趣的广告文案、以及有影响力的广告推广人，来达到以最低的成本使用推特广告，“击中”最有购买可能的潜在客户，了解用户的需求，为用户体验优化提供方向的目标。


## 流程
![Image of Architecture](https://github.com/yh2866/AD-Targeting-for-Apple-Products-on-Twitter/blob/master/website/img/diagram2.png)

1. 通过 Twiiter API 抓取包含关键词 airpod 的数据，对数据进行简单的处理，存入MangoDB 中。
2. 数据分析流程

   * 使用用户个人描述及用户信息，建立用户画像（包含地域、活跃时间、客户端、用户职业、兴趣、受教育程度、是否结婚、有孩子等标签），定位对 airpod 感兴趣的受众。
   * 使用 LDA 算法分析推文主题作为广告核心话题，可以把这些主题理解为用户对 Airpods 最关注的点。同时通过分析这些包含了主观情感色彩的推文来了解用户对产品的看法，为用户体验优化提供方向。
   * 通过构造社交网络，结合 PageRank 算法挖掘出有影响力的用户作为广告推广人。
3. 使用 Flask框架搭建网站，实现可视化。
  

## 不足

无法真正花钱在 Twitter 上打广告查看效果，缺乏清晰的效果统计工具，以及合理的广告结算方式。


## 目录介绍
```data_collection```：数据采集代码

```data_processing```：数据清洗和数据分析代码，包含词云、LDA、情感分析、及PageRank的代码

```data_processing/main.ipynb```：数据分析代码汇总

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

### 用户基本信息页面
![Image of Architecture](https://github.com/yh2866/AD-Targeting-for-Apple-Products-on-Twitter/blob/master/website/img/geo.png)

### 主题分析和情感分析页面
![Image of Architecture](https://github.com/yh2866/AD-Targeting-for-Apple-Products-on-Twitter/blob/master/website/img/sen.png)

### 用户重要性分析页面
![Image of Architecture](https://github.com/yh2866/AD-Targeting-for-Apple-Products-on-Twitter/blob/master/website/img/influ.png)

### 广告策略页面
![Image of Architecture](https://github.com/yh2866/AD-Targeting-for-Apple-Products-on-Twitter/blob/master/website/img/ad-banner.png)
![Image of Architecture](https://github.com/yh2866/AD-Targeting-for-Apple-Products-on-Twitter/blob/master/website/img/ad-airpod.png)


## 成员

|     姓名           |          邮件        | 
|  -------------------   |   ------------------| 
| Jingyi Wang            | jw3592@columbia.edu |
| Fangbing Liu           | fl2476@columbia.edu    |
| Yuanqing Hong        |  yh2866@columbia.edu   |
