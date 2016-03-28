# 第四次作业

##摘要
####所选微分方程：
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bdv%7D%7Bdt%7D%3Da-bv)

* 使用**Euler method**计算自由落体中速度与时间关系
* 使用**matplotlib**绘制图像 

 

## 背景
* 含摩擦力情况下物体受外力运动，如降落伞下降。

* 关键点在于，当速度增大至一定值时，加速度为零，即保持恒定的速度运动，达到稳定值。
##正文
* 按照**Euler method**，利用**for**循环语句计算**v**值

* 利用**matplotlib**画图

* 直接解微分方程可得：

![](http://latex.codecogs.com/gif.latex?%5Cint_0%5Ev%20%5Cfrac%7B%7B%5Crm%20d%7Dv%7D%7Ba-bv%7D%20%3D%20%5Cint_0%5Et%7B%7B%5Crm%20d%7Dt%7D)

![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Ba%7D%7Bb%7D%281-e%5E%7B-bt%7D%29)

* 这里是[源代码](https://github.com/yyfwhu/computationalphysics_N2013301020096/blob/master/hw4.py)


* 这里是[数据](https://github.com/yyfwhu/computationalphysics_N2013301020096/blob/master/%E7%AC%AC%E5%9B%9B%E6%AC%A1%E4%BD%9C%E4%B8%9A%E6%95%B0%E6%8D%AE)  
![friction](https://github.com/yyfwhu/computationalphysics_N2013301020096/blob/master/figure_1.jpg)
  
##总结
* 下一步，继续完善一下绘图效果。这个比较简单，毕竟建房子难，装修还是比较简单的嘛。有空再装饰一下
选题还是比较简单的。。。。
github不能显示公式真是头疼

##致谢
* 感谢[matplotlib教程](http://liam0205.me/2014/09/11/matplotlib-tutorial-zh-cn/)写的非常详细
* 感谢[蔡老师的例子](https://github.com/caihao/computational_physics_whu/blob/master/chapter1/uranium_decay.py)虽然太长，以后慢慢研读
