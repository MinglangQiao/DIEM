# DIEM
verify the fixation number vs. cc curve in DIEM

here is the [DIEM Website](https://thediemproject.wordpress.com/videos-and%C2%A0data/) 
```
1. 先测平均每帧有多少个fixation， 比如20个

2. 忽略那些每帧fixation数少于阀值的frame

3. 对fixation数大于阀值的frame， 先取前2个，用一个人测剩下的人， 循环完这2个人，再取平均； 再取前3个人， 用1个人测剩下的2的人， 循环完3个人取平均;
再取4个人，用1个人测剩下的3个人， 循环完这4个人取平均; ......; 一直取到低于阀值那么多个人， 比阀值多的就不再继续取了


```

