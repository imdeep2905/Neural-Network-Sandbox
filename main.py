#initial checking
from Backend.NeuralNetwork import NN
import tensorflow as tf
if __name__ == "__main__":
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
    my_model=NN(layers_n=4,layers=[784,300,100,10],activ_fns=["None","elu","elu","softmax"],epochs=30)
    my_model.connect_network(normalize=True)
    my_model.fit(x_train,y_train)
    my_model.train_visualize()