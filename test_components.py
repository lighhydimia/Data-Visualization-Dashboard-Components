from dashboard_components.data import sample_timeseries
from dashboard_components.components import chart_card, summary_kpis
import pandas as pd

def test_sample_data():
    df = sample_timeseries(n=10)
    assert isinstance(df, pd.DataFrame)
    assert 'date' in df.columns
    assert len(df) == 10

def test_chart_card_creates_figure():
    df = sample_timeseries(n=20)
    card = chart_card('t', df, x='date', y='value', kind='line')
    assert card['type'] == 'chart'
    fig = card['figure']
    # Plotly figure has 'data' attribute with at least one trace
    assert len(fig.data) >= 1

def test_summary_kpis():
    df = sample_timeseries(n=5)
    kpis = summary_kpis(df, numeric_cols=['value'])
    assert isinstance(kpis, list)
    assert len(kpis) >= 1
