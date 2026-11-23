import os

import matplotlib.pyplot as plt
import pandas as pd


class SalesDashboard:
    def __init__(self, filename):
        self.filename = filename
        self.data = None

    def load_data(self):
        try:
            self.data = pd.read_csv(self.filename)

            required_columns = ["Date", "Product", "Sales"]
            missing_columns = [
                column
                for column in required_columns
                if column not in self.data.columns
            ]

            if missing_columns:
                print("Missing column(s):", ", ".join(missing_columns))
                return False

            # Convert values to the types needed for charts.
            self.data["Date"] = pd.to_datetime(
                self.data["Date"], errors="coerce"
            )
            self.data["Sales"] = pd.to_numeric(
                self.data["Sales"], errors="coerce"
            )

            # Ignore rows with invalid dates or sales values.
            self.data = self.data.dropna(subset=["Date", "Sales"])

            print("Sales Data Loaded Successfully!")
            return True

        except FileNotFoundError:
            print("Error: sales.csv file not found!")
            return False
        except Exception as e:
            print("Error loading CSV:", e)
            return False

    def display_data(self):
        print("\nRetail Sales Data:")
        print(self.data)

    def line_graph(self):
        daily_sales = self.data.groupby("Date")["Sales"].sum()

        plt.figure()
        plt.plot(daily_sales.index, daily_sales.values, marker="o")
        plt.title("Daily Retail Sales")
        plt.xlabel("Date")
        plt.ylabel("Sales")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def bar_chart(self):
        product_sales = self.data.groupby("Product")["Sales"].sum()

        plt.figure()
        plt.bar(product_sales.index, product_sales.values)
        plt.title("Product-wise Sales")
        plt.xlabel("Product")
        plt.ylabel("Total Sales")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


# Put sales.csv in the same folder as this Python file.
script_folder = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_folder, "sales.csv")

dashboard = SalesDashboard(csv_path)

if dashboard.load_data():
    dashboard.display_data()
    dashboard.line_graph()
    dashboard.bar_chart()