import matplotlib.pyplot as plt
import pandas as pd


class Visualiser:
    def load_data(self, file_path):
        """
        Load data from a CSV file.
        """
        self.data = pd.read_csv(file_path)

        return self.data

    
    def plot_theme_distribution(df, bank_name, sentiment_label = "negative"):
        # Filter the DataFrame
        filtered_df = df[
            (df["bank"] == bank_name) & 
            (df["sentiment_label"].str.lower() == sentiment_label.lower())
        ]
        
        # Plot
        ax = filtered_df["identified_theme"].value_counts().plot(
            kind="bar",
            title=f"Issue Customer Report for {bank_name} Mobile Banking ({sentiment_label.capitalize()})",
            ylabel="Frequency",
            xlabel="Issue",
            color="skyblue",
            figsize=(10, 6)
        )
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.show()


    def plot_bank_rating_distribution(df, bank_name):
    
        bank_df = df[df["bank"] == bank_name]
    
        if bank_df.empty:
            print(f"No data found for bank: {bank_name}")
            return
    
    
        ax = bank_df["rating"].value_counts().sort_index().plot(
            kind="bar",
            title=f"Rating Distribution for {bank_name} Mobile Banking",
            xlabel="Rating",
            ylabel="Number of Reviews",
            color="teal",
            figsize=(8, 5)
        )
        plt.xticks(rotation=0)
        plt.grid(axis="y", linestyle="--", alpha=0.5)
        plt.tight_layout()
        plt.show()

        def plot_sentiment_trend_by_bank(df, bank_name):
       
            # Filter for the bank
            bank_df = df[df["bank"] == bank_name].copy()
        
            if bank_df.empty:
                print(f"No reviews found for bank: {bank_name}")
                return
        
            # Ensure 'date' column is datetime
            bank_df["date"] = pd.to_datetime(bank_df["date"])
            bank_df["month"] = bank_df["date"].dt.to_period("M").astype(str)
        
            # Count sentiments per month
            counts = bank_df.groupby(["month", "sentiment_label"]).size().unstack(fill_value=0)
        
            # Plot
            counts.plot(kind="line", marker="o", figsize=(12, 6),
                        title=f"Sentiment Trend Over Time – {bank_name}")
            plt.xlabel("Month")
            plt.ylabel("Number of Reviews")
            plt.grid(True, linestyle="--", alpha=0.5)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()