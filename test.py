import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException
import time

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
            # Wait for the "Don't have an account? Register" button to be clickable and click it
            register_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "toggle-button"))
            )
            register_button.click()
        except Exception as e:
            print(f"Error: Could not find or click on the Register button. {e}")
            self.fail("Register button not clickable")

        # Step 2: Input the registration details 
        try:
            driver.find_element(By.NAME, "username").send_keys("testuser")
            driver.find_element(By.NAME, "password").send_keys("testpassword")
            driver.find_element(By.CLASS_NAME, "submit-button").click()
        except Exception as e:
            print(f"Error: Could not input data or click submit. {e}")
            self.fail("Failed to input registration details or submit the form")

        # Step 3: Ignore any alert if registration fails and proceed
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())  # Wait for the alert
            alert = driver.switch_to.alert
            alert.accept()  # Close the alert and ignore it
        except UnexpectedAlertPresentException:
            print("No alert detected or alert ignored, proceeding to login.")

        # Step 4: Toggle back to Login form after registration (without waiting)
        try:
            # Wait for the "Already have an account? Login" button to be clickable and click it
            login_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "toggle-button"))
            )
            login_button.click()
        except Exception as e:
            print(f"Error: Could not find or click on the Login button. {e}")
            self.fail("Login button not clickable")

        # Step 5: Just click the Login button (no need to re-enter the credentials)
        try:
            driver.find_element(By.CLASS_NAME, "submit-button").click()
        except Exception as e:
            print(f"Error: Could not click submit button. {e}")
            self.fail("Failed to submit login form")

        # Step 6: Check if logged in (looking for a logout button or user-specific element)
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "logout-button"))  # Replace with actual logout element
            )
            logout_button = driver.find_element(By.CLASS_NAME, "logout-button")
            self.assertTrue(logout_button.is_displayed(), "Logout button is not visible, login failed.")
            print("Successfull in registering and loggin in")
        except Exception as e:
            print(f"Error: Could not find logout button. {e}")
            self.fail("Login failed, could not find logout button")
            
    def login(self):
        driver = self.driver

        # Step 2: Input login credentials and submit
        try:
            driver.find_element(By.NAME, "username").send_keys("testuser")
            driver.find_element(By.NAME, "password").send_keys("testpassword")
            driver.find_element(By.CLASS_NAME, "submit-button").click()
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
      except Exception as e:
          print(f"Error: Restaurant form not visible. {e}")
          self.fail("Restaurant form not visible")

      # Step 2: Fill in the form fields
      try:
          driver.find_element(By.NAME, "id").send_keys("102")
          driver.find_element(By.NAME, "name").send_keys("Test Restaurant")
          driver.find_element(By.NAME, "type").send_keys("Indian")
          driver.find_element(By.NAME, "location").send_keys("Mysuru")
          driver.find_element(By.NAME, "rating").send_keys("4.5")
          driver.find_element(By.NAME, "top_food").send_keys("Panner Tikka")
      except Exception as e:
          print(f"Error: Could not input data into the form. {e}")
          self.fail("Failed to input restaurant details into the form")

      # Step 3: Click the "Add Restaurant" button
      try:
          add_button = WebDriverWait(driver, 10).until(
              EC.element_to_be_clickable((By.CLASS_NAME, "submit-button"))
          )
          add_button.click()
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
          time.sleep(1)  # Allow scrolling to complete
          edit_button.click()  # Click the "Edit" button
      except Exception as e:
          print(f"Error: Could not find or click the Edit button. {e}")
          self.fail("Failed to locate or click the Edit button")


      # Step 2: Modify the restaurant details in the form
      try:
          name_field = driver.find_element(By.NAME, "name")
          name_field.clear()
          name_field.send_keys("Updated Test Restaurant")

          type_field = driver.find_element(By.NAME, "type")
          type_field.clear()
          type_field.send_keys("Updated Cuisine")

          location_field = driver.find_element(By.NAME, "location")
          location_field.clear()
          location_field.send_keys("Updated Location")

          rating_field = driver.find_element(By.NAME, "rating")
          rating_field.clear()
          rating_field.send_keys("5.0")

          top_food_field = driver.find_element(By.NAME, "top_food")
          top_food_field.clear()
          top_food_field.send_keys("Updated Food")
      except Exception as e:
          print(f"Error: Could not input updated data into the form. {e}")
          self.fail("Failed to input updated restaurant details into the form")

      # Step 3: Submit the updated details
      try:
          update_button = WebDriverWait(driver, 10).until(
              EC.element_to_be_clickable((By.CLASS_NAME, "submit-button"))
          )
          update_button.click()
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
          time.sleep(1)  # Allow scrolling to complete
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
    runner = unittest.TextTestRunner()
    runner.run(suite())
