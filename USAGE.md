# Usage Notes

This repo supplies tiny UI-agnostic component factories (they return dicts or Plotly figures).
The examples show how to render them with Streamlit and Dash. Extend components with props for colors, sizing, or add React wrappers.

Files of interest:
- `src/dashboard_components/components.py` — core helpers (kpi_card, chart_card, data_table)
- `examples/streamlit_app.py` — how to compose a quick Streamlit dashboard
- `examples/dash_app.py` — minimal Plotly Dash app using the components
