import scrapy

class IMDBSpider(scrapy.Spider):
    name = "imdb_spider"
    start_urls = ['https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm']
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }    
    
    def parse(self, response):
        for movie in response.xpath('//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li'):
            try:
                rating = movie.xpath('./div[2]/div/div/span/div/span/text()').get()
                title = movie.xpath('./div[2]/div/div/div[2]/a/h3/text()').get()
                year = movie.xpath('./div[2]/div/div/div[3]/span[1]/text()').get()
                duration = movie.xpath('./div[2]/div/div/div[3]/span[2]/text()').get()
            except Exception:
                continue

            yield {
                'Título': title,
                'Año': year,
                'Duración': duration,
                'Rating': rating
            }