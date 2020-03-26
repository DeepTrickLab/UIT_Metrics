# Metrics of Unsupervised Image-to-Image Translation
## Preparation
* Clone: `git clone https://github.com/DeepTrickLab/UIT_Metrics.git`
* Install dependency:
  * numpy
  * Tensorflow 2.x
  * Pytorch (for LPIPS)
  * Matplotlib
  * YAML
## Reconstruction Metrics
### Scores Meaning
* LPIPS: Higher means further/more different. Lower means more similar.
* PSNR: Higher means more similar. 42~45db stands for close. 45db above: extremely close.
* SSIM: range[0, 1], 1 means completely similar. 0.980~0.990: allowance 0.990 above: extremely close.

## Usage
### Dummy Execution
```
./recon_run.sh <ImageA_Directory> <ImageB_Directory> <Output_Directory> <Figure_Title>
```
## Citation
### LPIPS
```
@inproceedings{zhang2018perceptual,
  title={The Unreasonable Effectiveness of Deep Features as a Perceptual Metric},
  author={Zhang, Richard and Isola, Phillip and Efros, Alexei A and Shechtman, Eli and Wang, Oliver},
  booktitle={CVPR},
  year={2018}
}
```