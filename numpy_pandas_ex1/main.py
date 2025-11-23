import pandas as pd
import numpy as np

print('\n---CERINTA 1---')

matrice = np.loadtxt("Matrice32.txt",dtype=int,delimiter=' ')

print('\n---CERINTA 2---')
valori = np.random.uniform(-3,3,50)
etichete = [f"R_{i}" for i in range(1,51)]

seria = pd.Series(data=valori, index=etichete)

print(seria)

print('\n---CERINTA 3---')
matrice_2d = np.random.uniform(-5,5,(11,6))
etichete_randuri = [f"R{i}"for i in range(1,12)]
etichete_coloane = [f"V{i}"for i in range(1,7)]

df = pd.DataFrame(data= matrice_2d,
                  index=etichete_randuri,
                  columns=etichete_coloane)

print(df)

print('\n---CERINTA 4---')
matrice = np.full(shape=(7,7),fill_value=9.0)
print(matrice)

matrice[:,:] = 0.0
matrice[1:-1,1:-1]=1.0
print(matrice)

print('\n---CERINTA 5---')
# sintaxa - dictionary comprehension
# dictionar = { CHEIE : VALOARE for i in range(...) }
date_studenti = {
    f"Stud_{i}": np.random.randint(1,11,5)
    for i in range(1,7)
}
df_studenti = pd.DataFrame(date_studenti)
print(df_studenti)

print('\n---CERINTA 6---')
s1 = pd.read_csv("Seria_1.csv")['Date']
s2 = pd.read_csv("Seria_2.csv")['Date']

dictionar = {
    'C_1':s1,
    'C_2':s2
}
df = pd.DataFrame(dictionar)
print(df)

print('\n---CERINTA 7---')
df = pd.read_csv("NVDA.csv");
df['RV'] = (df['Close']-df['Open'])/(df['High']-df['Low'])
df.to_csv("NVDA_RA.csv",index=False)
print(df)

print('\n---CERINTA 8---')
dictionar = {
    f"An_{i}":{
        f"Stud_{j}":np.random.randint(1,11,size=3)
        for j in range(1,8)
    }for i in range(1,4)
}
df = pd.DataFrame(dictionar)
print(df)

print('\n---CERINTA 9---')

matrice = np.ones(shape=(7,7))

matrice[0,:]=444
matrice[-1,:]=444
matrice[:,0]=444
matrice[:,-1]=444

np.fill_diagonal(matrice,55)

matrice[3,3]=111

print(matrice)

