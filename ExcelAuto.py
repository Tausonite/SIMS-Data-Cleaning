import pandas as pd

xldf = pd.read_excel(r'C:/Users/samou/Desktop/Python/PythonSIMSTest.xlsx', skiprows=12) #skipfooter can also be used but is not adaptable to longer column records
#bin garbage columns with useless data
xldf = xldf[:xldf[xldf['531_CsP_N51_NCrTaO_1.dp'] == '*** DATA END ***'].index[0]]
#this is the smarter way of slicing the data below the DATA END tag and deleting everything from then on
xldf_fixed = xldf.dropna(axis=1,how='all')
#this just drops the columns with all NaN values
#now we just need to fix the column names, reassign column titles (i.e depth is useless) and export the file

def fix_columns():
    #df.replace(to_replace='Depth', value='I[cnt/s]')
    #this approach doesn't fix the poor positioning of columns
    column_titles = df.row1
    for x in column_titles:
        if x == 'Depth':
            column_titles.remove('Depth')
        elif x == 'NaN':
            pass
        else:
            pass
    return column.titles
