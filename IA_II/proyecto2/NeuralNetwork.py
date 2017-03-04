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
maxIter = 1000

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
def dsigmoid(z):
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
    def __init__(self, nI, nH, nO, nHL = 1):
        # number of input, hidden, and output nodes
        self.nI = int(nI + 1) # +1 for bias node
        # self.nHL = 1 #UNA SOLA CAPA OCULTA POR AHORA
        self.nH = int(nH + 1)
        self.nO = int(nO)

        # activations for nodes
        self.actI = np.ones((1,self.nI))
        self.actH = np.ones((1, self.nH)) #CAMBIAR DIMENSIONES SI IMPLEMENTAMOS MAS CAPAS..
        self.actO = np.ones((1, self.nO))

        # create parameters of the neural network (weights) and
        # randomly initialize them
        ep = 0.12 # epsilon
        self.thetasI = np.random.rand(self.nH-1, self.nI) * 2 * ep - ep
        self.thetasH = np.random.rand(self.nO, self.nH) * 2 * ep - ep
        # self.thetasI = np.array([[-30, 20, 20],[10, -20, -20]])
        # self.thetasH = np.array([[-10, 20, 20]])
        # print "init"
        # print self.thetasI
        # print self.thetasH

    """
        Descripction: forward propagation for the neural network
        @param x: one training examples
    """

    def forwardPropagation(self, x):

        #a(1) = x
        self.actI[0][1:] = x
        # print self.actI
        # print len(self.thetasI)
        # print(self.thetasI)
        # print(x)
        # print x.shape

        #CAMBIAR DIMENSIONES SI IMPLEMENTAMOS MAS CAPAS..
        #z(2) = theta(1) * a(1)
        z = np.transpose(np.dot(self.thetasI, np.transpose(self.actI)))
        #a(2) = g(z(2))
        # print z.shape
        # print self.actH.shape
        for i in range(0,self.nH-1):
            self.actH[0][i+1] = sigmoid(z[0][i])

        self.actH[0][0] = 1 # bias units
        #z(3) = theta(2) * a(2)
        # print "z"
        # print self.thetasH.shape
        # print self.actH.shape
        z = np.transpose(np.dot(self.thetasH, np.transpose(self.actH)))
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

    def backPropagation(self, X, y):

        # Set Δ(l)i,j := 0 for all (l,i,j), (hence you end up having a matrix full of zeros)
        deltaH = np.zeros((self.nO, self.nH))
        deltaI = np.zeros((self.nH-1, self.nI))

        for i in range(0, len(X)):
            #a(1) = x
            # self.actI = x

            # Perform forward propagation to compute a(l) for l=2,3,…,L
            self.forwardPropagation(X[i])
            # print "act0"
            # print self.actO
            #
            # 3. Using y(t), compute δ(L)=a(L)−y(t)
            # Where L is our total number of layers and a(L) is the vector of outputs of the activation units for the last layer. So our "error values" for the last layer are simply the differences of our actual results in the last layer and the correct outputs in y. To get the delta values of the layers before the last layer, we can use an equation that steps us back from right to left:
            # print y[i]
            errorO = self.actO - y[i]
            # print "errorO"
            # print errorO
            #
            # 4. Compute δ(L−1),δ(L−2),…,δ(2) using δ(l)=((Θ(l))Tδ(l+1)) .∗ a(l) .∗ (1−a(l))
            # The delta values of layer l are calculated by multiplying the delta values in the next layer with the theta matrix of layer l. We then element-wise multiply that with a function called g', or g-prime, which is the derivative of the activation function g evaluated with the input values given by z(l).
            # print self.actI
            # print self.thetasH
            # print np.dot(np.transpose(self.thetasH), errorO)
            actHT = np.transpose(self.actH)
            errorH = np.dot(np.transpose(self.thetasH), np.transpose(errorO)) * dsigmoid(actHT) #actHT * (1 - actHT)
            # print "actH?"
            # print dsigmoid(actHT)
            # print "errorH"
            # print errorH

            # The g-prime derivative terms can also be written out as:
            #
            # g′(z(l))=a(l) .∗ (1−a(l))
            # 5. Δ(l)i,j:=Δ(l)i,j+a(l)jδ(l+1)i or with vectorization, Δ(l):=Δ(l)+δ(l+1)(a(l))T
            # Hence we update our new Δ matrix.
            # print errorO.shape
            # print self.actH.shape
            # if len(errorO) == 1:
            #     deltaH = deltaH + errorO * self.actH
            # else:
            #     deltaH = deltaH + np.dot(errorO, np.transpose(self.actH))
            deltaH = deltaH + np.dot(np.transpose(errorO), self.actH)

            # print deltaI
            # print self.actI
            # print self.actI.shape
            deltaI = deltaI + np.dot(errorH[1:], self.actI)
        # D(l)i,j:=1m(Δ(l)i,j+λΘ(l)i,j), if j≠0.
        # D(l)i,j:=1mΔ(l)i,j If j=0
        # The capital-delta matrix D is used as an "accumulator" to add up our values as we go along and eventually compute our partial derivative. Thus we get ∂∂Θ(l)ijJ(Θ)= D(l)ij
        # print "deltas"
        # print deltaH
        # print deltaI
        DH = np.zeros((self.nO, self.nH))
        DI = np.zeros((self.nH-1, self.nI))
        for i in range(0, self.nO):
            DH[i][0] = deltaH[i][0]
            for j in range(1, self.nH):
                DH[i][j] = deltaH[i][j] + self.thetasH[i][j]/len(X)

        for i in range(0, self.nH-1):
            DI[i][0] = deltaI[i][0]
            for j in range(1, self.nI):
                DI[i][j] = deltaI[i][j] + self.thetasI[i][j]/len(X)

        return [DI, DH]

    def cost(self, X,y):
        aux = 0
        #Varias cosas que no tengo claras, nuestro forward creo que solo funciona con una neurona de salida
        # por lo cual nunca le tengo que dar un x y el calcula, si se dan cuenta si k = 1 es la
        # regresion logica por lo cual creo que falta algo, aunque la y por lo que entendi no cambia
        # ya que y[i]k deberia ser la misma para todos.
        for i in range(0,len(y)):
            aux1 = 0
            for k in range(0,self.nO):
                h = self.forwardPropagation(X[i])
                aux1 += y[i][k] * np.log(h[0][k]) + (1 - y[i][k]) * np.log(1-h[0][k])
            aux += aux1
        return -aux/len(y)

    """
        Descripction: runs gradientDescent algorithm
        Parameters:
            @param alpha     : learning rate.
            @param varList   : all variables in the model.
            @param resultList: store the result of the data.
    """
    def gradientDescent(self, alpha, varList, resultList):
        conv = False  # Let you know if the function converge.
        JofTheta = [] # Store values of the cost function for plotting

        # Calculate the initial cost.
        cos = self.cost(varList, resultList)
        # print "cos1"
        # print cos
        JofTheta.append(cos)

        i = 0 # Initialize the counter of iterations.
        while (not(conv) and (i <= maxIter)):
            auxthetaI = self.thetasI
            auxthetaH = self.thetasH
            # print "before"
            # print auxthetaI
            # print auxthetaH
            # Get new thetas
            derivate = self.backPropagation(varList, resultList)

            # Gradient checking
            # gc = self.gradientChecking(varList, resultList)
            # print gc[0]
            # print gc[1]
            # if (np.all(gc[0] - derivate[0]  < 0.001) or np.all(gc[1] - derivate[1] < 0.001)):
            #     print "noooooooooooooooo, mori"
            #     break

            # Update of thetas
            self.thetasI = auxthetaI - alpha * derivate[0]
            self.thetasH = auxthetaH - alpha * derivate[1]

            # print "after"
            # print self.thetasI
            # print self.thetasH
            newcost = self.cost(varList , resultList)
            # print "newcost"
            # print newcost
            # print "derivate"
            # print derivate[0]
            # print derivate[1]
            JofTheta.append(newcost)

            i = i + 1 # Update the actual number of iterations.
            if (abs(newcost - cos) <= 0.001):
                conv = True
                # print "thetas"
                # print self.thetasI
                # print self.thetasH

            # print "dif cos"
            # print abs(newcost - cos)
            cos = newcost



        return {'converge' : conv, 'costFunction' : JofTheta, 'nIterations': i}


    def gradientChecking(self, X, y):
        epsilon = 0.0001;

        auxThetaI = self.thetasI
        self.thetasI = auxThetaI + epsilon;
        costThetasP = self.cost(X, y)
        self.thetasI = auxThetaI - epsilon;
        costThetasM = self.cost(X, y)
        gradApproxI = (costThetasP - costThetasM)/(2 * epsilon)
        self.thetasI = auxThetaI

        auxThetaO = self.thetasH
        self.thetasH = auxThetaO + epsilon;
        costThetasP = self.cost(X, y)
        self.thetasH = auxThetaO - epsilon;
        costThetasM = self.cost(X, y)
        gradApproxO = (costThetasP - costThetasM)/(2 * epsilon)
        self.thetasH = auxThetaO

        return [gradApproxI, gradApproxO]
