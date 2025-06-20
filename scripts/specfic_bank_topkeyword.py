from bertopic import BERTopic
import pandas as pd
def specfic_bank_keyword(df , bank):
    df["cleaned_text"] = df[df["bank"] == bank]["review"].apply(preprocess)
    topic_model = BERTopic()
    topics, probs = topic_model.fit_transform(all_review_df["cleaned_text"].tolist())
    return topic_model