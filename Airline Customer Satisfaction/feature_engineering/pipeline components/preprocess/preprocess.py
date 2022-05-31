import argparse
def preprocessing(data):
    import joblib
    import numpy as np
    import pandas as pd
    from sklearn.model_selection import train_test_split
    #from sklearn.utils import resample
    #from sklearn.preprocessing import StandardScaler
    df = joblib.load(data)
    
    
    #drop rows with missing values
    df.dropna(inplace=True)
    #new column total delay
    df['total_delay'] = df['Departure Delay in Minutes'] + df['Arrival Delay in Minutes']
    
    #drop 'Departure Delay in Minutes',and 'Arrival Delay in Minutes'
    df.drop(columns=['Departure Delay in Minutes','Arrival Delay in Minutes'], inplace=True)
    
    #satisfied and dissatisfied in number 
    satisfaction_map = {"satisfied": 1,"dissatisfied": 0 }
    df['satisfaction']  = df['satisfaction'].map(satisfaction_map)

    #Male and Female in number 
    Gender_map = {"Male": 1,"Female": 2 }
    df['Gender']  = df['Gender'].map(Gender_map)

    #Loyal and disloyal in number 
    Customer_Type_map = {"Loyal Customer": 1,"disloyal Customer": 0 }
    df['Customer Type']  = df['Customer Type'].map(Customer_Type_map)

    #Business travel and Business travel in number 
    Type_of_Travel_map = {"Business travel": 1,"Personal Travel": 2 }
    df['Type of Travel']  = df['Type of Travel'].map(Type_of_Travel_map)

    #Business and Eco and Eco plus in number 
    Class_map = {"Business": 1,"Eco": 3, "Eco Plus": 2 }
    df['Class']  = df['Class'].map(Class_map)

    cols = ['Flight Distance', 'total_delay', 'Checkin service', 'On-board service']

    Q1 = df[cols].quantile(0.25)
    Q3 = df[cols].quantile(0.75)
    IQR = Q3 - Q1

    df = df[~((df[cols] < (Q1 - 1.5 * IQR)) |(df[cols] > (Q3 + 1.5 * IQR))).any(axis=1)]   
    
    #Split dataset
    
    X = df.drop('satisfaction',axis=1)
    y = df['satisfaction'] 
    X_train,X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 111)
    

    data_dic = {"X_train": x_train,"X_test": x_test, "Y_train": y_train, "Y_test": y_test}

    joblib.dump(data_dic,'clean_data')

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--data')
  args = parser.parse_args()
  preprocessing(args.data)