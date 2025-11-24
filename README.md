import pandas as pd
import numpy as np
import os

print("="*60)
print("     PYTHON DATA SCIENCE - GHID PRACTIC & TEORETIC")
print("="*60)

# ==============================================================================
# 0. SETUP - GENERARE DATE FICTIVE (Ca să poți rula codul oriunde)
# ==============================================================================
def genereaza_date_test():
    print("\n[SETUP] Generare fișiere de test...")
    
    # Date Natalitate
    df_nat = pd.DataFrame({
        'Indicativ': ['AB', 'CJ', 'TM', 'B', 'IS'],
        'M_Urban': [1500, 4500, 3500, 9000, 4000],
        'F_Urban': [1400, 4300, 3400, 8500, 3800],
        'M_Rural': [1800, 2000, 1900, 100, 4500],
        'F_Rural': [1700, 1900, 1800, 90, 4300]
    })
    df_nat.to_csv("natalitate.csv", index=False)
    
    # Date Populație și Regiuni
    df_pop = pd.DataFrame({
        'Indicativ': ['AB', 'CJ', 'TM', 'B', 'IS'],
        'Regiune': ['Centru', 'Nord-Vest', 'Vest', 'Buc-Ilfov', 'Nord-Est'],
        'Populatie': [325000, 700000, 700000, 1880000, 800000]
    })
    df_pop.to_csv("PopulatieJudete.csv", index=False)
    
    # Date Bursiere (NVDA)
    df_stock = pd.DataFrame({
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'Open': [150, 155, 148], 'Close': [153, 158, 150],
        'High': [155, 160, 152], 'Low': [148, 152, 145]
    })
    df_stock.to_csv("NVDA.csv", index=False)
    print("[SETUP] Fișierele CSV au fost create cu succes.\n")

genereaza_date_test()

# ==============================================================================
# 1. PYTHON CORE - STRUCTURI DE DATE ȘI COMPREHENSIONS
# ==============================================================================
print("-" * 30)
print("1. PYTHON CORE")
print("-" * 30)

# A. List Comprehension (Crearea listelor într-o linie)
# Vrem o listă de etichete: "Student_1", "Student_2"...
# Sintaxa: [EXPRESIE for ITEM in ITERABIL]
etichete = [f"Student_{i}" for i in range(1, 6)]
print(f"List Comprehension: {etichete}")

# B. Dictionary Comprehension (Crearea dicționarelor dinamic)
# Vrem pătratele numerelor: {1: 1, 2: 4, 3: 9...}
patrate = {x: x**2 for x in range(1, 6)}
print(f"Dict Comprehension: {patrate}")

# C. Dicționar de Dicționare (Nested) - Model Examen
# Structura: An -> Student -> Listă Note
# Folosim numpy pentru note aleatoare
note_complexe = {
    f"An_{i}": {
        f"Stud_{j}": np.random.randint(1, 11, 3) # Array cu 3 note (1-10)
        for j in range(1, 4)
    } for i in range(1, 3)
}
# Transformare directă în DataFrame (Pandas știe să despacheteze asta!)
df_complex = pd.DataFrame(note_complexe)
print("\nDataFrame din Dicționar Imbricat:")
print(df_complex)

# ==============================================================================
# 2. NUMPY - CALCULE NUMERICE ȘI MATRICE
# ==============================================================================
print("\n" + "-" * 30)
print("2. NUMPY (Matrice)")
print("-" * 30)

# A. Inițializare
arr_zero = np.zeros((3, 3)) # Matrice 3x3 de zerouri
arr_range = np.arange(0, 10, 2) # [0, 2, 4, 6, 8]

# B. EXERCIȚIU TIPIC: Matricea 7x7 cu model specific
# - Bordura: 444
# - Diagonala: 55
# - Centrul: 111
print("Exercițiu Matrice 7x7:")
mat = np.ones((7, 7)) # Stratul 1: Totul e 1

# Slicing (Feliere) pentru bordură
mat[0, :] = 444  # Prima linie
mat[-1, :] = 444 # Ultima linie
mat[:, 0] = 444  # Prima coloană
mat[:, -1] = 444 # Ultima coloană

# Diagonala principală
np.fill_diagonal(mat, 55)

