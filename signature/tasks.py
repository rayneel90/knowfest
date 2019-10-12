from base64 import b64decode
import cv2
import numpy as np
import os
from glob import glob
import cv2
import numpy as np
from skimage.measure import compare_ssim as ssim
# import matplotlib.pyplot as plt
from glob import glob


# In current demo version, this acount is hardcoded to Yuvraj's account. When
# deployed on real data, this will check the input account number against all
# available accounts

def check_cust(cust_id):

    return "Success" if os.path.exists(os.path.join('media/sample/', cust_id)) \
            else "Failure"

class SignatureCheck():
    # Initialize data step
    def __init__(self,acct_no):
        ## Initialise with sample image for given account no
        self.acct_no = acct_no
        imgs = glob('media/sample/{}/*'.format(acct_no))
        smpl = [cv2.imread(i)for i in imgs] # read the image
        self.sample = [cv2.cvtColor(cv2.resize(i, (2000, 2000)), cv2.COLOR_BGR2GRAY) for i in smpl] #resizing & grayscale

    def verify_sig(self,cutoff_percent,test_image_path):
        # import and convert test image to grayscale
        test_image = cv2.imread(test_image_path)
        test_image = cv2.resize(test_image, (2000, 2000))
        test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

        ## Test MSE
        # sum of the squared difference between the two images;
        # NOTE: the two images must have the same dimension
        mse = [np.sum((i.astype("float") - test_image.astype("float")) ** 2) for i in self.sample]
        mse = [i / float(i.shape[0] * i.shape[1]) for i in self.sample]

        ## Calculate Structural similarity Index
        s = np.mean([ssim(i, test_image) for i in self.sample])

        ## Cut-off settings
        check ='Signature Match'
        return s, s > cutoff_percent

# This function will take an input object ( which contain attributes `image` and
# `account`) and compute the authenticity

def check_authenticity(input):
    try:
        arr = np.frombuffer(b64decode(input.image), np.uint8)
    except Exception as e:
        return None, "invalid text string"
    else:
        img = cv2.imdecode(arr, cv2.IMREAD_ANYCOLOR)
        return True, None  # change this to implement the actual check

