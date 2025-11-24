import pandas as pd  # Importăm biblioteca și îi dăm porecla 'pd'

# 1. Încărcarea fișierelor în variabile (DataFrames)
# Funcția read_csv citește textul separat prin virgulă și îl face tabel
df_industrie = pd.read_csv("Industrie.csv")
df_populatie = pd.read_csv("PopulatieLocalitati.csv")

# 2. Verificarea datelor (Inspecția vizuală)
# Funcția .head() ne arată primele 5 rânduri
print("--- Tabelul Industrie (primele 5 rânduri) ---")
print(df_industrie.head())

print("\n--- Tabelul Populație (primele 5 rânduri) ---")
print(df_populatie.head())

#CERINTA 1
print("\n\n---CERINTA 1")


# df_industrie['Cifra de afaceri'] = df_industrie.drop(columns=['Siruta','Localitate']).sum(axis=1)
df_industrie['Cifra de afaceri'] = df_industrie.iloc[:,2:].sum(axis=1) #iloc (integer location)
df_final = df_industrie[['Siruta', 'Localitate','Cifra de afaceri']]
# df_final.to_csv("Output1.csv",index = False)
print(df_final.head())

# CERINTA 2
print("\n\n---CERINTA 2")

df_total = pd.merge(df_industrie,df_populatie[['Siruta' , 'Populatie']], on='Siruta')

df_total['CF/loc'] = df_total['Cifra de afaceri'] / df_total['Populatie']

df_final2 = df_total.sort_values(by='CF/loc',ascending=False)

df_export = df_final2[['Siruta','Localitate','CF/loc']]

# df_export.to_csv("Output2.csv",index  =False)
print(df_export.head())

# CERINTA 3
print("\n\n---CERINTA 3")

df_ind = pd.read_csv("Industrie.csv")
df_ind['Total_Temp'] = df_ind.iloc[:,2:].sum(axis=1)
df_filtrat  =df_ind[df_ind['Total_Temp']>0].copy()
df_filtrat['Activitate']  =df_filtrat.drop(columns=['Siruta', 'Localitate','Total_Temp']).idxmax(axis=1)

df_final3 = df_filtrat[['Siruta','Localitate','Activitate']]
# df_final3.to_csv("Output3.csv",index = False)
print(df_final3.head())

# CERINTA 4
print("\n\n---CERINTA 4")

df_ind = pd.read_csv("Industrie.csv")
df_pop = pd.read_csv("PopulatieLocalitati.csv")

df_total = pd.merge(df_ind,df_pop[['Siruta','Judet']], on='Siruta')

df_de_grupat = df_total.drop(columns=['Siruta','Localitate'])

# print(df_de_grupat)

df_final4 = df_de_grupat.groupby('Judet').sum()
df_final4 = df_final4.reset_index()
# df_final4.to_csv("Output4.csv",index = False)
print(df_final4.head())

# CERINTA 5
print("\n\n---CERINTA 5")
# df_final4['Total pe jud'] = df_final4.iloc[:,1:].sum(axis=1)
# df_total = df_final4[['Judet','Total pe jud']]
df_ind = pd.read_csv("Industrie.csv")
df_pop = pd.read_csv("PopulatieLocalitati.csv")

df_ind['Total localitate'] = df_ind.iloc[:,2:].sum(axis=1)
df_merged = pd.merge(df_ind[['Siruta','Total localitate']],
                     df_pop[['Siruta','Judet','Populatie']],
                     on='Siruta')
# print(df_merged)
df_judete = df_merged[['Judet','Total localitate','Populatie']].groupby('Judet').sum()
df_judete = df_judete.reset_index()
# print(df_judete)
df_judete['CA/loc'] = df_judete['Total localitate'] / df_judete['Populatie']
df_final5 = df_judete.sort_values(by='CA/loc',ascending=False)[['Judet','CA/loc']]
print(df_final5)
df_final5.to_csv("Output5.csv",index = False)


