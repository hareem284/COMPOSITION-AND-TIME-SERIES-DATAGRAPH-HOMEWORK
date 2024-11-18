import matplotlib.pyplot as plt
#importing seaborn
import seaborn as sns
#importing pandas to read data frame
import pandas as pd
#reading dataframe using pandas
rdf=pd.read_csv("FuelConsumption(5).csv")
print(rdf.info())
#checking for any null values
rdf.isnull().any()
print(rdf)
#making a pie chart
plt.pie(rdf=['FUELTYPE'],colors='maroon')
plt.show()
#creating another pie chart for vehicle class
plt.pie(rdf,x='VEHICLECLASS',colors='purple')
plt.show()
#creating a lineplot
sns.set_style('whitegrid')
sns.set_context('notebook')
plt.title("READING CO2EMISSIONS!!!!!!!!!!!!")
sns.lineplot(rdf,x='CO2EMISSIONS',palette='blue')
plt.show()
