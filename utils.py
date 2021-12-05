import os

def getData(path):
    data = os.listdir('data/' + path)
    data = [i for i in data if i.endswith('.png')]
    return data

def create_folder(path):
    if not os.path.exists('data/' + path):
        os.mkdir('data/'+path)
        print('data/'+path, 'created')
    else:
        print('data/'+path, 'already exists')

def move_images(keyword, src, dst1, dst2):
    data = getData(src)
    for image in data:
        if keyword in image:
            os.rename('data/'+src + image, 'data/'+ src + dst1 + image)
        else:
            os.rename('data/'+src + image, 'data/'+ src + dst2 + image)

def split_data():
    create_folder('noisy')
    create_folder('denoised')
    move_images('noisy', '', 'noisy/', 'denoised/')


def train_test(folder):
    create_folder(folder + '/train')
    create_folder( folder + '/test')
    move_images('TRAIN', folder + '/','train/','test/')

def create_class(path):
    create_folder(path + '/tb')
    create_folder(path + '/non-tb')
    move_images('px',path+'/','tb/','non-tb/')

# create_class('denoised/train')