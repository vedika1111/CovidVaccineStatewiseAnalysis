import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("E:\DSBDA\DSBDA Datasets\covid_vaccine_statewise.csv")
print("The top five rows are: ")
data.head()
print("The last five rows are: ")
data.tail()
print("The shape is: ")
data.shape
print("The columns present in the dataset are: ")
data.columns
data.describe()
data.describe(include='object')
data.info()
data.isnull().sum()

avg_firstdose = data["First Dose Administered"].astype("float").mean(axis = 0)
print("Average of First Dose:", avg_firstdose)

data["First Dose Administered"].fillna(value = avg_firstdose, inplace=True)
data

avg_seconddose = data["Second Dose Administered"].astype("float").mean(axis = 0)
print("Average of Second Dose:", avg_seconddose)

data["Second Dose Administered"].fillna(value = avg_seconddose, inplace = True)
data

first_dose = data.groupby('State')[['First Dose Administered']].sum()
first_dose

first_dose = data.groupby('State')[['Second Dose Administered']].sum()
first_dose

male = data["Male(Individuals Vaccinated)"].sum()
print("The total number of male individuals vaccinated are", int(male))

female = data["Female(Individuals Vaccinated)"].sum()
print("The total number of female individuals vaccinated are", int(female))


