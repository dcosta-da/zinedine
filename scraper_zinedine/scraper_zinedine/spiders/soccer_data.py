import scrapy
from datetime import datetime

class SoccerData(scrapy.Spider):
    name = "soccer_data"

    def start_requests(self):
        
        seasons_a = [f"{y}-{y+1}" for y in range(2018, datetime.now().year)]
        competitions_a = [(11, 'Serie-A'), (9, 'Premier-League')]

        seasons_b = [f"{y}" for y in range(2018, datetime.now().year)]
        competitions_b = [(55, 'K-League-1'), (25, 'J1-League')]

        all_links_a = [
            f'https://fbref.com/en/comps/{comp_code_a}/{season_a}/schedule/{season_a}-{comp_name_a}-Scores-and-Fixtures'
            for season_a in seasons_a
            for comp_code_a, comp_name_a in competitions_a
        ]

        all_links_b = [
            f'https://fbref.com/en/comps/{comp_code_b}/{season_b}/schedule/{season_b}-{comp_name_b}-Scores-and-Fixtures'
            for season_b in seasons_b
            for comp_code_b, comp_name_b in competitions_b
        ]

        all_links = all_links_a + all_links_b

        for link in all_links:
            yield scrapy.Request(url=link, callback=self.matches_urls)


    def matches_urls(self, response):
        match_report = response.css('td[data-stat="match_report"]>a::attr(href)').getall() 

        match_report_links = [f"https://fbref.com{link}" for link in match_report]
        
        print(match_report_links)