import scrapy


class QuotesSpiderWithArgs(scrapy.Spider):
    name = "quotes_with_args"

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'

        # scrapy crawl myspider -a category=electronics
        tag = getattr(self, 'tag')
        if tag is not None:
            url = url + "tag/" + tag

        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        authors = []
        for author in response.css('.author + a::attr(href)'):
            author_name = author.extract().split('/')[-1]
            authors.append(author_name)

        print(authors)
