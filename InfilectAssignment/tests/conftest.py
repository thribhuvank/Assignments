import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser_name == "IE":
        driver = webdriver.Ie(IEDriverManager().install())
    elif browser_name == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("https://weathershopper.pythonanywhere.com/")

    request.cls.driver = driver
    yield
    driver.close()
