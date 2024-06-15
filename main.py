import pandas as pd
import openpyxl


pd.set_option('display.max_columns', None)

# API url from network
url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season=2012-13&SeasonType=Regular%20Season&StatCategory=PTS"
r = requests.get(url=url).json()

table_header = r['resultSet']['headers']
table_rows = r['resultSet']['rowSet']
df = pd.DataFrame(table_rows, columns=table_header)

file_name = 'nba.xlsx'

df.to_excel(file_name)
print(df) # printing the data frame

print('File written in xlsx file.')
