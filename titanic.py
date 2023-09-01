
# Importing necessary libraries

#  
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#   Loading titanic dataset from seaborn library


titanic=sns.load_dataset("titanic")


titanic.head()


#   Below boxplot shows that age column some outliers

#  
sns.boxplot(titanic.age)
plt.show()

#     
#   Plotting Histogram for better visualization of age distribution

#  
plt.hist(data=titanic,x='age',bins=20,rwidth=0.9)
plt.xlabel('age in years')
plt.ylabel("count")
plt.show()

#     
#   Looking for the normal distribution of age column

#  
sns.distplot(titanic.age,bins=20,color='g')
plt.show()

#     
#    1.IQR :Inter Quartile Range over(age)

#     
#    Q1: 25% value of the age column called as 1st quartile<br>
#      Q3: 75% value of the age column called as 3rd Quartile

#  
# Finding quartile values
q1=titanic.age.quantile(0.25)
q3=titanic.age.quantile(0.75)
q1,q3

#     
#   IQR :Inter Quartile Range is the difference between Q3 and Q1

#  
iqr=q3-q1
iqr

#     
#   Finding the lower whisker:Q1-1.5*IQR <BR>
#     Finding the upper whisker:Q3+1.5*IQR

#  
lower_whisker=q1-1.5*iqr
upper_whisker=q3+1.5*iqr
lower_whisker, upper_whisker

#     
#   Finding the rows with outliers in age
# 

#  
titanic[(titanic['age']>upper_whisker) | (titanic['age']<lower_whisker)]

#     
#   Removing outliers

#  
data=titanic[(titanic['age']<upper_whisker) & (titanic['age']>lower_whisker)]

#  
data.shape

#     
#   Plotting the Boxplot after removing the outliers

#  
sns.boxplot(data=data,x='age',color='purple')
plt.show()

#     
#   2.Z-score Method<br>
# Z-score=mean()+threshold*std()<br>
# Z-score indicates how many standard deviation away a data point is

#  
titanic.head()
titanic.shape

#     
# ## z=(x-mean)/std()

#  
titanic['Z-Score']=(titanic.age-titanic.age.mean())/titanic.age.std()

#  
titanic.head()

#     
#    Rows whose z-score value is greater than 3 and less than -3 are considered as outliers

#  
titanic[(titanic['Z-Score']>3) | (titanic['Z-Score']<-3)]

#     
#   Removing the outliers

#  
new_data=titanic[(titanic['Z-Score']<2) & (titanic['Z-Score']>-2)]

#  
new_data.shape

#  
sns.boxplot(data=new_data,x='age',color='purple')
plt.show()

#     
# <H3>Percentile method

#  
titanic.head()

#  
titanic.drop(columns=['Z-Score'],inplace=True)

#  
min_threshold,max_threshold=titanic.age.quantile([0.05,0.95])
min_threshold,max_threshold

#  
titanic[(titanic.age>max_threshold) | (titanic.age<min_threshold)]

#  
no_outlier=titanic[(titanic.age<max_threshold) & (titanic.age>min_threshold)]

#  
no_outlier.shape

#  
sns.boxplot(data=no_outlier,x='age',color='green')
plt.show()

#  
df=sns.load_dataset("titanic")

#  
df

#  



