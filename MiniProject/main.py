from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.analysis import perform_analysis
from src.visualization import plot_product_sales, plot_monthly_sales

def main():

    print("Retail Sales Analysis Project")

    df = load_data(r"C:\Users\VICKY\OneDrive\Desktop\Dhinesh\MiniProject\data\sales_data.csv")

    df = preprocess_data(df)

    perform_analysis(df)

    plot_product_sales(df)

    plot_monthly_sales(df)

if __name__ == "__main__":
    main()