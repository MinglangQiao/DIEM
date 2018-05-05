This repository provides database properties and download links in the paper
* [ **Predicting Video Saliency using Object-to-Motion CNN and Two-layer Convolutional LSTM**](https://arxiv.org/abs/1709.06316)

# DIEM
verify the fixation number .vs cc curve in DIEM

here is the [DIEM Website](https://thediemproject.wordpress.com/videos-and%C2%A0data/) 
```
1. 先测平均每帧有多少个fixation， 比如20个

2. 忽略那些每帧fixation数少于阀值的frame

3. 对fixation数大于阀值的frame， 先取前2个，用一个人测剩下的人， 循环完这2个人，再取平均； 再取前3个人， 用1个人测剩下的2的人， 循环完3个人取平均;
再取4个人，用1个人测剩下的3个人， 循环完这4个人取平均; ......; 一直取到低于阀值那么多个人， 比阀值多的就不再继续取了


```

### database
The basic properties of the existing eye-tracking databases

| Database  | valid fixations of each frame | total fixations | total frames | Videos | subjects | Year |
| :---:  | :---:  | :---:  | :---:  |:---:  | :---:  | :---:  |
| [CRCNS](https://crcns.org/data-sets/eye/eye-1)  | 3.60  | 118,785  | 32,989  | 50  | 4.7(ave)  | 2004  |
| [SFU](http://www.sfu.ca/~ibajic/#data)  | 14.94  | 47,061  | 3,150  | 12  | 15  | 2012  |
| [DIEM](https://thediemproject.wordpress.com/) | 57.80  | 13,897,289 | 240,452  | 84  | 50(total_record: 5586)  | 2011  |
| Hollywood | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| Xu | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| IRCCyN  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| [VAGBA](http://ilab.usc.edu/vagba/dataset/VidCom/)  | 11.52  | 172,859  | 15,000  | 50  | 14  | 2011  |
| [GazeCom](http://www.inb.uni-luebeck.de/fileadmin/files/MITARBEITER/Dorr/EyeMovementDataSet.html)  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| [ASCMN](http://www.tcts.fpms.ac.be/attention/index.php?categorie2/databases&database=001)  | 9.36  | 95,271  | 10,180  | 24  | 13(actual 10)  | 2012 |
| [Coutrot-2](http://antoinecoutrot.magix.net/public/databases.html) | 39.32  | 670,409  | 17,049  | 15  | 40  | 2015  |
| CAMO  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| Marat | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| [SAVAM](http://compression.ru/video/savam/)  | 55.76(some peopel view twice)  | 1,023,758  | 19,760(actual 18360)  | 43(41)  | 50(actual 48, 10 people look twice, total_record: 2378)  | 2014  |
| TUD  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| Peters | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| [Coutrot-1](http://antoinecoutrot.magix.net/public/databases.html) | 66.65  | 1,742,344  | 26,140 | 60 | 20(actual 72)  | 2013  |
