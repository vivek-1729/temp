import numpy as np
from scipy.ndimage import zoom
from PIL import Image
from matplotlib import pyplot as plt
import cv2, imageio
def cv2_clipped_zoom(img, zoom_factor, x1, x2, y1, y2):
    """
    Center zoom in/out of the given image and returning an enlarged/shrinked view of 
    the image without changing dimensions
    Args:
        img : Image array
        zoom_factor : amount of zoom as a ratio (0 to Inf)
    """
    height, width = img.shape[:2] # It's also the final desired shape
    new_height, new_width = int(height * zoom_factor), int(width * zoom_factor)
    cropped_img = img[y1:y2, x1:x2]
    # return cropped_img

    # Handle padding when downscaling
    resize_height, resize_width = min(new_height, height), min(new_width, width)
    # pad_height1, pad_width1 = (height - resize_height) // 2, (width - resize_width) //2
    # pad_height2, pad_width2 = (height - resize_height) - pad_height1, (width - resize_width) - pad_width1
    # pad_spec = [(pad_height1, pad_height2), (pad_width1, pad_width2)] + [(0,0)] * (img.ndim - 2)

    result = cv2.resize(cropped_img, (resize_width, resize_height))
    # result = np.pad(result, pad_spec, mode='constant')
    # assert result.shape[0] == height and result.shape[1] == width
    return result

x1, y1, x2, y2 = (100,100,400,300)
fname = 'base.png'
# fname = 'download.png'
baseImg = cv2.imread(fname)
baseImg = cv2.rectangle(baseImg, (x1,y1), (x2,y2), (255,0,0), 2)
cv2.imshow('base', baseImg)
cv2.imwrite('orig2.png', baseImg)
cv2.waitKey(0)


img = imageio.imread(fname)
imgArray = cv2_clipped_zoom(img,1.5, x1, x2, y1, y2)
zoomImg = Image.fromarray(imgArray)
opencvImage = cv2.cvtColor(np.array(zoomImg), cv2.COLOR_RGB2BGR)
# cv2.imwrite('zoom2.png', opencvImage)
cv2.imshow('zoom', opencvImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
