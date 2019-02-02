import pandas as pd
import matplotlib.pyplot as plt 
from numpy import array,median,mean


def normalize(row,m1,m2):
	for i in range(4):
		row[i]=(row[i]-m1)/(m2-m1)


def euclid(x1,x2,x3,x4,y1,y2,y3,y4):
	return ((x1-x2)**2+(x3-x4)**2+(y1-y2)**2+(y3-y4)**2)**.5


def union(lst1, lst2): 
    final_list = list(set(lst1) | set(lst2)) 
    return final_list


def intersect(lst1, lst2): 
    return list(set(lst1) & set(lst2))


def jack(l1,l2):
	return len(intersect(l1,l2))/len(union(l1,l2))


def maximum(list1):
	ll=len(list1)
	for i in range(ll):
		for j in range(ll):
			if list1[i][j]==1:
				list1[i][j]=0

	mi=list1[0][0]
	ans=[0,0]
	for i in range(ll):
		for j in range(ll):
			if list1[i][j]>=mi:
				mi=list1[i][j]
				ans[0]=i
				ans[1]=j
	return ans


#names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
names=[0,1,2,3,4]
data = pd.read_csv("iris.csv",names=names)
data=data.iloc[:,:4]

row,column=data.shape
#print(type(row))
#print(data.iloc[0][0])
#print(data.head())

# ===========================================Normallization=============================================
m1=data.min().min()
m2=data.max().max()

#print(m1,m2)

for index,ro in data.iterrows():
	normalize(ro,m1,m2)
	
#print(data.head())

#==========================================Euclidian Distance===========================================
similar=[[0 for i in range(row)] for j in range(row)]

for i in range(row):
	for j in range(row):
		similar[i][j]=euclid(data.iloc[i][0],data.iloc[j][0],data.iloc[i][1],data.iloc[j][1],
							 data.iloc[i][2],data.iloc[j][2],data.iloc[i][3],data.iloc[j][3])
		
#print(similar[10][10],similar[0][1])

#=========================================Cluster=======================================================
cluster=[[] for i in range(row)]
#print(cluster)
for i in range(len(similar)):
	avg=sum(similar[i])/len(similar[i])
	for j in range(len(similar[i])):
		if similar[i][j]<avg:
			cluster[i].append(j)
#print(len(cluster))


#========================================Subset==========================================================
dele=[]
for i in range(len(cluster)):
	for j in range(len(cluster)):
		if i!=j:
			if set(cluster[j])<set(cluster[i]):
				dele.append(j)
#print(len(dele))
dele=list(set(dele))
#print(len(dele))
count=0
for i in (dele):
	cluster=cluster[:i-count]+cluster[i+1-count:]
	count+=1

#print(len(cluster))


#========================================Clustering=======================================================
p=len(cluster)
print("Enter No of cluster - ")
k=int(input())
while(k!=p):
	jackard=[[0 for j in range(p)] for i in range(p)]
	for i in range(p):
		for j in range(p):
			jackard[i][j]=jack(cluster[i],cluster[j])
	m=maximum(jackard)
	cluster[m[0]]=union(cluster[m[0]],cluster[m[1]])
	cluster.pop(m[1])
	p=p-1
	
#print(cluster)
# for i in range(len(cluster)):
# 	print(len(cluster[i]))
	#print(cluster[i])
#print(len(cluster[1]))
#print(len(cluster[2]))

#=====================================Remove Overlap=============================================================

final=[]
for i in range(len(cluster)):
	me=[]
	for k in range(4):
		m=[]
		for j in range(len(cluster[i])):
			m.append(data.iloc[cluster[i][j]][k])
		m=array(m)
		me.append(mean(m))
		#me.append(median(m))
	#final.append(median(array(me)))
	final.append(me)

#print(len(final))

for i in range(row):
	lis=[]

	if i in cluster[0] and i in cluster[1] and i in cluster[2]:
		l0=euclid(data.iloc[i][0],final[0][0],data.iloc[i][1],final[0][1],data.iloc[i][2],final[0][2],data.iloc[i][3],final[0][3])
		l1=euclid(data.iloc[i][0],final[1][0],data.iloc[i][1],final[1][1],data.iloc[i][2],final[1][2],data.iloc[i][3],final[1][3])
		l2=euclid(data.iloc[i][0],final[2][0],data.iloc[i][1],final[2][1],data.iloc[i][2],final[2][2],data.iloc[i][3],final[2][3])

		lis.append(l0)
		lis.append(l1)
		lis.append(l2)

		if l0==min(lis):
			cluster[1].remove(i)
			cluster[2].remove(i)

		elif l1==min(lis):
			cluster[0].remove(i)
			cluster[2].remove(i)

		elif l2==min(lis):
			cluster[0].remove(i)
			cluster[1].remove(i)


	elif i in cluster[0] and i in cluster[1]:
		l0=euclid(data.iloc[i][0],final[0][0],data.iloc[i][1],final[0][1],data.iloc[i][2],final[0][2],data.iloc[i][3],final[0][3])
		l1=euclid(data.iloc[i][0],final[1][0],data.iloc[i][1],final[1][1],data.iloc[i][2],final[1][2],data.iloc[i][3],final[1][3])

		lis.append(l0)
		lis.append(l1)

		if l0==min(lis):
			cluster[1].remove(i)

		elif l1==min(lis):
			cluster[0].remove(i)


	elif i in cluster[0] and i in cluster[2]:
		l0=euclid(data.iloc[i][0],final[0][0],data.iloc[i][1],final[0][1],data.iloc[i][2],final[0][2],data.iloc[i][3],final[0][3])
		l2=euclid(data.iloc[i][0],final[2][0],data.iloc[i][1],final[2][1],data.iloc[i][2],final[2][2],data.iloc[i][3],final[2][3])

		lis.append(l0)
		lis.append(l2)
		if l0==min(lis):
			cluster[2].remove(i)

		elif l2==min(lis):
			cluster[0].remove(i)


	elif i in cluster[1] and i in cluster[2]:
		l1=euclid(data.iloc[i][0],final[1][0],data.iloc[i][1],final[1][1],data.iloc[i][2],final[1][2],data.iloc[i][3],final[1][3])
		l2=euclid(data.iloc[i][0],final[2][0],data.iloc[i][1],final[2][1],data.iloc[i][2],final[2][2],data.iloc[i][3],final[2][3])

		lis.append(l1)
		lis.append(l2)
		

		if l1==min(lis):
			cluster[2].remove(i)

		elif l2==min(lis):
			cluster[1].remove(i)







#print(me,list(m).index(m))

#=============================================== Plot ===============================================

xc=[final[0][0],final[1][0],final[2][0]]
yc=[final[0][1],final[1][1],final[2][1]]


for i in range(len(cluster)):
	print(len(cluster[i]))

colors=['red','green','yellow']

for i in range(k):
	x=data.iloc[cluster[i]][0]
	y=data.iloc[cluster[i]][1]
	plt.scatter(x,y,c=colors[i],s=50)
	plt.scatter(xc,yc,c='black',s=100)


plt.show()
