import os
from tqdm import tqdm

dir_imgs = './imgs'
dir_out = './out'
dir_model = './model'


ls_imgs = os.listdir(dir_imgs)


for img_ind in tqdm(ls_imgs):
    try:
        os.system('sbb_binarize --patches -m '+dir_model+' '+os.path.join(dir_imgs,img_ind)+' '+os.path.join(dir_out,img_ind) )
    except:
        pass
