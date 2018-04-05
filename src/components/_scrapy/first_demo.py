import scrapy


class QuoteFetch(scrapy.Spider):
    name = "quote_fetch"

    def start_requests(self):
        url = "https://www.geyanw.com/lizhimingyan/1834.html"
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        with open(r'C:\Users\Linux\Desktop\text.txt', 'a', encoding='UTF-8', newline='\n') as f:

            title = response.css("div.title>h2::text").extract_first()
            print("title is %s" % title)
            f.write(title + "\n")
            for quote in response.css('div.content'):
                # yield {
                #     'text': quote.css('p::text').extract_first(),
                # }
                for temp in quote.css('p::text').extract():
                    f.write(temp + "\n")
                    print("text is %s" % temp)

            next_page = response.css('div.context>ul>li a::attr(href)').extract_first()
            if next_page is not None:
                yield response.follow(next_page, self.parse)
