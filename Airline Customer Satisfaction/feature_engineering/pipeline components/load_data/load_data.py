def load_data():
    #importing libraries
    import joblib
    import pandas as pd
# importing the joblib files
    
    df = pd.read_csv('https://raw.githubusercontent.com/charlesa101/KubeflowUseCases/draft/Airline%20Customer%20Satisfaction/data/raw/Invistico_Airline.csv?token=AOWDH2KVJKVICW2WFVKFYGLBAKVNW')
    joblib.dump(df, 'data')

if __name__ == '__main__':
    load_data()