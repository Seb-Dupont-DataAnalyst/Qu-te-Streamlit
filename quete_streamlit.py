import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import streamlit.components.v1 as components




link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

df_cars['continent_fact'] = df_cars['continent'].factorize()[0]


# st.set_page_config(layout='wide')

# Titre principale
#components.html("<body style='color:white;font-family:verdana; font-size:60px; border: 2px solid white; text-align: center; padding: 1px'><b>Cinéma Le Creusois</b></body>")
st.markdown('<style>' + open('style.css').read() +
            '</style>', unsafe_allow_html=True)
st.markdown('<body class="title">Streamlit : build and share data apps</body>',
            unsafe_allow_html=True)

st.sidebar.title("Bonjour :racing_car: :car:")

choice = st.sidebar.selectbox("", ('Analyse descriptive', "Analyse des corrélations"))

# Création Sidebar avec les différents choix
liste_pays = df_cars['continent'].unique().tolist()
liste_pays.insert(0, 'Tous')

st.title('')
st.title('')

choix_pays = st.sidebar.radio('Select countries', liste_pays)
#choix_pays = st.selectbox('Select a continent :', liste_pays)

if choice == 'Analyse descriptive':

    if choix_pays != 'Tous':

        df_cars = df_cars[df_cars['continent'] == choix_pays]


    st.subheader('')

    st.markdown("<body class='p3'>Quelques graphiques pour l'analyse descriptive :</body>",
                    unsafe_allow_html=True)
    st.title('')

    


    fig4 = px.pie(df_cars, values='year', names='continent', color='continent',color_discrete_map={'US.':'lightcyan',
                                 'Japan.':'cyan',
                                 'Europe.':'royalblue'})
    fig4.update_layout(title_text="<b>Répartition des modèles par continent",
                       title_x=0.5, title_font_family="Verdana")
    st.write(fig4)
    st.markdown("<body class='p4'>Près de 2/3 des modèles du dataset proviennent des Etats-Unis.</body>",
                    unsafe_allow_html=True)
    st.header('')

    fig3 = px.histogram(df_cars, x="year", color="continent", color_discrete_map={'US.':'lightcyan',
                                 'Japan.':'cyan',
                                 'Europe.':'royalblue'})
    fig3.update_layout(title_text="<b>Répartition des modèles par années",
                        title_x=0.5, title_font_family="Verdana")
    fig3.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)',
                            'paper_bgcolor': 'rgba(0,0,0,0)'})
    fig3.update_xaxes(showgrid=False, gridwidth=1,
                       gridcolor='black', linecolor='rgba(0,0,0,0)')
    fig3.update_yaxes(showgrid=False, gridwidth=1,
                        gridcolor='black', linecolor='rgba(0,0,0,0)')
    fig3.update_xaxes(title_text="<b>Années")
        #fig8.update_yaxes(title_text="<b>Distance par gallon")
    st.write(fig3)

    fig1 = px.box(df_cars, x="weightlbs", color="continent", color_discrete_map={'US.':'lightcyan',
                                 'Japan.':'cyan',
                                 'Europe.':'royalblue'})
    fig1.update_layout(title_text="<b>Répartition des modèles par poids",
                        title_x=0.5, title_font_family="Verdana")
    fig1.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)',
                            'paper_bgcolor': 'rgba(0,0,0,0)'})
    fig1.update_xaxes(showgrid=False, gridwidth=1,
                       gridcolor='black', linecolor='rgba(0,0,0,0)')
    fig1.update_yaxes(showgrid=False, gridwidth=1,
                        gridcolor='black', linecolor='rgba(0,0,0,0)')
    fig1.update_xaxes(title_text="<b>Poids")
        #fig8.update_yaxes(title_text="<b>Distance par gallon")
    st.write(fig1)

    st.title('')

    fig2 = px.box(df_cars, x="hp", color="continent", color_discrete_map={'US.':'lightcyan',
                                 'Japan.':'cyan',
                                 'Europe.':'royalblue'})
    fig2.update_layout(title_text="<b>Répartition des modèles par puissance",
                        title_x=0.5, title_font_family="Verdana")
    fig2.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)',
                            'paper_bgcolor': 'rgba(0,0,0,0)'})
    fig2.update_xaxes(showgrid=False, gridwidth=1,
                        gridcolor='black', linecolor='rgba(0,0,0,0)')
    fig2.update_yaxes(showgrid=False, gridwidth=1,
                        gridcolor='black', linecolor='rgba(0,0,0,0)')
    fig2.update_xaxes(title_text="<b>Puissance (cv)")
        #fig8.update_yaxes(title_text="<b>Distance par gallon")
    st.write(fig2)


    st.markdown("<body class='p4'>Sans surprise, les modèles US sont dans une catégorie à part avec des poids et des puissances beaucoup plus importants que les modèles japonais ou européens.</body>",
                    unsafe_allow_html=True)
    

