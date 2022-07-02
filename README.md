# Fetching data from HTML #
### *A program that displays selected information from a website after the user provides the URL and XPath.* ###
#### Project carried out as part of the praktycznypython.pl course. ####

### List of contents: ###
1. Description of the program operation.
2. Python modules used.
3. Tests.

![Picture](https://th.bing.com/th/id/R.3880091120f9e25c09d48747f5434e2e?rik=ciMr1g89pDmmKg&pid=ImgRaw&r=0)
Source: *https://th.bing.com/th/id/R.3880091120f9e25c09d48747f5434e2e?rik=ciMr1g89pDmmKg&pid=ImgRaw&r=0*

### 1. Description of the program operation. ###

- The program gets the URL and XPath from the command line. 
- Extracts text from HTML by removing white space from the beginning and end of the line.
- Display each HTML element on a separate line.

**Data used in the script:** Leroy Merlin store website.

### 2. Python modules used ###

- click
- lxml.html 
- pytest
- requests
- sys

### 3. Tests ###

The package contains tests to test the codes with the help of Pytest.

*Author: Marta Solarz*
