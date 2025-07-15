import streamlit as st
import pandas as pd
import plotly.express as px
import io
import math
from navigation import make_sidebar
make_sidebar()  # Create the sidebar for navigation
st.set_page_config(page_title="Gantt Chart - Prácticas DATA SCIENCE - CTA 2025", layout="wide")

st.title("Gantt Chart - Prácticas DATA SCIENCE - CTA 2025")
df = pd.DataFrame([
    dict(Task="Base de datos DTX - HCP", Start='2025-01-15', Finish='2025-03-31'),
    dict(Task="Conectar SAP con DTX", Start='2025-04-01', Finish='2025-04-30'),
    dict(Task="Reunión con DSI", Start='2025-04-07', Finish='2025-04-08'),
    dict(Task="TFG DANC Laura", Start='2025-01-15', Finish='2025-05-31'),
    dict(Task="Análisis ECMO-RCP Badajoz", Start='2025-03-27', Finish='2025-05-04'),
    dict(Task="Completar análisis DANC", Start='2025-07-01', Finish='2025-07-18'),
    dict(Task="Resumen mensual", Start='2025-04-15', Finish='2025-07-18')
])

# Sort DataFrame by start date
df = df.sort_values(by="Start")

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Task")
fig.update_layout(showlegend=False)  # Hide the legend
fig.update_layout(
    xaxis=dict(showgrid=True, gridwidth=1, gridcolor='LightGray'),
    yaxis=dict(showgrid=False, gridwidth=1, gridcolor='LightGray'),
    plot_bgcolor='rgba(240, 240, 240, 0.8)',  # Light gray plot area background
    paper_bgcolor='rgba(250, 250, 250, 0.8)',  # Light background for the entire figure
)
for idx, row in df.iterrows():
    periods = pd.date_range(row["Start"],row["Finish"], freq='1D')
    center_pos = math.floor(len(periods) / 2)
    x_dates = periods[center_pos]
    fig.add_annotation(
        {
            "x": x_dates,#row["Finish"],
            "y": row["Task"],
            "text": "",
            "align": "center",
            "showarrow":False,
        }
    )
# No need for fig.show() as st.plotly_chart is used later



st.plotly_chart(fig)  #Display the plotly chart in Streamlit

# buffer = io.StringIO()
# fig.write_html(buffer, include_plotlyjs='cdn')
# html_bytes = buffer.getvalue().encode()
# st.download_button(
#     label='Export to HTML',
#     data=html_bytes,
#     file_name='Gantt.html',
#     mime='text/html'
# ) 