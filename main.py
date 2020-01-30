#initial checking
from Backend.NeuralNetwork import NN
import tensorflow as tf
if __name__ == "__main__":
    '''
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
    my_model=NN(layers_n=4,layers=[784,300,100,10],activ_fns=["None","elu","elu","softmax"],epochs=2)
    my_model.connect_network(normalize=True,y=28,x=28)
    my_model.fit(x_train,y_train)
    my_model.train_visualize()
    my_model.save_model("test")
    '''
    
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
    my_model=NN()
    my_model.load_model("test")
    #print(my_model.model.summary())
    #my_model.evaluate(x_test,y_test)