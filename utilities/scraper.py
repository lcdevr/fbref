import pandas as pd

def scrape_so_matches(url, teamname, league, o_filepath):
    df = pd.read_html(url)[1]
    df.insert(loc=0,column='Team',value=teamname)
    df.to_csv(o_filepath)

def scrape_so_goalkeeper(url, teamname, league, o_filepath):
    df = pd.read_html(url)[2]
    df = df.iloc[:2]
    df.insert(loc=0,column='Team',value=teamname)
    df = df.reset_index(drop=True)
    print(df)

def scrape_so_shooting(url, teamname, league, o_filepath):
    df = pd.read_html(url)[3]
    print(df)

def scrape_so_playing(url, teamname, league, o_filepath):
    df = pd.read_html(url)[4]
    print(df)

def scrape_so_misc(url, teamname, league, o_filepath):
    df = pd.read_html(url)[5]
    print(df)