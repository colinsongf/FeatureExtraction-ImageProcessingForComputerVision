# coding: utf-8
# 根据《计算机视觉特征提取与图像处理》71页高斯平均算子公式编写
# 2016年01月29日11:51:47
# Author: Haoyang Xie

import numpy as np

# in order to use math.exp()...
import math

def gaussian_template(winSize, sigma):
#  Parameters: winsize    - size of template (odd, integer)
#              sigma      - variance of Gaussian function

	# centre is half of winSize
	# 在matlab中，centre = floor(winSize/2) + 1
	# 因为matlab下标从1开始，5/2 + 1 = 3, 正好处于中间
	# 在numpy中，下表从0开始，正中间是2， 5/2=2, 不用再加1
	centre = np.int(winSize/2)

	# normlizese by the total sum
	sum = 0.0

	# the kernel
	kernel = np.zeros((winSize, winSize), np.float)

	for i in range(winSize):
		for j in range(winSize):
			#kernel[i,j] = math.exp(-(((j-centre)*(j-centre))+((i-centre)*(i-centre)))/ np.float(2*sigma*sigma))
			kernel[i][j] = math.exp(-( ((j-centre)**2 + (i-centre)**2) / (2*(sigma**2)) )) #/ (2*3.14*sigma*sigma)
			sum += kernel[i,j]

	kernel = kernel/sum
	return kernel


if __name__ == '__main__':
	kel = gaussian_template(5, 1.0)
	print '高斯核是: '
	print np.around(kel, 4)




