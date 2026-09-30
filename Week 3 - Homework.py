##### Week 3 Homework #####
##### CSEC-380/480 Advanced Cybersecurity Automation - Kurt Wickboldt ####


'''
#1) 1 Points: Create a GitHub account with a new public repo titled "DePaul Cybersecurity Automation Test"
Inside this repo:
    a: Create a readme file with the text "This is a sample readme"
    b: Create a new branch called "Step B" and add the contents of sample_script.py as a new file. 
       This file should be in the root directory. Commit your changes to the branch.
    d: Open a pull request and merge your Step B branch into the master/main branch
    e: Create a new branch called "Step E" and add a "def hello_world()" 
       function that returns a string "Hello World!". 
       Commit your changes but do not merge them into the main branch.
    f: Submit the link to your repo in this assignment. 
       (Make sure your repo is public and readable to anyone. 
       The link should include your repo, not just your profile!)
'''
print(
    "1F. Link to GitHub Repo: https://github.com/Het-Kotadiya/DePaul-Cybersecurity-Automation-Test.git"
)


'''
#2) 2 Points: During your pentest you find a website that you believe to be of high value:
              (https://my.cdm.depaul.edu/v2/Public/Schedule?Department=CSEC&CourseNumber=&Quarter=1&Year=2027)
You decide to probe it to find all course information so you can use that information at a later date.
You must use BeautifulSoup for this function.

    2.1 Write a function that will ingest a URL and collect the following information:
      - Course Title
      - When the Course Meets (Weekday doesn't have to be included, but fine if you do)
      - Where the course Meets (It's ok if the formatting for online only classes is a little off)

    2.2 The same function should print out the course information in order. i.e.
        CSEC 440 Information Security Management
            W 5:45PM - 9:00PM
            Lewis Center Room 1110 LEWIS 01110, Loop
            W 5:45PM - 9:00PM
            Online:Sync-Classroom Link Online

        CSEC 428 It Risk Management
            M 5:45PM - 9:00PM
            Online: Sync Online
            
        CSEC 594 Computer Information and Network Security Capstone
            M 5:45PM - 9:00PM
            CDM Center 214 CDM 00214, Loop
            -
            Online: Async Online
        ...

    NOTE: This problem is only to be done against the CDM URL.
'''

def get_courses(site_name):
    pass
    # Print parsed courses

print(f"Problem 2.2:")
get_courses('https://my.cdm.depaul.edu/v2/Public/Schedule?Department=CSEC&CourseNumber=&Quarter=1&Year=2027')


'''
#3) 2 Points: Create a function 'capture' that will query a webpage for a list of top URLs, and
take a homepage screenshot for each of the top 10.  Use the following URL for the script:
https://raw.githubusercontent.com/bensooter/URLchecker/master/top-1000-websites.txt

Return the list of sites to the user, and save the top 10 screenshots to the CURRENT DIRECTORY.
The filename should be of the website. i.e. google.png, facebook.png

Note: Your script is expected to pull content directly from
the URL meaning if the URL were to change, so would the results of your script.
You may use any combination of OS, Selenium, Requests, and BeautifulSoup.
If you have a reason to use a different library, please check with me first.
'''

def capture(url):
    top_ten = []
    return top_ten

url = 'https://raw.githubusercontent.com/bensooter/URLchecker/master/top-1000-websites.txt'
print(f"Problem 3: {capture(url)}")