if choice == 'Analyse des corrélations':

    if choix_pays != 'Tous':

        df_cars = df_cars[df_cars['continent'] == choix_pays]

    st.subheader('')
    st.markdown('<body class="p3">Heatmap de corrélation :</body>',
                    unsafe_allow_html=True)
    st.header('')
    fig, axes = plt.subplots(figsize=(12, 5))
    sns.heatmap(df_cars.corr(), annot=True, cmap="YlGnBu")
    sns.set(rc={'figure.facecolor': 'white'})
    st.write(fig)
    st.write("A la lecture de ce heatmap, 4 variables sont fortement corrélées (hp, weightlbs, cylinders, cubicinches). Nous allons nous intéresser à d'autres corrélations ici.")
    st.title('')

    st.markdown("<body class='p3'>Quelques analyses de corrélation :</body>",
                unsafe_allow_html=True)
    st.title('')
    fig7 = px.scatter(df_cars, x="time-to-60",
                    y="hp", trendline="ols", color="continent", color_discrete_map={'US.':'lightcyan',
                                 'Japan.':'cyan',
                                 'Europe.':'royalblue'})
    fig7.update_layout(title_text="<b>Corrélation entre l'accélération et la puissance",
                    title_x=0.5, title_font_family="Verdana")
    fig7.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)',
                        'paper_bgcolor': 'rgba(0,0,0,0)'})
    fig7.update_xaxes(showgrid=False, gridwidth=1,
                    gridcolor='black', linecolor='rgba(0,0,0,0)')
    fig7.update_yaxes(showgrid=False, gridwidth=1,
                    gridcolor='black', linecolor='rgba(0,0,0,0)')
    fig7.update_xaxes(title_text="<b>Temps (sec)")
    fig7.update_yaxes(title_text="<b>Puissance")
    st.write(fig7)
    st.write('Plus le modèle est puissant, plus la durée pour atteindre les 60 miles est faible')

    st.title('')
    fig8 = px.scatter(df_cars, x="year",
                    y="mpg", trendline="ols", color="continent", color_discrete_map={'US.':'lightcyan',
                                 'Japan.':'cyan',
                                 'Europe.':'royalblue'})
    fig8.update_layout(title_text="<b>Corrélation entre la consommation et l'année de fabrication",
                    title_x=0.5, title_font_family="Verdana")
    fig8.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)',
                        'paper_bgcolor': 'rgba(0,0,0,0)'})
    fig8.update_xaxes(showgrid=False, gridwidth=1,
                    gridcolor='black', linecolor='rgba(0,0,0,0)')
    fig8.update_yaxes(showgrid=False, gridwidth=1,
                    gridcolor='black', linecolor='rgba(0,0,0,0)')
    fig8.update_xaxes(title_text="<b>Années")
    fig8.update_yaxes(title_text="<b>Distance par gallon")
    st.write(fig8)
    st.write("La distance parcourue par gallon ne cesse d'augmenter au fil du temps soit une baisse de la consommation des véhicules")
    st.title('')

