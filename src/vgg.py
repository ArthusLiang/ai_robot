import os
import re
import shutil
import tensorflow as tf
import tensorflow_hub as hub

current_file_dir = os.path.dirname(os.path.realpath(__file__))
path_root = os.path.abspath(os.path.join(current_file_dir, '../'))
path_model = os.path.join(path_root, 'models/magenta_arbitrary-image-stylization-v1-256_2')

path_style = os.path.join(path_root, 'data/style2.png')
path_content = os.path.join(path_root, 'data/content.png')
path_output = os.path.join(path_root, 'data/out.jpg')

default_re = re.compile(r'.(jpg|png)$', re.I)

class VGG:
    def __init__(self):
        self.hub_module = hub.load(path_model)
        return
    
    def __load(self, path, need_resize=True):
        image = tf.io.read_file(path)
        image = tf.io.decode_image(image, 3)
        if need_resize:
            image = tf.image.resize(image, [256,256]) # [256,256]
        return tf.cast(image / 255, tf.float32)
    
    def run(self):
        style = self.__load(path_style)
        style = style[tf.newaxis, :]
        content = self.__load(path_content, False)
        content = content[tf.newaxis, :]
        outputs = self.hub_module(content, style)
        stylized_image = outputs[0] * 255
        # tf.keras.preprocessing.image.save_img(path_output, stylized_image[0])
        return
    
with tf.device('/CPU:0'):
    vgg = VGG()
    vgg.run()
    print('Finish Job!')