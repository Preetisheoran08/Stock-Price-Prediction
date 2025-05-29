from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd

def scrape_yahoo_history(symbol: str, headless: bool = True):
    url = f"https://finance.yahoo.com/quote/{symbol}/history?p={symbol}"

    # set up Chrome
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    try:
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
        
        driver.get(url)

        # wait for the history table to load its rows
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "div[data-testid='history-table'] table tbody tr")
            )
        )

        # scroll a bit to trigger any lazy-loading
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(1)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        table = soup.select_one("div[data-testid='history-table'] table")
        
        if not table:
            return []

        # pull out header names
        headers = [th.get_text(strip=True) for th in table.thead.find_all("th")]

        data = []
        for row in table.tbody.find_all("tr"):
            cols = [td.get_text(strip=True) for td in row.find_all("td")]
            # skip any rows that don't have the full set of columns
            if len(cols) == len(headers):
                record = dict(zip(headers, cols))
                data.append(record)

        return data

    except Exception as e:
        print(f"Error scraping data: {e}")
        return []
    finally:
        driver.quit()


if __name__ == "__main__":
    symbol = "NVDA"
    history = scrape_yahoo_history(symbol)

    # Convert to a DataFrame
    df = pd.DataFrame(history)

    # Print a quick preview
    print(df.head())

    # Save to CSV
    output_file = f"{symbol}_history.csv"
    df.to_csv(output_file, index=False)
    print(f"Saved full history to '{output_file}'")
