# Patient Analytics Dashboard

An interactive Patient Analytics Dashboard built with Python and Streamlit to visualize patient counts.

**Live demo:** https://patient-analytics-dashboard-gtiznupxed4fjjyhajzpr3.streamlit.app/

## Features

- Interactive visualizations of patient counts
- Filters to explore the data by different categories
- Responsive layout that works in the browser
- Deployed on Streamlit Community Cloud

## Tech Stack

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/python/) / Matplotlib (for charts)

## Getting Started

### Prerequisites

- Python 3.9 or higher
- pip

### Installation

```bash
# Clone the repository
git clone <your-repository-url>
cd patient-analytics-dashboard

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run the App

```bash
streamlit run app.py
```

The dashboard will open at `http://localhost:8501`.

## Project Structure

```
patient-analytics-dashboard/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── data/               # Patient dataset (CSV)
└── README.md           # Project documentation
```

## Usage

1. Open the dashboard in your browser.
2. Use the sidebar filters to narrow down the patient data.
3. Explore the charts to see patient counts and trends.

## Deployment

This app is deployed on [Streamlit Community Cloud](https://streamlit.io/cloud). To deploy your own copy:

1. Push the project to a GitHub repository.
2. Sign in to Streamlit Community Cloud and click **New app**.
3. Select your repository, branch, and `app.py` as the main file.
4. Click **Deploy**.

## Contributing

Contributions are welcome. Fork the repo, create a feature branch, and open a pull request.

## License

This project is licensed under the MIT License.
