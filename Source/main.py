import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(path):
    data = pd.read_csv(path)
    return data

def preprocess_data(data):
    df = data.drop(columns=['country'], errors='ignore')
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(df)
    return pd.DataFrame(scaled, columns=df.columns)

def perform_pca(data, n_components=3):
    pca = PCA(n_components=n_components)
    components = pca.fit_transform(data)
    return pd.DataFrame(components, columns=[f'PC{i+1}' for i in range(n_components)])

def cluster_data(data, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(data)
    data['Cluster'] = labels
    return data, kmeans

def main():
    print("This script performs clustering on country data using K-Means and PCA.")
    print("Please ensure your dataset is located in the 'Sample' folder.")
    print("Example usage: df = load_data('Sample/Country-data.csv')")

if __name__ == "__main__":
    main()
