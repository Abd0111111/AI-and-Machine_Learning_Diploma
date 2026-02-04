import dash
from dash import dcc, html
from dash.dependencies import Output, Input, State
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import requests

app = dash.Dash(__name__)
BASE_URL = "http://127.0.0.1:5000"


def apply_dark_theme(fig):
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            color="#e5e7eb",
            size=13
        ),
        title=dict(
            x=0.5,
            xanchor="center",
            font=dict(size=18)
        ),
        xaxis=dict(
            showgrid=True,
            gridcolor="rgba(255,255,255,0.08)",
            zeroline=False
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor="rgba(255,255,255,0.08)",
            zeroline=False
        ),
        margin=dict(l=60, r=40, t=60, b=60)
    )
    return fig


# نفس دوال جلب الرسومات عندك
def fetch_top_customers():
    resp = requests.get(f"{BASE_URL}/top-customers")
    df = pd.DataFrame(resp.json())

    df_top = (
        df
        .sort_values("total_spent", ascending=False)
        .head(10)
    )

    fig = px.bar(
        df_top,
        x="total_spent",
        y="customer_name",
        orientation="h",
        color="total_spent",
        color_continuous_scale="Blues_r",
        labels={
            "total_spent": "Total Spent",
            "customer_name": "Customer"
        },
        title="Top 10 Customers by Total Spending"
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        coloraxis_showscale=False
    )

    fig = apply_dark_theme(fig)
    return fig


def fetch_best_products():
    resp = requests.get(f"{BASE_URL}/best-products")
    df = pd.DataFrame(resp.json())

    df_top = (
        df
        .sort_values("total_quantity", ascending=False)
        .head(5)
    )

    fig = px.bar(
        df_top,
        x="product_name",
        y="total_quantity",
        color="total_quantity",
        color_continuous_scale="Blues",
        labels={
            "total_quantity": "Quantity Sold",
            "product_name": "Product"
        },
        title="Top 5 Best Selling Products"
    )

    fig.update_layout(
        coloraxis_showscale=False
    )

    fig = apply_dark_theme(fig)
    return fig


def fetch_best_products_by_branch():
    resp = requests.get(f"{BASE_URL}/best-products-by-branch")
    df = pd.DataFrame(resp.json())

    top_products = (
        df
        .groupby("product_name")["total_quantity"]
        .sum()
        .nlargest(5)
        .index
    )

    df_top = df[df["product_name"].isin(top_products)]

    top_branches = (
        df_top
        .groupby("branch_name")["total_quantity"]
        .sum()
        .nlargest(5)
        .index
    )

    df_top = df_top[df_top["branch_name"].isin(top_branches)]

    pivot = (
        df_top
        .pivot_table(
            index="product_name",
            columns="branch_name",
            values="total_quantity",
            fill_value=0
        )
    )

    pivot = pivot.loc[
        pivot.sum(axis=1).sort_values(ascending=False).index
    ]

    fig = go.Figure()

    colors = px.colors.qualitative.Plotly

    for i, branch in enumerate(pivot.columns):
        fig.add_trace(
            go.Bar(
                x=pivot.index,
                y=pivot[branch],
                name=branch,
                marker_color=colors[i % len(colors)]
            )
        )

    fig.update_layout(
        barmode="stack",
        title="Top 5 Best Selling Products by Top 5 Branches",
        xaxis_title="Product",
        yaxis_title="Quantity Sold",
        xaxis_tickangle=-40,
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            font=dict(color="#e5e7eb")
        )
    )

    fig = apply_dark_theme(fig)
    return fig


def fetch_branch_revenue():
    resp = requests.get(f"{BASE_URL}/branch-revenue")
    df = pd.DataFrame(resp.json())

    df_top = (
        df
        .sort_values("total_revenue", ascending=False)
        .head(5)
    )

    fig = px.bar(
        df_top,
        x="total_revenue",
        y="branch_name",
        orientation="h",
        color="total_revenue",
        color_continuous_scale="Blues",
        labels={
            "total_revenue": "Total Revenue",
            "branch_name": "Branch"
        },
        title="Top 5 Branches by Revenue"
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        coloraxis_showscale=False
    )

    fig = apply_dark_theme(fig)
    return fig

def fetch_monthly_sales():
    resp = requests.get(f"{BASE_URL}/monthly-sales")
    df = pd.DataFrame(resp.json())

    df["month"] = pd.to_datetime(df["month"])
    df = df.sort_values("month")

    fig = px.line(
        df,
        x="month",
        y="total_sales",
        markers=True,
        labels={
            "month": "Month",
            "total_sales": "Total Sales"
        },
        title="Monthly Sales Trend Over Time"
    )

    fig.update_layout(
        xaxis_tickformat="%b %Y"
    )

    fig = apply_dark_theme(fig)
    return fig


def fetch_seasonal_demand():
    resp = requests.get(f"{BASE_URL}/seasonal-product-demand")
    df = pd.DataFrame(resp.json())

    df["month"] = pd.to_datetime(df["month"])
    df["month_name"] = df["month"].dt.month_name()

    month_order = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    top_products = (
        df.groupby("product_name")["total_quantity"]
        .sum()
        .nlargest(10)
        .index
    )

    df_top = df[df["product_name"].isin(top_products)]

    pivot = (
        df_top.groupby(["product_name", "month_name"])["total_quantity"]
        .mean()
        .reset_index()
        .pivot(index="product_name", columns="month_name", values="total_quantity")
        .reindex(columns=month_order)
    )

    fig = px.imshow(
        pivot,
        labels=dict(x="Month", y="Product", color="Avg Quantity"),
        x=month_order,
        y=pivot.index,
        color_continuous_scale="Blues",
        aspect="auto",
        title="Average Monthly Demand Pattern (Seasonality)"
    )

    fig.update_layout(
        coloraxis_colorbar=dict(
            tickfont=dict(color="#e5e7eb"),
            title=dict(font=dict(color="#e5e7eb"))
        )
    )

    fig = apply_dark_theme(fig)
    return fig

