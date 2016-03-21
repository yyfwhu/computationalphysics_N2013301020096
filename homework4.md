# 第四次作业

##摘要
####所选微分方程：
$$\frac{dv}{dt} =a-bv$$

* 使用**Euler method**计算自由落体中速度与时间关系
* 使用**matplotlib**绘制图像 

 

## 背景
* 含摩擦力情况下物体受外力运动，如降落伞下降。
* 关键点在于，当速度增大至一定值时，加速度为零，即保持恒定的速度运动，达到稳定值。
##正文
* 按照**Euler method**，利用**for**循环语句计算**v**值

* 利用**matplotlib**画图

* 直接解微分方程可得：
   $$\int_0^v\frac {{\rm d}v}{a-bv}=\int_0^t{{\rm d}t}$$
   $$v=\frac{a}{b}(1-e^{-bt})$$
  
![friction](https://github.com/yyfwhu/computationalphysics_N2013301020096/blob/master/figure_1.jpg)
  
##总结

##致谢
