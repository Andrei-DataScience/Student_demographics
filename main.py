import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
data_math = pd.read_csv('student_math_clean.csv')
data_portuguese = pd.read_csv('student_portuguese_clean.csv')

# Demographic Information
# Distribution of students across schools
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
data_math['school'].value_counts().plot(kind='bar', color=['skyblue', 'lightcoral'])
plt.title('Distribution of Students Across Schools (Math)')

plt.subplot(1, 3, 2)
data_portuguese['school'].value_counts().plot(kind='bar', color=['skyblue', 'lightcoral'])
plt.title('Distribution of Students Across Schools (Portuguese)')

# # Gender distribution
plt.subplot(1, 3, 3)
data_math['sex'].value_counts().plot(kind='bar', color=['lightblue', 'lightpink'])
plt.title('Gender Distribution (Math)')

plt.tight_layout()
plt.show()

# Age distribution
plt.figure(figsize=(12, 5))
plt.subplot(3, 2, 1)
plt.hist(data_math["age"] , bins=15, color='skyblue', edgecolor='black')
plt.title('Age Distribution (Math)')
plt.xlabel('Age')
plt.ylabel('Number of Students')

plt.subplot(3,2,2)
plt.hist(data_portuguese["age"],bins=15, color='skyblue', edgecolor='black')
plt.title('Age Distribution (Portuguese)')
plt.xlabel('Age')


f_math = data_math[data_math["sex"] == "F"] 
m_math = data_math[data_math["sex"] == "M"] 

f_portuguese = data_portuguese[data_portuguese["sex"] == "F"] 
m_portuguese = data_portuguese[data_portuguese["sex"] == "M"] 

plt.subplot(3,2,3)
plt.hist(f_math["age"], bins=20 , color='skyblue', edgecolor='black')
plt.title('Age Distribution (Math, Females)')
plt.xlabel('Age')
plt.ylabel('Number of Students')

plt.subplot(3,2,4)
plt.hist(f_portuguese["age"], bins=20, color='skyblue', edgecolor='black')
plt.title('Age Distribution (Potruguese, Females)')
plt.xlabel('Age')
plt.ylabel('Number of Students')

plt.subplot(3,2,4)
plt.hist(m_math["age"], bins=15, color='skyblue', edgecolor='black')
plt.title('Age Distribution (Math, Males)')
plt.xlabel('Age')

plt.subplot(3,2,6)
plt.hist(m_portuguese["age"],bins=15, color='skyblue', edgecolor='black')
plt.title('Age Distribution (Potuguese, Males)')
plt.xlabel('Age')


plt.tight_layout()
plt.show()

