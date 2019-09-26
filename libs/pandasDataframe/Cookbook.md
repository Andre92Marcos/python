**Add Column to dataframe**


    column = [1,2]
    df[columnLabel] = Series(column , index=df.index)


**Create Dataframe**

    d = {'exchange': [], 'symbol': [], 'name' : []}
    df = pd.DataFrame(data=d)