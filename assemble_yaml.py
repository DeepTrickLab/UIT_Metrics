import yaml
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs = "*", help = 'yaml files')
    parser.add_argument('-o', '--output', default='metrics.yaml', help='output filename')
    opt = parser.parse_args()
    
    yaml_files = []
    for filename in opt.files:
        with open(filename, 'r') as stream:
            file = yaml.load(stream, Loader=yaml.FullLoader)
            yaml_files.append(file)
            
    output_dict = yaml_files[0].copy()
    for line in yaml_files[0]:
        for idx in range(1,len(yaml_files)):
            output_dict[line].update(yaml_files[idx][line])
    
    with open(opt.output, 'w') as fp:
        yaml.dump(output_dict, fp)