# Centrul (indexul 3,3)
mat[3, 3] = 111

print(mat)

# ==============================================================================
# 3. PANDAS - ANALIZA DE DATE (DATA SCIENCE)
# ==============================================================================
print("\n" + "-" * 30)
print("3. PANDAS (Analiza Datelor)")
print("-" * 30)

# A. Citire și Inspecție
df = pd.read_csv("natalitate.csv")
print("Primele 5 rânduri (Head):")
print(df.head())

# B. Vectorizare (Calcule pe coloane întregi)
# Nu folosim 'for'! Facem operatii matematice direct pe coloane.
df['Total_Nascuti'] = df['M_Urban'] + df['F_Urban'] + df['M_Rural'] + df['F_Rural']

# C. Matricea de Corelație
# Arată legătura dintre variabile (-1 la 1)
cols_numerice = ['M_Urban', 'F_Urban', 'M_Rural', 'F_Rural']
print("\nMatricea de Corelație:")
print(df[cols_numerice].corr())

# ==============================================================================
# 4. PANDAS AVANSAT - MERGE ȘI GROUPBY
# ==============================================================================
print("\n" + "-" * 30)
print("4. MERGE & GROUPBY (SQL in Python)")
print("-" * 30)

# A. MERGE (Unirea tabelelor)
# Aducem informația despre Populație și Regiune lângă Nașteri
df_pop = pd.read_csv("PopulatieJudete.csv")
# on='Indicativ' este cheia comună (ex: AB, CJ)
df_total = pd.merge(df, df_pop[['Indicativ', 'Populatie', 'Regiune']], on='Indicativ')

# Calculăm o rată (Nașteri la 1000 locuitori)
df_total['Rata_Natalitate'] = (df_total['Total_Nascuti'] / df_total['Populatie']) * 1000

# B. GROUPBY (Agregare)
# Vrem să vedem totalul populației pe fiecare Regiune
# as_index=False păstrează 'Regiune' ca și coloană normală (util!)
grup_regiuni = df_total.groupby('Regiune', as_index=False)[['Populatie', 'Total_Nascuti']].sum()
print("\nTotaluri pe Regiuni:")
print(grup_regiuni)

# C. IDQXMAX (Găsirea Campionului) - "Boss Level"
# Vrem să știm CARE județ are cele mai multe nașteri în fiecare regiune.
# .max() ne dă numărul. .idxmax() ne dă INDEXUL (numele județului).

def gaseste_lider(grup):
    # Setăm indicativul ca index temporar, ca idxmax să ne returneze 'CJ', 'AB' etc.
    return grup.set_index('Indicativ')['Total_Nascuti'].idxmax()

# Folosim include_groups=False pentru compatibilitate cu Pandas nou
lideri = df_total.groupby('Regiune').apply(gaseste_lider, include_groups=False)
print("\nJudețele cu cele mai multe nașteri per Regiune:")
print(lideri)

# ==============================================================================
# 5. BONUS - VECTORIZARE BURSIERĂ
# ==============================================================================
print("\n" + "-" * 30)
print("5. VECTORIZARE (Stock Market)")
print("-" * 30)
df_stock = pd.read_csv("NVDA.csv")
# Formula: (Close - Open) / (High - Low)
df_stock['Volatilitate'] = (df_stock['Close'] - df_stock['Open']) / (df_stock['High'] - df_stock['Low'])
print(df_stock[['Date', 'Volatilitate']])

print("\n" + "="*60)
print("     SCRIPT FINALIZAT CU SUCCES")
print("="*60)

# ==============================================================================
# 6. DATA CLEANING - GESTIONAREA VALORILOR LIPSĂ (NaN)
# ==============================================================================
print("\n" + "-" * 30)
print("6. DATA CLEANING (Curățare)")
print("-" * 30)

# Creăm un DataFrame cu "găuri" (np.nan)
df_dirty = pd.DataFrame({
    'Produs': ['Laptop', 'Mouse', 'Tastatura', 'Monitor', None],
    'Pret': [2500, np.nan, 150, np.nan, 0],
    'Stoc': [10, 50, np.nan, 20, 100]
})
print("Tabel cu valori lipsă:")
print(df_dirty)

