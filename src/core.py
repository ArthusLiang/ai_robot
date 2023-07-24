import sys
import os

# 获取命令行参数列表
args = sys.argv

def get_args():
    ret = {}
    args = sys.argv
    if len(args) > 1:
        for arg in args[1:]:
            pair = arg.split("=")
            if len(pair) > 1:
                ret[pair[0]]=pair[1]
    return ret

current_file_dir = os.path.dirname(os.path.realpath(__file__))
path_root = os.path.abspath(os.path.join(current_file_dir, '../'))
path_model = os.path.join(path_root, 'models/magenta_arbitrary-image-stylization-v1-256_2')
path_style = os.path.join(path_root, 'data/style2.png')
path_content = os.path.join(path_root, 'data/content.png')
path_output = os.path.join(path_root, 'data/out.jpg')