import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            # 'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        page = response.url.split("/")[-2]

        filename = 'quotes-%s.txt' % page
        with open(filename, 'w') as f:
            # 使用selectors过滤指定的页面标签
            for sel in response.css('div.quote'):
                quote_text = sel.css('span.text::text').extract_first()
                author = sel.css('small.author::text').extract_first()
                f.write(quote_text + "\n" + "----" + author + "\n\n")

        self.log('Saved file %s' % filename)
        """
        for sel in response.css('div.quote'):
            quote_text = sel.css('span.text::text').extract_first()
            author = sel.css('small.author::text').extract_first()
            # scrapy crawl quotes -o filename.json/xml/csv...必须是字典类型
            yield {'text': quote_text, 'author': author}

        next_page = response.css('li.next a::attr(href)').extract_first()
        next_page_num = int(str(next_page).split("/")[-2])
        if next_page is not None and next_page_num < 5:
            # 将相对路径拼接为绝对路径
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
