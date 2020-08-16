from selenium import webdriver
from userinfo import username,password
import time
from selenium.common.exceptions import NoSuchElementException


browser=webdriver.Firefox()

def openPage(url):
    browser.get(url)
    time.sleep(5)
    
def login(username,password):
    usernameArea=browser.find_element_by_css_selector("input[name='username']")
    usernameArea.click()
    passwordArea=browser.find_element_by_css_selector("input[name='password']")
    usernameArea.send_keys(username)
    passwordArea.send_keys(password)
    loginButton=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]/button")
    time.sleep(3)
    loginButton.click()
    time.sleep(3)
    notnowButton=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
    notnowButton.click()
    time.sleep(3)
    
def followingButton():
    followingButton=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
    followingButton.click()
    time.sleep(3)
    
def getFollowingNumber():
    followingnumber=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span")
    time.sleep(1)
    return int(followingnumber.text)

def getFollowersNumber():
    followerNumber=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span").text
    time.sleep(1)
    return int(followerNumber)

def follow(page,followrange):
    i=1
    count=0
    url="https://www.instagram.com/"+page+"/followers/"
    openPage(url)
    login(username,password)
    followersButton=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span")
    followersButton.click()
    time.sleep(3)
    while(count<getFollowersNumber()):
        if(checkCount(count,followrange)):
            browser.close()
            break
        try:
            follow=browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li["+str(i)+"]/div/div[3]/button")
        except NoSuchElementException:
            follow=browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li["+str(i)+"]/div/div[2]/button")
            
        if(follow.text=="Takip Et" or follow.text=="Follow"):
            follow.click()
            time.sleep(1)
            count+=1
            printInfo(count)
        i+=1
            
def unfollow(unfollowrange):
    url="https://www.instagram.com/"+username+"/following/"
    i=1
    count=0
    openPage(url)
    login(username,password)
    getFollowingNumber()
    followingButton()
    while(count<getFollowingNumber()):
        try:
            user=browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li["+str(i)+"]/div/div[3]/button")
        except NoSuchElementException:
            user=browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li["+str(i)+"]/div/div[2]/button")
        user.click()
        time.sleep(1)
        unfollowuser=browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]")
        unfollowuser.click()
        time.sleep(2)
        count+=1
        printInfo(count)
        if(checkCount(count,unfollowrange)):
            browser.close()
            break
        i+=1
        
def printInfo(count):
    print(str(count)+" user followed/unfollowed.")
    
def checkCount(count,unfollowrange):
    if(count==unfollowrange):
        return True
    else:
        return False    
    


    
    
    
    
    