from utilities import scraper
from utilities import file_util
import time
import csv


def scrape_so_matches(i_filepath):
    data = file_util.open_csv(i_filepath)
    for x in data:
        season = x[0]
        league = x[1]
        team = x[2]
        so_match_link = x[3]
        o_filepath = f'data/{season}/{league}/so_matches/{team}.csv'
        file_util.check_delete_file(o_filepath)
        scraper.scrape_matches(so_match_link,team,league,o_filepath)
        time.sleep(8)
        
def main():
    i_filepath = 'lookups/23_24/squad_overview.csv'
    scrape_so_matches(i_filepath)

if __name__ == "__main__":
    main()
    

# f'data\{season}\{league}\so_matches\{team}'