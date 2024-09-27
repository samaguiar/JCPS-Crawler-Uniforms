from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize an empty dictionary to store school names and website URLs
website_list = {}

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the webpage with the list of schools
driver.get("https://www.jefferson.kyschools.us/schools/school-profile-pages")
driver.maximize_window()

# Create an explicit wait for elements to load
wait = WebDriverWait(driver, 10)

# Find all the <a> tags that link to the school profile pages
school_links = driver.find_elements(By.XPATH, '//a[contains(@href, "https://www.jefferson.kyschools.us/page/")]')

# Iterate over each school link element
for link_element in school_links:
    # Extract the text (school name) and href (URL) of the link
    school_name = link_element.text
    school_url = link_element.get_attribute('href')

    print(f"Opening school page for {school_name}: {school_url}")

    # Navigate to the school profile page
    driver.get(school_url)

    # Wait for the "School Website" link to appear on the page
    try:
        website_link_element = wait.until(
            EC.presence_of_element_located((By.XPATH, '//a[text()="School Website"]'))
        )

        # Extract the website URL
        website_url = website_link_element.get_attribute('href')
        print(f"School Website for {school_name}: {website_url}")

        # Save the school name and website URL in the dictionary
        website_list[school_name] = website_url

    except Exception as e:
        print(f"Could not find the 'School Website' link for {school_name}: {e}")

    # Go back to the list of schools to continue processing the next link
    driver.back()

# Print the final list of schools and their websites
for school, url in website_list.items():
    print(f"School: {school}, Website: {url}")

# Close the browser after finishing
driver.quit()

