# easystudy
雨课堂刷课代码（yuketang.py）

此代码仅作学习交流使用，产生的其他任何后果需自己承担，参考博客链接：https://www.52pojie.cn/thread-1777239-1-1.html

此代码可用于某农业大学雨课堂某规范课，需要修改：x_csrftoken、cookie、starttime；其他课程需修改classroomid、numstart、numend；其他学校需修改schoolurl（不确定其他学校是否可用）

打开F12，在网络里找heartbeat，cookie在标头，csrftoken和classroomid一般在cookie中包含，没有的话在应用程序的cookie里找（非前面提到的cookie）

numstart和numend：打开F12，点网络，点开一个课程视频，新生成的网络名称里面有一个193开头的八位数字，找到第一个和最后一个视频的数字替换numstart和numend

2023.10.27亲测可用，本来不懂这些刷课代码，只是在网上找帖子改下参数什么的，后来朋友发现源代码时间戳有问题（刷课时间显示2021年），后来学了下html和爬虫的基础知识，尝试复现了一下源代码，并进行了少许更改，但是对刷课技术仍然是一知半解，独立实现一个新网站的刷课代码还是很困难，如果有比较懂的大佬知道怎么学相关知识还望不吝赐教。
