import pandas as pd

def formatting_csv(df):
    """
    Perform cleaning/formatting  on the given DataFrame.

    Parameters:
        df (pandas DataFrame): The input DataFrame to be cleaned and formatted.

    Returns:
        pandas DataFrame: The formatted DataFrame after applying data cleaning operations.
    """

    # Remove leading and trailing spaces in all fields
    for k in df.keys():
        df[k] = df[k].str.strip()

    # Put columns in a list
    listco = df.columns
    listNoPoint = []

    # For duplicate elements, removing '.1' from the name
    for l in listco:
        if l.endswith('.1'):
            l = l.replace('.1', '')
        listNoPoint.append(l)

    # Transpose the dataframe to have the columns at the top
    df = df.T

    # Removing the auto index
    df.reset_index(drop=True, inplace=True)

    # Adding the list of element in the first row
    df.insert(0, 'NameDB', listNoPoint)

    # Put the columns on 1st row (and the index)
    df = df.set_axis(df.iloc[0], axis=1)
    df = df[1:]
    # df = df.replace('\n','', regex=True)
    # df = df.replace('\r','', regex=True)
    # df = df.replace('\r\n','', regex=True)

    # Replacing NaN with empty strings
    df = df.fillna('')

    return df