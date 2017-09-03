
# coding: utf-8

# # Production vs Stage Environment Data Comparison 

# In[2]:

#importing the Pandas Library 
import pandas as pd


# In[ ]:

# Since we have to work with info from both the Production and Stage
# environments, we need to assign both .csv files to their respectively
# names dataframe objects


# In[121]:

# Creates production DataFrame
df_prod = pd.read_csv('prod.csv')


# In[122]:

# Creates stage DataFrame
df_stage = pd.read_csv('stage.csv')


# In[123]:

# Checking if the data was assigned properly by comparing output of the 
# .head() function to the .csv file.
df_prod.head(5)


# In[124]:

df_prod.describe()


# In[125]:

df_stage.describe()


# In[147]:

# This is the best method to rename columns, so the new name 
# sticks to the old name instead of the column location.  

df_stage = df_stage.rename(columns={'version':'Stage_Version', 'container':'Stage_Containter'})  


# In[127]:

df_prod = df_prod.rename(columns={'version':'Prod_Version', 'container':'Prod_Containter'})


# In[128]:

# Checking to see if the columns were renamed properly 
df_stage.head(5)


# In[139]:

# Creating a new data frame using the pd.merge() fucntion, where the data frames
# that are to be merged are listed, along with the column they are to be merged based on.
# The 'how' component of this is assigned with 'outer' which means that the 
# new data frame will include everything, not just the data that matches up.

df_merged=pd.merge(df_stage, df_prod, on='library', how='outer')


# In[148]:

# Creating an if statement where if the stage version and the prod version are equal,
# assigns the respective column 'matches' with 'yes', else 'no'.

df_merged['matches'] = df_merged.apply(lambda x: 'yes' if x.Stage_Version == x.Prod_Version else 'no', axis=1)


# In[149]:

# Fills the new dataframe at Stage_Version column to 0 if there exists no value (NaN)

df_merged['Stage_Version'].fillna('0',inplace=True)


# In[150]:

df_merged


# In[138]:

#simplest way to find number of rows
len(df_stage) 


# In[144]:

# Writes data frame into an updated .csv file 
df_merged.to_csv('df_merged.csv', index=False)


# In[145]:

df_merged['Prod_Version'].fillna('0',inplace=True) #fill NaN values with object (not string) 0


# In[151]:

df_merged


# In[152]:

df_merged.to_csv('df_merged.csv', index=False)


# In[171]:

df_POS = df_merged.groupby(['matches']).count()


# In[172]:

df_POS


# In[176]:

df_POS.iat[0,0]


# In[177]:

df_POS.iat[1,0]


# In[228]:

columns = ['Both ','Unique']


# In[229]:

data = df_POS.iat[[0,0], [1,0]]


# In[230]:

index = [0]


# In[231]:

df_piechart1 = pd.DataFrame(index = index, columns = columns)


# In[232]:

df_piechart1


# In[233]:

df_piechart1.iat[0,0] = df_POS.iat[0,0]


# In[234]:

df_piechart1


# In[235]:

df_piechart1.iat[0,1] = df_POS.iat[1,0]


# In[236]:

df_piechart1


# In[237]:

df_piechart1['total'] = df_piechart1['Both'] + df_piechart1['Unique']


# In[238]:

df_piechart1


# In[239]:

# The library needed to make data visualizations 

import matplotlib.pyplot as plt


# In[240]:

fig1, ax1 = plt.subplots()


# In[241]:

sizes = [int(df_piechart1.Both), int(df_piechart1.Unique)]


# In[245]:

sizes


# In[242]:

ax1.pie(sizes, labels=columns, autopct='%1.1f%%', shadow=True, startangle=90)


# In[243]:

ax1.axis('equal')


# In[244]:

plt.show()


# In[246]:

df_piechart1.plot.bar()


# In[247]:

get_ipython().magic(u'matplotlib inline')


# In[248]:

df_piechart1.plot.bar()


# In[ ]:



