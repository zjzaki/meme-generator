import time

from selenium import webdriver
from meme_generator import add_meme
from meme_generator.utils import make_png_or_gif


def wakapi(images, texts, args):


    # 图片生成代码
    url = texts[0]
    save_fn = str(time.time()) + ".png"

    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    option.add_argument("--window-size=1280,1024")
    option.add_argument("--hide-scrollbars")

    driver = webdriver.Chrome(option)

    driver.get(url)
    print(driver.title)

    scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(scroll_width, scroll_height)
    driver.save_screenshot(save_fn)
    driver.quit()
    images = [("images", open(save_fn, "rb"))]

    def f():
        pass

    return make_png_or_gif(images[0],f)


add_meme(
    "wakapi",
    wakapi,
    min_texts=1,
    max_texts=2,
    keywords=["wakapi排行榜"],
)
