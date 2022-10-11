# Importing Libraries Needed
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import easygui
import pandas as pd

# Setting up and connecting to the webpage using a webdriver---------------------------------------------------------------------------------------------------------------------

# Setting the path location of the Chrome web driver
web_driver = Service("X:\Data Analytics\Software\Python\Selenium\ChromeDriver.exe")

# Establishing the specific driver options along with adding extensions to the chrome driver (adblock,xpath finder)
driver_options = webdriver.ChromeOptions()
driver_options.add_extension("X:\Data Analytics\Software\Python\Selenium\SelectorsHub.crdownload")
driver_options.add_extension(r"X:\Data Analytics\Software\Python\Selenium\ublockorigin.crx")

# Creating the driver object
driver = webdriver.Chrome(service=web_driver, options=driver_options)

# Maximizing the window and specifying the site to get the data from
driver.maximize_window()
driver.get("https://www.overbuff.com/heroes")



# Getting the XPATH to all needed buttons on the Webpage ---------------------------------------------------------------------------------------------------------------

# Gathering paths to Time Frame buttons
this_week = driver.find_element(By.XPATH, "//div[normalize-space()='This Week']")
this_month = driver.find_element(By.XPATH, "//div[normalize-space()='This Month']")
last_three_months = driver.find_element(By.XPATH, "//div[normalize-space()='Last 3 Months']")
last_six_months = driver.find_element(By.XPATH, "//div[normalize-space()='Last 6 Months']")

# Gathering paths to Gaming System buttons
pc = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]")
psn = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]")
xbl = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[3]")
switch = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[4]")

# Gathering paths to Game Type buttons
quick_play = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[3]/div[1]")
competitive = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[3]/div[2]")

# Gathering paths to Role buttons
role_all = driver.find_element(By.XPATH, "//div[@class='columns twelve']//div//div[4]//div[1]")
offense = driver.find_element(By.XPATH, "//div[@class='columns twelve']//div//div[4]//div[2]")
defense = driver.find_element(By.XPATH, "//div[@class='columns twelve']//div//div[4]//div[3]")
tank = driver.find_element(By.XPATH, "//div[@class='columns twelve']//div//div[4]//div[4]")
support = driver.find_element(By.XPATH, "//div[@class='columns twelve']//div//div[4]//div[5]")

# Gathering paths to Rank buttons
rank_all = driver.find_element(By.XPATH, "//div[@class='container main']//div[5]//div[1]")
bronze = driver.find_element(By.XPATH, "//div[@class='container main']//div[5]//div[2]")
silver = driver.find_element(By.XPATH, "//div[@class='container main']//div[5]//div[3]")
gold = driver.find_element(By.XPATH, "//div[@class='container main']//div[5]//div[4]")
platinum = driver.find_element(By.XPATH, "//div[@class='container main']//div[5]//div[5]")
diamond = driver.find_element(By.XPATH, "//div[@class='container main']//div[5]//div[6]")
master = driver.find_element(By.XPATH, "//div[@class='container main']//div[5]//div[7]")
grandmaster = driver.find_element(By.XPATH, "//div[@class='container main']//div[5]//div[8]")

# Gathering paths to Stat Tab buttons
overview = driver.find_element(By.XPATH, "//div[normalize-space()='Overview']")
primary = driver.find_element(By.XPATH, "//div[normalize-space()='Primary']")
eliminations = driver.find_element(By.XPATH, "//div[normalize-space()='Eliminations']")
medals = driver.find_element(By.XPATH, "//div[normalize-space()='Medals']")

# Defining functions to gather data from tables on webpage----------------------------------------------------------------------------------------------------------------

# Function to sleep the program to make sure webpage has enough time to load data before the next button click
def click(button):

    # Sleeping the program for 0.7 seconds
    time.sleep(0.7)

    # Performing the button click on the webpage
    button.click()

# Function to create dataframes for each stat tab on the webpage tables.
def create_df(stats,number_rows):

    # Checking to make sure the stat value matches to ensure right dataframe is created
    if(stats == overview):

        # Creating the dataframe with n number of rows and columns already specified
        overview_df = pd.DataFrame(index=range(number_rows),columns=['time_frame','system','game_type','role','rank','stats','hero', 'class', 'pick_rate','win_rate','tie_rate','on_fire'])

        # Returning the dataframe that was created
        return overview_df

    # Checking to make sure the stat value matches to ensure right dataframe is created
    if(stats == primary):

        # Creating the dataframe with n number of rows and columns already specified
        primary_df = pd.DataFrame(index=range(number_rows),columns=['time_frame', 'system', 'game_type', 'role', 'rank', 'stats', 'hero', 'class', 'elims_per_game','obj_kills_per_game','obj_time_per_game','damage_per_game','healing_per_game'])

        # Returning the dataframe that was created
        return primary_df

    # Checking to make sure the stat value matches to ensure right dataframe is created
    if(stats == eliminations):

        # Creating the dataframe with n number of rows and columns already specified
        eliminations_df = pd.DataFrame(index=range(number_rows),columns=['time_frame', 'system', 'game_type', 'role', 'rank', 'stats', 'hero', 'class', 'elim_death_ratio','elims_per_game','solo_kills', 'final_blows'])

        # Returning the dataframe that was created
        return eliminations_df

    # Checking to make sure the stat value matches to ensure right dataframe is created
    if(stats == medals):

        # Creating the dataframe with n number of rows and columns already specified
        medals_df = pd.DataFrame(index=range(number_rows),columns=['time_frame', 'system', 'game_type', 'role', 'rank', 'stats', 'hero', 'class', 'medals_per_game','gold_per_game','silver_per_game', 'bronze_per_game','cards_per_game'])

        # Returning the dataframe that was created
        return medals_df

