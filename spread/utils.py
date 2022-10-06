import pandas
import pkg_resources


def get_stock_id(symbol):
    stocks_data = get_stocks_dict()

    for stock in stocks_data:
        if symbol.strip().upper() == stock["symbol"].upper():
            return stock["id"]

    raise Exception(f"Stock '{symbol}' not found")


def get_stocks_dict():
    resource_package = "investpy"
    resource_path = "/".join(("resources", "stocks.csv"))
    if pkg_resources.resource_exists(resource_package, resource_path):
        stocks = pandas.read_csv(
            pkg_resources.resource_filename(resource_package, resource_path),
            keep_default_na=False,
        )
    else:
        raise FileNotFoundError("Stocks file not found or errored.")

    if stocks is None:
        raise IOError("Stocks list not found or unable to retrieve.")

    stocks = stocks.where(pandas.notnull(stocks), None)

    columns = stocks.columns.tolist()

    return stocks[columns].to_dict(orient="records")
