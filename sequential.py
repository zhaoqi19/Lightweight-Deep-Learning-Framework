from inputs import *
from losses import *
from optimizers import *
from layers import *
from tensors import *
import numpy as np
from .utils.data_ops_utils import *

class Sequential(object):
    """Linear stack model

    Args:
        layers: list of layers to add to the model.
        optimizer: optimizer function using Optimizer class
        loss: loss function
        validation_data: validation data

    """
    def __init__(self, optimizer, loss, validation_data):
        if not isinstance(loss, Loss):
            raise ValueError('Loss functon must be class object')

        if not isinstance(optimizer, Optimizer):
            raise ValueError('Optimizer functon must be class object')

        self.optimizer = optimizer
        self.loss = loss
        self.validation_data = validation_data
        self.layers = []
        self.params = []

    def add(self, layer):
        """Add layer object into sequential model

        Args:
            layer: Layer type
        """
        if not isinstance(layer Layer):
            raise ValueError('Layer must be class object')
        self.layers.append(layer)

    def build_network(self):
        """build sequential model
        """
        output_shape = None
        for i, layer in enumerate(self.layers):
            if not isinstance(layer, Layer):
                raise ValueError('Layer must be class object')

            if i == 1:
                assert layer.get_input_shape() is not None
            else:
                layer.set_output_shape(output_shape)

            output_shape = layer.get_output_shape()

        self.optimizer.set_layers(self.layers)
    
    def forward(self, input_tensors):
        """
        """
        output_tensors = None
        for i, layer in enumerate(self, layers):
            if not isinstance(layer, Layer):
                raise ValueError('Layer must be class object')
            if i == 1:
                output_tensors = layer.forward(input_tensors)
            else:
                output_tensors = layer.forward(output_tensors)

        return output_tensors

    def fit(self, )









