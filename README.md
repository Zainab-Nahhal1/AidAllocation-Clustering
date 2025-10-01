# AidAllocation-Clustering

🌍 Fund Allocation Using Unsupervised Learning

Problem:
HELP International raised $10M to support countries in need. Using socio-economic and health indicators, clustering helps identify economically backward nations requiring urgent aid.


📊 Dataset:
Source: Kaggle


Features include: child_mort, income, gdpp, health, life_expec, inflation, exports, imports, total_fer.


Approach:

EDA: Found key patterns (low income, high child mortality & fertility, poor healthcare).

Feature Scaling & PCA: Normalized features & reduced to 2 components.


Clustering Models:

K-Means (k=3) → clear separation of backward, developing, and developed nations.

DBSCAN → identified noise/outliers.

Hierarchical → dendrogram confirmed 3 groups.


Insights:

Backward nations → low income, high child mortality, high fertility.

Developed nations → high GDP & income, strong healthcare.

Africa dominated backward clusters; countries like Qatar & Luxembourg led the top tier.


Outcomes:

Showed how unsupervised ML can guide fund allocation & policy decisions.

K-Means, DBSCAN, and Hierarchical clustering gave consistent results.