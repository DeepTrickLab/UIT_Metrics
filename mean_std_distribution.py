import argparse
import numpy as np
import yaml
import matplotlib.pyplot as plt

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, help = 'yaml files')
    parser.add_argument('-n', '--name', type=str, help = 'A name for figure title', default="")
    parser.add_argument('-o', '--output_name', type=str, help = 'output filename', default="histogram")
    parser.add_argument('--nbins', type=int, help = 'distribution nbins', default=20)
    opt = parser.parse_args()
    
    with open(opt.file, 'r') as stream:
        score_dict = yaml.load(stream, Loader=yaml.FullLoader)
    score_name = []
    for filename in score_dict:
        for metric_name in score_dict[filename]:
            score_name.append(metric_name)
        break
        
    score_lists = {x:[] for x in score_name}
    for filename in score_dict:
        for metric_name in score_dict[filename]:
            score_lists[metric_name].append(score_dict[filename][metric_name])
            
    # row = 1. column = len(score_name)
    fig, axs = plt.subplots(1, len(score_name), sharey=True)
    for idx, metric_name in enumerate(score_lists):
        mean_val = np.mean(score_lists[metric_name])
        std_val = np.std(score_lists[metric_name])
        axs[idx].hist(score_lists[metric_name], bins=opt.nbins, align='left')
        axs[idx].set_title(metric_name)
        axs[idx].set_xlabel('score\nmean: %.3f\nstd: %.3f' % (mean_val, std_val))
        axs[idx].set_ylabel('amount')
    fig.suptitle(opt.name, fontsize=16)
    plt.savefig(opt.output_name + '.png',bbox_inches='tight')