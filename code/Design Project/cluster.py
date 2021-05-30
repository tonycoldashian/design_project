import pandas as pd
import matplotlib.pyplot as plt 
#from sklearn.neighbours import KNeighboursClassifier

#file read
dataset = pd.read_csv(r'C:/Users/Aswyn/Documents/project/outputdataframe.csv')
reference = pd.read_csv(r'C:/Users/Aswyn/Documents/project/book1.csv')

#columns to list
sub_int = dataset['subject_interest']
co_curi = dataset['co_curicular']
biology = dataset['bio_m']
personality_type = dataset['pers_type']


#defining to null list, 1: index values for bio intersed students, 2: marks of those students
biolist=[]
biomarks=[]

#extracting bio interested students
for i in range(0,55):
    if sub_int[i]==0:
        biolist.append(i)
        biomarks.append(biology[i])

#reference columns to list
#for i in range(0,):
#    if reference['personality'] == personality_type[i]:
        

#print(biolist)    
plt.scatter(personality_type,co_curi)
plt.show()