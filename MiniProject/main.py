from MiniProject.src.data_loader import load_data
from MiniProject.src.preprocessing import preprocess_data
from MiniProject.src.analysis import perform_analysis
from MiniProject.src.visualization import plot_product_sales, plot_monthly_sales


def main():

    print("Retail Sales Analysis Project")

    df = load_data("MiniProject/data/sales_data.csv")

    df = preprocess_data(df)

    perform_analysis(df)

    plot_product_sales(df)

    plot_monthly_sales(df)


if __name__ == "__main__":
    main()