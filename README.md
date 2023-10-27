# easystudy
雨课堂刷课代码
此代码仅作学习交流使用，产生的其他任何后果需自己承担，参考博客链接：https://www.52pojie.cn/thread-1777239-1-1.html
此代码可用于某农业大学雨课堂某规范课，需要修改：x_csrftoken、cookie、starttime；其他课程需修改classroomid、numstart、numend；其他学校需修改schoolurl（不确定其他学校是否可用）
打开F12，在网络里找heartbeat，cookie在标头，csrftoken和classroomid一般在cookie中包含，没有的话在应用程序的cookie里找（非前面提到的cookie）
numstart和numend：打开F12，点网络，点开一个课程视频，新生成的网络名称里面有一个193开头的八位数字，找到第一个和最后一个视频的数字替换numstart和numend
