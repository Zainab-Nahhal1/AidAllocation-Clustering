# Country Data Clustering Project

This project applies **Exploratory Data Analysis (EDA)**, **Principal Component Analysis (PCA)**, and **K-Means Clustering** to understand and group countries based on multiple socio-economic and health indicators.

---

## 📘 Project Overview
The goal of this project is to analyze a dataset of countries with attributes such as GDP per capita, income, life expectancy, child mortality, imports, exports, and more. By applying unsupervised learning techniques, we can identify distinct clusters that represent countries with similar economic and development profiles.

---

## ⚙️ Workflow Summary

### 1. **Data Loading**
- The dataset (e.g., `Country-data.csv`) should be placed inside the **Sample** folder.
- It includes numerical features describing each country's economic and health status.

### 2. **Data Preprocessing**
- The column `country` is excluded for clustering.
- All numeric features are normalized using **MinMaxScaler** to ensure fair comparison across variables.

### 3. **Exploratory Data Analysis (EDA)**
Typical EDA steps performed include:
- Statistical summary (`describe()`)
- Distribution plots and boxplots to detect outliers
- Correlation heatmaps to understand feature relationships

### 4. **Dimensionality Reduction using PCA**
- PCA reduces feature dimensions while retaining maximum variance.
- It helps visualize and interpret country clusters in a 2D or 3D space.

### 5. **Clustering using K-Means**
- The **K-Means** algorithm is used to group countries into clusters.
- The optimal number of clusters (k) can be found using the **Elbow Method** or **Silhouette Score**.

### 6. **Results Interpretation**
Each cluster is analyzed to determine characteristics such as:
- Economic status (high, medium, low income)
- Life expectancy and health level
- Trade activity (imports/exports)

Clusters can then be interpreted, for example, as:
- **Cluster 0**: High-income developed nations  
- **Cluster 1**: Developing nations with improving economy  
- **Cluster 2**: Low-income or high child-mortality countries

---

## 🧩 Folder Structure

```
Country_Data_Clustering_Project/
│
├── Source/
│   ├── __init__.py
│   └── main.py
│
├── Sample/             # Place your dataset here
├── tests/
│   └── test_sample.py
│
├── .gitignore
├── Makefile
└── README.md
```

---

## 🚀 How to Run the Project

### 1. **Install dependencies**
```bash
pip install pandas scikit-learn matplotlib seaborn
```

### 2. **Run the script**
```bash
make run
```

### 3. **Run tests**
```bash
make test
```

---

## 🧠 Key Learnings
- Gained understanding of unsupervised learning and clustering.
- Learned how PCA reduces dimensions and improves visualization.
- Practiced applying K-Means on real-world economic data.

---

**Author:** Zainab Nahal  
**Language:** Python  
**Techniques:** EDA, PCA, K-Means Clustering
