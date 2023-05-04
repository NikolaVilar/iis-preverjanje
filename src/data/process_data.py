import pandas as pd

# # read files
df_a = pd.read_csv('../../data/raw/students.txt', sep=';')
df_b = pd.read_csv('../../data/raw/students_grades.csv', sep=',')
df_c = pd.read_excel('../../data/raw/students_school.xlsx')

# print(df_c)
print(df_a.columns)
print(df_b.columns)

# columns_str = "student_id;sex;age;address;famsize;Pstatus;Medu;Fedu;Mjob;Fjob;reason;guardian;traveltime;studytime;failures;schoolsup;famsup;paid;activities;nursery;higher;internet;romantic;famrel;freetime;goout;Dalc;Walc;health"
# column_names = columns_str.split(';')
# df = pd.DataFrame(columns=column_names)
# print(df.columns)

# # Merge 
merged_df = pd.merge(df_a, df_b, on='student_id')
merged_df = pd.merge(merged_df, df_c, on='student_id')

merged_df['final_grade'] = merged_df[['G1', 'G2', 'G3']].mean(axis=1)

merged_df.drop(['G1', 'G2', 'G3'], axis=1, inplace=True)


merged_df.to_csv('../../data/processed/current_data.csv', index=False)
