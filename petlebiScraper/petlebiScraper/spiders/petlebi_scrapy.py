import scrapy

class petlebiSpider(scrapy.Spider):
    name = 'petlebi'
    start_urls = ['https://www.petlebi.com/kedi-petshop-urunleri', 'https://www.petlebi.com/kopek-petshop-urunleri', 'https://www.petlebi.com/kus-petshop-urunleri', 'https://www.petlebi.com/kemirgen-petshop-urunleri']

    def parse(self, response):
        for products in response.css('div.col-lg-4.col-md-4.col-sm-6.search-product-box'):
            try:
                item = {
                'product URL': products.css('a.p-link::attr(href)').get(),
                'product name': products.css('a.p-link::attr(title)').get(),
                'product price': products.css('span.commerce-discounts::text').get().replace(' TL',''), 
                'ID ': products.css('a.p-link::attr(id)').get(),
                'IMG ': products.css('img.img-fluid.lazy.mb-2').get(),  
                }
                
                request = scrapy.Request(products.css('a.p-link::attr(href)').get(), callback=self.parseItem)
                request.meta['item'] = item

                yield request
            except:
                item = {
                'product URL': products.css('a.p-link::attr(href)').get(),
                'product name': products.css('a.p-link::attr(title)').get(),
                'product price': products.css('span.commerce-discounts::text').get().replace(' TL',''), 
                'ID ': products.css('a.p-link::attr(id)').get(),
                'IMG ': products.css('img.img-fluid.lazy.mb-2').get()
                }
               
                request = scrapy.Request(products.css('a.p-link::attr(href)').get(), callback=self.parseItem)
                request.meta['item'] = item

                yield request
            
            for i in range (3):
                for a in range (2, 118):
                    dest = ['https://www.petlebi.com/kedi-petshop-urunleri?page=', 'https://www.petlebi.com/kopek-petshop-urunleri?page=', 'https://www.petlebi.com/kus-petshop-urunleri?page=', 'https://www.petlebi.com/kemirgen-petshop-urunleri?page=']
                
                    next_page = dest[i] + str(a)
                    if next_page is not None: 
                        yield response.follow(next_page, callback=self.parse) 
                    else:
                        break
    
    def parseItem(self, response):
        item = response.meta['item']
        for data in response.css('div.tab-content.product-text-area'):
            try:
                item['barcode'] = data.css('div.col-10.pd-d-v::text').get()
                item['brand'] = data.css('a::text').get()
                item['description'] = data.css('p::text').get()
            except:
                item['barcode'] = data.css('div.col-10.pd-d-v::text').get()
                item['brand'] = data.css('a::text').get()
                item['description'] = data.css('p::text').get()
        yield item
                