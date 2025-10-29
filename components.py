"""Reusable dashboard components for Streamlit and Dash demos."""
from typing import Optional, Dict, Any
import pandas as pd
import plotly.express as px

def kpi_card(title: str, value: Any, subtitle: Optional[str] = None) -> Dict[str, Any]:
    """Return a small dict representing a KPI card that UI layers can render."""
    return {"type": "kpi", "title": title, "value": value, "subtitle": subtitle}

def chart_card(title: str, df: pd.DataFrame, x: str, y: str, kind: str = 'line'):
    """Create a Plotly figure and metadata for a chart card."""
    if kind == 'line':
        fig = px.line(df, x=x, y=y, title=title)
    elif kind == 'bar':
        fig = px.bar(df, x=x, y=y, title=title)
    elif kind == 'scatter':
        fig = px.scatter(df, x=x, y=y, title=title)
    else:
        raise ValueError(f"Unknown kind: {kind}")
    return {"type": "chart", "title": title, "figure": fig}

def data_table(df: pd.DataFrame, max_rows: int = 100):
    """Return a table dict for UI to render (DataFrame truncated)."""
    return {"type": "table", "data": df.head(max_rows)}

# small helper to compute simple aggregations
def summary_kpis(df: pd.DataFrame, numeric_cols: Optional[list] = None):
    if numeric_cols is None:
        numeric_cols = df.select_dtypes('number').columns.tolist()
    kpis = []
    for c in numeric_cols:
        kpis.append(kpi_card(f"{c} (sum)", float(df[c].sum()), subtitle=f"mean={df[c].mean():.2f}"))
    return kpis
