import numpy as np

def perform_analysis(df):

    print("\nSales Analysis")

    total_sales = np.sum(df["Sales"])

    avg_sales = np.mean(df["Sales"])

    print("Total Sales:", total_sales)
    print("Average Sales:", avg_sales)

    best_product = df.groupby("Product")["Sales"].sum().idxmax()

    print("Best Selling Product:", best_product)