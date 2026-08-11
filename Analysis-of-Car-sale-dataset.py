import pandas as p
import numpy as n
import matplotlib.pyplot as mat
import seaborn as sea


# accessing the DataSet
print(" reading the data-set")
df = p.read_csv("car details v4.csv")

print(df)

# Data exploration and study 

print('********************Exploration of dataset******************* ')

print('\n','\n','study the data informations')
print(df.info()) # getting the information about dataset

print(' taking dataset static descrition, shape, columns names, with top five and bottom five rows')
print(df.describe(),'\n', df.shape,'\n', df.tail(10),'\n', df.head(10), "\n", df.columns)
 # study dataset static descrition, shape, columns names, and first five and last five rows

print('datatypes of each column')
print(df.dtypes) # datatypes of columns

#  checking for missing or improper data
print('looking for improper data in the dataset')
for col in df.columns:
  print(df[col].head())   # improper data

# organised the data properly
print("**************organised the data properly*************")
print('removing the unit and chage tha data in the numberical types')
df['Engine'] = df['Engine'].str.replace('cc','')
print(df['Engine']) # removing 'cc'
df['Engine'] = df['Engine'].astype(float)
print(df['Engine'].dtype)
print('extraxted the numberical data only')
df['Max Power'] = df['Max Power'].str.extract(r'(\d+)')
print(df['Max Power']) # Extracted only numberical data

# type convert from str to float
df['Max Power'] = df['Max Power'].astype(float) 
df['Max Torque'] = df['Max Torque'].str.extract(r'(\d+)')
df['Max Torque'] = df['Max Torque'].astype(float)

# checking for missing data
print('seek for missing data')
print(df.isnull().sum())
print(df.dtypes)
print( 'removing the Drivetrai column from dataset ')
df.drop(columns=['Drivetrain'], inplace= True) # Since this ['Drivetrain'] column is useless for we remove it

# rechecking current staus of dataset
print(' recheck point')
print(df.columns)

# filling the missing data
print('filling the null values')
df.fillna(0, inplace = True)
# rechecking
print('rechecking for null value')
print(df.isnull().sum())

# checking for duplicate values
print('checking for duplicate values')

print(df.duplicated().sum())


# Analysising the data-set

cars = df["Make"].value_counts().sort_values(ascending=False).head()
print(f" the number of cars campany make \n {cars}")

data = df.loc[ df["Make"].isin(cars.index)]
sea.countplot(data=data, x= data['Make'])
mat.title("number of cars")
mat.show()


# price analysis
print('the list of highest selling')
H_S = df.groupby('Make')['Price'].sum().sort_values(ascending= False)
print( H_S)
print(f" the most Expensive company is {H_S.idxmax()} with total {H_S.max()} price")
#  Mercedes-Benz with  749810995 price  is the most expensive company according to this dataset
print(f" The cheapest company is {H_S.idxmin()} with total {H_S.min()} price")
# The Fiat is the cheapest company with 61000 price
H_SS=df.groupby("Make")["Price"].mean().sort_values(ascending=False).head(10)
mat.Figure(figsize=(9,9))
sea.barplot( x=H_SS.index, y=H_SS.values)
mat.xticks(rotation = 65)
mat.xlabel("Company")
mat.ylabel("sales")
mat.title("Companies VS price")
mat.show()
# Owner analysis

O_A = df.groupby("Owner")['Model'].count().sort_values(ascending= False)
'''
this the Owner list with 
Owner
First               1619
Second               373
Third                 42
UnRegistered Car      21
Fourth                 3
4 or More              1

'''

print("The Owner Count...")
print(O_A)
print(f' the highest owner type is {O_A.idxmax()} with {O_A.max()} cars counts')
print(f' the lowest owner type is {O_A.idxmin()} with {O_A.min()} cars counts')
# fuel analysis
F_A = df.groupby('Fuel Type')['Make'].count().sort_values(ascending= False)

'''
Here is the fuel type and their preferance

Fuel Type
Diesel          1049
Petrol           942
CNG               50
Electric           7
LPG                5
Hybrid             3
CNG + CNG          1
Petrol + CNG       1
Petrol + LPG       1

'''
# Diesel VS Petrol
fuel = ["Diesel","Petrol"]
fuel_data = df.loc[df["Fuel Type"].isin(fuel)]
print(fuel_data)
sea.countplot(data= fuel_data, x= fuel_data["Fuel Type"])
mat.title("Diesel VS Petrol")
mat.xlabel("fuel")
mat.ylabel("consumer")
mat.show()

