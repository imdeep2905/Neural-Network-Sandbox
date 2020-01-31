#initial checking
from Backend.NeuralNetwork import NN
from Backend.DataPreprocessing import DataProcessor,DataSplitter
import tensorflow as tf
if __name__ == "__main__":
    my_data=DataSplitter(path="C:\\Users\\Deep Raval\\Desktop",name="housing.csv")
    input_n=my_data.smart_preprocess()
    #s,x,y=my_data.get_xy(label_last=False)
    s,xtr,ytr,xva,yva,xte,yte=my_data.get_splitted_xy(test_r=0.2,val_r=0.1)
    print(my_data.data.head())
    my_model=NN(layers_n=3,layers=[input_n,5,1], opti_tech="Adam",lr=0.8,loss_fn="mse" ,activ_fns=["None","elu","relu"],epochs=30)
    my_model.connect_network(shape=s,normalize=True)
    my_model.fit(xtr,ytr,xva,yva)
    my_model.evaluate(xte,yte)
    my_model.train_visualize()