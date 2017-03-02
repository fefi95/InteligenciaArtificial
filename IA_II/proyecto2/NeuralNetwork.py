#!/usr/bin/env python
# -*- coding: latin-1 -*-
#TEMPORAL POR COMENTARIOS DEL CODIGO
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

import numpy as np              # This provides access to an efficient
                                # multi-dimensional container of generic data.
# .----------------------------------------------------------------------------.

np.random.seed(1)

"""
    Descripction: sigmoid function of the neural network
    @param z : sample
"""
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

"""
    Descripction: derivate of sigmoid function of the neural network
    @param x : sample
"""
def dSigmoid(z):
    return z * (1 - z)

"""
    Description: neural network of one hidden layer
"""

class NeuralNetwork:

    """
        Descripction: contructor of the neural network
        @param ni  : number of input units
        @param nHL : number of hidden layers
        @param nH  : number of units per hidden layer
        @param n0  : number of output units/classes
    """
    def __init__(self, nI, nHL, nH, nO):
        # number of input, hidden, and output nodes
        self.nI = nI + 1 # +1 for bias node
        self.nHL = 1 #UNA SOLA CAPA OCULTA POR AHORA
        self.nH = nH
        self.nO = nO

        # activations for nodes
        self.actI = np.ones(nI)
        self.actH = np.ones(nH) #CAMBIAR DIMENSIONES SI IMPLEMENTAMOS MAS CAPAS..
        self.actO = np.ones(nO)

        # create parameters of the neural network (weights)
        self.thetasI = np.array(self.nHL + 2, self.nHL + 2)
        self.thetasO = np.array(self.nHL + 2, self.nHL + 2)

        #randomly initialize the parameters (weights)
        self.thetasI = 2 * np.random.random((1,nI)) - 1
        self.thetasO = 2 * np.random.random((1,nI)) - 1

    """
        Descripction: forward propagation for the neural network
        @param x: one training examples
    """

    def forwardPropagation(x):

        #a(1) = x
        self.actI = x

        #CAMBIAR DIMENSIONES SI IMPLEMENTAMOS MAS CAPAS..
        #z(2) = theta(1) * a(1)
        z = np.dot(self.actI, self.thetasI)
        #a(2) = g(z(2))
        self.actH = sigmoid(z)
        self.actH[0] = 1 #bias unit

        #z(3) = theta(2) * a(2)
        z = np.dot(self.actH, self.thetasO)
        #a(3) = g(z(3))
        self.actO = sigmoid(z)

        # return the hypothesis h_theta(x)
        return self.actO

    """
        Descripction: backward propagation for the neural network
        (one training example)
        @param X : vector of training examples
        @param Y : vector of results (classification) of x
    """

    def backPropagation(X, Y):

        # Set Δ(l)i,j := 0 for all (l,i,j), (hence you end up having a matrix full of zeros)
        deltaI = np.zeros(self.nH + 1, self.nO)
        deltaO = np.zeros(self.nI + 1, self.nH)

        for i in range(0, len(X)):
            #a(1) = x
            # self.actI = x

            # Perform forward propagation to compute a(l) for l=2,3,…,L
            self.forwardPropagation(X[i])
            #
            # 3. Using y(t), compute δ(L)=a(L)−y(t)
            # Where L is our total number of layers and a(L) is the vector of outputs of the activation units for the last layer. So our "error values" for the last layer are simply the differences of our actual results in the last layer and the correct outputs in y. To get the delta values of the layers before the last layer, we can use an equation that steps us back from right to left:
            errorO = self.actO - y
            #
            # 4. Compute δ(L−1),δ(L−2),…,δ(2) using δ(l)=((Θ(l))Tδ(l+1)) .∗ a(l) .∗ (1−a(l))
            # The delta values of layer l are calculated by multiplying the delta values in the next layer with the theta matrix of layer l. We then element-wise multiply that with a function called g', or g-prime, which is the derivative of the activation function g evaluated with the input values given by z(l).

            errorH = np.dot(thetaI.transpose(), errorO) * dsigmoid(self.actH)

            # The g-prime derivative terms can also be written out as:
            #
            # g′(z(l))=a(l) .∗ (1−a(l))
            # 5. Δ(l)i,j:=Δ(l)i,j+a(l)jδ(l+1)i or with vectorization, Δ(l):=Δ(l)+δ(l+1)(a(l))T
            # Hence we update our new Δ matrix.

            deltaO = deltaO + np.dot(errorO, np.transpose(self.actH))
            deltaI = deltaI + np.dot(errorH, np.transpose(self.actI))

        # D(l)i,j:=1m(Δ(l)i,j+λΘ(l)i,j), if j≠0.
        # D(l)i,j:=1mΔ(l)i,j If j=0
        # The capital-delta matrix D is used as an "accumulator" to add up our values as we go along and eventually compute our partial derivative. Thus we get ∂∂Θ(l)ijJ(Θ)= D(l)ij
        DO = deltaO/ m
        DI = deltaI/ m

    def cost(x,y):
        aux = 0
        #Varias cosas que no tengo claras, nuestro forward creo que solo funciona con una neurona de salida
        # por lo cual nunca le tengo que dar un x y el calcula, si se dan cuenta si k = 1 es la
        # regresion logica por lo cual creo que falta algo, aunque la y por lo que entendi no cambia
        # ya que y[i]k deberia ser la misma para todos.
        for i in range(0,len(y)):
            for k in range(0,self.nO):
                h = self.forwardPropagation()
                aux += y[i] * np.log(h) + (1 - y[i]) * np.log(1-h)
        return -aux/len(y)

    def training():
        pass
        # Implement the cost function
        # Implement backpropagation to compute partial derivatives
        # Use gradient checking to confirm that your backpropagation works. Then disable gradient checking.
        # Use gradient descent or a built-in optimization function to minimize the cost function with the weights in theta.

"""
    Descripction: runs gradientDescent algorithm
    Parameters:
        @param alpha     : learning rate.
        @param varList   : all variables in the model.
        @param resultList: store the result of the data.
        @param thetas    : array with the parameters to use.
        @param row       : number of rows.
        @param columns   : number of columns.
"""
def gradientDescent(alpha, varList, resultList, thetas, rows, columns):
    conv = False  # Let you know if the function converge.
    JofTheta = [] # Store values of the cost function for plotting

    # Calculate the initial cost.
    cos = cost(varList, resultList, thetas, rows)
    JofTheta.append(cos)

    i = 0 # Initialize the counter of iterations.
    while (not(conv) and (i <= maxIter)):
        # Update of theta's
        auxtheta = [0] * (columns - 1)  # Store the new theta's value.

        for j in range(columns-1):
            auxtheta[j] = dcost(alpha, varList, resultList, thetas, rows, j)

        thetas = np.array(auxtheta, dtype=np.float128) # Update the thetas value.
        newcost = cost(varList , resultList, thetas, rows)
        JofTheta.append(newcost)

        i = i + 1 # Update the actual number of iterations.
        if (abs(newcost - cos) <= 0.001):
            conv = True
        cos = newcost

    return {'converge' : conv, 'costFunction' : JofTheta, 'thetas': thetas, 'nIterations': i}
