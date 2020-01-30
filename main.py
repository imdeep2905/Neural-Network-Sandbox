#initial checking
from Backend.NeuralNetwork import NN
from Backend.DataPreprocessing import DataProcessor
import tensorflow as tf
if __name__ == "__main__":
    my_data=DataProcessor(path="C:\\Users\\Deep Raval\\Desktop\\TitanicKaggle",name="train.csv")
    input_n=my_data.smart_preprocess()
    x,y,s=my_data.get_xy(label_last=False)
    my_model=NN(layers_n=3,layers=[input_n,12,1], opti_tech="Adam",lr=0.01,loss_fn="binary_crossentropy" ,activ_fns=["None","relu","sigmoid"],epochs=30)
    my_model.connect_network(shape=s,normalize=True)
    my_model.fit(x,y)
    my_model.train_visualize()