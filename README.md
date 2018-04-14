# DIEM
verify the fixation number vs. cc curve in DIEM

here is the [DIEM Website](https://thediemproject.wordpress.com/videos-and%C2%A0data/) 
```
1. 先测平均每帧有多少个fixation， 比如20个

2. 忽略那些每帧fixation数少于阀值的frame

3. 对fixation数大于阀值的frame， 先取前2个，用一个人测剩下的人， 循环完这2个人，再取平均； 再取前3个人， 用1个人测剩下的2的人， 循环完3个人取平均;
再取4个人，用1个人测剩下的3个人， 循环完这4个人取平均; ......; 一直取到低于阀值那么多个人， 比阀值多的就不再继续取了


```

### database
The basic properties of the existing eye-tracking databases

| Database  | valid fixation each frame | total fixation | total frame | Videos | subjects | Year |
| :---:  | :---:  | :---:  | :---:  |:---:  | :---:  | :---:  |
| [CRCNS](https://crcns.org/data-sets/eye/eye-1)  | 3.60  | 118785  | 32989  | 50  | 4.7(ave)  | 2004  |
| SFU  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| DIEM | Content Cell  | 58 | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| Hollywood | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| Xu | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| IRCCyN  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| ASCMN  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| CAMO  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| Marat | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| SAVAM  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| TUD  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| Peters | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| Coutrot-1 | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
