# Data Visualization — Dashboard Components

A small collection of reusable **Data Visualization / Dashboard Components** for building dashboards quickly with Streamlit and Plotly Dash.  
Sponsor-friendly: compact, well-documented components ideal for tutorials, demos, and production prototypes — great for GitHub Sponsors.

## Features

- Reusable components: KPI cards, chart cards, data table helpers.
- Examples for **Streamlit** and **Plotly Dash** showing how to compose a dashboard.
- Small sample dataset generator and convenience data loader.
- Tests and CI to get you started quickly.

## Quickstart

1. Create virtualenv and install dependencies:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Run the Streamlit example:
```bash
streamlit run examples/streamlit_app.py
# Opens at http://localhost:8501
```

3. Run the Dash example:
```bash
python examples/dash_app.py
# Opens at http://127.0.0.1:8050
```

## Sponsorship

If you find this project useful, please consider sponsoring development to fund:
- More components (maps, advanced table features)
- Implementation for additional frameworks (React, Vue)
- Accessibility and performance improvements

Add a `FUNDING.yml` file and Sponsor button on the repo for an easy support flow.

## Structure

- `src/dashboard_components` — components & helpers
- `examples` — runnable demo apps
- `docs` — usage notes
- `tests` — unit tests

## License

MIT
