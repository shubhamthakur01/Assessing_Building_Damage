from os import path, makedirs, listdir
import sys
import numpy as np
np.random.seed(1)
import random
random.seed(1)

sys.setrecursionlimit(10000)
from multiprocessing import Pool

import torch
from torch import nn
from torch.backends import cudnn

from torch.autograd import Variable

import pandas as pd
from tqdm import tqdm
import timeit
import cv2

from zoo.models import *


from pipeline1 import Xview_Fn

from utils import *

from skimage.morphology import remove_small_objects

import matplotlib.pyplot as plt
import seaborn as sns

from skimage.morphology import square, dilation

from flask import Flask ,request, redirect, url_for,render_template ,request

import os 
from PIL import Image


from flask_ngrok import run_with_ngrok




APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
run_with_ngrok(app)

@app.route("/")

def index():
	return render_template("index.html")

@app.route("/upload" ,methods =['POST'])

def upload():
	target = os.path.join(APP_ROOT , "static/")
	print(target)

	if not os.path.isdir(target):
		os.mkdir(target)

	
	pre_image=request.files["pre_image"]
	print(pre_image)
	
	I_1 = np.asarray(Image.open(pre_image))
	if I_1.shape[2] == 4:
	    I_1 = I_1[:,:,0:3]
	    
	#I=I[::-1, :]
	filename_pre = pre_image.filename
	#destination = "/".join([target , "shubham.jpg"])
	destination = "/".join([target , "pre_image.png"])
	print(destination)
	I1 = Image.fromarray(I_1)
	I1.save(destination)


	post_image=request.files["post_image"]
	print(post_image)
	I_2 = np.asarray(Image.open(post_image))
	
	if I_2.shape[2] == 4:
	    I_2 = I_2[:,:,0:3]
	
	filename_post = post_image.filename
	#destination = "/".join([target , "shubham.jpg"])
	destination = "/".join([target , "post_image.png"])
	print(destination)
	I2 = Image.fromarray(I_2)
	I2.save(destination)
	Xview_Fn(I_1,I_2)
	
	return render_template("complete1.html")


if __name__ == "__main__":
	app.run()

