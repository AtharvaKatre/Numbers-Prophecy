import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import requests
from bs4 import BeautifulSoup
import random

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table

# nltk.download('brown')
# nltk.download('indian')
# nltk.download('gutenberg')

#-------------------------------------------BENFORD'S LAW--------------------------------------------------------------------------------------------
# covid cases
covid_cases = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv').drop(['Date','Country','Recovered','Deaths'],axis=1)
covid_cases['Confirmed']=covid_cases[covid_cases['Confirmed']!=0]
covid_cases.dropna(inplace=True)
covid_table = pd.DataFrame({'Total Records':[len(covid_cases)],'Maximum Value':[covid_cases['Confirmed'].max()],'Minimum Value':[covid_cases['Confirmed'].max()],'Order of Magnitude':[len(str(covid_cases['Confirmed'].max()))-len(str(covid_cases['Confirmed'].min()))]})

covid_cases = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/covid_cases.csv')

# Eathquake depths
earthquake_depths = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/earthquake_depths.csv')
earthquake_depths_table = pd.DataFrame({'Total Records':[earthquake_depths['count'].sum()],'Maximum Value':'NA','Minimum Value':'NA','Order of Magnitude':'2'})

# highways length
highways = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/highways.csv')
highways_table = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/highways_table.csv')

# area of countries
country_area = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/country_area.csv')
country_area_table = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/country_area_table.csv')

# stars distance
stars_distance = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/stars_distance.csv')
stars_distance_table = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/stars_distance_table.csv')

#pornhub views
porn_views = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/porn_views.csv')
porn_views_table = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/porn_views_table.csv')

# population of countries
countries_population = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/countries_population.csv')
countries_population_table = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/countries_population_table.csv')

# mass of exoplanets
exoplanet_mass = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/exoplanet_mass.csv')
exoplanet_mass_table = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/exoplanet_mass_table.csv')

# runs scored
cricket_runs = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/cricket_runs.csv')
cricket_stats_table = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/cricket_stats_table.csv')

# deaths due to terrorism
terrorism_deaths = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/terrorism_deaths.csv')
terrorism_deaths_table = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/terrorism_deaths_table.csv')

# movies revenue
movie_revenue = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/movie_revenue.csv')
movie_revenue_table = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/movie_revenue_table.csv')

# moon craters
moon_craters = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/moon_craters.csv')
moon_craters_table = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/moon_craters_table.csv')

# fibonacci series
fibonacci_list = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/fibonacci_list.csv')
fibonacci_list_table = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/fibonacci_list_table.csv')

# deaths due to natural disasters
disasters_deaths = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/disasters_deaths.csv')
disasters_deaths_table = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/disasters_deaths_table.csv')

# infectious disease
global_diseases = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/global_diseases.csv')
global_diseases_table = pd.DataFrame({'Total Records':[global_diseases['count'].sum()],'Maximum Value':'NA','Minimum Value':'NA','Order of Magnitude':'6'})

# sunni muslims
sunni_muslims = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/sunni_muslims.csv')
sunni_muslims_table = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/sunni_muslims_table.csv')

# damage due to disasters
disasters_damage = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/disasters_damage.csv')
disasters_damage_table = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/disasters_damage_table.csv')

def onload_benfordfig():
    fig = go.Figure()
    fig.add_trace(
        go.Bar(x=covid_cases['Digits'], y=covid_cases['count'], text=covid_cases['percentage'], showlegend=False,
               name='', marker_color='yellow'))
    fig.update_layout(xaxis=dict(
        type='category',
        categoryarray=['1', '2', '3', '4', '5', '6', '7', '8', '9'],

    ), yaxis=dict(showgrid=False))
    fig.update_traces(textposition='outside')
    fig.add_trace(
        go.Scatter(x=covid_cases['Digits'], y=covid_cases['benford count'], name="Predicted by<br>Benford's Law",
                   mode="lines+markers", hoverinfo='skip', marker_symbol='circle', marker_size=6,
                   marker_line_width=2, ))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(yaxis_title='Leading Digit Frequency',
                      xaxis_title="Leading Digits<br><br>Data Source : <a href='https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'>Covid-19 Data</a>",
                      title='Count of daily Covid-19 Cases<br>around the World', title_x=0.5, template='plotly_dark',
                      showlegend=True)
    fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.99
    ))
    fig.layout.xaxis.fixedrange = True
    fig.layout.yaxis.fixedrange = True
    return fig

# dict of benford datasets
benford_datasets = {'Count of daily Covid-19 cases worldwide':1,'Depth of Earthquakes globally in km':2,'Length of Highways in India':3,'Total Area of Countries in km²':4,'Distance of Stars from Earth in light years':5,'Views count on Pornhub':6,'Population of Countries':7,'Mass of Exoplanets in Earth mass':8,'Runs scored by Batsmen in Test Cricket':9,'People killed by Terrorism':10,'Revenue generated by Movies in $US':11,"Diameter of Moon's craters in km":12,'First 1000 Fibonnaci numbers':13,'Deaths due to Natural Disasters':14,'Count of  Global Infectious Disease cases':15,'Number of Sunni Muslims per country':16,'Damage suffered due to Natural Disasters globally in $US':17}

# -----------------------------------------------ZIPF'S LAW-----------------------------------------------------------------------------------
# brown corpus
# word_count = len(brown.words())
browncorpus = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/browncorpus.csv')

# marathi corpus
# marathi_word_count = len(nltk.corpus.indian.words('marathi.pos'))
marathi_corpus = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/marathi_corpus.csv')

# bible corpus
# bible_word_count = len(nltk.corpus.gutenberg.words('bible-kjv.txt'))
bible_corpus = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/bible_corpus.csv')

# surnames
surnames = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/surnames.csv')

# cities area
city_area = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/city_area.csv')

# dog victim's age
dog_attack = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/dog_attack.csv')

# on load zipf figure
def onload_zipffig():
    fig = go.Figure()
    fig.add_trace(
        go.Bar(x=browncorpus['word'].head(50), y=browncorpus['count'].head(50), text=browncorpus['percentage'].head(50),
               name='<extra></extra> ', hoverinfo='x+y+text', showlegend=False, marker_color='yellow'))
    fig.update_layout(yaxis=dict(showgrid=False))
    fig.update_traces(textposition='outside')
    fig.add_trace(
        go.Scatter(x=browncorpus['word'].head(50), y=browncorpus['zipf_dist'].head(50), name="Zipfian Distribution",
                   mode="lines+markers", hoverinfo='skip', marker_symbol='circle', marker_size=6,
                   marker_line_width=2, ))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(yaxis_title='No. of Occurences',
                      xaxis_title="<br>Data Source : <a href='https://en.wikipedia.org/wiki/Brown_Corpus'>Brown Corpus</a>",
                      title='Top 50 Most Common Words<br>in the English Language', title_x=0.5, template='plotly_dark',
                      showlegend=True)
    fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.99
    ))
    fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    fig.layout.xaxis.fixedrange = True
    fig.layout.yaxis.fixedrange = True
    return fig

# random book
book_num = random.randint(1, 64602)  # 64602 is the total number of books available through the website
url = "http://www.gutenberg.org/files/64446/64446-0.txt"
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser", )
# while str(soup).split()[0] == "<!DOCTYPE":
#     book_num = random.randint(1, 64602)
#     url = "http://www.gutenberg.org/files/{}/{}-0.txt".format(book_num, book_num)
#     res = requests.get(url)
#     soup = BeautifulSoup(res.content, "html.parser", )
url2 = "http://www.gutenberg.org/ebooks/{}".format(book_num)
res2 = requests.get(url2)
soup2 = BeautifulSoup(res2.content, "html.parser")
book_title = soup2.find("h1", itemprop="name").text
book_words = pd.DataFrame(str(soup).lower().split(), columns=['word'])
book_word_count = len(book_words)
book_words['word'] = book_words['word'].apply(lambda x: None if x in [",",".","``","''",";","?","--","(",")",":","!",'''"''',"'"] else x)
book_words.dropna(inplace=True)
book_words['word'] = book_words['word'].apply(lambda x: x.lower() if x != "I" else x)
book_words = book_words['word'].value_counts().head(50).rename('count').rename_axis('word').reset_index()
book_words['percentage'] = book_words['count'].apply(lambda x: str(round((x / book_word_count) * 100, 2)) + "%")
zipf_dist = []
for i in range(1, len(book_words) + 1):
    zipf_dist.append(int(book_words['count'][0] / i))
book_words['zipf_dist'] = zipf_dist
book_words.index = range(1, len(book_words) + 1)
random_book_table = pd.DataFrame(range(0,11),columns=['Rank'])
random_book_table[['Word','Count','Percentage']] = book_words[['word', 'count', 'percentage']].head(10)
random_book_table.drop(random_book_table.head(1).index,inplace=True)

# random book fig
def onload_random_book():
    fig = go.Figure()
    fig.add_trace(
        go.Bar(x=book_words['word'], y=book_words['count'], text=book_words['percentage'], name='<extra></extra> ',
               showlegend=False, marker_color='yellow'))
    fig.update_layout(yaxis=dict(showgrid=False))
    fig.update_traces(textposition='outside', textfont=dict(color='white'))
    fig.add_trace(
        go.Scatter(x=book_words['word'], y=book_words['zipf_dist'], name="Zipfian Distribution", mode="lines+markers",
                   hoverinfo='skip', marker_symbol='circle', marker_size=6, marker_line_width=2, ))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(yaxis_title='No. of Occurences',
                      xaxis_title="<br>Data Source : <a href='http://www.gutenberg.org/'>Gutenberg Project</a>",
                      title='Top 50 Most Common Words in<br>' + book_title, title_x=0.5, template='plotly_dark',
                      showlegend=True)
    fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.99
    ))
    fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    fig.layout.xaxis.fixedrange = True
    fig.layout.yaxis.fixedrange = True
    return random_book_table.to_dict('records'),fig

# dict of zipf datasets
zipf_datasets = {'Most Common Words in the English Language':1,'Most Common Words in the Marathi Language':2,'Most Common Words in the English Bible':3,'Most Common Surnames in the US':4,'Top Cities by Area':5,"Victim's Age in Dog Attacks (upto 10 years old)":6}

# ---------------------------------------------BREVITY LAW--------------------------------------------------------------------------------------------
# browncorpus2
browncorpus2 = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/browncorpus2.csv')

# onload brevity fig
def onload_brevity_fig():
    fig = px.scatter(browncorpus2, x=browncorpus2.index, y='count', color='word size',
                     hover_data=['word'])
    fig.update_layout(yaxis=dict(showgrid=False), xaxis=dict(showgrid=False))
    fig.update_traces(marker=dict(size=12,
                                  symbol='circle',
                                  line=dict(width=1, color='black')),
                      selector=dict(mode='markers'))
    fig.update_layout(yaxis_title='No. of Occurences',
                      xaxis_title="Word Rank<br><br>Data Source : <a href='https://en.wikipedia.org/wiki/Brown_Corpus'>Brown Corpus</a>",
                      title='Top 250 Most Common Words<br>in the English Language', title_x=0.5, template='plotly_dark',
                      showlegend=True)
    fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.99
    ),legend_title_text=None)
    fig.update_layout(
        xaxis=dict(
            tickmode='linear',
            tick0=0,
            dtick=50
        )
    )
    fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    fig.layout.xaxis.fixedrange = True
    fig.layout.yaxis.fixedrange = True
    return fig

def onload_brevity_fig_log_log():
    fig = px.scatter(browncorpus2, x=browncorpus2.index, y='count', color='word size',
                     hover_data=['word'])
    fig.update_layout(yaxis=dict(showgrid=False), xaxis=dict(showgrid=False))
    fig.update_traces(marker=dict(size=12,
                                  symbol='circle',
                                  line=dict(width=1, color='black')
                                  ),
                      selector=dict(mode='markers'))
    fig.update_xaxes(type="log")
    fig.update_yaxes(type="log")
    fig.update_layout(yaxis_title='No. of Occurences',
                      xaxis_title="<br>Data Source : <a href='https://en.wikipedia.org/wiki/Brown_Corpus'>Brown Corpus</a>",
                      title='Top 250 Most Common Words<br>in the English Language', title_x=0.5,
                      template='plotly_dark', showlegend=True)
    fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.99
    ),legend_title_text=None)
    fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    fig.layout.xaxis.fixedrange = True
    fig.layout.yaxis.fixedrange = True
    return fig
# ------------------------------------------Titius–Bode law---------------------------------------------------------------------------------------
# planet distance
planets_distance = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/planets_distance.csv')

# onload t-b graph
def onload_tb_graph():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=planets_distance['Planet'], y=planets_distance['T–B rule distance (AU)'],
                             name="T-B Rule Prediction", mode="lines", hoverinfo='skip', line_width=2,
                             line_color='orange'))
    fig.add_trace(go.Scatter(x=planets_distance['Planet'], y=planets_distance['Semimajor axis (AU)'], name='Planet',
                             hoverinfo='y', text=planets_distance['Planet'], mode='markers+text',
                             marker_color='yellow'))
    fig.update_traces(textposition='top center')
    fig.update_layout(xaxis=dict(showgrid=False))
    fig.update_layout(yaxis=dict(showgrid=False))
    fig.update_yaxes(type='linear')
    fig.update_traces(marker=dict(size=16,
                                  symbol='octagon-dot',
                                  line=dict(width=1, color='black')
                                  ),
                      selector=dict(mode='markers+text'))
    fig.update_layout(yaxis_title='Mean Distance from Sun (AU - Astronomical Distance)',
                      xaxis_title="<br>Data Source : <a href='https://en.wikipedia.org/wiki/Titius–Bode_law'>Wikipedia</a>",
                      title='Eight planets, Ceres and Pluto versus<br>the predicted distances by Titius–Bode law.',
                      title_x=0.5, template='plotly_dark', showlegend=True)
    fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    fig.layout.xaxis.fixedrange = True
    fig.layout.yaxis.fixedrange = True
    return fig

