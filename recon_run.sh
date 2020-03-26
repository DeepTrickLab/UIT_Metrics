
echo Processing LPIPS
python ./PerceptualSimilarity/compute_dists_dirs.py -d0 $1 -d1 $2 -o $3/lpips_score.yaml --use_gpu
echo Processing PSNR and SSIM
python ./Tensorflow/psnr_ssim.py -d0 $1 -d1 $2 -o $3/psnr_ssim_score.yaml
echo Assemble LPIPS, PSNR and SSIM score to one yaml file
python assemble_yaml.py $3/lpips_score.yaml $3/psnr_ssim_score.yaml -o $3/recon_metrics.yaml
echo Output Image Table with metric score
python write_img_text.py -y $3/recon_metrics.yaml -o $3/imageTable -d $1 $2
echo Output score distribution
python mean_std_distribution.py -f $3/recon_metrics.yaml -n $4 -o $3/recon_histogram
echo Done