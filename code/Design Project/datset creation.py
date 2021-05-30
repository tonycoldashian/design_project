import pandas as pd
import pprint

dataset = pd.read_csv('C:/Users/Aswyn/Documents/project/finalDATASET.csv')

#reading columns as lists
sub_interest= dataset['SUBJECT INTEREST']
co_curicular= dataset['CO CURRICULAR INTERESTS']
studm_bio = dataset['BIOLOGY']
studm_chem = dataset['CHEMISTRY']
studm_math= dataset['MATHEMATICS']
studm_lang = dataset['LANGUAGE']
studm_phy = dataset['PHYSICS']
studm_poli = dataset['POLITICS']
studm_geo = dataset['GEOGRAPHY']
studm_hist = dataset['HISTORY']
pers_type = dataset['PERS_TYP']
 
'''studdict = { 'stud_sub_interest':dataset['SUBJECT INTEREST'],
'co_curicular' : dataset['CO CURRICULAR INTERESTS'],
'studm_bio': dataset['BIOLOGY'],'studm_che':dataset['CHEMISTRY']}'''

#to convert string values into numerical values

for i in range(0,55):
    string=sub_interest[i]
    cocuri_string=co_curicular[i]
    perstypestr= pers_type[i]
    
    string= string.upper()
    cocuri_string= cocuri_string.upper()
    perstypestr = perstypestr.upper()
    
    if string=='BIOLOGY':
        sub_interest[i]=0
        
    elif string=='CHEMISTRY':
        sub_interest[i]=1 
        
    elif string=='MATHEMATICS':
        sub_interest[i]=2
        
    elif string=='ENGLISH' or string=='MALAYALAM' or string=='HINDI':
        sub_interest[i]=3
         
    elif string=='PHYSICS':
        sub_interest[i]=4
        
    elif string=='POLITICS':
        sub_interest[i]=5
    
    elif string=='IT':
        sub_interest[i]=6
    
    elif string=='GEOGRAPHY':
        sub_interest[i]=7
    
    elif string=='HISTORY':
        sub_interest[i]=8
    
    if cocuri_string=='SPORTS':
        co_curicular[i]=0
        
    elif cocuri_string=='LITERATURE':
        co_curicular[i]=1
    
    elif cocuri_string=='ARTS':
        co_curicular[i]=2
     
    if perstypestr == 'INTJ':
        pers_type[i]= 1
        
    
    elif perstypestr == 'INTP':
        pers_type[i]= 2
        
    
    elif perstypestr == 'ENTJ':
        pers_type[i]= 3
        
    
    elif perstypestr == 'ENTP':
        pers_type[i]= 4
        
    
    elif perstypestr == 'INFJ':
        pers_type[i]= 5
        
    
    elif perstypestr == 'INFP':
        pers_type[i]= 6
        
    
    elif perstypestr == 'ENFJ':
        pers_type[i]= 7
        
    
    elif perstypestr == 'ENFP':
        pers_type[i]= 8
        
    
    elif perstypestr == 'ISTJ':
        pers_type[i]= 9
        
    
    elif perstypestr == 'ISFJ':
        pers_type[i]= 10
        
    
    elif perstypestr == 'ESTJ':
        pers_type[i]= 11
        
    
    elif perstypestr == 'ESFJ':
        pers_type[i]= 12
        
    
    elif perstypestr == 'ISTP':
        pers_type[i]= 13
        
    
    elif perstypestr == 'ISFP':
        pers_type[i]= 14
        
    
    elif perstypestr == 'ESTP':
        pers_type[i]= 15
        
    
    elif perstypestr == 'ESFP':
        pers_type[i]= 16
        
            
#making a dictionary of student
dict ={  'subject_interest': sub_interest,
        'co_curicular' : co_curicular, 
        'bio_m':studm_bio, 
        'chem_m':studm_chem,
        'math_m':studm_math,
        'lang_m':studm_lang, 
        'phy_m':studm_phy, 
        'poli_m':studm_poli,
        'geo_m':studm_geo,
        'hist_m':studm_hist,
        'pers_type':pers_type
    }   

'''for i in range(0,55):
    print(str(sub_interest[i]) +' ||  ' +str(co_curicular[i]) +' || '+str(studm_bio[i]))'''

#creating a CSV file from the dictionary 
dataframe= pd.DataFrame(dict) 
dataframe.to_csv('C:/Users/Aswyn/Documents/outputdataframe.csv')
