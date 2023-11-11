#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 08:34:44 2022

@author: bounasr
"""

import os
from PIL import Image, ImageOps
import numpy as np
import math

def sliding_window(image, patch_size=[299,299],
                   step_size=299,
                   output_path = "folder_path",
                   output_name = "name"):

    for i in range(0, image.shape[0] - patch_size[0] + 1, step_size):
        for j in range(0, image.shape[1] - patch_size[1] + 1, step_size):
            patch = image[i:i + patch_size[0], j:j + patch_size[1]]
            im_patch = Image.fromarray(patch)
            im_patch.save(output_path + "/" + str(output_name) + str(i) + "-" + str(j) + ".jpg")
            print(i, j)


def load_images(path):
    print('Loading images...')
    images = [os.path.join(path, f) for f in os.listdir(path)]

    return images

def main():
    images = load_images('image_path')
    for img in images:
        print('Processing: ' + str(img))
        img_file = Image.open(img)
        image = np.array(img_file.convert('RGB'))
        sliding_window(image, output_name=img.split('/')[6].split('.')[0])


if __name__ == "__main__":
    main()
