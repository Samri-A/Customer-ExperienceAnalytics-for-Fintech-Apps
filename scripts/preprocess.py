import pandas as pd
def preprocess(df , bank):
    df.drop(columns=["replyContent" , "userName" , "repliedAt" , "thumbsUpCount" , "reviewCreatedVersion" , "appVersion" , "userImage"] , inplace = True)
    df.columns = [ "source_id" ,"review" , "rating"  , "date" ]
    df["bank"] = bank
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df["date"] = df["date"].dt.normalize()
    return df[:400]
