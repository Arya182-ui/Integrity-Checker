import plotly.express as px
import pandas as pd

def plot_changes(log_file="logs.csv"):
    df = pd.read_csv(log_file)
    fig = px.histogram(df, x="timestamp", color="change_type", title="File Change Frequency")
    fig.show()
