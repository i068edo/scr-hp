from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import csv
import datetime
 
options = Options()
#以下のコメントアウトを解除すると、ヘッドレスモードが有効になります。
#options.add_argument("--headless")
driver = webdriver.Chrome("C:\chromedriver-win32\chromedriver",options=options)

def my_favorite_hp(url, pg_dn):
    driver.get(url)
    sleep(3)
    for i in range(pg_dn):
        driver.execute_script('window.scrollBy(0, 100);')
        sleep(1)

def output_news_data(artist_name):
    if artist_name == "ReoNa":
        print(news_title.text)
        print(news_date)
        print(news_url)
        csvlist = []
        csvlist.append(artist_name)
        csvlist.append(news_date)
        csvlist.append(news_title.text)
        csvlist.append(news_url)
        writer.writerow(csvlist)
    else:
        print(news_title.text)
        print(news_date.text)
        print(news_url.get_attribute("href"))
        csvlist = []
        csvlist.append(artist_name)
        csvlist.append(news_date.text)
        csvlist.append(news_title.text)
        csvlist.append(news_url.get_attribute("href"))
        writer.writerow(csvlist)
    sleep(3)




csv_date = datetime.datetime.today().strftime("%Y%m%d")
csv_file_name = "favorite_hp_" + csv_date + ".csv"
f = open(csv_file_name, "w", encoding="CP932", errors="ignore")
 
writer = csv.writer(f, lineterminator="\n") 
csv_header = ["アーティスト","更新日時","ニュースタイトル","url"]
writer.writerow(csv_header)


#ReoNa_hp 
my_favorite_hp("https://www.reona-reona.com/", 7)
for item in range(1, 5):  # 1から4までの4回繰り返し
    for news_list in driver.find_elements_by_xpath(f'//div[@class="info_add"]/dt[{item}]'):
        news_title = news_list.find_element_by_xpath('./div/p')
        news_date_year = news_list.find_element_by_xpath('./p/span[1]')
        news_date_md = news_list.find_element_by_xpath('./p/span[2]')
        news_date = news_date_year.text + " " + news_date_md.text
        news_url = "https://www.reona-reona.com/"

        output_news_data("ReoNa")

#LiSA_info
my_favorite_hp("https://www.lxixsxa.com/info/", 0)
for item in range(1, 5):  # 1から4までの4回繰り返し
    for news_list in driver.find_elements_by_xpath(f'//ul[@class="p-news_list"]/li[{item}]'):
        news_title = news_list.find_element_by_xpath('./div/div[2]')
        news_date = news_list.find_element_by_xpath('./div/div[1]')
        news_url = news_list.find_element_by_xpath('./div/a')

        output_news_data("LiSA")

#米津玄師_info
my_favorite_hp("https://reissuerecords.net/news/", 0)
for item in range(1, 3):  # 1から4までの4回繰り返し
    for news_list in driver.find_elements_by_xpath(f'//ul[@class="news_list"]/li[{item}]'):
        news_title = news_list.find_element_by_xpath('./article/a/div[2]/h1')
        news_date = news_list.find_element_by_xpath('./article/a/div[2]/ul/li[2]')
        news_url = news_list.find_element_by_xpath('./article/a')

        output_news_data("米津玄師")


#優里_info
my_favorite_hp("https://www.yuuriweb.com/news/", 0)
for item in range(1, 5):  # 1から4までの4回繰り返し
    for news_list in driver.find_elements_by_xpath(f'//div[@id="news_list"]/li[{item}]'):
        news_title = news_list.find_element_by_xpath('./div/p[1]')
        news_date = news_list.find_element_by_xpath('./div/p[2]')
        news_url = news_list.find_element_by_xpath('./a')

        output_news_data("優里")

#ヨルシカ_info
my_favorite_hp("https://yorushika.com/news/5/", 0)
for item in range(1, 5):  # 1から4までの4回繰り返し
    for news_list in driver.find_elements_by_xpath(f'//ul[@class="list--news"]/li[{item}]'):
        news_title = news_list.find_element_by_xpath('./a/p[2]')
        news_date = news_list.find_element_by_xpath('./a/p[1]')
        news_url = news_list.find_element_by_xpath('./a')

        output_news_data("ヨルシカ")

#ずっと真夜中でいいのに_info
my_favorite_hp("https://zutomayo.net/news/", 0)
for item in range(1, 5):  # 1から4までの4回繰り返し
    for news_list in driver.find_elements_by_xpath(f'//article/section[{item}]'):
        news_title = news_list.find_element_by_xpath('./div/div/h3')
        news_date = news_list.find_element_by_xpath('./div/div/p')
        news_url = news_list.find_element_by_xpath('./div/div[2]/p/a')

        output_news_data("zutomayo")

#hakubi_info
my_favorite_hp("https://hakubikyoto.com/news", 0)
for item in range(1, 5):  # 1から4までの4回繰り返し
    for news_list in driver.find_elements_by_xpath(f'//div[@class="p-news_page-wrapper"]/div[{item}]'):
        news_title = news_list.find_element_by_xpath('./a/h3/span')
        news_date = news_list.find_element_by_xpath('./a/div')
        news_url = news_list.find_element_by_xpath('./a')

        output_news_data("hakubi")




f.close()