print('the fuel comparison','\n',f'the petrol user are { F_A.loc['Petrol']}','\n',f'while the Diesel user are { F_A.loc['Diesel']}')
print(F_A)

# owner analysis

print('Average price by owner')
A_P_O = df.groupby('Owner')['Price'].mean().sort_values(ascending= False)
print(A_P_O)

mil = df.groupby('Fuel Type')["Kilometer"].mean()
print(mil)
# Transmission
Tra = df.groupby('Transmission')["Make"].count().sort_values(ascending=False)
print(' the Transmission list')
print(Tra)

T_P =  df.groupby('Transmission')['Price'].mean().sort_values(ascending= False)
# City analysis
lo = df.groupby("Location")['Price'].sum().sort_values(ascending= False)

print(' The Location V/S price ')
print(lo)
print(f'the highest prices {lo.max()} on {lo.idxmax()} ')
print(f'the cheapest prices {lo.min()} on {lo.idxmax()}')

l_c = df.groupby('Location')['Model'].count().sort_values(ascending= False)

print(' the city with most cars')
print(l_c)
print(f'Where the most of cars on { l_c.idxmax()} with total {l_c.max()} cars')

# Engine Analysis
print(f" the Engine size {df['Engine'].mean()}")

largest = df.loc[df["Engine"].idxmax()]
print(f"Largest engine: {largest['Engine']} cc")
print(f"Car: {largest['Make']} {largest['Model']}")

smallest = df.loc[df["Engine"].idxmin()]
print(f"smallet engine: {smallest['Engine']} cc")
print(f"Car: {largest['Make']} {largest['Model']}")

# Seating Capacity Analysis
print(f' the Avrage seating capacity is {df['Seating Capacity'].mean()}')
S = df.groupby("Seating Capacity")['Model'].count()
print(' the list range according to seating capacity','\n',S)

print('********* Price Analysis************')

EX = df.groupby('Model')["Price"].max()

print(f'the most expensive car is  {EX.idxmax()} with {EX.max()} ')

Ch = df.groupby('Model')["Price"].min()

print(f'the most expensive car is  {Ch.idxmin()} with {Ch.min()} ')

Med = df.groupby('Model')["Price"].median()

print("Median of the cars", '\n', Med)

print(' The distribution','\n',df['Price'].describe())

# Top 10 by Avg price

Avg_price = df.groupby("Make")["Price"].mean().sort_values(ascending= False).head(10)
mat.Figure(figsize=(9,9))
sea.barplot(x=Avg_price.index,y=Avg_price.values)
mat.xlabel("Company")
mat.ylabel("Average price")
mat.title("Top 10 Cars by Average Price ")
mat.xticks(rotation = 55, fontsize = 8)
mat.show()

# Engine Size vs Price
E_VS_P = df.groupby("Engine")["Price"].mean().sort_values(ascending= False).head(10)
mat.Figure(figsize=(9,9))
sea.scatterplot(x= E_VS_P.index,y=E_VS_P.values)
mat.xlabel("Engine size")
mat.ylabel("Average price")
mat.title("Engine Size vs Price")
mat.xticks(rotation = 55, fontsize = 8)
mat.show()
# Average Price by Fuel Type
Avg_price_by_fuel = df.groupby("Fuel Type")["Price"].mean().sort_values(ascending= False).head(10)
mat.Figure(figsize=(9,9))
sea.barplot(x=Avg_price_by_fuel.index,y=Avg_price_by_fuel.values)
mat.xlabel("Fuel type")
mat.ylabel("Average price")
mat.title("Average Price by Fuel Type")
mat.xticks(rotation = 55, fontsize = 8)
mat.show()

# Fuel Type Distribution

mat.Figure(figsize=(9,9))
sea.countplot(data=df, x="Fuel Type")
mat.xlabel("Fuel")
mat.ylabel("Number's of cars")
mat.title("Fuel Type Distribution")
mat.xticks(rotation = 55, fontsize = 8)
mat.show()

print("++++++++++++++++++++++ NUMPY +++++++++++++++++++++++++++++")

print(" Give the data to numpy")

price = df['Price'].to_numpy()

print(f" Avrager: {n.mean(price)}")

print(f" standard Deviations: {n.std(price)}")
print(f" median: {n.median(price)}")
print(f" maximun: {n.max(price)}")
print(f" Minimun: {n.min(price)}")
print(f" Variance {n.var(price)}")

print(f" percentile of","\n",f" 25% = {n.percentile(price,25)}","\n",f" 50% = {n.percentile(price,50)}","\n",f" 75% = {n.percentile(price,75)}")