# ------------------------------------------------MOORE'S LAW----------------------------------------------------------------------------------------

# microprocessor
transistor_mp = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/transistor_mp.csv')

# GPU
transistor_gpu = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/transistor_gpu.csv')

# RAM
transistor_ram = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/transistor_ram.csv')

# Flash memory
transistor_flash = pd.read_csv('https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/DFs/transistor_flash.csv')

def onload_moore_graph():
    fig = px.scatter(transistor_mp, x='Date', y='transistor count', hover_data=transistor_mp.columns,
                     color='Designer')
    fig.update_layout(yaxis=dict(showgrid=False), xaxis=dict(showgrid=False))
    fig.update_yaxes(type="log")
    fig.update_traces(marker=dict(size=12,
                                  symbol='diamond-tall-dot',
                                  line=dict(width=1, color='black')
                                  ),
                      selector=dict(mode='markers'))
    fig.update_layout(yaxis_title='Count',
                      xaxis_title="<br>Data Source : <a href='https://en.wikipedia.org/wiki/transistor_count'>Wikipedia</a>",
                      title='Number of MOS Transistors on<br>Microprocessor (1971 - 2020)', title_x=0.5,
                      template='plotly_dark')
    fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    fig.layout.xaxis.fixedrange = True
    fig.layout.yaxis.fixedrange = True
    return fig

# dict of moore datasets
moore_datasets = {'Number of MOS Transistors on Microprocessor':1,'Number of MOS Transistors on GPU':2,'Number of MOS Transistors on RAM':3,'Number of MOS Transistors on Flash Memory':4}

# stigler df
stigler_df = pd.read_csv("https://raw.githubusercontent.com/AtharvaKatre/Numbers-Prophecy/main/assets/datasets/Stigler's%20law.csv")

# -------------------------------------------------DASH APP----------------------------------------------------------------------------------------
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY],meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])
server = app.server

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <meta name="description" content="An online experiment to demonstrate the biases and predictability of our world">
        <meta name="keywords" content="numbers, number, prophecy, benford, law, laws, zipf, zipf's law, brevity, brevity law, bode, bode's law, moore, moore's law, Stigler's law of Eponymy, what is random, what is not random, predictability, biases, empirical law, scientific laws, prediction, data sets, natural datasets,">
        <meta name="author" content="Atharva Katre">
        <title>{%title%}Numbers Prophecy</title>
        <script data-ad-client="ca-pub-5006482200117782" async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
        {%favicon%}
        {%css%}
        <style>
        .coffee-container {
          position: relative;
        }
        .coffee-center {
          margin: 0;
          position: absolute;
          top: 50%;
          left: 50%;
          -ms-transform: translate(-50%, -50%);
          transform: translate(-50%, -50%);
        }
        </style>
    </head>
    <body>
        {%app_entry%}
        <br>
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        <div class="coffee-container">
        <div class="coffee-center">
        <script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="AtharvaKatre" data-color="#FFDD00" data-emoji="" data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" data-align='center'></script>
        </div>
        </div>
        <br>
        <br>
        </footer>
    </body>
