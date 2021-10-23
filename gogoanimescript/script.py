import time
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import requests
from webdriver_manager.firefox import GeckoDriverManager


def get_video_stream_url(ep_link):
    video_stream_url = ""
    r = requests.get(ep_link)
    a = str(r.content).find('<iframe src="//')
    b = str(r.content)[a+15::1].find('"')
    c = str(r.content)[a+15::1]
    url = "https://"+c[0:b]
    s = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=s)
    driver.get(url)
    driver.find_element_by_css_selector(
        "div.jw-icon.jw-icon-display.jw-button-color.jw-reset").send_keys(Keys.ENTER)
    time.sleep(3)
    with open("./a.txt", "w") as c:
        for request in driver.requests:
            if(request.url.find(".m3u8") > 0):
                video_stream_url = request.url
    driver.quit()
    return video_stream_url


# capabilities = {
#     "browserName": "chrome",
#     "version": "81.0",
#     "enableVNC": True,
#     "enableVideo": True,

# }
# a = get_video_stream_url(
#     "https://gogoanime.pe/dragon-quest-dai-no-daibouken-2020-episode-54")

    # driver = webdriver.Remote(
    #     command_executor="http://174.138.28.204:4444/wd/hub",
    #     desired_capabilities=capabilities)
