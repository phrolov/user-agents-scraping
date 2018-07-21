### Scrapy project for (potentially) different user agent databases around the web

It currently supports [WhatIsMyBrowser.com](https://developers.whatismybrowser.com/useragents/explore/)

Use `category` spider argument to limit the number of items:

    scrapy crawl whatismybrowser -a category='hardware_type_specific/computer'
