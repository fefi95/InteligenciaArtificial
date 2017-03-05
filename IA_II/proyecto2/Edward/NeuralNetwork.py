#!/usr/bin/env python
# -*- coding: latin-1 -*-
"""
    Universidad Simon Bolivar
    CI-5438 - Inteligencia Artificial
    Edward Fernandez 10-11121
    Carlos Ferreira 11-10323
    Stefani Castellanos 11-11394

    Description:
        This file contains the backpropagation implementation for neural networks
"""

# .----------------------------------------------------------------------------.
# Import libraries to use.

from random import seed
from random import random
from math   import exp

# .----------------------------------------------------------------------------.

"""
    Description: 
        Sigmoid function of the neural network (transfer the activation to see
        what the neuron output really is.
    Params:
        @param activation: this is the sample to see the neuron output.
"""
def sigmoid(activation):
    return 1.0 / (1.0 + exp(-activation))

"""
    Description: 
        Derivate of sigmoid function of the neural network.
        Calculate the derivative of an neuron output.
    Params:
        @param output: neuron output to use.
"""
def dsigmoid(output):
    return output * (1 - output)

class NeuralNetwork:
    """
        Description: 
            Creates a new neural network ready for training.
        Params:
            @param nInput : the number of inputs.
            @param nNeuron: the number of neurons to have in the hidden layer. 
            @param nOutput: the number of outputs.
    """
    def __init__(self, nInput, nNeuron, nOutput):
        # Creates the list to use like a neural network.
        self.net = list()
        # Creates nNeuron for the hidden layer and each neuron in the hidden layer has nInputs,
        # each with nNeuron + 1 weights because we have to add the bias. 
        hLayers = [{'weights': [random() for i in range(nInput + 1)]} for i in range(nNeuron)] 

        # Add the hidden layers to our neural network.
        self.net.append(hLayers)

        # For the output layer, we know that connects to the hidden layer and it has nOutputs neurons,
        # each with nNeuron + 1 weights.
        outLayer = [{'weights': [random() for i in range(nNeuron + 1)]} for i in range(nOutput)]

        # Add the output layer to our neural network.
        self.net.append(outLayer)   

    """
        Description:
            Calculate the activation of one neuron given for an input.
        Params:
            @param weights: is the network weight.
            @param inputs : is the input to use.
    """
    def neuronActivation(self, weights, inputs):
        # We asume the bias is in the first position.
        activation = weights[-1]
        for i in range(len(weights)-1):
            activation += weights[i] * inputs[i]
        return activation

    """
        Description:
            Forward propagation for the neural network.
            Calculate for each layer of the network the ouptus for each neuron.
        Params:
            @param row: input to predict.
    """
    def forwardPropagation(self, row):
        inputs = row

        for layer in self.net:
            newInputs = []
            for neuron in layer:
                # Calculate the neuron activation.
                print "neuron"
                print neuron['weights']
                print "input"
                print inputs
                activation = self.neuronActivation(neuron['weights'], inputs)
                
                # The neuron's output is stored in the neuron.
                neuron['output'] = sigmoid(activation)

                # Stores the outputs for a layer.
                newInputs.append(neuron['output'])
            # Inputs for the following layer.
            inputs = newInputs  
        return inputs

    """
        Description:
            Backward propagation for the neural network.
            Calculate for each layer of the network the ouptus for each neuron.
        Params:
            @param expected: is the expected output value..
    """
    def backPropagation(self, expected):
        for i in reversed(range(len(self.net))):
            layer = self.net[i]
            errors = list()
            
            # Error for the hidden layers.
            if i != len(self.net)-1:
                for j in range(len(layer)):
                    error = 0.0
                    # The error for a given neuron.
                    for neuron in self.net[i + 1]:
                        error += (neuron['weights'][j] * neuron['delta'])
                    errors.append(error)
            else:
                # Error for the output layer.
                for j in range(len(layer)):
                    neuron = layer[j]
                    # The error for a given neuron.
                    errors.append(expected[j] - neuron['output'])
            
            for j in range(len(layer)):
                neuron = layer[j]

                # Calculate the error for a given neuron.
                neuron['delta'] = errors[j] * dsigmoid(neuron['output'])

    """
        Description:
            Updates the weights for a neural network.
        Params:
            @param row  : Input row of data.
            @param alpha: learning rate to use.
    """
    def update_weights(self, row, alpha):
        for i in range(len(self.net)):
            inputs = row[:-1]
            if i != 0:
                inputs = [neuron['output'] for neuron in self.net[i - 1]]
            for neuron in self.net[i]:
                for j in range(len(inputs)):
                    # Update the network weight.
                    neuron['weights'][j] += alpha * neuron['delta'] * inputs[j]
                neuron['weights'][-1] += alpha * neuron['delta']

"""
    Description:
        Training a given neural network.
    Params:
        @param neuralNet: neural network to use.
        @param data     : training dataset.
        @param alpha    : learning rate to use.
        @param nIter    : number of iterations to update the neural network for 
                          each row in the training dataset.
        @param nOutputs : expected number of output values.
"""
def trainNetwork(neuralNet, data, alpha, nIter, nOutputs):
    for i in range(nIter):
        sumError = 0
        for row in data:
            outputs = neuralNet.forwardPropagation(row)
            expected = [0 for j in range(nOutputs)]
            print(int(row[-1]))
            expected[int(row[-1])] = 1
            sumError += sum([(expected[j]-outputs[j])**2 for j in range(len(expected))])
            neuralNet.backPropagation(expected)
            neuralNet.update_weights(row, alpha)
        print('>epoch=%d, lrate=%.3f, error=%.3f' % (i, alpha, sumError))

"""
    Description:
        Make a prediciton with a given neural network.
        Return the index in the neural network output that has the larger probability.
    Params:
        @param neuralNet: neural network to use.
        @param row      : sample. 
"""
def predict(neuralNet, row):
    outputs = neuralNet.forwardPropagation(row)
    return outputs.index(max(outputs))

# .----------------------------------------------------------------------------.