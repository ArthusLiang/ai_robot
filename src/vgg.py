import re
import tensorflow as tf
import tensorflow_hub as hub

from core import path_model

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
    
    def run(self, path_input_content, path_input_style, path_output):
        style = self.__load(path_input_style)
        style = style[tf.newaxis, :]
        content = self.__load(path_input_content, False)
        content = content[tf.newaxis, :]
        outputs = self.hub_module(content, style)
        stylized_image = outputs[0] * 255
        tf.keras.preprocessing.image.save_img(path_output, stylized_image[0])
        return
