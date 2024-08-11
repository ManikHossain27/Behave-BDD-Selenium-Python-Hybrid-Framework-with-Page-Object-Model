import allure
from allure_commons.types import AttachmentType
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
    base_url = ConfigReader.read_configuration("basic info", "url")
    context.driver.get(base_url)
    #driver.implicitly_wait(5)


def after_scenario(context, driver):
    context.driver.quit()


#To take a screenshot only on failure, write the following method (after_step)
def after_step(context, step):
    if step.status == "failed":
        # Access the scenario title
        scenario_title = context.scenario.name if hasattr(context, 'scenario') else 'Scenario_Failed'
        # Attach screenshot to Allure report with scenario title
        allure.attach(context.driver.get_screenshot_as_png()
                      , name=f"Scenario: {scenario_title} failed"
                      , attachment_type=AttachmentType.PNG)