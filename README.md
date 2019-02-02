It is a python program to do KMeans Clustering in a general method.The steps I have done - 

1. Collect any dataset without decision attribute. The dataset may be collected from UCI machine learning repository. 
If the dataset contains the decision attribute then I remove it as I will perform clustering of objects in the dataset.

2. Let the dataset has m rows and n columns where, each row is an object and each column is an attribute or feature of 
the object in the dataset. So I can consider the dataset as an m*n matrix.

3. Normalize the attribute values within the range [0, 1] using any Min-Max normalization technique to give all the attributes
an equal importance.

4. Create a similarity matrix S of size m*m where, each (i, j)-th entry in the matrix gives the dissimilarity measurement 
between i-th and j-th objects. Use Eucledian distance to measure the dissimilarity.

5. The i-th row indicates similarity of i-th object with all other objects. Find the average dissimilarity of i-th object 
with other objects and form a cluster Ci with i-th object and objects having dissimilarity less than the average similarity.
Repeat this process for all rows of the similarity matrix. Thus, I have now m clusters.

6. Remove the clusters (if any) which are subset of some other clusters. As a result I have now say, p (< m) clusters.

7. Create a similarity matrix C of size p*p where, each (i, j)-th entry in the matrix gives the similarity measurement 
between i-th cluster Ci and  j-th cluster Cj using Jackard similarity measure. 

8. Out of all p*p entries in matrix C, find out the maximum value. If multiple maximum values occur, choose any one randomly. 
Let, ckl is the maximum value selected, that implies clusters Ck and Cl are the most similar clusters among all p clusters. 
Merge these two clusters Ck and Cl to get a new cluster Ckl.

9. Repeat steps 6 to 8 until desire number (say, at most K) of clusters are obtained. 
