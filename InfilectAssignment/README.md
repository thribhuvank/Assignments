

Weathershopper:

Note: Each page will have an 'i' icon that you can click and read the task you need to complete.Please read the Instructions by clicking on the 'i' icon before proceeding to next step.

1)Make script configurable to run across chrome,firefox,IE,Safari,edge

2)visit ://weathershopper.pythonanywhere.com/

3)Get the temperature

4)Based on temperature choose to buy sunscreen or moisturizer

5)If you choose sunscreen, then read Instructions and then add product accordingly

6)If you choose moisturizer, then read Instructions and then add product accordingly

7)Verify the cart

8)Make a payment (For card details refer --> https://stripe.com/docs/testing#cards ) The website has dummy card numbers. Don’t worry, we don’t expect you to actually pay the amount.

Solution Expectations:

1)Code should be designed within Page Object Model

2)Define all the proper variables and methods names

3)Code should work without any error

4)Use valid required assertions

Prerequisites

a) Install Python 3.x

b) Add Python 3.x to your PATH environment variable

c) If you do not have it already, get pip (NOTE: Most recent Python distributions come with pip)

d) pip install -r requirements.txt to install dependencies

e) Install Selenium

Tasks and descriptions: Task 1 : Navigate to URL a) Open https://weathershopper.pythonanywhere.com in your browser

Task 2 : If current temperature less than specific temperature navigate to moisturizer products a) Visit the URL: https://weathershopper.pythonanywhere.com/moisturizer

Task 3 : If current temperature more than specific temperature navigate to sunscreens products a) Visit the URL: https://weathershopper.pythonanywhere.com/sunscreen

Task 4: Add the least expensive moisturizer products into the cart based on conditions a) Visit the URL: https://weathershopper.pythonanywhere.com/moisturizer

Task 5: Add the least expensive sunscreen products into the cart based on conditions a) Visit the URL:https://weathershopper.pythonanywhere.com/sunscreen

Task 6: Verify product count in cart a) Verif cart count after adding specific products

Task 7: Verify cart page a) Check product details coming correctly or not

Task 8: Make payment by using dummy values a) Enter the details to the payment page and verify the success page.

How to Run:

1) Open Project in terminal

2) Navigate to tests folder

3)Execute command >py.test -v -s or pytest -v -s or py.test test_assignment.py -v -s
