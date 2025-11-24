import pandas as pd

print("\n---CERINTA 1---")

df_nat = pd.read_csv("natalitate.csv")
coloane_numerice = ['M_Urban','F_Urban','M_Rural','F_Rural']
df_subset = df_nat[coloane_numerice]

matrice_corelatie = df_subset.corr()
# matrice_corelatie.to_csv("Output1.csv")
print(matrice_corelatie)

print("\n---CERINTA 2---")
df_nat['NascutiViiMasculin'] = df_nat['M_Urban']+df_nat['M_Rural']
df_nat['NascutiViiFeminin'] = df_nat['F_Urban']+df_nat['F_Rural']
df_rezultat  = df_nat[['Indicativ','NascutiViiMasculin','NascutiViiFeminin']].copy()
print(df_rezultat)
# df_rezultat.to_csv("Output2.csv",index=False)

print("\n---CERINTA 3---")
df_nat = pd.read_csv("natalitate.csv")
df_pop = pd.read_csv("PopulatieJudete.csv")
df_merged = pd.merge(df_nat,df_pop[['Indicativ','Populatie']],on='Indicativ')
# print(df_merged)
categorii = ['M_Urban', 'F_Urban', 'M_Rural', 'F_Rural']
for col in categorii:
    df_merged[col] = (df_merged[col]/df_merged['Populatie'])*1000

df_merged=df_merged.drop(columns=['Populatie']).round(3)
print(df_merged)
# df_merged.to_csv("Output3.csv",index=False)

print("\n---CERINTA 4---")
df_nat = pd.read_csv("natalitate.csv")
df_pop = pd.read_csv("PopulatieJudete.csv")
df_merged = pd.merge(df_nat,df_pop,on='Indicativ').drop(columns=['Indicativ','Judet'])
df_merged = df_merged.groupby('Regiune').sum()
df_merged = df_merged.reset_index()
df_merged['NascutiUrban'] = ((df_merged['M_Urban']+df_merged['F_Urban'])/df_merged['Populatie'])*1000
df_merged['NascutiRural'] = ((df_merged['M_Rural']+df_merged['F_Rural'])/df_merged['Populatie'])*1000

df_rezultat = df_merged[['Regiune','NascutiRural','NascutiUrban']]
df_rezultat.to_csv("Output4.csv",index=False)
print(df_rezultat)

print("\n---CERINTA 5---")
df_nat = pd.read_csv("natalitate.csv")
df_pop = pd.read_csv("PopulatieJudete.csv")

df_merged = pd.merge(df_nat,df_pop[['Indicativ','Regiune']],on='Indicativ')

def gaseste_judetele_top(grup):
    grup = grup.set_index('Indicativ')

    return pd.Series({
        'NascutiMasculinUrban': grup['M_Urban'].idxmax(),
        'NascutiFemininUrban': grup['F_Urban'].idxmax(),
        'NascutiMasculinRural': grup['M_Rural'].idxmax(),
        'NascutiFemininRural': grup['F_Rural'].idxmax()
    })

df_rezultat = df_merged.groupby('Regiune').apply(gaseste_judetele_top)
df_rezultat = df_rezultat.reset_index()
df_rezultat.to_csv("Output5.csv",index=False)

print(df_rezultat.head())