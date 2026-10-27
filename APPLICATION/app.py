import pandas as pd
import streamlit as st

df=pd.read_csv('movies.csv')
def predict(type:str,year:int):
    if type in list(df['type'].unique()):
        movies=df[df['type']==type]
        if year in range(1925,2021):
            movies=movies[movies['release_year']==year]
    else:
        if year in range(1925,2021):
            movies=df[df['release_year']==year]
        else:
            movies=df
    return list(movies['title']),len(list(movies['title']))

st.title('Year Based Suggestor')
st.info('This model is capable to sugggest movie based on the type like Movie/Show u want and also based on year from 1925 to 2021')
type=st.selectbox('Choose the type of show: ',['All','Movie','TV Show'])
year=st.selectbox('Choose the release year: ',range(1925,2022))
movies,count=predict(type,year)
st.info(f'There are total of {count} {type} as per your choice!')
show=st.selectbox(f'How many {type} to view?',range(1,count+1))
if st.button('Total Movies'):
    if type not in  ['Movie','TV Show']:
        type='Movie/Show'
    st.header('Movies are :')
    for i in movies[:show]:
        st.subheader(i)
predict('TV Show',2003)