# Machine-Learning-solution-for-Robot-Navigation (Python based project)
This projects involves the implementation of Machine Learning solution to help robot navigation through identification of ground terrain.
# Project Description
1. The project aims at implementing a Machine Learning solution to help robots identify their ground terrain.
2. The inputs are obtained from IMU and the output is one of possible 9 surface types (classification problem).
# Scope
1. Data Analysis
2. Feature Engineering
3. Implementing ML models for classifications
4. Optimization.

## Data Analysis
### Data Inbalance
 ![image](https://user-images.githubusercontent.com/69100847/169323201-44df869f-c882-40e1-b4d1-f6f12a41caf2.png)

### Histogram and Frequency Plots
![image](https://user-images.githubusercontent.com/69100847/169323746-75e32f40-c3ec-4e0b-ba4f-b69cc5cc473b.png)

### Heat Map
![image](https://user-images.githubusercontent.com/69100847/169324094-587f70dd-d9e0-4b77-bbbb-195f65253f32.png)

### Outlier Handling (Skewness)
![image](https://user-images.githubusercontent.com/69100847/169325639-2f073f85-beda-41fd-a0c7-8187c962cc6e.png)


## Feature Engineering
Based on the understanding of the nature of the problem, Feature Engineering was used to create more features that would make the ML model become more efficient

![image](https://user-images.githubusercontent.com/69100847/169326546-43489bfd-f9f4-4d96-b45e-08203f19efb9.png)

## Radnom Forest Classifier (Machine Learning Model)

Random Forest Classifer with stratified folds of k=10 was used. The original dataset and two more for outlier handling were fed to the model.

![image](https://user-images.githubusercontent.com/69100847/169327149-9a9040b3-b35f-4492-ab0b-7bdcc3ff4caa.png)


### Feature Importance

![image](https://user-images.githubusercontent.com/69100847/169327339-67e4905e-4ef2-4f25-87f6-543f7812f7d7.png)

### Principal Component Analysis

![image](https://user-images.githubusercontent.com/69100847/169328192-522a4160-aa2b-4b84-8875-c53a5157f54d.png)


### Random Search for Random Forest Classifer

![image](https://user-images.githubusercontent.com/69100847/169329433-1ace3e50-cc88-4b4a-846d-dae4e2b7e6f5.png)


![image](https://user-images.githubusercontent.com/69100847/169329520-a7656341-1f8d-4387-a17a-dd69415ffb0e.png)


![image](https://user-images.githubusercontent.com/69100847/169329764-b52b3abb-6b58-4363-a275-8935aabe7b5c.png)


### Grid Search

![image](https://user-images.githubusercontent.com/69100847/169330363-e96cefc8-4573-4c3c-9c59-b0d5179a5bb4.png)


### Keras Deep Learning

![image](https://user-images.githubusercontent.com/69100847/169330865-0472ebd7-4897-44bc-847b-3ceddc978173.png)


![image](https://user-images.githubusercontent.com/69100847/169330940-e204dd2a-e7e7-4c94-9ed0-8a21d4630610.png)


![image](https://user-images.githubusercontent.com/69100847/169331015-c548a54a-e0f3-4922-937b-85b8ad96fde2.png)