def fetch_stock_planning():
    resp = requests.get(f"{BASE_URL}/stock-planning")
    df = pd.DataFrame(resp.json())

    avg_quantity = df["total_quantity"].mean()
    avg_revenue = df["total_revenue"].mean()

    fig = px.scatter(
        df,
        x="total_quantity",
        y="total_revenue",
        labels={
            "total_quantity": "Total Quantity Sold",
            "total_revenue": "Total Revenue"
        },
        title="Branch Stock Planning Matrix",
        color_discrete_sequence=["steelblue"]
    )

    fig.add_shape(
        type="line",
        x0=avg_quantity,
        y0=df["total_revenue"].min(),
        x1=avg_quantity,
        y1=df["total_revenue"].max(),
        line=dict(dash="dash", color="gray")
    )

    fig.add_shape(
        type="line",
        x0=df["total_quantity"].min(),
        y0=avg_revenue,
        x1=df["total_quantity"].max(),
        y1=avg_revenue,
        line=dict(dash="dash", color="gray")
    )

    fig = apply_dark_theme(fig)
    return fig

# قائمة كل الرسومات
figures = [
    fetch_top_customers(),
    fetch_best_products(),
    fetch_best_products_by_branch(),
    fetch_branch_revenue(),
    fetch_monthly_sales(),
    fetch_seasonal_demand(),
    fetch_stock_planning()
]

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <style>
            button {
                transition: background-color 0.3s ease, color 0.3s ease;
                border: none;
                border-radius: 8px;
                padding: 10px 24px;
                cursor: pointer;
                font-weight: 600;
                font-size: 15px;
            }
            button#prev-btn {
                background-color: #1e293b;
                color: #e5e7eb;
                margin-right: 10px;
            }
            button#prev-btn:hover:not(:disabled) {
                background-color: #3b4a6b;
            }
            button#prev-btn:disabled {
                background-color: #4b5563;
                cursor: not-allowed;
                color: #9ca3af;
            }

            button#next-btn {
                background-color: #2563eb;
                color: white;
            }
            button#next-btn:hover:not(:disabled) {
                background-color: #3b82f6;
            }
            button#next-btn:disabled {
                background-color: #60a5fa;
                cursor: not-allowed;
                color: #bfdbfe;
            }
        </style>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''


app.layout = html.Div(
    style={
        "backgroundColor": "#0f172a",
        "minHeight": "100vh",
        "padding": "40px 0"
    },
    children=[

        html.Div(
            style={
                "maxWidth": "1200px",
                "margin": "0 auto",
                "padding": "20px"
            },
            children=[

                html.H1(
                    "Retail Data Analysis Dashboard",
                    style={
                        "textAlign": "center",
                        "marginBottom": "40px",
                        "color": "#e5e7eb",
                        "fontSize": "34px",
                        "fontWeight": "600"
                    }
                ),

                html.Div(
                    [
                        html.Button(
                            "Previous",
                            id="prev-btn",
                            n_clicks=0,
                            style={
                                "backgroundColor": "#1e293b",
                                "color": "#e5e7eb",
                                "border": "none",
                                "padding": "10px 24px",
                                "borderRadius": "8px",
                                "cursor": "pointer",
                                "marginRight": "10px"
                            }
                        ),

                        html.Button(
                            "Next",
                            id="next-btn",
                            n_clicks=0,
                            style={
                                "backgroundColor": "#2563eb",
                                "color": "white",
                                "border": "none",
                                "padding": "10px 24px",
                                "borderRadius": "8px",
                                "cursor": "pointer"
                            }
                        ),
                    ],
                    style={
                        "textAlign": "center",
                        "marginBottom": "30px"
                    },
                ),

                html.Div(
                    style={
                        "backgroundColor": "#020617",
                        "padding": "25px",
                        "borderRadius": "14px",
                        "boxShadow": "0 8px 25px rgba(0,0,0,0.35)"
                    },
                    children=[
                        dcc.Graph(id="main-graph", figure=figures[0])
                    ]
                ),

                html.Div(
                    id="figure-title",
                    style={
                        "textAlign": "center",
                        "fontSize": "18px",
                        "marginTop": "18px",
                        "color": "#cbd5f5"
                    }
                ),

                dcc.Store(id="figure-index", data=0)

            ]
        )
    ]
)
@app.callback(
    Output("main-graph", "figure"),
    Output("figure-title", "children"),
    Output("figure-index", "data"),
    Output("prev-btn", "disabled"),
    Output("next-btn", "disabled"),
    Input("prev-btn", "n_clicks"),
    Input("next-btn", "n_clicks"),
    State("figure-index", "data"),
)
def update_graph(prev_clicks, next_clicks, current_index):
    changed_id = dash.callback_context.triggered[0]["prop_id"].split(".")[0]

    if changed_id == "prev-btn":
        current_index = max(0, current_index - 1)
    elif changed_id == "next-btn":
        current_index = min(len(figures) - 1, current_index + 1)

    fig = figures[current_index]
    title = fig.layout.title.text if fig.layout.title else ""

    prev_disabled = current_index == 0
    next_disabled = current_index == len(figures) - 1

    return fig, title, current_index, prev_disabled, next_disabled


if __name__ == '__main__':
    app.run(debug=True)
