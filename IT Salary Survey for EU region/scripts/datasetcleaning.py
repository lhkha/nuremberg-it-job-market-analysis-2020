'''Bereinigen und erstellen Sie einen Datensatz, der nur Daten aus Nürnberg und seinen Nachbarregionen enthält.'''

import pandas as pd
#1. Datei lesen
df = pd.read_csv('it_salaries_2020.csv')
#2. Spaltennamen ändern
df_renamed = df.rename(columns={
    'City': 'city',
    'Position ': 'position', #Es gibt ein Leerzeichen am Ende des Spaltennamens
    'Total years of experience': 'exp_years_total',
    'Years of experience in current position': 'exp_years_current',
    'Seniority level': 'seniority_level',
    'Your main technology / programming language': 'main_tech',
    'Other technologies/programming languages you use often': 'other_tech',
    'Yearly brutto salary (without bonus and stocks) in EUR': 'salary_base',
    'Yearly bonus in EUR': 'salary_bonus',
    'Employment status': 'employment_status',
    'Сontract duration': 'contract_type',
    'Main language at work': 'work_language',
    'Company size': 'company_size'})
#3.Wichtige Spalten auswählen
important_columns = [
    'city', 'position', 'exp_years_total', 'seniority_level', 
    'main_tech', 'salary_base', 'work_language', 'company_size']
df_cleaned = df_renamed[important_columns]
#4. Zeilen mit fehlenden Werten entfernen
df_cleaned = df_cleaned.dropna(subset=['city', 'position'])
#5 Angemessene Gehaltsniveaus herausfiltern
df_cleaned['salary_base'] = pd.to_numeric(df_cleaned['salary_base'])
df_cleaned = df_cleaned[(df_cleaned['salary_base'] >= 10000) & (df_cleaned['salary_base'] <= 250000)]
#6 Nuremberg/Bayern
nbg_pattern = 'nürnberg|nuremberg|erlangen|fürth'
df_cleaned['is_nbg'] = df_cleaned['city'].astype(str).str.lower().str.contains(nbg_pattern, regex=True)
#7. Nuremberg-Daten in eine separate CSV exportieren
nuremberg_data = df_cleaned[df_cleaned['is_nbg']==True]
nuremberg_data.to_csv('it_salaries_2020_nuremberg.csv')


''' Der neue Datensatz ist nach den einzelnen technologischen Fähigkeiten aufgeschlüsselt. '''
#8. maintech teilen
nuremberg_data['main_tech_split'] = nuremberg_data['main_tech'].astype(str).str.split(r'[,/]+')
#9. Erweitere die Werte in der Liste in separate Zeilen.
nuremberg_data_exploded = nuremberg_data.explode('main_tech_split')
#10. Entfernen Sie überflüssige Leerzeichen und verwenden Sie einheitliche Groß- und Kleinschreibung.
nuremberg_data_exploded['main_tech_split'] = nuremberg_data_exploded['main_tech_split'].str.strip()
#11. Neue CSV file
nuremberg_data_exploded.to_csv('maintech_split.csv', index=False)