import streamlit as st
from dashboard_components.components import chart_card, kpi_card, data_table, summary_kpis
from dashboard_components.data import sample_timeseries
import pandas as pd

st.set_page_config(layout='wide', page_title='Dashboard Components Demo')

st.title('Dashboard Components — Streamlit Demo')

df = sample_timeseries(100)

# KPI row
kpis = summary_kpis(df, numeric_cols=['value'])
cols = st.columns(len(kpis))
for c, k in zip(cols, kpis):
    c.metric(k['title'], f"{k['value']:.2f}", k.get('subtitle'))

st.markdown('---')

# Chart and table
left, right = st.columns([2,1])
chart = chart_card('Value over time', df, x='date', y='value', kind='line')
with left:
    st.plotly_chart(chart['figure'], use_container_width=True)
with right:
    st.write('Sample data')
    st.dataframe(data_table(df, max_rows=20)['data'])
