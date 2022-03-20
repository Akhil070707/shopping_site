import scrapy


class shoesSpider(scrapy.Spider):
    name = 'shoes'
    start_urls =['https://www.mytheresa.com/int_en/men/shoes.html']

    def parse(self, response):
        for products in response.css('div.product-info'):
            yield{
                'name': products.css('a').attrib['title'],
                'brand':products.css('span::text').get(),
                'price':products.css('span.price::text').get().replace('€',''),
                'link':products.css('a').attrib['href'],
                'size': response.xpath('//*[@id="top"]/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[7]/ul/li[1]/span/ul/li').get().replace('<br> <br></li>"','')




            }




        next_page =response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)
