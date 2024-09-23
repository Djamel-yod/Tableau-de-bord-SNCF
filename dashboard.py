from dash import Dash, html, dcc, Input, Output, State
import plotly.express as px
import pandas as pd
from itertools import chain



import dash_bootstrap_components as dbc
import dash_html_components as html


from urllib.request import urlopen
import json
import numpy as np
import plotly.express as px


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB,
                                           dbc.icons.BOOTSTRAP])
server= app.server

# Chargement des données
data=pd.read_csv("data.csv",sep=";")



""" 
          Prétraitement des données et tracé de la carte:
          Cette carte est la repartitions du nombre d'incidents par régions.
"""

# Remplacer les abréviations de certaines régions par leurs noms
data["Région"].replace(["RA","B","N","IdF"],["Auvergne-Rhône-Alpes","Bretagne","Normandie","Île-de-France"],inplace=True)

# Compter le nombre d'incidents dans chaque régions
df_counts=data["Région"].value_counts()

# Création d'un dataframe avec pour colonnes les régions et le nombre d'incidents
dict={"Région": df_counts.index.tolist(), "Nombre d'incidents":df_counts.values.tolist()}
df_inc = pd.DataFrame(dict)

# Ajout de la Corse qui n'existe pas dans les données de base. On va lui affecter la valeur 0
df_inc.set_index("Région",inplace=True)
df_inc.loc["Corse"] = 0
df_inc.reset_index(inplace=True)

# Récupération des données géographiques
with urlopen('https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/regions-version-simplifiee.geojson') as response:
    geojson = json.load(response)
df_geo = pd.DataFrame([x['properties'] for x in geojson['features']])

# Jointure des deux dataframes en utilisant la région comme clé (df des données brutes et df des coordonées géographiques des villes)
df_final=df_geo.merge(df_inc,left_on="nom",right_on="Région")
df_final=df_final[["nom","code","Nombre d'incidents"]]
df_final['randNumCol'] = np.random.randint(0, 10, df_final.shape[0]).astype('str')

# Figure
fig1 = px.choropleth_mapbox(df_final, geojson=geojson, featureidkey='properties.nom', locations='nom',
                        color="Nombre d'incidents", range_color=(0,41), center = {"lat":47, "lon":2},
                        zoom=4.5, mapbox_style="carto-positron",
                        opacity=0.5, labels={'nom':'Région'})

fig1.update_layout(mapbox_style="open-street-map",
                  showlegend=False,
                  margin={"r":0,"t":0,"l":0,"b":0},
                  width=600,
                  height=400,
                  )


""" 
          Prétraitement des données et tracé du graphique en bar qui sera la repartion des incidents
          suivant leurs origines:
"""

# Compter le nombre d'incidents dans chaque régions
df_counts_origin=data["Origine"].value_counts()

# Création d'un dataframe avec pour colonnes les régions et le nombre d'incidents
dict={"Origine": df_counts_origin.index.tolist(), "Nombre d'incidents":df_counts_origin.values.tolist()}
df_counts_origin = pd.DataFrame(dict)


# Tracer la Repartition des incidents en fonction de leurs origines
fig2=px.bar(df_counts_origin, x='Origine', y="Nombre d'incidents", color="Origine")
fig2.update_xaxes(showticklabels=False, title_text=None)
fig2.update_layout(
    title_text=None,
    yaxis_title="Nombre d'incidents",
)


""" 
          Prétraitement des données et tracé du graphique en camembert qui sera la repartion des incidents
          suivant le niveau de gravité:
"""

# Création d'un dataframe avec pour colonnes les régions et le nombre d'incidents
df_counts_gravite=data["Gravité EPSF"].value_counts()
dict3={"Gravité": df_counts_gravite.index.tolist(), "Nombre d'incidents": df_counts_gravite.values.tolist()}
df_counts_gravite=pd.DataFrame(dict3)

# Figure de la repartition des incidents par gravité

fig3= px.pie(df_counts_gravite, values="Nombre d'incidents", names="Gravité", hole=0.3)



""" 
          Prétraitement des données et tracé du graphique temporel au fil des mois de la gravité des incidents:
"""


df_counts_date=data["Date"].value_counts()
dict3={"Date": df_counts_date.index.tolist(), "Nombre d'incidents": df_counts_date.values.tolist()}
df_counts_date=pd.DataFrame(dict3)

df_counts_date['Date'] = pd.to_datetime(df_counts_date['Date'])

# Calcul de la somme des incidents par mois
incidents_par_mois = df_counts_date.groupby(df_counts_date['Date'].dt.month)['Nombre d\'incidents'].sum()


# Les labels de tout les mois de Janvier à Décembre

month_labels = ["Janvier", "Février", "Mars", "Avril", "Mai",
               "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]


""" On constate que ce n'est pas tout les mois qui existe dans notre dataframe: Les mois vont de janvier à Aout.
    Il est donc probable qu'il n'yai pas eu d'incidents de Septembre à Décembre. N'ayant pas les moyens 
    de le vérifier, Nous allons considérer qu'il n'ya pas eu d'incidents ces mois.
"""

# Considérons que incidents_par_mois.index contient les mois existant dans notre dataframe

# Créer un vecteur contenant tout les mois
all_months = set(range(1, 13))

# Différence entre le nombre de mois existant et le nombre de mois dans l'année
missing_months = all_months.difference(incidents_par_mois.index)

# Créer un serie d'index pour les mois inexistants
missing_months_index = pd.Index(missing_months)

# Concatener les deux serie  d'index (mois existant et inexistant)
new_index = incidents_par_mois.index.union(missing_months_index)

# Fill missing month values with 0 (or a different default value)
incidents_par_mois = incidents_par_mois.reindex(new_index, fill_value=0)

incidents_par_mois.index=month_labels

fig4=px.line(df_counts_date, x=incidents_par_mois.index, y=incidents_par_mois.values)
fig4.update_layout(
    title_text=None,
    yaxis_title="Nombre d'incidents",
    xaxis_title="Mois"
)



"""
Carte du nombre total d'incidents
"""

total_incidents= len(data["Nature"])



app.layout = dbc.Container([
    
    dbc.Row([
        dbc.Col(html.H1("Dashboard Analytique des Incidents de sécurité à la SNCF en 2023", 
                        style={"textAlign":"center", "text-decoration-color": "#007bff","color": "blue",
                               "textShadow": "2px 2px 4px #000", "fontSize": "48px", "backgroundColor": "White"}
                        
                        ), width=14,), 
            
            ],  style={'margin-bottom': '50px'}),
 
    
    dbc.Row([
        
        dbc.Col([
        dbc.Card(
    dbc.CardBody(
        [
            html.H3([html.I(className="bi bi-train-front me-2"),
                     "Total Incidents"], className="text-nowrap", style={"textAlign":"center"}),
            html.H1(total_incidents, style={"textAlign":"center", "color": "red"})
        ], className="border-start border-success border-5", style={"background-color": "yellow"},
                    ), 
    
                    ),
                ], width=5, className="four columns"),
        
        
        dbc.Col([ dbc.Card([
            
                dcc.Graph(figure=fig1),
                
                ], style={'border': '0'})
               
                
                ], width=3, className="twelve columns"),
        
        
         
            ]),
    
    
    dbc.Row([
    dbc.Col([
        dcc.Graph(figure=fig2)
    ], className="four columns"),

    dbc.Col([
        dcc.Graph(figure=fig3)
    ], className="four columns"),
    
            ]),



        ])

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port='8080')