</html>
'''

app.title = ''

# ----------------------------APP Components----------------------------------------------

tab1 = html.Div([
    html.Br(),
    dbc.Row(html.H3("Benford's Law"),style={'font-family':'Times','color':'Yellow','text-decoration':'underline'}),
    html.Br(),
    dbc.Row(html.H5('Imagine a large dataset, say something like a list of every country and its population.'),style={'color':'#b4b4b4','padding-left':'20px','textAlign':'left'}),
    dbc.Table([html.Thead(html.Tr([html.Th("Country"), html.Th("Popultion")]))] + [html.Tbody([
                                        html.Tr([html.Td("Afghanistan"), html.Td([html.Span("3",style={'color':'white'}),"8,041,754"])]),
                                        html.Tr([html.Td("Albania"), html.Td([html.Span("2",style={'color':'white'}),",880,917"])]),
                                        html.Tr([html.Td("Algeria"), html.Td([html.Span("4",style={'color':'white'}),"3,053,054"])]),
                                        html.Tr([html.Td("Andorra"), html.Td([html.Span("7",style={'color':'white'}),"7,142"])]),
                                        html.Tr([html.Td(""), html.Td("↑ Leading Digit",style={'color':'yellow'})]),
                                     ],style={'color':'grey'})],bordered=False,style={'textAlign':'left','width':'50%'}
              ),
    dbc.Row(html.H5(['Chances are, the leading digit will be a ',html.Span('1',style={'color':'white'}),' more often than a ',html.Span('2',style={'color':'white'}),'. And ',html.Span('2',style={'color':'white'}),'s would probably occur more often than ',html.Span('3',style={'color':'white'}),'s, and so on.'],style={'color':'#b4b4b4','padding-left':'20px','textAlign':'left'})),
    dbc.Row(html.H5(["This odd phenomenon is Benford's Law, also called the first digit law. If a set of values were truly random, each leading digit would appear about ",html.Span('11%',style={'color':'white'})," of the time, but Benford's Law predicts a logarithmic distribution. This phenonmenon occurs so regularly that it is even used in fraudulent accounting detection."],style={'color':'#b4b4b4','padding-left':'20px','textAlign':'left'})),
    html.Br(),
    dbc.Row(
            html.Div([
                    dbc.Col(html.H5("Select from the available datasets"),style={'text-align':'left','padding':'0'}),
                    dcc.Dropdown(
                        id='benford dropdown',
                        options=[{'label': key, 'value': value} for key,value in benford_datasets.items()],style={'color':'black','textAlign':'left'},
                        value=1,
                        searchable=False,
                        optionHeight=55,
                        clearable=False,
                    ),
                ],style={'width': '80%', 'display': 'inline-block','padding-left':'20px'}
            )
    ),
    html.Br(),
    html.Br(),
    html.Div([
        dash_table.DataTable(
            id='benford table',
            columns=[{"name": i, "id": i} for i in covid_table.columns],
            data=covid_table.to_dict('records'),
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
                style_cell={
                    'whiteSpace': 'normal',
                    'height': 'auto',
                    'textAlign': 'left',
                    'backgroundColor': 'rgb(50, 50, 50)',
                    'color': 'white'
                },
            style_table={'width':'60%'},
        )
    ],className='center'),
    html.Br(),
    dbc.Row([
        dbc.Col(
            html.Div([
                dcc.Loading(
                    children=[dcc.Graph(
                                id="benford graph",
                                figure = onload_benfordfig(),
                                config = {'displaylogo': False}
                                )
                            ],color='yellow'
                )
            ])
        )
    ], no_gutters=True, justify='center'),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.H5('References :',style={'textAlign':'left',}),
            html.Ul(html.Li(html.A(["Number 1 and Benford's Law - Numberphile (Youtube) ",html.Span("(Must Watch)",style={'color':'white'})],href='https://youtu.be/XXjlR2OK1kM',target="_blank"),style={'textAlign':'left'})),
            html.Ul(html.Li(html.A("Benford's law in the natural sciences",href='https://agupubs.onlinelibrary.wiley.com/share/M8RKM777RDKY8DIVY4DG?target=10.1029/2010GL044830',target="_blank"),style={'textAlign':'left'})),
            html.Ul(html.Li(html.A("Why do Joe Biden's votes not follow Benford's Law? (Youtube)",href='https://youtu.be/etx0k1nLn78',target="_blank"),style={'textAlign':'left'})),
            html.Ul(html.Li(html.A("What is Benford’s Law and why is it important for data science?",href='https://towardsdatascience.com/what-is-benfords-law-and-why-is-it-important-for-data-science-312cb8b61048',target="_blank"),style={'textAlign':'left'})),
        ])
    ]),
], className='ml-5 mr-5 mt-4')

tab2 = html.Div([
    html.Br(),
    dbc.Row(html.H3("Zipf's Law"), style={'font-family':'Times','color': 'Yellow', 'text-decoration': 'underline'}),
    html.Br(),
    dbc.Row(html.H5(["Named for linguist George Kingsley Zipf, who around 1935 was the first to draw attention to this phenomenon, the law examines the frequency of words in natural language and how the most common word occurs ",html.Span('twice',style={'color':'white'})," as often as the second most frequent word, ",html.Span('thrice',style={'color':'white'})," as often as the third most frequent word and so on until the least frequent word."],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
    dbc.Row(html.H5(["So the word in the position ,",html.Span('n',style={'color':'white'})," appears ",html.Span("1/n",style={'color':'white'})," times as often as the most frequent one."],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
    dbc.Row(html.H5("Zipfian distributions have been found in the population ranks of cities, solar flare intensities, corporation sizes, income rankings and ranks of the number of people watching the same TV channel and many other fields.",
        style={'color': '#b4b4b4', 'textAlign': 'left', 'padding-left': '20px'})),

    html.Br(),
    dbc.Row(
            html.Div([
                dbc.Col(html.H5("Select from the available datasets"), style={'text-align': 'left', 'padding': '0'}),
                dcc.Dropdown(
                            id='zipf dropdown',
                            options=[{'label': key, 'value': value} for key,value in zipf_datasets.items()],style={'color':'black','textAlign':'left'},
                            value=1,
                            searchable=False,
                            clearable=False,
                            optionHeight=55,
                        ),
                    ],
                    style={'width': '80%', 'display': 'inline-block','padding-left':'20px'}),
        ),
    dbc.Row(
            dcc.RadioItems(
                id='zipf radio',
                options=[
                    {'label': 'Linear', 'value': 'lin'},
                    {'label': 'Log - Log', 'value': 'log-log'}
                ],
                value='lin',
                labelStyle={'display': 'inline-block','padding':'10px'}
            ),style={'padding-left':'20px'}
    ),
    dbc.Row([
            dbc.Col(
                html.Div([
                    dcc.Loading(
                    children=[dcc.Graph(
                                id="zipf graph",
                                figure = onload_zipffig(),
                                config = {'displaylogo': False}
                                )
                            ],color='yellow'
                )
                ])
            )
        ], no_gutters=True, justify='center'),

    html.Br(),
    html.Br(),

    dbc.Row([
        html.H5('Try it yourself!',style={'textAlign':'left','padding-left':'20px'})
        ]),

    html.Br(),

    html.H5(["Click the button below to analyze a random book from the ", html.A('Gutenberg Project',href='https://www.gutenberg.org/',target='_blank'),", an online library of 60,000 eBooks.",],style={'color':'#b4b4b4','textAlign':'left','padding-left':'20px'}),
    html.H5("You'll notice that most of the times the words follow a Zipfian distribution.",style={'color':'#b4b4b4','textAlign':'left','padding-left':'20px'}),
    html.Br(),

    html.Div([
        html.Button('Analyze a random book',id='random book',n_clicks=0),
    ],className='center'),

    html.Br(),

    dbc.Row(
                dcc.RadioItems(
                    id='random graph radio',
                    options=[
                        {'label': 'Linear', 'value': 'lin'},
                        {'label': 'Log - Log', 'value': 'log-log'}
                    ],
                    value='lin',
                    labelStyle={'display': 'inline-block','padding':'10px'}
                ),style={'padding-left':'20px'}
        ),

    dbc.Row([
       dbc.Col([
           dcc.Loading(
               children=[dcc.Graph(
                                   id = 'random graph',
                                   figure = {},
                                   config = {'displaylogo': False}
                                )],type='default',color='yellow'
               )
       ]),
    ], no_gutters=True, justify='center'),

    html.Br(),

    html.Div([
                dcc.Loading(children=[dash_table.DataTable(
                    id='zipf random table',
                    columns=[{"name": i, "id": i} for i in random_book_table.columns],
                    data=random_book_table.to_dict('records'),
                    style_header={'backgroundColor': 'rgb(30, 30, 30)','fontWeight':'bold'},
                        style_cell={
                            'whiteSpace': 'normal',
                            'height': 'auto',
                            'width': 'auto',
                            'textAlign': 'left',
                            'backgroundColor': 'rgb(50, 50, 50)',
                            'color': '#b4b4b4'
                        },
                    style_table={'width':'100%'},
                )],type='default',color='yellow')
            ],className='center'
    ),

    html.Br(),
    dbc.Row([
            dbc.Col([
                html.H5('References :',style={'textAlign':'left',}),
                html.Ul(html.Li(html.A(["The Zipf Mystery - Vsauce (Youtube) ",html.Span("(Must Watch)",style={'color':'white'})],href='https://youtu.be/fCn8zs912OE',target="_blank"),style={'textAlign':'left'})),
                html.Ul(html.Li(html.A("Research article on Zipf's Law published at The Royal Society",href='https://royalsocietypublishing.org/doi/10.1098/rsif.2015.0330',target="_blank"),style={'textAlign':'left'})),
                html.Ul(html.Li(html.A("Zipf Curves and Website Popularity",href='https://www.nngroup.com/articles/zipf-curves-and-website-popularity/',target="_blank"),style={'textAlign':'left'})),
                html.Ul(html.Li(html.A("Why Zipf's law explains so many big data and physics phenomenons",href='https://www.datasciencecentral.com/profiles/blogs/why-zipf-s-law-explains-so-many-big-data-and-physics-phenomenons',target="_blank"),style={'textAlign':'left'})),
            ])
        ]),
], className='ml-5 mr-5 mt-4')

tab3 = html.Div([
    html.Br(),
    dbc.Row(html.H3("Brevity Law"), style={'font-family':'Times','color': 'Yellow', 'text-decoration': 'underline'}),
    html.Br(),
    dbc.Row(html.H5(["Also called as Zipf's law of abbreviation, it qualitatively states that the ",html.Span('more',style={'color':'white'})," frequently a word is used, the ",html.Span('shorter',style={'color':'white'})," that word tends to be, and vice versa."],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
    dbc.Row(html.H5(["As shown in the graph below a few shorter words are used more often than many other longer words."],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
    html.Br(),
    dbc.Row(
            dcc.RadioItems(
                id='brevity radio',
                options=[
                    {'label': 'Linear', 'value': 'lin'},
                    {'label': 'Log - Log', 'value': 'log-log'}
                ],
                value='lin',
                labelStyle={'display': 'inline-block','padding':'10px'}
            ),style={'padding-left':'20px'}
    ),

    dbc.Row([
            dbc.Col(
                    dcc.Loading(
                    children=[dcc.Graph(
                                id="brevity graph",
                                figure = onload_brevity_fig(),
                                config = {'displaylogo': False}
                                )
                            ],color='yellow'
                )
            )
        ], no_gutters=True, justify='center'),
    html.Br(),
    dbc.Row([
                dbc.Col([
                    html.H5('References :',style={'textAlign':'left',}),
                    html.Ul(html.Li(html.A("Brevity law - Wikipedia",href='https://en.wikipedia.org/wiki/Brevity_law',target="_blank"),style={'textAlign':'left'})),
                    html.Ul(html.Li(html.A("The Brevity Law as a Scaling Law, and a Possible Origin of Zipf’s Law for Word Frequencies",href='https://www.mdpi.com/1099-4300/22/2/224/htm',target="_blank"),style={'textAlign':'left'})),
                    html.Ul(html.Li(html.A("On the physical origin of linguistic laws and lognormality in speech",href='https://royalsocietypublishing.org/doi/10.1098/rsos.191023',target="_blank"), style={'textAlign': 'left'})),
                    html.Ul(html.Li(html.A("Pareto principle aka the 80/20 rule (related)",href='https://en.wikipedia.org/wiki/Pareto_principle',target="_blank"),style={'textAlign':'left'})),            ])
            ]),

], className='ml-5 mr-5 mt-4')

tab4 = html.Div([
    html.Br(),
    dbc.Row(html.H3("Titius–Bode Law"), style={'font-family':'Times','color': 'Yellow', 'text-decoration': 'underline'}),
    html.Br(),
    dbc.Row(html.H5(["The Titius–Bode law, first announced in 1766 by Johann Daniel Titius but was popularized only from 1772 by Johann Elert Bode is a formulaic prediction of spacing between planets in any given solar system."],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
    dbc.Row(html.H5(["The formula suggests that, extending outward, each planet should be approximately ",html.Span("twice",style={'color':'white'})," as far from the Sun as the ",html.Span("one before",style={'color':'white'}),". The hypothesis correctly anticipated the orbits of Ceres in 1801 (in the asteroid belt) and Uranus in 1781, but failed as a predictor of Neptune's orbit in 1846 and that of Pluto, which was regarded as the ninth planet when it was discovered in 1930."],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
    html.Br(),
    dbc.Row([
            dbc.Col(
                html.Div([
                    dcc.Loading(
                    children=[dcc.Graph(
                                id="t-b graph",
                                figure = onload_tb_graph(),
                                config = {'displaylogo': False}
                                )
                            ],color='yellow'
                    )
                ])
            )
    ], no_gutters=True, justify='center'),
    html.Br(),
    dbc.Row([
            dbc.Col([
                html.H5('References :',style={'textAlign':'left',}),
                html.Ul(html.Li(html.A("Titius Bode Law Explained (Youtube)",href='https://youtu.be/grkcA4AAiUY',target="_blank"),style={'textAlign':'left'})),
                html.Ul(html.Li(html.A("Bode's law - Britannica",href='https://www.britannica.com/science/Bodes-law',target="_blank"),style={'textAlign':'left'})),
                html.Ul(html.Li(html.A("Testing the Titius-Bode law on exoplanets",href='https://astrobites.org/2014/05/19/testing-the-titius-bode-law-on-exoplanets/',target="_blank"),style={'textAlign':'left'})),
            ])
    ]),
], className='ml-5 mr-5 mt-4')

tab5 = html.Div([
    html.Br(),
    dbc.Row(html.H3("Moore's Law"),style={'font-family':'Times','color': 'Yellow', 'text-decoration': 'underline'}),
    html.Br(),
    dbc.Row(html.H5(["In 1994 Intel released Intel 4004 is a 4-bit CPU, the first commercially produced microprocessor. It was also the first logic circuit integrated in one chip using MOS (metal–oxide–semiconductor) silicon gate technology. The IC had ", html.Span("2,250",style={'color':'white'})," MOS transistors. Fast forward to 2017 AMD launched EPYC Rome a 64-bit microprocessor with an astonishing ", html.Span("39.5 Billion",style={'color':'white'})," transistors."],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
    dbc.Row(html.H5(["Named after Gordan Moore, co-founder and chairman of Intel Corporation, Moore's law is the observation that the number of transistors in a dense integrated circuit (IC) ", html.Span("doubles",style={'color':'white'})," about every ",html.Span("two",style={'color':'white'})," years."],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
    dbc.Row(html.H5(["Moore's prediction has been used in the semiconductor industry to guide long-term planning and to set targets for research and development, thus functioning a bit like a self-fulfilling prophecy."],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
    dbc.Row(html.H5(["However, over the decades, some, including Moore himself at times, fretted that they could see the ",html.Span("end",style={'color':'white'})," in sight, as it got harder to make smaller and smaller transistors."],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),

    html.Br(),
        dbc.Row(
                html.Div([
                        dbc.Col(html.H5("Select from the available datasets"),style={'text-align':'left','padding':'0'}),
                        dcc.Dropdown(
                            id='moore dropdown',
                            options=[{'label': key, 'value': value} for key,value in moore_datasets.items()],style={'color':'black','textAlign':'left'},
                            value=1,
                            optionHeight=55,
                            searchable=False,
                            clearable=False,
                        ),
                    ],style={'width': '80%', 'display': 'inline-block','padding-left':'20px'}
                )
        ),
    html.Br(),
        dbc.Row([
                    dbc.Col(
                        html.Div([
                            dcc.Loading(
                                children=[dcc.Graph(
                                            id="moore graph",
                                            figure = onload_moore_graph(),
                                            config = {'displaylogo': False}
                                            )
                            ],color='yellow'
                    )
                        ])
                    )
                ], no_gutters=True, justify='center'),
    html.Br(),
    dbc.Row([
                dbc.Col([
                    html.H5('References :',style={'textAlign':'left',}),
                    html.Ul(html.Li(html.A("Moore's Law - Explained! (Youtube)",href='https://youtu.be/CUnQNTwmHHo',target="_blank"),style={'textAlign':'left'})),
                    html.Ul(html.Li(html.A("How Does a Transistor Work? - Veritasium (Youtube)",href='https://youtu.be/IcrBqCFLHIY',target="_blank"),style={'textAlign':'left'})),
                    html.Ul(html.Li(html.A("Catching a single Transistor - Looking inside the i9-9900K: A single 14nm++ Trigate Transistor (Youtube)",href='https://youtu.be/TtuUANbaEFI',target="_blank"),style={'textAlign':'left'})),
                    html.Ul(html.Li(html.A("We’re not prepared for the end of Moore’s Law",href='https://www.technologyreview.com/2020/02/24/905789/were-not-prepared-for-the-end-of-moores-law/',target="_blank"), style={'textAlign': 'left'})),
                ])
        ]),

], className='ml-5 mr-5 mt-4')

tab6 = html.Div([
    html.Br(),
    dbc.Row(html.H3("Stigler's law of Eponymy"), style={'font-family':'Times','color': 'Yellow', 'text-decoration': 'underline', 'textAlign':'left'}),
    html.Br(),
    dbc.Row(html.H5(["This law isn't a scientific discovery or a prediction of any kind but in fact emphasises on human nature and how collaborative and complex the processes of scientific discovery really are."],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
    dbc.Row(html.H5(["Stigler's Law tells us ",html.Span('''"No scientific discovery is named after its original discoverer."''',style={'color':'white'})],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
    dbc.Row(html.H5(["Notable examples include ",html.Span("Hubble's law",style={'color':'white'}),", which was derived by Georges Lemaître two years before Edwin Hubble, the ",html.Span("Pythagorean theorem",style={'color':'white'}),", which was known to Babylonian mathematicians before Pythagoras, ",html.Span("Halley's Comet",style={'color':'white'}),", which was observed by astronomers since at least 240 BC, the ",html.Span("Arabic numerals",style={'color':'white'})," we use every day actually originated in India, and ",html.Span("all the laws mentioned on this website.",style={'color':'white'})],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
    dbc.Row(html.H5(['''The generalization is not limited to science. Stigler himself named the sociologist Robert K. Merton as the discoverer of ''',html.Span('''"Stigler's law"''',style={'color':'white'}),''' to show that it follows its own decree, though the phenomenon had previously been noted by others.'''],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
    html.Br(),
    dbc.Row(
        dbc.Col(
            html.H5("Below table list examples of Stigler's Law",style={'textAlign':'left'})
        )
    ),
    dbc.Row(
        dbc.Col(
            dash_table.DataTable(
                        data=stigler_df.to_dict('records'),
                        columns=[{'id': c, 'name': c} for c in stigler_df.columns],
                        page_size=10,
                        style_header={'backgroundColor': 'rgb(30, 30, 30)','fontWeight':'bold','textAlign':'center'},
                        style_cell={
                            'whiteSpace': 'normal',
                            'height': 'auto',
                            'width': 'auto',
                            'textAlign': 'left',
                            'backgroundColor': 'rgb(50, 50, 50)',
                            'color': '#b4b4b4'
                        },
                    )
        )
    ),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.H5('References :', style={'textAlign': 'left',}),
            html.Ul(html.Li(html.A("Stigler's law of eponymy (Wikipedia)", href='https://en.wikipedia.org/wiki/Stigler%27s_law_of_eponymy', target="_blank"),style={'textAlign': 'left'})),
            html.Ul(html.Li(html.A("Why nothing in science is ever named after its actual discoverer?", href='https://io9.gizmodo.com/stiglers-law-why-nothing-in-science-is-ever-named-afte-5820736', target="_blank"),style={'textAlign': 'left'})),
            html.Ul(html.Li(html.A("Stigler’s law and human nature", href='https://www.johndcook.com/blog/2019/01/12/stiglers-law/', target="_blank"),style={'textAlign': 'left'})),
        ])
    ]),

], className='ml-5 mr-5 mt-4')

tabs = dbc.Tabs(
    [
        dbc.Tab(tab1, label="Benford's Law", tabClassName="ml-auto mr-auto"),
        dbc.Tab(tab2, label="Zipf's Law", tabClassName="ml-auto mr-auto"),
        dbc.Tab(tab3, label="Brevity Law", tabClassName="ml-auto mr-auto"),
        dbc.Tab(tab4, label="Titius-Bode Law", tabClassName="ml-auto mr-auto"),
        dbc.Tab(tab5, label="Moore Law", tabClassName="ml-auto mr-auto"),
        dbc.Tab(tab6, label="Stigler's Law of Eponymy", tabClassName="ml-auto mr-auto"),
    ],
    card=True,
)

app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(html.H3(html.B("Numbers Prophecy"),
                               className='text-center mt-4',
                               style={'color': 'Yellow', 'text-decoration': 'None','font-family':'Times'})
                ),
    ),
    dbc.Row(
        dbc.Col(html.P(["by ",html.A("Atharva Katre",href="https://www.linkedin.com/in/atharvakatre", target='_blank', style={'color':'white','text-decoration':'underline'})],className='text-center',style={'color':'#b4b4b4'}))
        ),
    html.Br(),
    html.Br(),
    dbc.Row(
        dbc.Col(
            html.H4([html.Span('''"The universe is under no obligation to make sense to you"''',style={'color':'white'})," - Neil DeGrasse Tyson."],style={'color':'#b4b4b4'}),className='text-center'
        )
    ),
    html.Br(),
    html.Br(),
    dbc.Row(html.H4(["The world we observe and experience around us is influenced by our actions and our interactions with it. Studies have shown that human behaviour isn't random. But seriously ",html.A("What is Random?",href="https://youtu.be/9rIy0xY99a0",target='_blank',style={'text-decoration':'underline'})," and ",html.A("What is Not Random?",href='https://youtu.be/sMb00lz-IfE',target='_blank',style={'text-decoration':'underline'})],style={'color':'#b4b4b4','textAlign':'left'})),
    dbc.Row(html.H4([html.Span("Researchers have found that out that our languages, information, technological advancements and even natural phenomena follow obscure patterns. These are termed as ", style={'color':'#b4b4b4'}), html.A("Empirical Statistical Laws",href="https://en.wikipedia.org/wiki/Empirical_statistical_laws",target='_blank',style={'text-decoration':'underline'})],style={'textAlign':'left'})),
    html.Br(),
    dbc.Row(html.H4(["This is an experiment to demonstrate the ",html.Span("biases",style={'color':'white'})," and ",html.Span("predictability",style={'color':'white'})," of our world."],style={'color':'#b4b4b4','textAlign':'left'})),
    html.Br(),
    html.Br(),
    html.Br(),
    dbc.Card(tabs),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Footer([html.Span("Created by ",style={'color':'#b4b4b4'}),html.A("Atharva Katre",href="https://www.linkedin.com/in/atharvakatre",target='_blank',id="creator",style={'text-decoration':'underline','cursor': 'pointer','color':'white'})]),
    html.Br(),
],style={'textAlign': 'center','width':'85%'}, fluid=True)

# app.layout = dbc.Container([
#     dbc.Row(
#         dbc.Col(html.H3(html.B("Numbers Prophecy"),
#                                className='text-center mt-4',
#                                style={'color': 'Yellow', 'text-decoration': 'None','font-family':'Times'})
#                 ),
#     ),
#     dbc.Row(
#         dbc.Col(html.P(["by ",html.A("Atharva Katre",href="https://linktr.ee/AtharvaKatre",style={'color':'white','text-decoration':'underline'})],className='text-center',style={'color':'#b4b4b4'}))
#         ),
#     html.Br(),
#     html.Br(),
#     html.Br(),
#     dbc.Row(
#         dbc.Col(
#             html.H4([html.Span('''"The universe is under no obligation to make sense to you"''',style={'color':'white'})," - Neil DeGrasse Tyson."],style={'color':'#b4b4b4'}),className='text-center'
#         )
#     ),
#     html.Br(),
#     dbc.Row(html.H4(["But the world we observe and experience around us is influenced by our actions and our interactions with it. And studies have shown that human behaviour isn't random. But seriously ",html.A("What is Random?",href="https://youtu.be/9rIy0xY99a0",target='_blank',style={'text-decoration':'underline'})," and ",html.A("What is Not Random?",href='https://youtu.be/sMb00lz-IfE',target='_blank',style={'text-decoration':'underline'})],style={'color':'#b4b4b4','textAlign':'left'})),
#     dbc.Row(html.H4(["Researchers have found that out that our languages, information, technological advancements and even natural phenomena follow obscure patterns."],style={'color':'#b4b4b4','textAlign':'left'})),
#     html.Br(),
#     dbc.Row(html.H4(["This is an experiment to demonstrate the ",html.Span("biases",style={'color':'white'})," and ",html.Span("predictability",style={'color':'white'})," of our world."],style={'color':'#b4b4b4','textAlign':'left'})),
#     html.Br(),
#     html.Br(),
#     html.Br(),
#     dbc.Row(html.H3("Benford's Law"),style={'font-family':'Times','color':'Yellow','text-decoration':'underline'}),
#     html.Br(),
#     dbc.Row(html.H5('Imagine a large dataset, say something like a list of every country and its population.'),style={'color':'#b4b4b4','padding-left':'20px','textAlign':'left'}),
#     dbc.Table([html.Thead(html.Tr([html.Th("Country"), html.Th("Popultion")]))] + [html.Tbody([
#                                         html.Tr([html.Td("Afghanistan"), html.Td([html.Span("3",style={'color':'white'}),"8,041,754"])]),
#                                         html.Tr([html.Td("Albania"), html.Td([html.Span("2",style={'color':'white'}),",880,917"])]),
#                                         html.Tr([html.Td("Algeria"), html.Td([html.Span("4",style={'color':'white'}),"3,053,054"])]),
#                                         html.Tr([html.Td("Andorra"), html.Td([html.Span("7",style={'color':'white'}),"7,142"])]),
#                                         html.Tr([html.Td(""), html.Td("↑ Leading Digit",style={'color':'yellow'})]),
#                                      ],style={'color':'grey'})],bordered=False,style={'textAlign':'left','width':'50%'}
#               ),
#     dbc.Row(html.H5(['Chances are, the leading digit will be a ',html.Span('1',style={'color':'white'}),' more often than a ',html.Span('2',style={'color':'white'}),'. And ',html.Span('2',style={'color':'white'}),'s would probably occur more often than ',html.Span('3',style={'color':'white'}),'s, and so on.'],style={'color':'#b4b4b4','padding-left':'20px','textAlign':'left'})),
#     dbc.Row(html.H5(["This odd phenomenon is Benford's Law, also called the first digit law. If a set of values were truly random, each leading digit would appear about ",html.Span('11%',style={'color':'white'})," of the time, but Benford's Law predicts a logarithmic distribution. This phenonmenon occurs so regularly that it is even used in fraudulent accounting detection."],style={'color':'#b4b4b4','padding-left':'20px','textAlign':'left'})),
#     html.Br(),
#     dbc.Row(
#             html.Div([
#                     dbc.Col(html.H5("Available Datasets"),style={'text-align':'left','padding':'0'}),
#                     dcc.Dropdown(
#                         id='benford dropdown',
#                         options=[{'label': key, 'value': value} for key,value in benford_datasets.items()],style={'color':'black','textAlign':'left'},
#                         value=1,
#                         searchable=False,
#                         clearable=False,
#                     ),
#                 ],style={'width': '80%', 'display': 'inline-block','padding-left':'20px'}
#             )
#     ),
#     html.Br(),
#     html.Br(),
#     html.Div([
#         dash_table.DataTable(
#             id='benford table',
#             columns=[{"name": i, "id": i} for i in covid_table.columns],
#             data=covid_table.to_dict('records'),
#             style_header={'backgroundColor': 'rgb(30, 30, 30)'},
#                 style_cell={
#                     'whiteSpace': 'normal',
#                     'height': 'auto',
#                     'textAlign': 'left',
#                     'backgroundColor': 'rgb(50, 50, 50)',
#                     'color': 'white'
#                 },
#             style_table={'width':'60%'},
#         )
#     ],className='center'),
#     html.Br(),
#     dbc.Row([
#         dbc.Col(
#             html.Div([
#                 dcc.Loading(
#                     children=[dcc.Graph(
#                                 id="benford graph",
#                                 figure = onload_benfordfig(),
#                                 config = {'displaylogo': False}
#                                 )
#                             ],color='yellow'
#                 )
#             ])
#         )
#     ], no_gutters=True, justify='center'),
#     html.Br(),
#     dbc.Row([
#         dbc.Col([
#             html.H5('References :',style={'textAlign':'left',}),
#             html.Ul(html.Li(html.A(["Number 1 and Benford's Law - Numberphile (Youtube) ",html.Span("(Must Watch)",style={'color':'white'})],href='https://youtu.be/XXjlR2OK1kM',target="_blank"),style={'textAlign':'left'})),
#             html.Ul(html.Li(html.A("Benford's law in the natural sciences",href='https://agupubs.onlinelibrary.wiley.com/share/M8RKM777RDKY8DIVY4DG?target=10.1029/2010GL044830',target="_blank"),style={'textAlign':'left'})),
#             html.Ul(html.Li(html.A("Why do Joe Biden's votes not follow Benford's Law? (Youtube)",href='https://youtu.be/etx0k1nLn78',target="_blank"),style={'textAlign':'left'})),
#             html.Ul(html.Li(html.A("What is Benford’s Law and why is it important for data science?",href='https://towardsdatascience.com/what-is-benfords-law-and-why-is-it-important-for-data-science-312cb8b61048',target="_blank"),style={'textAlign':'left'})),
#         ])
#     ]),
#     html.Br(),
#     html.Br(),
#     html.Br(),
#     dbc.Row(html.H3("Zipf's Law"), style={'font-family':'Times','color': 'Yellow', 'text-decoration': 'underline'}),
#     html.Br(),
#     dbc.Row(html.H5(["Named for linguist George Kingsley Zipf, who around 1935 was the first to draw attention to this phenomenon, the law examines the frequency of words in natural language and how the most common word occurs ",html.Span('twice',style={'color':'white'})," as often as the second most frequent word, ",html.Span('thrice',style={'color':'white'})," as often as the third most frequent word and so on until the least frequent word."],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
#     dbc.Row(html.H5(["So the word in the position ,",html.Span('n',style={'color':'white'})," appears ",html.Span("1/n",style={'color':'white'})," times as often as the most frequent one."],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
#     dbc.Row(html.H5("Zipfian distributions have been found in the population ranks of cities, solar flare intensities, corporation sizes, income rankings and ranks of the number of people watching the same TV channel and many other fields.",
#         style={'color': '#b4b4b4', 'textAlign': 'left', 'padding-left': '20px'})),
#
#     html.Br(),
#     dbc.Row(
#             html.Div([
#                 dbc.Col(html.H5("Available Datasets"), style={'text-align': 'left', 'padding': '0'}),
#                 dcc.Dropdown(
#                             id='zipf dropdown',
#                             options=[{'label': key, 'value': value} for key,value in zipf_datasets.items()],style={'color':'black','textAlign':'left'},
#                             value=1,
#                             searchable=False,
#                             clearable=False,
#                         ),
#                     ],
#                     style={'width': '80%', 'display': 'inline-block','padding-left':'20px'}),
#         ),
#     dbc.Row(
#             dcc.RadioItems(
#                 id='zipf radio',
#                 options=[
#                     {'label': 'Linear', 'value': 'lin'},
#                     {'label': 'Log - Log', 'value': 'log-log'}
#                 ],
#                 value='lin',
#                 labelStyle={'display': 'inline-block','padding':'10px'}
#             ),style={'padding-left':'20px'}
#     ),
#     dbc.Row([
#             dbc.Col(
#                 html.Div([
#                     dcc.Loading(
#                     children=[dcc.Graph(
#                                 id="zipf graph",
#                                 figure = onload_zipffig(),
#                                 config = {'displaylogo': False}
#                                 )
#                             ],color='yellow'
#                 )
#                 ])
#             )
#         ], no_gutters=True, justify='center'),
#
#     html.Br(),
#     html.Br(),
#
#     dbc.Row([
#         html.H5('Try it yourself!',style={'textAlign':'left','padding-left':'20px'})
#         ]),
#
#     html.Br(),
#
#     html.H5(["Click the button below to analyze a random book from the ", html.A('Gutenberg Project',href='https://www.gutenberg.org/',target='_blank'),", an online library of 60,000 eBooks.",],style={'color':'#b4b4b4','textAlign':'left','padding-left':'20px'}),
#     html.H5("You'll notice that most of the times the words follow a Zipfian distribution.",style={'color':'#b4b4b4','textAlign':'left','padding-left':'20px'}),
#     html.Br(),
#
#     html.Div([
#         html.Button('Analyze a random book',id='random book',n_clicks=0),
#     ],className='center'),
#
#     html.Br(),
#
#     dbc.Row(
#                 dcc.RadioItems(
#                     id='random graph radio',
#                     options=[
#                         {'label': 'Linear', 'value': 'lin'},
#                         {'label': 'Log - Log', 'value': 'log-log'}
#                     ],
#                     value='lin',
#                     labelStyle={'display': 'inline-block','padding':'10px'}
#                 ),style={'padding-left':'20px'}
#         ),
#
#     dbc.Row([
#        dbc.Col([
#            dcc.Loading(
#                children=[dcc.Graph(
#                                    id = 'random graph',
#                                    figure = {},
#                                    config = {'displaylogo': False}
#                                 )],type='default',color='yellow'
#                )
#        ]),
#     ], no_gutters=True, justify='center'),
#
#     html.Br(),
#
#     html.Div([
#                 dcc.Loading(children=[dash_table.DataTable(
#                     id='zipf random table',
#                     columns=[{"name": i, "id": i} for i in random_book_table.columns],
#                     data=random_book_table.to_dict('records'),
#                     style_header={'backgroundColor': 'rgb(30, 30, 30)','fontWeight':'bold'},
#                         style_cell={
#                             'whiteSpace': 'normal',
#                             'height': 'auto',
#                             'width': 'auto',
#                             'textAlign': 'left',
#                             'backgroundColor': 'rgb(50, 50, 50)',
#                             'color': '#b4b4b4'
#                         },
#                     style_table={'width':'100%'},
#                 )],type='default',color='yellow')
#             ],className='center'
#     ),
#
#     html.Br(),
#     dbc.Row([
#             dbc.Col([
#                 html.H5('References :',style={'textAlign':'left',}),
#                 html.Ul(html.Li(html.A(["The Zipf Mystery - Vsauce (Youtube) ",html.Span("(Must Watch)",style={'color':'white'})],href='https://youtu.be/fCn8zs912OE',target="_blank"),style={'textAlign':'left'})),
#                 html.Ul(html.Li(html.A("Research article on Zipf's Law published at The Royal Society",href='https://royalsocietypublishing.org/doi/10.1098/rsif.2015.0330',target="_blank"),style={'textAlign':'left'})),
#                 html.Ul(html.Li(html.A("Zipf Curves and Website Popularity",href='https://www.nngroup.com/articles/zipf-curves-and-website-popularity/',target="_blank"),style={'textAlign':'left'})),
#                 html.Ul(html.Li(html.A("Why Zipf's law explains so many big data and physics phenomenons",href='https://www.datasciencecentral.com/profiles/blogs/why-zipf-s-law-explains-so-many-big-data-and-physics-phenomenons',target="_blank"),style={'textAlign':'left'})),
#             ])
#         ]),
#     html.Br(),
#     html.Br(),
#     html.Br(),
#     dbc.Row(html.H3("Brevity Law"), style={'font-family':'Times','color': 'Yellow', 'text-decoration': 'underline'}),
#     html.Br(),
#     dbc.Row(html.H5(["Also called as Zipf's law of abbreviation, it qualitatively states that the ",html.Span('more',style={'color':'white'})," frequently a word is used, the ",html.Span('shorter',style={'color':'white'})," that word tends to be, and vice versa."],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
#     dbc.Row(html.H5(["As shown in the graph below a few shorter words are used more often than many other longer words."],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
#     html.Br(),
#     dbc.Row(
#                     dcc.RadioItems(
#                         id='brevity radio',
#                         options=[
#                             {'label': 'Linear', 'value': 'lin'},
#                             {'label': 'Log - Log', 'value': 'log-log'}
#                         ],
#                         value='lin',
#                         labelStyle={'display': 'inline-block','padding':'10px'}
#                     ),style={'padding-left':'20px'}
#             ),
#
#     dbc.Row([
#             dbc.Col(
#                     dcc.Loading(
#                     children=[dcc.Graph(
#                                 id="brevity graph",
#                                 figure = onload_brevity_fig(),
#                                 config = {'displaylogo': False}
#                                 )
#                             ],color='yellow'
#                 )
#             )
#         ], no_gutters=True, justify='center'),
#     html.Br(),
#     dbc.Row([
#                 dbc.Col([
#                     html.H5('References :',style={'textAlign':'left',}),
#                     html.Ul(html.Li(html.A("Brevity law - Wikipedia",href='https://en.wikipedia.org/wiki/Brevity_law',target="_blank"),style={'textAlign':'left'})),
#                     html.Ul(html.Li(html.A("The Brevity Law as a Scaling Law, and a Possible Origin of Zipf’s Law for Word Frequencies",href='https://www.mdpi.com/1099-4300/22/2/224/htm',target="_blank"),style={'textAlign':'left'})),
#                     html.Ul(html.Li(html.A("On the physical origin of linguistic laws and lognormality in speech",href='https://royalsocietypublishing.org/doi/10.1098/rsos.191023',target="_blank"), style={'textAlign': 'left'})),
#                     html.Ul(html.Li(html.A("Pareto principle aka the 80/20 rule (related)",href='https://en.wikipedia.org/wiki/Pareto_principle',target="_blank"),style={'textAlign':'left'})),            ])
#             ]),
#     html.Br(),
#     html.Br(),
#     html.Br(),
#     dbc.Row(html.H3("Titius–Bode Law"), style={'font-family':'Times','color': 'Yellow', 'text-decoration': 'underline'}),
#     html.Br(),
#     dbc.Row(html.H5(["The Titius–Bode law, first announced in 1766 by Johann Daniel Titius but was popularized only from 1772 by Johann Elert Bode is a formulaic prediction of spacing between planets in any given solar system."],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
#     dbc.Row(html.H5(["The formula suggests that, extending outward, each planet should be approximately ",html.Span("twice",style={'color':'white'})," as far from the Sun as the ",html.Span("one before",style={'color':'white'}),". The hypothesis correctly anticipated the orbits of Ceres in 1801 (in the asteroid belt) and Uranus in 1781, but failed as a predictor of Neptune's orbit in 1846 and that of Pluto, which was regarded as the ninth planet when it was discovered in 1930."],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
#     html.Br(),
#     dbc.Row([
#             dbc.Col(
#                 html.Div([
#                     dcc.Loading(
#                     children=[dcc.Graph(
#                                 id="t-b graph",
#                                 figure = onload_tb_graph(),
#                                 config = {'displaylogo': False}
#                                 )
#                             ],color='yellow'
#                     )
#                 ])
#             )
#     ], no_gutters=True, justify='center'),
#     html.Br(),
#     dbc.Row([
#             dbc.Col([
#                 html.H5('References :',style={'textAlign':'left',}),
#                 html.Ul(html.Li(html.A("Titius Bode Law Explained (Youtube)",href='https://youtu.be/grkcA4AAiUY',target="_blank"),style={'textAlign':'left'})),
#                 html.Ul(html.Li(html.A("Bode's law - Britannica",href='https://www.britannica.com/science/Bodes-law',target="_blank"),style={'textAlign':'left'})),
#                 html.Ul(html.Li(html.A("Testing the Titius-Bode law on exoplanets",href='https://astrobites.org/2014/05/19/testing-the-titius-bode-law-on-exoplanets/',target="_blank"),style={'textAlign':'left'})),
#             ])
#     ]),
#     html.Br(),
#     html.Br(),
#     html.Br(),
#     dbc.Row(html.H3("Moore's Law"),style={'font-family':'Times','color': 'Yellow', 'text-decoration': 'underline'}),
#     html.Br(),
#     dbc.Row(html.H5(["In 1994 Intel released Intel 4004 is a 4-bit CPU, the first commercially produced microprocessor. It was also the first logic circuit integrated in one chip using MOS (metal–oxide–semiconductor) silicon gate technology. The IC had ", html.Span("2,250",style={'color':'white'})," MOS transistors. Fast forward to 2017 AMD launched EPYC Rome a 64-bit microprocessor with an astonishing ", html.Span("39.5 Billion",style={'color':'white'})," transistors."],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
#     dbc.Row(html.H5(["Named after Gordan Moore, co-founder and chairman of Intel Corporation, Moore's law is the observation that the number of transistors in a dense integrated circuit (IC) ", html.Span("doubles",style={'color':'white'})," about every ",html.Span("two",style={'color':'white'})," years."],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
#     dbc.Row(html.H5(["Moore's prediction has been used in the semiconductor industry to guide long-term planning and to set targets for research and development, thus functioning a bit like a self-fulfilling prophecy."],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
#     dbc.Row(html.H5(["However, over the decades, some, including Moore himself at times, fretted that they could see the ",html.Span("end",style={'color':'white'})," in sight, as it got harder to make smaller and smaller transistors."],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
#
#     html.Br(),
#         dbc.Row(
#                 html.Div([
#                         dbc.Col(html.H5("Available Datasets"),style={'text-align':'left','padding':'0'}),
#                         dcc.Dropdown(
#                             id='moore dropdown',
#                             options=[{'label': key, 'value': value} for key,value in moore_datasets.items()],style={'color':'black','textAlign':'left'},
#                             value=1,
#                             searchable=False,
#                             clearable=False,
#                         ),
#                     ],style={'width': '80%', 'display': 'inline-block','padding-left':'20px'}
#                 )
#         ),
#     html.Br(),
#         dbc.Row([
#                     dbc.Col(
#                         html.Div([
#                             dcc.Loading(
#                                 children=[dcc.Graph(
#                                             id="moore graph",
#                                             figure = onload_moore_graph(),
#                                             config = {'displaylogo': False}
#                                             )
#                             ],color='yellow'
#                     )
#                         ])
#                     )
#                 ], no_gutters=True, justify='center'),
#     html.Br(),
#     dbc.Row([
#                 dbc.Col([
#                     html.H5('References :',style={'textAlign':'left',}),
#                     html.Ul(html.Li(html.A("Moore's Law - Explained! (Youtube)",href='https://youtu.be/CUnQNTwmHHo',target="_blank"),style={'textAlign':'left'})),
#                     html.Ul(html.Li(html.A("How Does a Transistor Work? - Veritasium (Youtube)",href='https://youtu.be/IcrBqCFLHIY',target="_blank"),style={'textAlign':'left'})),
#                     html.Ul(html.Li(html.A("Catching a single Transistor - Looking inside the i9-9900K: A single 14nm++ Trigate Transistor (Youtube)",href='https://youtu.be/TtuUANbaEFI',target="_blank"),style={'textAlign':'left'})),
#                     html.Ul(html.Li(html.A("We’re not prepared for the end of Moore’s Law",href='https://www.technologyreview.com/2020/02/24/905789/were-not-prepared-for-the-end-of-moores-law/',target="_blank"), style={'textAlign': 'left'})),
#                 ])
#         ]),
#     html.Br(),
#     html.Br(),
#     html.Br(),
#     dbc.Row(html.H3("Stigler's law of Eponymy"), style={'font-family':'Times','color': 'Yellow', 'text-decoration': 'underline', 'textAlign':'left'}),
#     html.Br(),
#     dbc.Row(html.H5(["This law isn't a scientific discovery or a prediction of any kind but in fact emphasises on human nature and how collaborative and complex the processes of scientific discovery really are."],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
#     dbc.Row(html.H5(["Stigler's Law tells us ",html.Span('''"No scientific discovery is named after its original discoverer."''',style={'color':'white'})],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
#     dbc.Row(html.H5(["Notable examples include ",html.Span("Hubble's law",style={'color':'white'}),", which was derived by Georges Lemaître two years before Edwin Hubble, the ",html.Span("Pythagorean theorem",style={'color':'white'}),", which was known to Babylonian mathematicians before Pythagoras, ",html.Span("Halley's Comet",style={'color':'white'}),", which was observed by astronomers since at least 240 BC, the ",html.Span("Arabic numerals",style={'color':'white'})," we use every day actually originated in India, and ",html.Span("all the laws mentioned on this website.",style={'color':'white'})],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
#     dbc.Row(html.H5(['''The generalization is not limited to science. Stigler himself named the sociologist Robert K. Merton as the discoverer of ''',html.Span('''"Stigler's law"''',style={'color':'white'}),''' to show that it follows its own decree, though the phenomenon had previously been noted by others.'''],style={'color': '#b4b4b4', 'padding-left': '20px', 'textAlign': 'left'})),
#     html.Br(),
#     dbc.Row(
#         dbc.Col(
#             html.H5("Below table list examples of Stigler's Law",style={'textAlign':'left'})
#         )
#     ),
#     dbc.Row(
#         dbc.Col(
#             dash_table.DataTable(
#                         data=stigler_df.to_dict('records'),
#                         columns=[{'id': c, 'name': c} for c in stigler_df.columns],
#                         page_size=10,
#                         style_header={'backgroundColor': 'rgb(30, 30, 30)','fontWeight':'bold','textAlign':'center'},
#                         style_cell={
#                             'whiteSpace': 'normal',
#                             'height': 'auto',
#                             'width': 'auto',
#                             'textAlign': 'left',
#                             'backgroundColor': 'rgb(50, 50, 50)',
#                             'color': '#b4b4b4'
#                         },
#                     )
#         )
#     ),
#     html.Br(),
#     html.Br(),
#     dbc.Row([
#         dbc.Col([
#             html.H5('References :', style={'textAlign': 'left',}),
#             html.Ul(html.Li(html.A("Stigler's law of eponymy (Wikipedia)", href='https://en.wikipedia.org/wiki/Stigler%27s_law_of_eponymy', target="_blank"),style={'textAlign': 'left'})),
#             html.Ul(html.Li(html.A("Why nothing in science is ever named after its actual discoverer?", href='https://io9.gizmodo.com/stiglers-law-why-nothing-in-science-is-ever-named-afte-5820736', target="_blank"),style={'textAlign': 'left'})),
#             html.Ul(html.Li(html.A("Stigler’s law and human nature", href='https://www.johndcook.com/blog/2019/01/12/stiglers-law/', target="_blank"),style={'textAlign': 'left'})),
#         ])
#     ]),
#     html.Br(),
#     html.Br(),
#     html.Br(),
#     html.Footer([html.Span("Created by ",style={'color':'#b4b4b4'}),html.A("Atharva Katre",href="https://www.linkedin.com/in/atharvakatre",id="creator",style={'text-decoration':'underline','cursor': 'pointer','color':'white'})]),
#     html.Br(),
#
# ],style={'textAlign': 'center','width':'80%'}, fluid=True)

# benford callback
@app.callback(
    Output(component_id="benford graph",component_property='figure'),
    Input(component_id='benford dropdown',component_property='value'),
)
def update_graph(graph_chosen):
    if graph_chosen==1:
        return onload_benfordfig()

    if graph_chosen==2:
        fig = go.Figure()
        fig.add_trace(
            go.Bar(x=earthquake_depths['Digits'], y=earthquake_depths['count'], text=earthquake_depths['percentage'],
                   showlegend=False, name='', marker_color='yellow'))
        fig.update_layout(xaxis=dict(
            type='category',
            categoryarray=['1', '2', '3', '4', '5', '6', '7', '8', '9'],

        ), yaxis=dict(showgrid=False))
        fig.update_traces(textposition='outside')
        fig.add_trace(go.Scatter(x=earthquake_depths['Digits'], y=earthquake_depths['benford count'],
                                 name="Predicted by<br>Benford's Law", mode="lines+markers", hoverinfo='skip',
                                 marker_symbol='circle', marker_size=6, marker_line_width=2, ))
        fig.update_traces(hovertemplate=None)
        fig.update_layout(yaxis_title='Leading Digit Frequency',
                          xaxis_title="Leading Digits<br><br>Data Source : <a href='https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2010GL044830'>AGU</a>",
                          title='Earthquake Depths (in km)', title_x=0.5, template='plotly_dark', showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen ==3:
        fig = go.Figure()
        fig.add_trace(go.Bar(x=highways['Digits'], y=highways['count'], text=highways['percentage'], showlegend=False,
                             name='', marker_color='yellow'))
        fig.update_layout(xaxis=dict(
            type='category',
            categoryarray=['1', '2', '3', '4', '5', '6', '7', '8', '9'],

        ), yaxis=dict(showgrid=False))
        fig.update_traces(textposition='outside')
        fig.add_trace(go.Scatter(x=highways['Digits'], y=highways['benford count'], name="Predicted by<br>Benford's Law",
                                 mode="lines+markers", hoverinfo='skip', marker_symbol='circle', marker_size=6,
                                 marker_line_width=2, ))
        fig.update_traces(hovertemplate=None)
        fig.update_layout(yaxis_title='Leading Digit Frequency',
                          xaxis_title="Leading Digits<br><br>Data Source : <a href='https://en.wikipedia.org/wiki/List_of_National_Highways_in_India_by_highway_number'>Wikipedia</a>",
                          title='Length of National Highways in India<br>(in km)', title_x=0.5, template='plotly_dark',
                          showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==4:
        fig = go.Figure()
        fig.add_trace(
            go.Bar(x=country_area['Digits'], y=country_area['count'], text=country_area['percentage'], showlegend=False,
                   name='', marker_color='yellow'))
        fig.update_layout(xaxis=dict(
            type='category',
            categoryarray=['1', '2', '3', '4', '5', '6', '7', '8', '9'],

        ), yaxis=dict(showgrid=False))
        fig.update_traces(textposition='outside')
        fig.add_trace(
            go.Scatter(x=country_area['Digits'], y=country_area['benford count'], name="Predicted by<br>Benford's Law",
                       mode="lines+markers", hoverinfo='skip', marker_symbol='circle', marker_size=6,
                       marker_line_width=2, ))
        fig.update_traces(hovertemplate=None)
        fig.update_layout(yaxis_title='Leading Digit Frequency',
                          xaxis_title="Leading Digits<br><br>Data Source : <a href='https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area'>Wikipedia</a>",
                          title='Total Area of Countries (in km²)', title_x=0.5, template='plotly_dark',
                          showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==5:
        fig = go.Figure()
        fig.add_trace(go.Bar(x=stars_distance['Digits'], y=stars_distance['count'], text=stars_distance['percentage'],
                             showlegend=False, name='', marker_color='yellow'))
        fig.update_layout(xaxis=dict(
            type='category',
            categoryarray=['1', '2', '3', '4', '5', '6', '7', '8', '9'],

        ), yaxis=dict(showgrid=False))
        fig.update_traces(textposition='outside')
        fig.add_trace(
            go.Scatter(x=stars_distance['Digits'], y=stars_distance['benford count'], name="Predicted by<br>Benford's Law",
                       mode="lines+markers", hoverinfo='skip', marker_symbol='circle', marker_size=6,
                       marker_line_width=2, ))
        fig.update_traces(hovertemplate=None)
        fig.update_layout(yaxis_title='Leading Digit Frequency',
                          xaxis_title="Leading Digits<br><br>Data Source : <a href='http://www.atlasoftheuniverse.com/stars.html'>An Atlas of the Universe</a>",
                          title='Distance of Stars from Earth<br>in light years', title_x=0.5, template='plotly_dark',
                          showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==6:
        fig = go.Figure()
        fig.add_trace(
            go.Bar(x=porn_views['Digits'], y=porn_views['count'], text=porn_views['percentage'], showlegend=False,
                   name='', marker_color='yellow'))
        fig.update_layout(xaxis=dict(
            type='category',
            categoryarray=['1', '2', '3', '4', '5', '6', '7', '8', '9'],

        ), yaxis=dict(showgrid=False))
        fig.update_traces(textposition='outside')
        fig.add_trace(
            go.Scatter(x=porn_views['Digits'], y=porn_views['benford count'], name="Predicted by<br>Benford's Law",
                       mode="lines+markers", hoverinfo='skip', marker_symbol='circle', marker_size=6,
                       marker_line_width=2, ))
        fig.update_traces(hovertemplate=None)
        fig.update_layout(yaxis_title='Leading Digit Frequency',
                          xaxis_title="Leading Digits<br><br>Data Source : <a href='https://www.kaggle.com/ljlr34449/porn-data'>Kaggle</a>",
                          title='Views count on Pornhub', title_x=0.5, template='plotly_dark', showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==7:
        fig = go.Figure()
        fig.add_trace(go.Bar(x=countries_population['Digits'], y=countries_population['count'],
                             text=countries_population['percentage'], showlegend=False, name='',
                             marker_color='yellow'))
        fig.update_layout(xaxis=dict(
            type='category',
            categoryarray=['1', '2', '3', '4', '5', '6', '7', '8', '9'],

        ), yaxis=dict(showgrid=False))
        fig.update_traces(textposition='outside')
        fig.add_trace(go.Scatter(x=countries_population['Digits'], y=countries_population['benford count'],
                                 name="Predicted by<br>Benford's Law", mode="lines+markers", hoverinfo='skip',
                                 marker_symbol='circle', marker_size=6, marker_line_width=2, ))
        fig.update_traces(hovertemplate=None)
        fig.update_layout(yaxis_title='Leading Digit Frequency',
                          xaxis_title="Leading Digits<br><br>Data Source : <a href='https://en.wikipedia.org/wiki/List_of_countries_by_past_and_projected_future_population'>Wikipedia</a>",
                          title='Population of Countries (1985 - 2015)', title_x=0.5, template='plotly_dark',
                          showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==8:
        fig = go.Figure()
        fig.add_trace(go.Bar(x=exoplanet_mass['Digits'], y=exoplanet_mass['count'], text=exoplanet_mass['percentage'],
                             showlegend=False, name='', marker_color='yellow'))
        fig.update_layout(xaxis=dict(
            type='category',
            categoryarray=['1', '2', '3', '4', '5', '6', '7', '8', '9'],

        ), yaxis=dict(showgrid=False))
        fig.update_traces(textposition='outside')
        fig.add_trace(
            go.Scatter(x=exoplanet_mass['Digits'], y=exoplanet_mass['benford count'], name="Predicted by<br>Benford's Law",
                       mode="lines+markers", hoverinfo='skip', marker_symbol='circle', marker_size=6,
                       marker_line_width=2, ))
        fig.update_traces(hovertemplate=None)
        fig.update_layout(yaxis_title='Leading Digit Frequency',
                          xaxis_title="Leading Digits<br><br>Data Source : <a href='http://www.exoplanet.eu/catalog'>Exoplanet.eu</a>",
                          title='Mass of Exoplanets (in Earth mass)', title_x=0.5, template='plotly_dark',
                          showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==9:
        fig = go.Figure()
        fig.add_trace(
            go.Bar(x=cricket_runs['Digits'], y=cricket_runs['count'], text=cricket_runs['percentage'], showlegend=False,
                   name='', marker_color='yellow'))
        fig.update_layout(xaxis=dict(
            type='category',
            categoryarray=['1', '2', '3', '4', '5', '6', '7', '8', '9'],

        ), yaxis=dict(showgrid=False))
        fig.update_traces(textposition='outside')
        fig.add_trace(
            go.Scatter(x=cricket_runs['Digits'], y=cricket_runs['benford count'], name="Predicted by<br>Benford's Law",
                       mode="lines+markers", hoverinfo='skip', marker_symbol='circle', marker_size=6,
                       marker_line_width=2, ))
        fig.update_traces(hovertemplate=None)
        fig.update_layout(yaxis_title='Leading Digit Frequency',
                          xaxis_title="Leading Digits<br><br>Data Source : <a href='https://www.kaggle.com/veeralakrishna/icc-test-cricket-runs'>Kaggle</a>",
                          title='Runs scored by Batsmen<br>in Test Cricket', title_x=0.5, template='plotly_dark',
                          showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==10:
        fig = go.Figure()
        fig.add_trace(
            go.Bar(x=terrorism_deaths['Digits'], y=terrorism_deaths['count'], text=terrorism_deaths['percentage'],
                   showlegend=False, name='', marker_color='yellow'))
        fig.update_layout(xaxis=dict(
            type='category',
            categoryarray=['1', '2', '3', '4', '5', '6', '7', '8', '9'],

        ), yaxis=dict(showgrid=False))
        fig.update_traces(textposition='outside')
        fig.add_trace(go.Scatter(x=terrorism_deaths['Digits'], y=terrorism_deaths['benford count'],
                                 name="Predicted by<br>Benford's Law", mode="lines+markers", hoverinfo='skip',
                                 marker_symbol='circle', marker_size=6, marker_line_width=2, ))
        fig.update_traces(hovertemplate=None)
        fig.update_layout(yaxis_title='Leading Digit Frequency',
                          xaxis_title="Leading Digits<br><br>Data Source : <a href='https://www.start.umd.edu/gtd/'>Global Terrorism Database</a>",
                          title='People killed by Terrorism<br>(1970 - 2018)', title_x=0.5, template='plotly_dark',
                          showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==11:
        fig = go.Figure()
        fig.add_trace(go.Bar(x=movie_revenue['Digits'], y=movie_revenue['count'], text=movie_revenue['percentage'],
                             showlegend=False, name='', marker_color='yellow'))
        fig.update_layout(xaxis=dict(
            type='category',
            categoryarray=['1', '2', '3', '4', '5', '6', '7', '8', '9'],

        ), yaxis=dict(showgrid=False))
        fig.update_traces(textposition='outside')
        fig.add_trace(
            go.Scatter(x=movie_revenue['Digits'], y=movie_revenue['benford count'], name="Predicted by<br>Benford's Law",
                       mode="lines+markers", hoverinfo='skip', marker_symbol='circle', marker_size=6,
                       marker_line_width=2, ))
        fig.update_traces(hovertemplate=None)
        fig.update_layout(yaxis_title='Leading Digit Frequency',
                          xaxis_title="Leading Digits<br><br>Data Source : <a href='https://www.themoviedb.org/documentation/api'>TMDB</a>",
                          title='Movie Revenue (in US$)', title_x=0.5, template='plotly_dark', showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==12:
        fig = go.Figure()
        fig.add_trace(
            go.Bar(x=moon_craters['Digits'], y=moon_craters['count'], text=moon_craters['percentage'], showlegend=False,
                   name='', marker_color='yellow'))
        fig.update_layout(xaxis=dict(
            type='category',
            categoryarray=['1', '2', '3', '4', '5', '6', '7', '8', '9'],

        ), yaxis=dict(showgrid=False))
        fig.update_traces(textposition='outside')
        fig.add_trace(
            go.Scatter(x=moon_craters['Digits'], y=moon_craters['benford count'], name="Predicted by<br>Benford's Law",
                       mode="lines+markers", hoverinfo='skip', marker_symbol='circle', marker_size=6,
                       marker_line_width=2, ))
        fig.update_traces(hovertemplate=None)
        fig.update_layout(yaxis_title='Leading Digit Frequency',
                          xaxis_title="Leading Digits<br><br>Data Source : <a href='https://en.wikipedia.org/wiki/List_of_craters_on_the_Moon'>Wikipedia</a>",
                          title="Diameter of Moon's Craters (in km)", title_x=0.5, template='plotly_dark',
                          showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==13:
        fig = go.Figure()
        fig.add_trace(go.Bar(x=fibonacci_list['Digits'], y=fibonacci_list['count'], text=fibonacci_list['percentage'],
                             showlegend=False, name='', marker_color='yellow'))
        fig.update_layout(xaxis=dict(
            type='category',
            categoryarray=['1', '2', '3', '4', '5', '6', '7', '8', '9'],

        ), yaxis=dict(showgrid=False))
        fig.update_traces(textposition='outside')
        fig.add_trace(
            go.Scatter(x=fibonacci_list['Digits'], y=fibonacci_list['benford count'], name="Predicted by<br>Benford's Law",
                       mode="lines+markers", hoverinfo='skip', marker_symbol='circle', marker_size=6,
                       marker_line_width=2, ))
        fig.update_traces(hovertemplate=None)
        fig.update_layout(yaxis_title='Leading Digit Frequency', xaxis_title='Leading Digits', title='First 1000 Fibonacci Numbers', title_x=0.5,
                          template='plotly_dark', showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==14:
        fig = go.Figure()
        fig.add_trace(
            go.Bar(x=disasters_deaths['Digits'], y=disasters_deaths['count'], text=disasters_deaths['percentage'],
                   showlegend=False, name='', marker_color='yellow'))
        fig.update_layout(xaxis=dict(
            type='category',
            categoryarray=['1', '2', '3', '4', '5', '6', '7', '8', '9'],

        ), yaxis=dict(showgrid=False))
        fig.update_traces(textposition='outside')
        fig.add_trace(go.Scatter(x=disasters_deaths['Digits'], y=disasters_deaths['benford count'],
                                 name="Predicted by<br>Benford's Law", mode="lines+markers", hoverinfo='skip',
                                 marker_symbol='circle', marker_size=6, marker_line_width=2, ))
        fig.update_traces(hovertemplate=None)
        fig.update_layout(yaxis_title='Leading Digit Frequency',
                          xaxis_title="Leading Digits<br><br>Data Source : <a href='https://www.emdat.be/'>EM-DAT, CRED / UCLouvain, Brussels, Belgium</a>",
                          title='Total Deaths worldwide due to<br>Natural Disasters (1900 - 2020)', title_x=0.5,
                          template='plotly_dark', showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==15:
        fig = go.Figure()
        fig.add_trace(
            go.Bar(x=global_diseases['Digits'], y=global_diseases['count'], text=global_diseases['percentage'],
                   showlegend=False, name='', marker_color='yellow'))
        fig.update_layout(xaxis=dict(
            type='category',
            categoryarray=['1', '2', '3', '4', '5', '6', '7', '8', '9'],

        ), yaxis=dict(showgrid=False))
        fig.update_traces(textposition='outside')
        fig.add_trace(go.Scatter(x=global_diseases['Digits'], y=global_diseases['benford count'],
                                 name="Predicted by<br>Benford's Law", mode="lines+markers", hoverinfo='skip',
                                 marker_symbol='circle', marker_size=6, marker_line_width=2, ))
        fig.update_traces(hovertemplate=None)
        fig.update_layout(yaxis_title='Leading Digit Frequency',
                          xaxis_title="Leading Digits<br><br>Data Source : <a href='https://www.who.int/data'>World Health Organization</a>",
                          title='Global Infectious Disease cases (2007)', title_x=0.5, template='plotly_dark',
                          showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==16:
        fig = go.Figure()
        fig.add_trace(
            go.Bar(x=sunni_muslims['Digits'], y=sunni_muslims['count'], text=sunni_muslims['percentage'],
                   showlegend=False,
                   name='', marker_color='yellow'))
        fig.update_layout(xaxis=dict(
            type='category',
            categoryarray=['1', '2', '3', '4', '5', '6', '7', '8', '9'],

        ), yaxis=dict(showgrid=False))
        fig.update_traces(textposition='outside')
        fig.add_trace(
            go.Scatter(x=sunni_muslims['Digits'], y=sunni_muslims['benford count'],
                       name="Predicted by<br>Benford's Law",
                       mode="lines+markers", hoverinfo='skip', marker_symbol='circle', marker_size=6,
                       marker_line_width=2, ))
        fig.update_traces(hovertemplate=None)
        fig.update_layout(yaxis_title='Leading Digit Frequency',
                          xaxis_title="Leading Digits<br><br>Data Source : <a href='https://correlatesofwar.org/data-sets/world-religion-data'>The Correlates of War Project</a>",
                          title='Number of Sunni Muslims per country', title_x=0.5, template='plotly_dark',
                          showlegend=True)
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==17:
        fig = go.Figure()
        fig.add_trace(
            go.Bar(x=disasters_damage['Digits'], y=disasters_damage['count'], text=disasters_damage['percentage'],
                   showlegend=False, name='', marker_color='yellow'))
        fig.update_layout(xaxis=dict(
            type='category',
            categoryarray=['1', '2', '3', '4', '5', '6', '7', '8', '9'],

        ), yaxis=dict(showgrid=False))
        fig.update_traces(textposition='outside')
        fig.add_trace(go.Scatter(x=disasters_damage['Digits'], y=disasters_damage['benford count'],
                                 name="Predicted by<br>Benford's Law", mode="lines+markers", hoverinfo='skip',
                                 marker_symbol='circle', marker_size=6, marker_line_width=2, ))
        fig.update_traces(hovertemplate=None)
        fig.update_layout(yaxis_title='Leading Digit Frequency',
                          xaxis_title="Leading Digits<br><br>Data Source : <a href='https://www.emdat.be/'>EM-DAT, CRED / UCLouvain, Brussels, Belgium</a>",
                          title='Damaged suffered (in US$) due to<br>Natural Disasters (1900 - 2000)', title_x=0.5,
                          template='plotly_dark', showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

# benford table callback
@app.callback(
    Output(component_id="benford table",component_property='data'),
    Input(component_id='benford dropdown',component_property='value'),
)
def update_table(table_chosen):
    if table_chosen==1:
        return covid_table.to_dict('records')
    if table_chosen==2:
        return earthquake_depths_table.to_dict('records')
    if table_chosen==3:
        return highways_table.to_dict('records')
    if table_chosen==4:
        return country_area_table.to_dict('records')
    if table_chosen==5:
        return stars_distance_table.to_dict('records')
    if table_chosen==6:
        return porn_views_table.to_dict('records')
    if table_chosen==7:
        return countries_population_table.to_dict('records')
    if table_chosen==8:
        return exoplanet_mass_table.to_dict('records')
    if table_chosen==9:
        return cricket_stats_table.to_dict('records')
    if table_chosen==10:
        return terrorism_deaths_table.to_dict('records')
    if table_chosen==11:
        return movie_revenue_table.to_dict('records')
    if table_chosen==12:
        return moon_craters_table.to_dict('records')
    if table_chosen==13:
        return fibonacci_list_table.to_dict('records')
    if table_chosen==14:
        return disasters_deaths_table.to_dict('records')
    if table_chosen==15:
        return global_diseases_table.to_dict('records')
    if table_chosen==16:
        return sunni_muslims_table.to_dict('records')
    if table_chosen==17:
        return disasters_damage_table.to_dict('records')

# zipf callback
@app.callback(
    Output(component_id='zipf graph', component_property='figure'),
    Input(component_id='zipf dropdown',component_property='value'),
    Input(component_id='zipf radio', component_property='value')
)
def update_graph(graph_chosen,type_chosen):
    if graph_chosen==1 and type_chosen=='lin':
        return onload_zipffig()

    if graph_chosen==1 and type_chosen=='log-log':
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(x=browncorpus.index, y=browncorpus['zipf_dist'], name="Zipfian Distribution", mode="lines",
                       hoverinfo='skip', line_width=2, line_color='orange'))
        fig.add_trace(go.Scatter(x=browncorpus.index, y=browncorpus['count'], name='Word', text=browncorpus['word'],
                                 hoverinfo='text+y', mode='markers+text', marker_color='yellow'))
        fig.update_traces(textposition='top center')
        fig.update_layout(xaxis=dict(showgrid=False))
        fig.update_layout(yaxis=dict(showgrid=False))
        fig.update_traces(hovertemplate=None)
        fig.update_xaxes(type="log")
        fig.update_yaxes(type="log")
        fig.update_layout(yaxis_title='No. of Occurences',
                          xaxis_title="<br>Data Source : <a href='https://en.wikipedia.org/wiki/Brown_Corpus'>Brown Corpus</a>",
                          title='Top 100 Most Common Words in the<br>English Language', title_x=0.5,
                          template='plotly_dark', showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==2 and type_chosen=='lin':
        fig = go.Figure()
        fig.add_trace(go.Bar(x=marathi_corpus['word'], y=marathi_corpus['count'], text=marathi_corpus['percentage'],
                             name='<extra></extra> ', hoverinfo='x+y+text', showlegend=False, marker_color='yellow'))
        fig.update_layout(yaxis=dict(showgrid=False))
        fig.update_traces(textposition='outside')
        fig.add_trace(go.Scatter(x=marathi_corpus['word'], y=marathi_corpus['zipf_dist'], name="Zipfian Distribution",
                                 mode="lines+markers", hoverinfo='skip', marker_symbol='circle', marker_size=6,
                                 marker_line_width=2, ))
        fig.update_traces(hovertemplate=None)
        fig.update_layout(yaxis_title='No. of Occurences',
                          xaxis_title="<br>Data Source : <a href='https://www.nltk.org/book/ch02.html#corpora-in-other-languages'>NLTK</a>",
                          title='Top 50 Most Common Words<br>in the Marathi Language', title_x=0.5,
                          template='plotly_dark', showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==2 and type_chosen=='log-log':
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=marathi_corpus.head(24).index, y=marathi_corpus['zipf_dist'].head(24),
                                 name="Zipfian Distribution", mode="lines", hoverinfo='skip', line_width=2,
                                 line_color='orange'))
        fig.add_trace(go.Scatter(x=marathi_corpus.head(24).index, y=marathi_corpus['count'].head(24),
                                 text=marathi_corpus['word'].head(24), hoverinfo='text+y', name='Word',
                                 mode='markers+text', marker_color='yellow'))
        fig.update_traces(textposition='top center')
        fig.update_layout(xaxis=dict(showgrid=False))
        fig.update_layout(yaxis=dict(showgrid=False))
        fig.update_traces(hovertemplate=None)
        fig.update_xaxes(type="log")
        fig.update_yaxes(type="log")
        fig.update_layout(yaxis_title='No. of Occurences',
                          xaxis_title="<br>Data Source : <a href='https://www.nltk.org/book/ch02.html#corpora-in-other-languages'>NLTK</a>",
                          title='Top 25 Most Common Words<br>in the Marathi Language', title_x=0.5,
                          template='plotly_dark', showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==3 and type_chosen=='lin':
        fig = go.Figure()
        fig.add_trace(go.Bar(x=bible_corpus['word'].head(50), y=bible_corpus['count'].head(50),
                             text=bible_corpus['percentage'].head(50), name='<extra></extra>', showlegend=False,
                             marker_color='yellow'))
        fig.update_layout(yaxis=dict(showgrid=False))
        fig.update_traces(textposition='outside')
        fig.add_trace(go.Scatter(x=bible_corpus['word'].head(50), y=bible_corpus['zipf_dist'].head(50),
                                 name="Zipfian Distribution", mode="lines+markers", hoverinfo='skip',
                                 marker_symbol='circle', marker_size=6, marker_line_width=2, ))
        fig.update_traces(hovertemplate=None)
        fig.update_layout(yaxis_title='No. of Occurences',
                          xaxis_title="<br>Data Source : <a href='http://www.gutenberg.org/'>Gutenberg Project</a>",
                          title='Top 50 Most Common Words<br>in the Bible (King James Version)', title_x=0.5,
                          template='plotly_dark', showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==3 and type_chosen=='log-log':
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(x=bible_corpus.index, y=bible_corpus['zipf_dist'], name="Zipfian Distribution", mode="lines",
                       hoverinfo='skip', line_width=2, line_color='orange'))
        fig.add_trace(go.Scatter(x=bible_corpus.index, y=bible_corpus['count'], text=bible_corpus['word'], name='Word',
                                 hoverinfo='text+y', mode='markers+text', marker_color='yellow'))
        fig.update_traces(textposition='top center')
        fig.update_layout(xaxis=dict(showgrid=False))
        fig.update_layout(yaxis=dict(showgrid=False))
        fig.update_traces(hovertemplate=None)
        fig.update_xaxes(type="log")
        fig.update_yaxes(type="log")
        fig.update_layout(yaxis_title='No. of Occurences',
                          xaxis_title="<br>Data Source : <a href='http://www.gutenberg.org/'>Gutenberg Project</a>",
                          title='Top 100 Most Common Words<br>in the Bible (King James Version)',
                          title_x=0.5, template='plotly_dark', showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==4 and type_chosen=='lin':
        fig = go.Figure()
        fig.add_trace(go.Bar(x=surnames['surname'].head(50), y=surnames['count'].head(50), name='<extra></extra>',
                             showlegend=False, marker_color='yellow'))
        fig.update_layout(yaxis=dict(showgrid=False))
        fig.update_traces(textposition='outside')
        fig.add_trace(
            go.Scatter(x=surnames['surname'].head(50), y=surnames['zipf_dist'].head(50), name="Zipfian Distribution",
                       mode="lines+markers", hoverinfo='skip', marker_symbol='circle', marker_size=6,
                       marker_line_width=2, ))
        fig.update_traces(hovertemplate=None)
        fig.update_layout(yaxis_title='No. of Occurences',
                          xaxis_title="<br>Data Source : <a href='https://en.wikipedia.org/wiki/List_of_most_common_surnames_in_North_America#United_States_(American)'>Wikipedia</a>",
                          title='Top 50 Most Common Surnames in<br>the US (2000 census)', title_x=0.5,
                          template='plotly_dark', showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==4 and type_chosen=='log-log':
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=surnames.index, y=surnames['zipf_dist'], name="Zipfian Distribution", mode="lines",
                                 hoverinfo='skip', line_width=2, line_color='orange'))
        fig.add_trace(go.Scatter(x=surnames.index, y=surnames['count'], text=surnames['surname'], name='Surname',
                                 hoverinfo='text+y', mode='markers+text', marker_color='yellow'))
        fig.update_traces(textposition='top center')
        fig.update_layout(xaxis=dict(showgrid=False))
        fig.update_layout(yaxis=dict(showgrid=False))
        fig.update_xaxes(type="log")
        fig.update_yaxes(type="log")
        fig.update_layout(yaxis_title='No. of Occurences',
                          xaxis_title="<br>Data Source : <a href='https://en.wikipedia.org/wiki/List_of_most_common_surnames_in_North_America#United_States_(American)'>Wikipedia</a>",
                          title='Top 100 Most Common Surnames in<br>the US (2000 census)', title_x=0.5,
                          template='plotly_dark', showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==5 and type_chosen=='lin':
        fig = go.Figure()
        fig.add_trace(go.Bar(x=city_area['city'], y=city_area['area'], name='<extra></extra>', showlegend=False,
                             marker_color='yellow'))
        fig.update_layout(yaxis=dict(showgrid=False))
        fig.update_traces(textposition='outside')
        fig.add_trace(
            go.Scatter(x=city_area['city'], y=city_area['zipf_dist'], name="Zipfian Distribution", mode="lines+markers",
                       hoverinfo='skip', marker_symbol='circle', marker_size=6, marker_line_width=2, ))
        fig.update_traces(hovertemplate=None)
        fig.update_layout(yaxis_title='Area in km²',
                          xaxis_title="<br>Data Source : <a href='https://en.wikipedia.org/wiki/List_of_largest_cities'>Wikipedia</a>",
                          title='Top 50 Cities by Area (in km²)', title_x=0.5, template='plotly_dark', showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==5 and type_chosen=='log-log':
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=city_area.index, y=city_area['zipf_dist'], name="Zipfian Distribution", mode="lines",
                                 hoverinfo='skip', line_width=2, line_color='orange'))
        fig.add_trace(
            go.Scatter(x=city_area.index, y=city_area['area'], text=city_area['city'], name='City', hoverinfo='text+y',
                       mode='markers+text', marker_color='yellow'))
        fig.update_traces(textposition='top center')
        fig.update_layout(xaxis=dict(showgrid=False))
        fig.update_layout(yaxis=dict(showgrid=False))
        fig.update_traces(hovertemplate=None)
        fig.update_xaxes(type="log")
        fig.update_yaxes(type="log")
        fig.update_layout(yaxis_title='Area in km²',
                          xaxis_title="<br>Data Source : <a href='https://en.wikipedia.org/wiki/List_of_largest_cities'>Wikipedia</a>",
                          title='Top 50 Cities by Area (in km²)', title_x=0.5, template='plotly_dark',
                          showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==6 and type_chosen=='lin':
        fig = go.Figure()
        fig.add_trace(
            go.Bar(x=dog_attack['age'], y=dog_attack['count'], text=dog_attack['percentage'], name='<extra></extra>',
                   showlegend=False, marker_color='yellow'))
        fig.update_layout(xaxis=dict(
            type='category',
            categoryarray=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],

        ), yaxis=dict(showgrid=False))
        fig.update_traces(textposition='outside', textfont=dict(color='white'))
        fig.add_trace(go.Scatter(x=dog_attack['age'], y=dog_attack['zipf_dist'], name="Zipfian Distribution",
                                 mode="lines+markers", hoverinfo='skip', marker_symbol='circle', marker_size=6,
                                 marker_line_width=2, ))
        fig.update_traces(hovertemplate=None)
        fig.update_layout(yaxis_title='No. of Occurences',
                          xaxis_title="Age 1(or less) to 10 years old <br><br>Data Source : <a href='https://en.wikipedia.org/wiki/List_of_fatal_dog_attacks_in_the_United_States'>Wikipedia</a>",
                          title="Victim's Age in Dog Attacks<br>(upto 10 years old) US (2000 - 2019)", title_x=0.5,
                          template='plotly_dark', showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==6 and type_chosen=='log-log':
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(x=dog_attack.index, y=dog_attack['zipf_dist'], name="Zipfian Distribution", mode="lines",
                       hoverinfo='skip', line_width=2, line_color='orange'))
        fig.add_trace(go.Scatter(x=dog_attack.index, y=dog_attack['count'],
                                 text=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], name='Age',
                                 hoverinfo='text+y', mode='markers+text', marker_color='yellow'))
        fig.update_traces(textposition='top center')
        fig.update_layout(xaxis=dict(showgrid=False))
        fig.update_layout(yaxis=dict(showgrid=False))
        fig.update_traces(hovertemplate=None)
        fig.update_xaxes(type="log")
        fig.update_yaxes(type="log")
        fig.update_layout(yaxis_title='No. of Occurences',
                          xaxis_title="Age 1(or less) to 10 years old <br><br>Data Source : <a href='https://en.wikipedia.org/wiki/List_of_fatal_dog_attacks_in_the_United_States'>Wikipedia</a>",
                          title="Victim's Age in Dog Attacks<br>(upto 10 years old) US (2000 - 2019)",
                          title_x=0.5, template='plotly_dark', showlegend=True)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ), hovermode='x')
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

# random zipf callback
@app.callback(
    Output(component_id='zipf random table', component_property='data'),
    Output(component_id='random graph', component_property='figure'),
    Input('random book','n_clicks'),
    Input('random graph radio','value')
)
def update_graph(n,type_chosen):
    if n==0:
        if type_chosen=='lin':
            return onload_random_book()
        if type_chosen=='log-log':
            book_num = random.randint(1, 64602)  # 64602 is the total number of books available through the website
            url = "http://www.gutenberg.org/files/{}/{}-0.txt".format(book_num, book_num)
            res = requests.get(url)
            soup = BeautifulSoup(res.content, "html.parser", )
            while str(soup).split()[0] == "<!DOCTYPE":
                book_num = random.randint(1, 64602)
                url = "http://www.gutenberg.org/files/{}/{}-0.txt".format(book_num, book_num)
                res = requests.get(url)
                soup = BeautifulSoup(res.content, "html.parser", )
            url2 = "http://www.gutenberg.org/ebooks/{}".format(book_num)
            res2 = requests.get(url2)
            soup2 = BeautifulSoup(res2.content, "html.parser")
            book_title = soup2.find("h1", itemprop="name").text

            book_words = pd.DataFrame(str(soup).lower().split(), columns=['word'])
            book_word_count = len(book_words)
            book_words['word'] = book_words['word'].apply(
                lambda x: None if x in [",", ".", "``", "''", ";", "?", "--", "(", ")", ":", "!", '''"''', "'"] else x)
            book_words.dropna(inplace=True)
            book_words['word'] = book_words['word'].apply(lambda x: x.lower() if x != "I" else x)
            book_words = book_words['word'].value_counts().head(50).rename('count').rename_axis('word').reset_index()
            book_words['percentage'] = book_words['count'].apply(
                lambda x: str(round((x / book_word_count) * 100, 2)) + "%")

            zipf_dist = []
            for i in range(1, len(book_words) + 1):
                zipf_dist.append(int(book_words['count'][0] / i))
            book_words['zipf_dist'] = zipf_dist
            book_words.index = range(1, len(book_words) + 1)

            fig = go.Figure()
            fig.add_trace(
                go.Scatter(x=book_words.index, y=book_words['zipf_dist'], name="Zipfian Distribution", mode="lines",
                           hoverinfo='skip', line_width=2, line_color='orange'))
            fig.add_trace(go.Scatter(x=book_words.index, y=book_words['count'], text=book_words['word'], name='Word',
                                     hoverinfo='text+y', mode='markers+text', marker_color='yellow'))
            fig.update_traces(textposition='top center')
            fig.update_layout(xaxis=dict(showgrid=False))
            fig.update_layout(yaxis=dict(showgrid=False))
            fig.update_traces(hovertemplate=None)
            fig.update_xaxes(type="log")
            fig.update_yaxes(type="log")
            fig.update_layout(yaxis_title='No. of Occurences',
                              xaxis_title="<br>Data Source : <a href='http://www.gutenberg.org/'>Gutenberg Project</a>",
                              title='Top 50 Most Common Words in <br>' + book_title, title_x=0.5,
                              template='plotly_dark', showlegend=True)
            fig.update_layout(legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="right",
                x=0.99
            ))
            fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            fig.layout.xaxis.fixedrange = True
            fig.layout.yaxis.fixedrange = True

            random_book_table = pd.DataFrame(range(0,11),columns=['Rank'])
            random_book_table[['Word','Count','Percentage']] = book_words[['word', 'count', 'percentage']].head(10)
            random_book_table.drop(random_book_table.head(1).index, inplace=True)
            return random_book_table.to_dict('records'), fig
    if n>0:
        book_num = random.randint(1, 64602)  # 64602 is the total number of books available through the website
        url = "http://www.gutenberg.org/files/{}/{}-0.txt".format(book_num, book_num)
        res = requests.get(url)
        soup = BeautifulSoup(res.content, "html.parser", )
        while str(soup).split()[0] == "<!DOCTYPE":
            book_num = random.randint(1, 64602)
            url = "http://www.gutenberg.org/files/{}/{}-0.txt".format(book_num, book_num)
            res = requests.get(url)
            soup = BeautifulSoup(res.content, "html.parser", )
        url2 = "http://www.gutenberg.org/ebooks/{}".format(book_num)
        res2 = requests.get(url2)
        soup2 = BeautifulSoup(res2.content, "html.parser")
        book_title = soup2.find("h1", itemprop="name").text

        book_words = pd.DataFrame(str(soup).lower().split(), columns=['word'])
        book_word_count = len(book_words)
        book_words['word'] = book_words['word'].apply(
            lambda x: None if x in [",", ".", "``", "''", ";", "?", "--", "(", ")", ":", "!", '''"''', "'"] else x)
        book_words.dropna(inplace=True)
        book_words['word'] = book_words['word'].apply(lambda x: x.lower() if x != "I" else x)
        book_words = book_words['word'].value_counts().head(50).rename('count').rename_axis('word').reset_index()
        book_words['percentage'] = book_words['count'].apply(lambda x: str(round((x / book_word_count) * 100, 2)) + "%")

        zipf_dist = []
        for i in range(1, len(book_words) + 1):
            zipf_dist.append(int(book_words['count'][0] / i))
        book_words['zipf_dist'] = zipf_dist
        book_words.index = range(1, len(book_words) + 1)

        if type_chosen=='lin':
            fig = go.Figure()
            fig.add_trace(
                go.Bar(x=book_words['word'], y=book_words['count'], text=book_words['percentage'], name='<extra></extra> ',
                       showlegend=False, marker_color='yellow'))
            fig.update_layout(yaxis=dict(showgrid=False))
            fig.update_traces(textposition='outside', textfont=dict(color='white'))
            fig.add_trace(go.Scatter(x=book_words['word'], y=book_words['zipf_dist'], name="Zipfian Distribution",
                                     mode="lines+markers", hoverinfo='skip', marker_symbol='circle', marker_size=6,
                                     marker_line_width=2, ))
            fig.update_traces(hovertemplate=None)
            fig.update_layout(yaxis_title='No. of Occurences',
                              xaxis_title="<br>Data Source : <a href='http://www.gutenberg.org/'>Gutenberg Project</a>",
                              title='Top 50 Most Common Words in <br>' + book_title, title_x=0.5, template='plotly_dark',
                              showlegend=True)
            fig.update_layout(legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="right",
                x=0.99
            ))
            fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            fig.layout.xaxis.fixedrange = True
            fig.layout.yaxis.fixedrange = True

            random_book_table = pd.DataFrame(range(0, 11), columns=['Rank'])
            random_book_table[['Word', 'Count', 'Percentage']] = book_words[['word', 'count', 'percentage']].head(10)
            random_book_table.drop(random_book_table.head(1).index, inplace=True)
            return random_book_table.to_dict('records'), fig
        if type_chosen=='log-log':
            fig = go.Figure()
            fig.add_trace(
                go.Scatter(x=book_words.index, y=book_words['zipf_dist'], name="Zipfian Distribution", mode="lines",
                           hoverinfo='skip', line_width=2, line_color='orange'))
            fig.add_trace(go.Scatter(x=book_words.index, y=book_words['count'], text=book_words['word'], name='Word',
                                     hoverinfo='text+y', mode='markers+text', marker_color='yellow'))
            fig.update_traces(textposition='top center')
            fig.update_layout(xaxis=dict(showgrid=False))
            fig.update_layout(yaxis=dict(showgrid=False))
            fig.update_traces(hovertemplate=None)
            fig.update_xaxes(type="log")
            fig.update_yaxes(type="log")
            fig.update_layout(yaxis_title='No. of Occurences',
                              xaxis_title="<br>Data Source : <a href='http://www.gutenberg.org/'>Gutenberg Project</a>",
                              title='Top 50 Most Common Words in <br>' + book_title, title_x=0.5,
                              template='plotly_dark', showlegend=True)
            fig.update_layout(legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="right",
                x=0.99
            ))
            fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            fig.layout.xaxis.fixedrange = True
            fig.layout.yaxis.fixedrange = True

            random_book_table = pd.DataFrame(range(0,11),columns=['Rank'])
            random_book_table[['Word','Count','Percentage']] = book_words[['word', 'count', 'percentage']].head(10)
            random_book_table.drop(random_book_table.head(1).index, inplace=True)
            return random_book_table.to_dict('records'), fig

