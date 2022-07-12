from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class Scraper :
    def __init__(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        #options.add_argument("--headless")
        options.add_argument('--no-sandbox')



        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
        self.driver = webdriver.Chrome(options=options)

        self.wait = WebDriverWait(self.driver, 10)



    def add_review_yell(self) -> None:

        url = "https://www.yell.com/reviews/places/addreview/id/master-plumbing-service-ltd-london-901743641"
        self.driver.get(url)

        div_start = self.driver.find_element_by_class_name("writeReview--rating")
        div_start.click()

        stars = self.driver.find_element(By.CSS_SELECTOR,f"label[for='rating-input-1-{self.business}']")
        stars.click()
        sleep(100)

        input_review = self.driver.find_element(By.ID,"review_body")
        input_review.send_keys(self.review)

        input_title = self.driver.find_element(By.ID,"title")
        input_title.send_keys(self.review_title)

        btn_guest = self.driver.find_element(By.CSS_SELECTOR,"a[data-tracking='REVIEWS:GUEST:SUBMIT']")
        btn_guest.click()

        input_first_name = self.wait.until(EC.visibility_of_element_located((By.ID,"firstName")))
        input_first_name.send_keys(self.first_name)

        input_last_name = self.driver.find_element(By.ID,"lastName")
        input_last_name.send_keys(self.last_name)

        input_email = self.driver.find_element(By.ID,"email")
        input_email.send_keys(self.email)


        btn_submit = self.driver.find_element(By.CSS_SELECTOR,"button[data-tracking='REVIEWS:GUEST:CONTINUE:SUBMIT']")
       # btn_submit.click()

        sleep(3)

    def add_review_checkatrade(self) -> None :
        url = "https://www.checkatrade.com/give-feedback/trades/masterplumbingserviceltd"
        self.driver.get(url)

        sleep(3)
        button_yes = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"button[color='#999999']")))
        button_yes.click()

        input_date = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[aria-label='Date work completed?']")))
        input_date.click()

        btn_previous_month = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'react-datepicker__day--outside-month')))
        btn_previous_month.click()

        radios_service = self.driver.find_elements(By.CSS_SELECTOR,"input[type='radio']")
        if self.service=="Central Heating" :
            radios_service[0].click()
        else:
            radios_service[1].click()

        input_job = self.driver.find_element(By.CSS_SELECTOR,"textarea[name='whatJob']")
        input_job.send_keys(self.job)

        input_review = self.driver.find_element(By.CSS_SELECTOR,"textarea[name='yourReview']")
        input_review.send_keys(self.review)

        btn_next = self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
        btn_next.click()
        sleep(1)

        divs_rating = self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME,"fpntma")))
        for div in divs_rating :
            button = div.find_elements(By.TAG_NAME,"button")[1]
            for i in range(3):
                button.click()

        btn_next = self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
        btn_next.click()

        div_price = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div[role='listbox']")))
        button_price = div_price.find_element(By.TAG_NAME,"button")
        button_price.click()
        btn_next = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"button[type='submit']")))
        btn_next.click()

        form = self.wait.until(EC.visibility_of_element_located((By.ID,"valueOfWork")))
        btn_yes = form.find_element(By.TAG_NAME,"button")
        btn_yes.click()

        btn_next = self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
        btn_next.click()

        form = self.wait.until(EC.visibility_of_element_located((By.ID,"wouldRecommend")))
        btn_yes = form.find_element(By.TAG_NAME,"button")
        btn_yes.click()

        btn_next = self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
        btn_next.click()
        input_first_name = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[name='first_name']")))
        input_last_name = self.driver.find_element(By.CSS_SELECTOR,"input[name='last_name']")
        input_post_code = self.driver.find_element(By.CSS_SELECTOR,"input[name='post_code']")
        input_mobile_number = self.driver.find_element(By.CSS_SELECTOR,"input[name='mobile_number']")
        input_email = self.driver.find_element(By.CSS_SELECTOR,"input[name='email']")

        input_first_name.send_keys(self.first_name)
        input_last_name.send_keys(self.last_name)
        input_post_code.send_keys(self.post_code)
        input_mobile_number.send_keys(self.tlf)
        input_email.send_keys(self.email)
        sleep(1)

        button_submit = self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
       # button_submit.click()
    
    def close_browser(self):
        self.driver.quit()