# A. Identificarea valorilor lipsă
print(f"\nUnde sunt lipsuri?\n{df_dirty.isna().sum()}") # Numără NaN pe fiecare coloană

# B. Umplerea golurilor (Fillna)
# Umplem prețul lipsă cu media prețurilor existente
media_pret = df_dirty['Pret'].mean()
df_dirty['Pret_Corectat'] = df_dirty['Pret'].fillna(media_pret)

# Umplem stocul cu 0 (presupunem că nu avem marfă)
df_dirty['Stoc'] = df_dirty['Stoc'].fillna(0)

# C. Ștergerea rândurilor compromise (Dropna)
# Ștergem orice rând care mai are vreun NaN (ex: Produsul 'None')
df_clean = df_dirty.dropna()
print("\nTabel Curățat:")
print(df_clean)

# ==============================================================================
# 7. TIME SERIES - LUCRUL CU DATE CALENDARISTICE
# ==============================================================================
print("\n" + "-" * 30)
print("7. TIME SERIES (Date & Timp)")
print("-" * 30)

# Folosim fișierul NVDA generat anterior
df_stock = pd.read_csv("NVDA.csv")

# A. Conversia la Datetime (CRUCIAL!)
# CSV-urile citesc datele ca text (String). Trebuie convertite.
df_stock['Date'] = pd.to_datetime(df_stock['Date'])

# B. Extragerea de informații
df_stock['An'] = df_stock['Date'].dt.year
df_stock['Luna'] = df_stock['Date'].dt.month
df_stock['Zi_Saptamana'] = df_stock['Date'].dt.day_name() # Monday, Tuesday...

print("Date bursiere cu detalii de timp:")
print(df_stock[['Date', 'Zi_Saptamana', 'Close']].head())

# C. Filtrare după dată
# Vrem doar datele de după 2 ianuarie 2023
filtru_data = df_stock[df_stock['Date'] > '2023-01-02']
print(f"\nTranzacții după 2 Ianuarie:\n{filtru_data}")

# ==============================================================================
# 8. FILTRARE AVANSATĂ (.isin și ~)
# ==============================================================================
print("\n" + "-" * 30)
print("8. FILTRARE AVANSATĂ")
print("-" * 30)

df_pop = pd.read_csv("PopulatieJudete.csv")

# A. .isin() - Echivalentul SQL "IN (...)"
# Vrem doar județele din lista specifică
tinta = ['CJ', 'TM', 'IS']
df_target = df_pop[df_pop['Indicativ'].isin(tinta)]
print(f"Doar județele targetate: {df_target['Indicativ'].tolist()}")

# B. Negația (~) - "TOT CE NU E..."
# Vrem toate județele CARE NU SUNT în lista tinta
df_restul = df_pop[~df_pop['Indicativ'].isin(tinta)]
print(f"Restul județelor: {df_restul['Indicativ'].tolist()}")

# ==============================================================================
# 9. NUMPY AVANSAT - RESHAPE & MASCĂ BOOLEANĂ
# ==============================================================================
print("\n" + "-" * 30)
print("9. NUMPY AVANSAT")
print("-" * 30)

# A. Reshape (Remodelarea matricei)
arr = np.arange(1, 13) # Vector 1D: [1, 2, ... 12]
print(f"Vector original (1D): {arr}")

matrice_3x4 = arr.reshape(3, 4) # Transformăm în 3 rânduri x 4 coloane
print(f"Matrice Reshaped (3x4):\n{matrice_3x4}")

# B. Masca Booleană (Filtrare fără for)
# Vrem toate numerele din matrice care sunt mai mari ca 5
mask = matrice_3x4 > 5
print(f"\nMasca (True/False):\n{mask}")

# Aplicăm masca
elemente_mari = matrice_3x4[mask]
print(f"Elementele > 5 selectate: {elemente_mari}")

# C. Modificare condiționată (Foarte util!)
# "Înlocuiește tot ce e mai mic de 5 cu 0"
matrice_3x4[matrice_3x4 < 5] = 0
print(f"\nMatrice modificată condiționat (Low values -> 0):\n{matrice_3x4}")

print("\n" + "="*60)
print("     ACTUALIZARE COMPLETĂ REUȘITĂ")
print("="*60)
