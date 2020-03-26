import argparse
import yaml
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec

def writeImageData(images, img_dplist,
                   data,   data_dplist,
                   filename=None, square_size=128):
    category_imgs = len(images)
    batch_size = len(images[0])
    imgs_nrow = category_imgs
    imgs_ncol = batch_size
    data_nrow = len(data_dplist)
    nrow = imgs_nrow + data_nrow
    ncol = imgs_ncol
    display_list = img_dplist + data_dplist
    fig = plt.figure(figsize=(ncol+1, nrow+1), dpi=square_size)
    gs = gridspec.GridSpec(nrow, ncol,
             wspace=0.0, hspace=0.0, 
             top=1.-0.5/(nrow+1), bottom=0.5/(nrow+1), 
             left=0.5/(ncol+1), right=1-0.5/(ncol+1))
    for j in range(ncol):
        for i in range(nrow):
            ax = plt.subplot(gs[i,j])
            if i >= imgs_nrow:
                ax.annotate('%.2f' % data[i - imgs_nrow][j],(0.25,0.5),
                           xycoords='axes fraction', va='center')
            else:
                # ax.imshow(img_to_uint8(images[i][j]))
                ax.imshow(images[i][j])
            ax.set_xticklabels([])
            ax.set_yticklabels([])
            ax.tick_params(axis=u'both', which=u'both',length=0)
            for axis in ['top','bottom','left','right']:
                ax.spines[axis].set_linewidth(0)
            if j == 0:
                plt.ylabel(display_list[i])
    if filename is not None:
        plt.savefig(filename + '.png',bbox_inches='tight')
    plt.close('all')
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o','--output', type=str, default=None)
    parser.add_argument('-y','--yaml', type=str, default=None)
    parser.add_argument('-d', '--dict', nargs = "*", help = 'all dictionary')
    opt = parser.parse_args()
    
    score_dict = None
    with open(opt.yaml, 'r') as stream:
        score_dict = yaml.load(stream, Loader=yaml.FullLoader)
    
    score_name = []
    for filename in score_dict:
        for metric_name in score_dict[filename]:
            score_name.append(metric_name)
        break
        
    score_lists = [[] for _ in range(len(score_name))]
    xa_path = opt.dict[0]
    xr_path = opt.dict[1]
    category_name = ['xa','xr']
    xa = []
    xr = []
    for f_idx,filename in enumerate(score_dict):
        tmp_xa = cv2.imread(os.path.join(xa_path,filename))
        tmp_xr = cv2.imread(os.path.join(xr_path,filename))
        tmp_xa = cv2.cvtColor(tmp_xa, cv2.COLOR_BGR2RGB)
        tmp_xr = cv2.cvtColor(tmp_xr, cv2.COLOR_BGR2RGB)
        xa.append(tmp_xa)
        xr.append(tmp_xr)
        for idx,metric_name in enumerate(score_dict[filename]):
            score_lists[idx].append(score_dict[filename][metric_name])
            
    writeImageData((xa,xr), category_name,
                   score_lists,   score_name,
                   filename=opt.output, square_size=128)