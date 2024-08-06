from selenium import webdriver

from utilities import ConfigReader


def before_scenario(context, driver):

    browser = ConfigReader.read_configuration("basic info", "browser")

    if browser.lower().__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser.lower().__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif browser.lower().__eq__("edge"):
        context.driver = webdriver.Edge()
    else:
        print("Provide a valid browser name from this list chrom/firefox/edge")

    context.driver.maximize_window()
    # base_url = ConfigReader.read_configuration("basic info", "url")
    # context.driver.get(base_url)
    #driver.implicitly_wait(5)


def after_scenario(context, driver):
    context.driver.quit()