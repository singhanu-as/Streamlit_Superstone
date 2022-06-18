import streamlit as st
import plotly.graph_objects as go
import pandas as pd
df=pd.read_csv(r'SampleSuperstore.csv')
st.write("Hello ,let's learn how to display Samplesuperstone data")

abc=st.selectbox('Pick the Region:' ,['East','West','South','Central'])
st.write(abc)
rslt_df = df[df['Region'] == abc]
rslt_df=rslt_df.head(50)
fig1 = go.Figure()
fig1.add_trace(go.Bar(y=rslt_df["Sub-Category"], x=rslt_df["Sales"], name="Sub-Category",orientation='h',
        textposition='outside',               
    marker=dict(
        color='#004953',
        line=dict(color='#004953', width=1)
    )))
fig1.update_layout(
    plot_bgcolor='#ffe0c0',
    paper_bgcolor='#ffe0c0'
) 
st.plotly_chart(fig1, use_container_width=True)

