from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
from geturls.items import GeturlsItem


class GeturlsSpider(BaseSpider):
        name = "geturls"
        start_urls = [
            "http://foodnetwork.com/recipes.html",
            "http://simplyrecipes.com",
            "http://recipe.com",
            "http://food.com/recipe",
            "http://bettycrocker.com/recipes",
            "http://tasteofhome.com/recipes",
            "http://realsimple.com",
            "http://momswhothink.com/recipes/food-and-recipes.html",
            "http://myrecipes.com"
        ]

        def parse(self, response):
	    items = []
            sel = HtmlXPathSelector(response)
            sites = sel.select('//ul/li')
		
            for site in sites:
		item = GeturlsItem()
                item['title'] = site.select('a/text()').extract()
                item['link'] = site.select('a/@href').extract()
                item['text'] = site.select('a/text()').extract()
		items.append(item) 
	    return items