# brevity callback
@app.callback(
    Output(component_id='brevity graph', component_property='figure'),
    Input(component_id='brevity radio',component_property='value')
)
def update_graph(type_chosen):
    if type_chosen=='lin':
        return onload_brevity_fig()
    if type_chosen=='log-log':
        return onload_brevity_fig_log_log()

# moore callback
@app.callback(
    Output(component_id='moore graph', component_property='figure'),
    Input(component_id='moore dropdown', component_property='value')
)
def update_graph(graph_chosen):
    if graph_chosen==1:
        return onload_moore_graph()
    if graph_chosen==2:
        fig = px.scatter(transistor_gpu, x='Date', y='transistor count', hover_data=transistor_gpu.columns,
                         color='Designer')
        fig.update_layout(yaxis=dict(showgrid=False), xaxis=dict(showgrid=False))
        fig.update_yaxes(type="log")
        fig.update_traces(marker=dict(size=12,
                                      symbol='diamond-tall-dot',
                                      line=dict(width=1, color='black')
                                      ),
                          selector=dict(mode='markers'))
        fig.update_layout(yaxis_title='Count',
                          xaxis_title="<br>Data Source : <a href='https://en.wikipedia.org/wiki/transistor_count'>Wikipedia</a>",
                          title='Number of MOS Transistors on GPU<br>(1982 - 2020)', title_x=0.5,
                          template='plotly_dark')
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==3:
        fig = px.scatter(transistor_ram, x='Date', y='transistor count', hover_data=transistor_ram.columns,
                         color='Designer')
        fig.update_layout(yaxis=dict(showgrid=False), xaxis=dict(showgrid=False))
        fig.update_yaxes(type="log")
        fig.update_traces(marker=dict(size=12,
                                      symbol='diamond-tall-dot',
                                      line=dict(width=1, color='black')
                                      ),
                          selector=dict(mode='markers'))
        fig.update_layout(yaxis_title='Count',
                          xaxis_title="<br>Data Source : <a href='https://en.wikipedia.org/wiki/transistor_count'>Wikipedia</a>",
                          title='Number of MOS Transistors on RAM<br>(1963 - 2019)', title_x=0.5,
                          template='plotly_dark')
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

    if graph_chosen==4:
        fig = px.scatter(transistor_flash, x='Date', y='transistor count', hover_data=transistor_flash.columns,
                         color='Designer')
        fig.update_layout(yaxis=dict(showgrid=False), xaxis=dict(showgrid=False))
        fig.update_yaxes(type="log")
        fig.update_traces(marker=dict(size=12,
                                      symbol='diamond-tall-dot',
                                      line=dict(width=1, color='black')
                                      ),
                          selector=dict(mode='markers'))
        fig.update_layout(yaxis_title='Count',
                          xaxis_title="<br>Data Source : <a href='https://en.wikipedia.org/wiki/transistor_count'>Wikipedia</a>",
                          title='Number of MOS Transistors on<br>Flash Memory (1985 - 2019)', title_x=0.5,
                          template='plotly_dark')
        fig.update_layout(margin=dict(t=50, b=0, l=20, r=20))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

if __name__ == '__main__':
    app.run_server(debug=False)
