import pandas as pd

def scrape_matches(url, teamname, league, o_filepath):
    df = pd.read_html(url)[1]
    df.insert(loc=0,column='Team',value=teamname)
    df.to_csv(o_filepath)

def scrape_goalkeeper():
    pass

def scrape_shooting():
    pass

def scrape_playing():
    pass

def scrape_misc():
    pass