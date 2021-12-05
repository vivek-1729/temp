import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import glob

folder = glob.glob("images/*.png") # opens all image files of type TIF
folder.reverse()
print(folder)

grid_size = len(folder)
x = 2 # number of columns in resulting image. Make sure the number of images is divideable by x
y = int(grid_size/x)
n = 1

def asgrid():
    """Run this script in the folder the images are in and and image pdf should be produced.
    Set desired number of columns with 'x'. Set desired column and row labels with x_label and y_label.
    The more columns you use, the more labels you will have to set. If there is an 'index out of range error',
    make sure the files have the right ending (.TIF).
    """
    # set x_labels and y_labels by hand, depending on your grid type
    x_label_unique = ['Full', 'Zoomed In'] # labels below image
    y_label_unique =  ['Noisy', 'Denoised'] # labels left of image

    y_label = []
    for i in y_label_unique:
            for z in range(len(y_label_unique)):
                y_label.append(i)
            
    x_label = x_label_unique*len(x_label_unique)

    fig = plt.figure(dpi=300)
    grid = ImageGrid(fig, 111,
                        nrows_ncols=(x, y),
                        axes_pad=0.1,
                        share_all = True)
                        
    # for image_file in folder:
    #     print(image_file)
    for i in range(grid_size):
        image_file = folder[i]
        image = mpl.image.imread("./"+image_file)
        grid[i].imshow(image)
        # grid[i].axis('off')
        grid[i].set_xlabel(x_label[i])
        grid[i].set_ylabel(y_label[i])
        grid[i].tick_params(which='both', labelsize=0, bottom=False, top=False, left=False)
    fig.savefig("image.png", bbox_inches='tight', pad_inches=0, frameon=False)

asgrid()