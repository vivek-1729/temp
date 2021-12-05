from genericpath import exists
import os
from posixpath import normpath
from typing import DefaultDict
os.chdir("data2/Denoising")
files = os.listdir()
noisy = [x for x in files if 'nosiy' in x]
denoised = list(set(files) - set(noisy))


def split_data(data):
    test = [x for x in data if 'TEST' in x]
    train = [x for x in data if 'TRAIN' in x]
    tb_test = [x for x in test if 'px' in x]
    non_tb_test = [x for x in test if 'nx' in x]
    tb_train = [x for x in train if 'px' in x]
    non_tb_train = [x for x in train if 'nx' in x]
    return tb_test, non_tb_test, tb_train, non_tb_train

n_tb_test, n_non_tb_test, n_tb_train, n_non_tb_train = split_data(noisy)
d_tb_test, d_non_tb_test, d_tb_train, d_non_tb_train = split_data(denoised)

# os.chdir('..')
# try:
#     os.makedirs("denoised/test/non-tb")
#     os.mkdir("denoised/test/tb")
#     os.mkdir("denoised/train")
#     os.mkdir("denoised/train/non-tb")
#     os.mkdir("denoised/train/tb")

#     os.makedirs("noisy/test/non-tb")
#     os.mkdir("noisy/test/tb")
#     os.mkdir("noisy/train")
#     os.mkdir("noisy/train/non-tb")
#     os.mkdir("noisy/train/tb")
# except FileExistsError:
#     print("File exists")


# print(os.listdir())

def move_file(path, files):
    [os.rename(x, path+x) for x in files]

# path = "../noisy/test/tb/"
# move_file(path, n_tb_test)

# path = "../noisy/test/non-tb/"
# move_file(path, n_non_tb_test)

# path = "../noisy/train/tb/"
# move_file(path, n_tb_train)

# path = "../noisy/train/non-tb/"
# move_file(path, n_non_tb_train)


# path = "../denoised/test/tb/"
# move_file(path, d_tb_test)

# path = "../denoised/test/non-tb/"
# move_file(path, d_non_tb_test)

# path = "../denoised/train/tb/"
# move_file(path, d_tb_train)

# path = "../denoised/train/non-tb/"
# move_file(path, d_non_tb_train)