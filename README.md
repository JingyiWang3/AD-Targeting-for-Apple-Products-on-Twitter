# Twitter 广告定向投放项目

**介绍** 

结合用户社交、兴趣，利用专业数据算法打造的 Airpods Twitter 广告营销推广策略

**目标**

1. 挖掘用户数据，建立用户标签，对其进行个性化推送，以更低的费用获得获取更大的营销效果。
2. 了解用户想法及需求，为用户体验优化提供方向，达到获客、黏客的目的。

**流程**
![Image of Architecture](https://github.com/yh2866/AD-Targeting-for-Apple-Products-on-Twitter/blob/master/website/img/diagram2.png)

**代码**

```data_collection```：获取数据

```data_processing```：数据清洗

```data_processing/main.ipynb``` 

```output```：中间结果图

```website```：网站搭建代码


**缺点**
1. 无法真正花钱在 Twitter 上打广告。
1. 缺少广告出价和付费方式，清晰的效果统计工具，以及合理的结算方式


#### The website is hosted on Google Cloud and can be access through: [http://35.196.85.28:5000/](http://35.196.85.28:5000/)

## Run Instruction:

clone the git repository: 

`git clone: git@github.com/yh2866/AD-Targeting-for-Apple-Products-on-Twitter.git`

get into "website" folder:

`python3 app.py`

get into "website/s3" folder:

`python -m SimpleHTTPServer`

And then, the website is availble through: '0.0.0.0:5000'




### Main page of website:
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


**Team Members:**

|UNI     |       Name             |           Email        |
| ------ |  -------------------   |   ---------------------|
|jw3592  |   Jingyi Wang            | jw3592@columbia.edu |
|fl2476  |  Fangbing Liu           | fl2476@columbia.edu    |
|yh2866  |   Yuanqing Hong        |  yh2866@columbia.edu   |
