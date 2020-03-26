import tensorflow as tf
import argparse
import os
import cv2
import pathlib
import yaml

def load_image(path):
    if(path[-3:] == 'dng'):
        import rawpy
        with rawpy.imread(path) as raw:
            img = raw.postprocess()
    elif(path[-3:]=='bmp' or path[-3:]=='jpg' or path[-3:]=='png'):
        import cv2
        return cv2.imread(path)[:,:,::-1]
    else:
        img = (255*plt.imread(path)[:,:,:3]).astype('uint8')

    return img

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d0','--dir0', type=str, default=None)
    parser.add_argument('-d1','--dir1', type=str, default=None)
    parser.add_argument('-o','--out', type=str, default=None)
    parser.add_argument('--yaml', type=str, default=None)
    opt = parser.parse_args()
    
    with open(opt.out, 'w') as f:
        files = os.listdir(opt.dir0)

        for file in files:
            if(os.path.exists(os.path.join(opt.dir1,file))):
                img0 = tf.io.read_file(os.path.join(opt.dir0,file))
                img1 = tf.io.read_file(os.path.join(opt.dir1,file))
                img0 = tf.io.decode_jpeg(img0)
                img1 = tf.io.decode_jpeg(img1)

                psnr01 = tf.image.psnr(img0, img1, 255)
                ssim01 = tf.image.ssim(img0, img1, 255)

                print('%s: ' % file)
                print('  psnr: %.3f' % psnr01)
                print('  ssim: %.3f' % ssim01)
                f.writelines('%s:\n'% file)
                f.writelines('  psnr: %.6f\n'% psnr01)
                f.writelines('  ssim: %.6f\n'% ssim01)
            