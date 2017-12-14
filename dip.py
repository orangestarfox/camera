#coding:utf-8
import numpy as np
import cv2
import scipy
from skimage import data,restoration 
from scipy.signal import convolve2d as conv2
from scipy import fftpack
def ImConv(I0,kernel):
	m,n,z=I0.shape
	I=np.zeros((m,n,3))
	I[:,:,0]=conv2(I0[:,:,0],kernel,boundary='symm',mode='same') 
	I[:,:,1]=conv2(I0[:,:,1],kernel,boundary='symm',mode='same') 
	I[:,:,2]=conv2(I0[:,:,2],kernel,boundary='symm',mode='same') 
	I=I.astype('uint8')
	return I
def convolve(star, psf):
	star_fft = fftpack.fftshift(fftpack.fftn(star))
    	psf_fft = fftpack.fftshift(fftpack.fftn(psf))
        ret=fftpack.fftshift(fftpack.ifftn(fftpack.ifftshift(star_fft*psf_fft)))
	return ret.real.astype('uint8')
def deconvolve(star, psf):
	star_fft = fftpack.fftshift(fftpack.fftn(star))
    	psf_fft = fftpack.fftshift(fftpack.fftn(psf))
        ret=fftpack.fftshift(fftpack.ifftn(fftpack.ifftshift(star_fft/psf_fft)))
	return abs(ret).astype('uint8')
def gray(array):
	R=array[:,:,0]
	G=array[:,:,1]
	B=array[:,:,2]
	gray = (R*299 + G*587 + B*114 + 500) / 1000
	gray=gray.astype('uint8')
	return gray
def draw(array):
	a =gray(array)
	depth = 10.  # (0-100)
	grad = np.gradient(a)  # 取图像灰度的梯度值
	grad_x, grad_y = grad  # 分别取横纵图像梯度值
	grad_x = grad_x * depth / 100.
	grad_y = grad_y * depth / 100.
	A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
	uni_x = grad_x / A
	uni_y = grad_y / A
	uni_z = 1. / A
	vec_el = np.pi / 2.2  # 光源的俯视角度，弧度值
	vec_az = np.pi / 4.  # 光源的方位角度，弧度值
	dx = np.cos(vec_el) * np.cos(vec_az)  # 光源对x 轴的影响
	dy = np.cos(vec_el) * np.sin(vec_az)  # 光源对y 轴的影响
	dz = np.sin(vec_el)  # 光源对z 轴的影响
	b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)  # 光源归一化
	b = b.clip(0, 255)
	m,n=b.shape
	B=np.zeros((m,n,3))
	B[:,:,0]=b
	B[:,:,1]=b
	B[:,:,2]=b	
	return B.astype('uint8')




























