from random import seed
from random import random
from math   import exp

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
            if i != len(self.net)-1:
                for j in range(len(layer)):
                    error = 0.0
                    for neuron in self.net[i + 1]:
                        error += (neuron['weights'][j] * neuron['delta'])
                    errors.append(error)
            else:
                for j in range(len(layer)):
                    neuron = layer[j]
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

# .----------------------------------------------------------------------------.

if __name__ == '__main__':
    seed(1)
    neuralNet = NeuralNetwork(2, 1, 2)
    neuralNet.net = [[{'output': 0.7105668883115941,'weights': [0.13436424411240122, 0.8474337369372327, 0.763774618976614]}],[{'output': 0.6213859615555266, 'weights': [0.2550690257394217, 0.49543508709194095]},{'output': 0.6573693455986976, 'weights': [0.4494910647887381, 0.651592972722763]}]]
    #expected = [0,1]
    #neuralNet.backPropagation(expected)
    for layer in neuralNet.net:
        print(layer)
# .----------------------------------------------------------------------------.