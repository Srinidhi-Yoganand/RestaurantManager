import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException
import time

# Function to simulate slow typing
def slow_type(element, text, delay=0.2):
    for character in text:
        element.send_keys(character)
        time.sleep(delay)  # Delay between characters

class RestaurantManagerTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()  # Start Chrome driver
        self.driver.get("http://localhost:3000")  # Open the main page of your application

    def tearDown(self):
        self.driver.quit()  # Close the browser after the test

    def test_registration_and_login(self):
        driver = self.driver

        # Step 1: Toggle to Registration form
        try:
            register_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "toggle-button"))
            )
            register_button.click()
            time.sleep(2)  # Delay after clicking the register button
        except Exception as e:
            print(f"Error: Could not find or click on the Register button. {e}")
            self.fail("Register button not clickable")

        # Step 2: Input the registration details 
        try:
            username_field = driver.find_element(By.NAME, "username")
            slow_type(username_field, "testuser", delay=0.2)  # Slow typing
            password_field = driver.find_element(By.NAME, "password")
            slow_type(password_field, "testpassword", delay=0.2)  # Slow typing
            driver.find_element(By.CLASS_NAME, "submit-button").click()
            time.sleep(2)  # Delay after clicking submit
        except Exception as e:
            print(f"Error: Could not input data or click submit. {e}")
            self.fail("Failed to input registration details or submit the form")
        
        # Step 3: Handle any potential alert
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert.accept()  # Close the alert
        except UnexpectedAlertPresentException:
            print("No alert detected or alert ignored, proceeding.")

        # Step 4: Toggle back to Login form after registration
        try:
            login_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "toggle-button"))
            )
            login_button.click()
            time.sleep(2)  # Delay after clicking the login button
        except Exception as e:
            print(f"Error: Could not find or click on the Login button. {e}")
            self.fail("Login button not clickable")

        # Step 5: Click the Login button (no need to re-enter the credentials)
        try:
            driver.find_element(By.CLASS_NAME, "submit-button").click()
            time.sleep(2)  # Delay after clicking submit
        except Exception as e:
            print(f"Error: Could not click submit button. {e}")
            self.fail("Failed to submit login form")

        # Step 6: Check if logged in (looking for a logout button or user-specific element)
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "logout-button"))
            )
            logout_button = driver.find_element(By.CLASS_NAME, "logout-button")
            self.assertTrue(logout_button.is_displayed(), "Logout button is not visible, login failed.")
            print("Successful in registering and logging in")
        except Exception as e:
            print(f"Error: Could not find logout button. {e}")
            self.fail("Login failed, could not find logout button")
            
    def login(self):
        driver = self.driver

        # Step 2: Input login credentials and submit
        try:
            username_field = driver.find_element(By.NAME, "username")
            slow_type(username_field, "testuser", delay=0.2)  # Slow typing
            password_field = driver.find_element(By.NAME, "password")
            slow_type(password_field, "testpassword", delay=0.2)  # Slow typing
            driver.find_element(By.CLASS_NAME, "submit-button").click()
            time.sleep(2)  # Delay after clicking submit
        except Exception as e:
            print(f"Error: Could not input login data or click submit. {e}")
            self.fail("Failed to input login details or submit the form")

        # Step 3: Wait for the user to be logged in (check for a logout button or other indicator)
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "logout-button"))
            )
            print("Login successful.")
        except Exception as e:
            print(f"Error: Could not find logout button. {e}")
            self.fail("Login failed, could not find logout button")

    def test_add_restaurant(self):
        driver = self.driver

        self.login()

        # Step 1: Wait for the restaurant form to be visible
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "restaurant-form"))
            )
            time.sleep(2)  # Delay after the form becomes visible
        except Exception as e:
            print(f"Error: Restaurant form not visible. {e}")
            self.fail("Restaurant form not visible")

        # Step 2: Fill in the form fields with slow typing
        try:
            id_field = driver.find_element(By.NAME, "id")
            slow_type(id_field, "102", delay=0.2)  # Slow typing for id
            name_field = driver.find_element(By.NAME, "name")
            slow_type(name_field, "Test Restaurant", delay=0.2)  # Slow typing for name
            type_field = driver.find_element(By.NAME, "type")
            slow_type(type_field, "Indian", delay=0.2)  # Slow typing for type
            location_field = driver.find_element(By.NAME, "location")
            slow_type(location_field, "Mysuru", delay=0.2)  # Slow typing for location
            rating_field = driver.find_element(By.NAME, "rating")
            slow_type(rating_field, "4.5", delay=0.2)  # Slow typing for rating
            top_food_field = driver.find_element(By.NAME, "top_food")
            slow_type(top_food_field, "Paneer Tikka", delay=0.2)  # Slow typing for top food
        except Exception as e:
            print(f"Error: Could not input data into the form. {e}")
            self.fail("Failed to input restaurant details into the form")

        # Step 3: Click the "Add Restaurant" button
        try:
            add_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "submit-button"))
            )
            add_button.click()
            time.sleep(2)  # Delay after clicking add button
        except Exception as e:
            print(f"Error: Could not click the Add Restaurant button. {e}")
            self.fail("Add Restaurant button not clickable")

        # Step 4: Handle the alert
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())  # Wait for the alert to appear
            alert = driver.switch_to.alert  # Switch to the alert
            alert_text = alert.text  # Get the alert text
            print(f"Alert text: {alert_text}")
            alert.accept()  # Accept (close) the alert
        except Exception as e:
            print(f"Error: Could not handle the alert. {e}")
            self.fail("Failed to handle the alert")
      
    def test_update_restaurant(self):
        driver = self.driver

        self.login()

        # Step 1: Locate the "Edit" button for the specific restaurant and scroll to it
        try:
            edit_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'restaurant-item')]//strong[contains(text(), 'Test Restaurant')]/../../div[@class='button-group']/button[@class='edit-button']"))
            )
            # Scroll to the "Edit" button
            driver.execute_script("arguments[0].scrollIntoView(true);", edit_button)
            time.sleep(2)  # Delay after scrolling to the button
            edit_button.click()  # Click the "Edit" button
        except Exception as e:
            print(f"Error: Could not find or click the Edit button. {e}")
            self.fail("Failed to locate or click the Edit button")

        # Step 2: Modify the restaurant details in the form with slow typing
        try:
            name_field = driver.find_element(By.NAME, "name")
            name_field.clear()
            slow_type(name_field, "Updated Test Restaurant", delay=0.2)

            type_field = driver.find_element(By.NAME, "type")
            type_field.clear()
            slow_type(type_field, "Updated Cuisine", delay=0.2)

            location_field = driver.find_element(By.NAME, "location")
            location_field.clear()
            slow_type(location_field, "Updated Location", delay=0.2)

            rating_field = driver.find_element(By.NAME, "rating")
            rating_field.clear()
            slow_type(rating_field, "5.0", delay=0.2)

            top_food_field = driver.find_element(By.NAME, "top_food")
            top_food_field.clear()
            slow_type(top_food_field, "Updated Food", delay=0.2)
        except Exception as e:
            print(f"Error: Could not input updated data into the form. {e}")
            self.fail("Failed to input updated restaurant details into the form")

        # Step 3: Submit the updated details
        try:
            update_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "submit-button"))
            )
            update_button.click()
            time.sleep(2)  # Delay after clicking update button
        except Exception as e:
            print(f"Error: Could not click the Update button. {e}")
            self.fail("Update button not clickable")

        # Step 4: Handle the alert
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())  # Wait for the alert to appear
            alert = driver.switch_to.alert  # Switch to the alert
            alert_text = alert.text  # Get the alert text
            print(f"Alert text: {alert_text}")
            alert.accept()  # Accept (close) the alert
        except Exception as e:
            print(f"Error: Could not handle the alert. {e}")
            self.fail("Failed to handle the alert after updating")
      
    def test_delete_restaurant(self):
        driver = self.driver

        self.login()

        # Step 1: Locate the "Delete" button for the specific restaurant and scroll to it
        try:
            delete_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//li[contains(@class, 'restaurant-item')]//strong[contains(text(), 'Test Restaurant')]/../../div[@class='button-group']/button[@class='delete-button']"
                ))
            )
            # Scroll to the "Delete" button
            driver.execute_script("arguments[0].scrollIntoView(true);", delete_button)
            time.sleep(2)  # Delay after scrolling to the delete button
            delete_button.click()  # Click the "Delete" button
        except Exception as e:
            print(f"Error: Could not find or click the Delete button. {e}")
            self.fail("Failed to locate or click the Delete button")

        # Step 2: Handle the confirmation alert
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())  # Wait for the alert to appear
            alert = driver.switch_to.alert  # Switch to the alert
            alert_text = alert.text  # Get the alert text
            print(f"Alert text: {alert_text}")
            alert.accept()  # Accept (confirm) the alert
        except Exception as e:
            print(f"Error: Could not handle the confirmation alert. {e}")
            self.fail("Failed to handle the confirmation alert after clicking Delete")

        # Step 3: Verify the restaurant has been deleted
        try:
            # Check that the restaurant no longer exists in the list
            WebDriverWait(driver, 10).until(
                EC.invisibility_of_element_located((
                    By.XPATH,
                    "//li[contains(@class, 'restaurant-item')]//strong[contains(text(), 'Test Restaurant')]"
                ))
            )
            print("Restaurant successfully deleted.")
        except Exception as e:
            print(f"Error: The restaurant was not deleted. {e}")
            self.fail("Failed to delete the restaurant or it still appears in the list")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(RestaurantManagerTest("test_registration_and_login"))
    suite.addTest(RestaurantManagerTest("test_add_restaurant"))
    suite.addTest(RestaurantManagerTest("test_update_restaurant"))
    suite.addTest(RestaurantManagerTest("test_delete_restaurant"))
    return suite


if __name__ == "__main__":
    with open("test_report.html", "w") as report:
        runner = HtmlTestRunner.HTMLTestRunner(stream=report, report_title="Restaurant Management Test Report")
        runner.run(suite())
