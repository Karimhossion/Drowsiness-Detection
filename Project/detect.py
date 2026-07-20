import cv2
import numpy as np
import os
from keras.models import load_model
from keras.layers import Dense
from pygame import mixer

# Patch Dense to handle quantization_config from newer Keras versions
_original_dense_init = Dense.__init__
def _patched_dense_init(self, **kwargs):
    kwargs.pop('quantization_config', None)
    _original_dense_init(self, **kwargs)
Dense.__init__ = _patched_dense_init
