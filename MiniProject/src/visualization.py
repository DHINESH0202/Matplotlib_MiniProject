import matplotlib.pyplot as plt

def plot_product_sales(df):

    product_sales = df.groupby("Product")["Sales"].sum()

    product_sales.plot(kind="bar")

    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Sales")

    plt.show()


def plot_monthly_sales(df):

    monthly_sales = df.groupby("Month")["Sales"].sum()

    plt.plot(monthly_sales.index, monthly_sales.values, marker="o")

    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")

    plt.grid(True)

    plt.show()