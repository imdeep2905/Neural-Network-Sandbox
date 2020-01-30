#initial checking
from Backend.NeuralNetwork import NN
from Backend.DataPreprocessing import DataProcessor
import tensorflow as tf
if __name__ == "__main__":
    my_data=DataProcessor(path="C:\\Users\\Deep Raval\\Desktop",name="heart.csv")
    x,y,s=my_data.get_xy()
    my_model=NN(layers_n=3,layers=[12,24,1], opti_tech="Adam",lr=0.2,loss_fn="binary_crossentropy" ,activ_fns=["None","elu","sigmoid"],epochs=30)
    my_model.connect_network(shape=s)
    my_model.fit(x,y)
    my_model.train_visualize()