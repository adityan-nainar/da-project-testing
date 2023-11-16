import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

st.title('DA Project :smile:')

df = pd.read_csv('BillionairesStatisticsDataset.csv')


#sidebar

st.sidebar.header('Filters here: ')

# country = st.sidebar.multiselect(
#     "Select the country: ",
#     options=df['country'].unique(),
#     default=df['country'].iloc[1]   
# )

container = st.sidebar.container()
all = st.sidebar.checkbox("Select all countries")
 
if all:
    country = container.multiselect("Select one or more options:",
         df['country'].unique(),df['country'].unique())
else:
    country = container.multiselect("Select one or more options:",
        df['country'].unique(),default=['India', 'Switzerland'])
       
# category = st.sidebar.multiselect(
#     "Select the category: ",
#     options=df['category'].unique(),
#     default=df['category'].iloc[1]
# )

container2 = st.sidebar.container()
all2 = st.sidebar.checkbox("Select all categories")
 
if all2:
    category = container2.multiselect("Select one or more options:",
         df['category'].unique(),df['category'].unique())
else:
    category = container2.multiselect("Select one or more options:",
        df['category'].unique(), default=['Technology'])
  

selfMade = st.sidebar.multiselect(
    "Select selfMade : ",
    options=df['selfMade'].unique(),
    default=df['selfMade'].unique()
)

age = st.sidebar.slider(
    'Select Age range',
    0, 100, (25, 75)
)

df_selection = df.query(
    "country == @country & category==@category & selfMade==@selfMade & age<=@age[1] & age>=@age[0]"
)


#Mainpage
st.markdown("##")

number_of_b = len(df_selection.index)
avg_age = round(df_selection['age'].mean(),1)
avg_final_worth = round(df_selection['finalWorth'].mean(),1)
left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.subheader("Number of billionaires: ")
    st.subheader(f"{number_of_b}")
with middle_column:
    st.subheader("Average age: ")
    st.subheader(f"{avg_age}")
with right_column:
    st.subheader("Average worth (in billion $): ")
    st.subheader(f"{avg_final_worth}")

st.markdown('---')


figure = px.bar(df_selection, x = 'rank', y = 'finalWorth')
figure.update_layout(title_text='Rank vs Worth', title_x=0.5)

fig = px.pie(df_selection, values='finalWorth', names='country', title='Country wise percentage')
fig.update_layout(title='Country wise percentage', title_x=0.37)

left_column, right_column = st.columns(2)
left_column.plotly_chart(figure, use_container_width=True)
right_column.plotly_chart(fig, use_container_width=True)

st.dataframe(df_selection)
