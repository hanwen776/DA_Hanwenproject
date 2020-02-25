import scrapy
class NewSpider(scrapy.Spider):
 name = "new_spider"
 start_urls = ['http://172.50.43/multi']
def parse(self, response):
    css_sel = 'img'
    for x in response.css(css_sel):
        new_xpath_sel = '@src'
        yield {
            'IMAGE link': x.path(new_xpath_sel).extract_first()
        }
    next_sel = '.next a::attr(href)'
    next_page = response.css(next_sel).extract_first()
    if next_page:
        yield scrapy.Request(response.urljoin(next_page), callback=self.parse)