import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

1.
df=pd.read_csv('/Users/priya/Documents/Projects/school/donation_project.csv',sep=",")
print(df.head(5)) 

dff=pd.read_csv('/Users/priya/Documents/Projects/school/schoools.csv',sep=",")
print(dff.columns)

2.
print(df.isnull().sum())
columns_to_fill = {
    'primary_focus_subject': 'Unknown',
    'primary_focus_area' :'Unknown',
    'secondary_focus_subject' :'Unknown',
    'secondary_focus_area' :'Unknown',
    'resource_type' :'Unknown',
    'grade_level' :'Unknown',
    'vendor_shipping_charges' : 0 ,
    'sales_tax' : 0 ,
    'fulfillment_labor_materials' : 0 ,  
    'payment_processing_charges' :0 ,     
    'students_reached' : 0 ,
    'date_completed' : 0 ,
    'date_thank_you_packet_mailed' : 0 ,
    'date_expiration' : 0
}
df.fillna(columns_to_fill, inplace=True)
print(df.isnull().sum())


print(dff.isnull().sum())
columns_to_fill = {
    'school_metro': 'Unknown',
    'school_ncesid': 0 ,
    'school_district' :'Unknown',
    'school_county' :'Unknown'
}
dff.fillna(columns_to_fill, inplace=True)
print(dff.isnull().sum())


3.
schools_dff = dff.loc[dff['school_state'] == 'NY','school_district']
print(schools_dff)

5.
print(df.groupby('primary_focus_subject')['total_donations'].count())

6.
donations_by_area = df.groupby('primary_focus_area')['total_donations'].count()
plt.figure()
donations_by_area.plot(kind='bar')

plt.xlabel('Primary Focus Area')
plt.ylabel('Total Donations')
plt.title('Total Donations by Primary Focus Area')
plt.xticks(rotation=45)
plt.show()

7.
df['date_posted'] = pd.to_datetime(df['date_posted'])

#project_over_time = df.groupby('date_posted').size()
project_over_time = df.resample('Y', on='date_posted').size()
project_over_time.plot(kind='bar')

plt.xlabel('date_posted')
plt.ylabel('Number of Projects')
plt.title('Total Projects Over Time')
plt.xticks(rotation=45)

plt.show()

8.
avg_price = df['total_price_including_optional_support'].mean()

project_total_price = df[df['total_price_including_optional_support'] > avg_price]

print(project_total_price['total_price_including_optional_support'])

print("*******************************************************")
9.

pivot_table = df.pivot_table(
    values ='total_price_excluding_optional_support',
    index='primary_focus_area',
    columns='poverty_level',
    aggfunc= 'mean'
    )
    
print(pivot_table)


10.
correlation = df['students_reached'].corr(df['total_donations'])

print(f"total_relations{correlation:.2f}")
plt.scatter(df['students_reached'], df['total_donations'], alpha=0.5)
plt.xlabel('Students Reached')
plt.ylabel('Total Donations')
plt.title('Correlation between Students Reached and Total Donations')
plt.show()


11. 
crosstab = pd.crosstab( 
    df['poverty_level'],
    df['primary_focus_area']
)
print(crosstab)

12.

plt.hist(df['total_donations'], bins=40)

plt.xlabel('tota_donations')
plt.ylabel('distribution')
plt.title('distribution of total_donations')
plt.show()

13.

sns.kdeplot(data=df, x="students_reached")

plt.xlabel =('students_reached')
plt.ylabel = ('density')
plt.title=('distribution of students_reached')
plt.show()

14.

percentail = df['total_price_excluding_optional_support'].quantile([0.25, 0.50, 0.75])
print (percentail)

print(df['total_price_excluding_optional_support'].describe())

15.

subject_counts = df['primary_focus_subject'].value_counts()

subject_counts.plot(kind='bar')

plt.xlabel=('primary_focus_subject')
plt.ylabel=('no.of projects')
plt.title=('Disribution of primary focused subjects')
plt.xticks(rotation=90)
plt.show()

16.

plt.boxplot(df['total_price_including_optional_support'])
plt.ylabel=('total_price_including_optional_support')
plt.title=('Boxplot of total_price')
plt.show()

sns.boxplot(y=df['total_price_including_optional_support'])
plt.title=('Distribution of total_price_including_optional_support')
plt.show()

17.
stats = df.groupby('primary_focus_subject')['students_reached'].agg(['mean', 'std']).reset_index()
print(stats) 

plt.figure(figsize=(10,6))
plt.bar(stats['primary_focus_subject'], stats['mean'], yerr=stats['std'], capsize=5)
plt.xticks(rotation=90)
plt.xlabel=('Primary Focus Subject')
plt.ylabel=('Average Students Reached')
plt.title=('Mean and Standard Deviation of Students Reached by Primary Focus Subject')
plt.show()

