import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class mlp:
    def __init__(self, inputs, targets, nhidden, beta=1, momentum=0.9, outtype='logistic'):
        # Set up network size
        self.nin = np.shape(inputs)[1]
        self.nout = np.shape(targets)[1]
        self.ndata = np.shape(inputs)[0]
        self.nhidden = nhidden

        self.beta = beta
        self.momentum = momentum
        self.outtype = outtype
    
        # Initialise network
        self.weights = []
        self.weights.append((np.random.rand(self.nin+1, self.nhidden[0])-0.5)*2/np.sqrt(self.nin))
        for i in range(len(self.nhidden)-1):
            self.weights.append((np.random.rand(self.nhidden[i]+1, self.nhidden[i+1])-0.5)*2/np.sqrt(self.nhidden[i]))
        self.weights.append((np.random.rand(self.nhidden[-1]+1, self.nout)-0.5)*2/np.sqrt(self.nhidden[-1]))

    def earlystopping(self, inputs, targets, valid, validtargets, eta, niterations=100):
        valid = np.concatenate((valid, -np.ones((np.shape(valid)[0], 1))), axis=1)
        
        old_val_error1 = 100002
        old_val_error2 = 100001
        new_val_error = 100000
        
        count = 0
        while (((old_val_error1 - new_val_error) > 0.001) or ((old_val_error2 - old_val_error1) > 0.001)):
            count += 1
            print(count)
            self.mlptrain(inputs, targets, eta, niterations)
            old_val_error2 = old_val_error1
            old_val_error1 = new_val_error
            validout = self.mlpfwd(valid)
            new_val_error = 0.5*np.sum((validtargets-validout)**2)
            
        print("Stopped", new_val_error, old_val_error1, old_val_error2)
        return new_val_error
        
    def mlptrain(self, inputs, targets, eta, niterations):
        """ Train the thing """    
        # Add the inputs that match the bias node
        inputs = np.concatenate((inputs, -np.ones((self.ndata, 1))), axis=1)
        change = range(self.ndata)
    
        updatew = [np.zeros(w.shape) for w in self.weights]
            
        for n in range(niterations):
    
            self.outputs = self.mlpfwd(inputs)

            error = 0.5*np.sum((self.outputs-targets)**2)
            if (np.mod(n, 100) == 0):
                print("Iteration: ", n, " Error: ", error)    

            # Different types of output neurons
            if self.outtype == 'linear':
                deltao = (self.outputs-targets)/self.ndata
            elif self.outtype == 'logistic':
                deltao = self.beta*(self.outputs-targets)*self.outputs*(1.0-self.outputs)
            else:
                print("error")
            
            deltas = [deltao]
            for i in range(len(self.nhidden), 0, -1):
                deltah = self.hidden[i]*self.beta*(1.0-self.hidden[i])*(np.dot(deltas[0], np.transpose(self.weights[i])))
                deltas.insert(0, deltah[:, :-1])
                      
            for i in range(len(self.weights)):
                updatew[i] = eta*(np.dot(np.transpose(self.hidden[i]), deltas[i])) + self.momentum*updatew[i]
                self.weights[i] -= updatew[i]
                
    def mlpfwd(self, inputs):
        """ Run the network forward """
        self.hidden = [inputs]
        for i in range(len(self.weights)-1):
            activation = np.dot(self.hidden[-1], self.weights[i])
            activation = 1.0/(1.0+np.exp(-self.beta*activation))
            activation = np.concatenate((activation, -np.ones((np.shape(inputs)[0], 1))), axis=1)
            self.hidden.append(activation)
        outputs = np.dot(self.hidden[-1], self.weights[-1])

        # Different types of output neurons
        if self.outtype == 'linear':
            return outputs
        elif self.outtype == 'logistic':
            return 1.0/(1.0+np.exp(-self.beta*outputs))
        elif self.outtype == 'softmax':
            normalisers = np.sum(np.exp(outputs), axis=1)*np.ones((1, np.shape(outputs)[0]))
            return np.transpose(np.transpose(np.exp(outputs))/normalisers)
        else:
            print("error")

    def confmat(self, inputs, targets):
        """Confusion matrix"""
        # Add the inputs that match the bias node
        inputs = np.concatenate((inputs, -np.ones((np.shape(inputs)[0], 1))), axis=1)
        outputs = self.mlpfwd(inputs)
        
        nclasses = np.shape(targets)[1]

        if nclasses == 1:
            nclasses = 2
            outputs = np.where(outputs > 0.5, 1, 0)
        else:
            # 1-of-N encoding
            outputs = np.argmax(outputs, 1)
            targets = np.argmax(targets, 1)

        cm = np.zeros((nclasses, nclasses))
        for i in range(nclasses):
            for j in range(nclasses):
                cm[i, j] = np.sum(np.where(outputs == i, 1, 0)*np.where(targets == j, 1, 0))

        print("Confusion matrix is:")
        print(cm)
        print("Percentage Correct: ", np.trace(cm)/np.sum(cm)*100)

def train_and_evaluate():
    # Load the dataset
    data = pd.read_csv('C:/coding/machine learning/diabetes.csv')
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values

    # Check data balance
    print("Class distribution in the dataset:")
    print(pd.Series(y).value_counts())

    # Preprocess the data
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    y = y.reshape(-1, 1)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the MLP with multiple hidden layers
    mlp_model = mlp(X_train, y_train, nhidden=[10, 5])
    mlp_model.mlptrain(X_train, y_train, eta=0.01, niterations=1000)  # Lower learning rate

    # Evaluate the model
    mlp_model.confmat(X_test, y_test)

    # Predict on the test set
    y_pred = mlp_model.mlpfwd(np.concatenate((X_test, -np.ones((X_test.shape[0], 1))), axis=1))
    y_pred = np.where(y_pred > 0.5, 1, 0)

    # Calculate performance metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1 Score: {f1}")

    return mlp_model, scaler

def predict(model, scaler, input_data):
    input_data = np.array(input_data).reshape(1, -1)
    input_data = scaler.transform(input_data)
    input_data = np.concatenate((input_data, -np.ones((input_data.shape[0], 1))), axis=1)
    output = model.mlpfwd(input_data)
    return output

if __name__ == "__main__":
    model, scaler = train_and_evaluate()
    test_input = eval(input())
    prediction = predict(model, scaler, test_input)
    print("Prediction for input {}: {}".format(test_input, prediction))
    # Interpret the prediction
    if 10**8*prediction > 0.5:
        print("The model predicts that the person has diabetes.")
    else:
        print("The model predicts that the person does not have diabetes.")