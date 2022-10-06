import pandas
import plotly.express as px
from investiny import historical_data

from utils import get_stock_id

FROM_DATE = "01/01/2000"  # MM/DD/YYYY
TO_DATE = "01/01/2022"  # MM/DD/YYYY

petr3 = historical_data(
    investing_id=get_stock_id("PETR3"), from_date=FROM_DATE, to_date=TO_DATE
)
petr4 = historical_data(
    investing_id=get_stock_id("PETR4"), from_date=FROM_DATE, to_date=TO_DATE
)

records = [
    {
        "index": i,
        "petr3": petr3["close"][i],
        "petr4": petr4["close"][i],
        "ratio": petr4["close"][i] / petr3["close"][i],
    }
    for i in range(len(petr3["close"]))
]

long_short = pandas.DataFrame.from_records(records)
long_short.set_index("index", inplace=True)

fig = px.line(x=long_short.index, y=long_short.ratio)

fig.add_hline(y=long_short.ratio.mean(), line_width=5, line_color="green")
fig.add_hline(
    y=(long_short.ratio.mean() - long_short.ratio.std()),
    line_width=3,
    line_color="orange",
    line_dash="dash",
)
fig.add_hline(
    y=(long_short.ratio.mean() + long_short.ratio.std()),
    line_width=3,
    line_color="orange",
    line_dash="dash",
)
fig.add_hline(
    y=(long_short.ratio.mean() - 2 * long_short.ratio.std()),
    line_width=3,
    line_color="red",
    line_dash="dash",
)
fig.add_hline(
    y=(long_short.ratio.mean() + 2 * long_short.ratio.std()),
    line_width=3,
    line_color="red",
    line_dash="dash",
)
fig.update_layout(
    xaxis_rangeslider_visible=False,
    title_text="Razão entre preços PETR4 e PETR3",
    template="simple_white",
)
fig.show()
