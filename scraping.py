from icrawler.builtin import BaiduImageCrawler

crawler = BaiduImageCrawler(downloader_threads=8, storage={"root_dir": "smartphone"})
crawler.crawl(keyword="智能手机", max_num=800)

crawler = BaiduImageCrawler(downloader_threads=8, storage={"root_dir": "ikemen"})
crawler.crawl(keyword="帅哥", max_num=800)

crawler = BaiduImageCrawler(downloader_threads=8, storage={"root_dir": "busaiku"})
crawler.crawl(keyword="丑脸", max_num=800)

crawler = BaiduImageCrawler(downloader_threads=8, storage={"root_dir": "pencil"})
crawler.crawl(keyword="pencil", max_num=800)

crawler = BaiduImageCrawler(downloader_threads=8, storage={"root_dir": "eraser"})
crawler.crawl(keyword="eraser", max_num=800)

crawler = BaiduImageCrawler(downloader_threads=8, storage={"root_dir": "towl"})
crawler.crawl(keyword="毛巾", max_num=800)

crawler = BaiduImageCrawler(downloader_threads=8, storage={"root_dir": "room"})
crawler.crawl(keyword="房间", max_num=800)