# Function created to clean the data from the webpage table and return the cleaned data
def clean_data(hero_data,time_frame,system,game_type,role,rank,stats):

    # Removing blank values from the front of the list
    hero_data.pop(0)

    # Separating values connected by \n in the output data
    character_and_role = hero_data[0].split('\n')

    # Removing the original data that was connected with \n and replacing it with the separated values
    hero_data.pop(0)

    # Inserting data into the front of the list
    hero_data.insert(0, character_and_role[1])
    hero_data.insert(0, character_and_role[0])
    hero_data.insert(0, stats.text)
    hero_data.insert(0, rank.text)
    hero_data.insert(0, role.text)
    hero_data.insert(0, game_type.text)
    hero_data.insert(0, system.text)
    hero_data.insert(0, time_frame.text)

    # Returning the cleaned data
    return hero_data

# Function created to append the data being retrieved to the dataframes created in the create_df function
def append_df(ow_df,row,cleaned_data):

    # Looping through the cleaned data and appending it to the dataframes
    for col in range(0, len(cleaned_data)):
        ow_df.loc[row,ow_df.columns[col]] = cleaned_data[col]

    # Returning the final dataset
    return ow_df

# Function to scrape the data from the webpage given specific parameters
def scraper(time_frame,system,game_type,role,rank,stats):

    # Locating the specified search criteria by clicking filter buttons for the table on the webpage
    click(time_frame)
    click(system)
    click(game_type)
    click(role)
    click(rank)
    click(stats)

    # Getting the rows and columns of the filtered table
    number_rows = len(driver.find_elements(By.XPATH, "//table/tbody/tr"))
    number_cols = len(driver.find_elements(By.XPATH, "//table/thead/tr/th"))

    # Getting the created dataframe specific to the stat table entered by the user
    ow_df=create_df(stats,number_rows)

    # Iterating through the rows and columns of the filtered table on the webpage to collect the data
    for row in range(1,number_rows+1):
        # Establishing a list to collect the data from each row
        hero_data= []
        for col in range(1,number_cols+1):
            # Appending the values in each row to the hero_data list
            hero_data.append(driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[4]/div[1]/div[2]/table[1]/tbody[1]/tr["+str(row)+"]/td["+str(col)+"]").text)

        # Sending data collected from the button clicks to extract text and be cleaned up
        cleaned_data = clean_data(hero_data,time_frame,system,game_type,role,rank,stats)

        # Appending the cleaned values and the values in the list hero_data to the dataframe
        ow_df=append_df(ow_df,row-1,cleaned_data)

    # Sending the final dataframe to be converted into csv file
    df_to_csv(ow_df,time_frame,system,game_type,role,rank,stats)

# Function to convert the final dataframe to a csv file
def df_to_csv(final_df,time_frame,system,game_type,role,rank,stats):

    # Converting the final dataframe to a csv file
    final_df.to_csv(time_frame.text.replace(" ", "") + "_" + system.text + "_" + game_type.text.replace(" ", "") + "_" + role.text + "_" + rank.text + "_" + stats.text, sep=",",encoding='utf-8')

# Function to close and quit the webdriver once data has been collected
def close_driver():

    # Closing the webdriver page
    driver.close()

    # Quit running the webdriver
    driver.quit()

# Defining the main function for the program -------------------------------------------------------------------------------------------------------------------------

# Main function where all program calls are made
def main():

    # Message to tell user not to close/minimize the tab until program is done
    easygui.msgbox("Please DO NOT close/minimize the tab until program has finished running. A message will be displayed once the program has finished.",title="WARNING")

    # Calling the web scraper function to collect the data
    scraper(last_six_months,pc,competitive,tank,grandmaster,primary)

    # Message to tell the user the program has successfully completed
    easygui.msgbox("The program has finished, you may now close/minimize the tab.", title="PROGRAM FINISHED")

    # Closing the Webdriver
    close_driver()


# Calling the main function of the program
main()