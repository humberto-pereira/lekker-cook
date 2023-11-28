
# Testing

## Validator Testing
### HTML
- No errors were returned when passing through the official [W3Cvalidator](https://validator.w3.org/nu/?doc=https%3A%2F%2Flekker-cook-00ac4ef685fa.herokuapp.com%2F)
### CSS
- No errors were found when passing through the official [jigsaw validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Flekker-cook-00ac4ef685fa.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=pt-BR)
### Python
- No errors were found when passing through the CI Python Linter [CI Python Linter](https://pep8ci.herokuapp.com/)
### Javascript
- No errors were found when passing through jshint Linter [jshint Linter](https://jshint.com/)


## Manual Testing
|Feature|Expect|Action|Result|
|--|--|--|--|
|navbar Home and logo| when clicked redirect to the Home page|clicked Home and logo on the navbar|Home page opened when clicked
|navbar favorite|when clicked redirect to the favorite page|clicked Favorite on the navbar|Favorite page opened when clicked|
|navbar Categories dropdown menu|when clicked a menu with all the categories should dropdown and when clicked on one category should open the selected category page|clicked on Categories on navbar and in all of the recipe categories|The categories menu dropped down, and all the recipe categories opened their respective category page.
|navbar login|when clicked redirects to the login page|clicked on login on navbar|login page opened when clicked|
navbar signup|when clicked redirects to the signup page|clicked on the signup on navbar|signup page opened when clicked|
navbar logout|when clicked ask if I'm sure I want to logout and when I click logout again should log me out|clicked on logout on the navbar|logout page opens, when I clicked logout again I was logged out|
|carousel|carousel should display a slide of images|when I open the home page|the carousel starts a automatic image slide|
|categories cards|when clicked should open their respective category page|clicked in all category cards|all of the cards opens their respective recipe category page
footer social media link icons|when clicked it opens new tab with the respective social media page|clicked in all social media link icons|all the links opens in a new tab|
categories page|when I click in any of the recipe cards it opens the respective recipe page|clicked on all recipe cards|all the cards opens its respective recipe page|
categories page recipe cards rating| it displays the average rating for its respective recipe|opened all the categories pages|all the recipe cards displays the average rating|
|categories page recipe cards favorite toggle button|when clicked it turns red and the recipe is added to the favorites page when pressed again it loses the red color and the recipe is removed from favorites page|clicked in the favorite button "add" and clicked again "remove"|all the recipes can be "added" or "removed" from the favorite pages and the toggle button display its two different states accordingly|
recipe page title and image|to open the recipe page must be logged in, if not logged in the user is redirected to the login page. When opened the recipe page should display the title followed by its image|opened all recipe pages|when not logged in the user is redirected to the login page. All recipe page displays the recipe title and image|
recipe rating|when you click on the star icons it should fill with the yellow color representing your rating 1 to 5 stars next click on the rating button bellow to apply your rating and immediately the average rating is updated|rated all the recipes|all recipe pages rating works accordingly|
recipe page text content|the recipe text content should be displayed with the correct formatting|opened all recipe pages|all recipes texts displays with the correct formatting|
recipe page favorites toggle button|when clicked it turns red and the recipe is added to the favorites page when pressed again it loses the red color and the recipe is removed from favorites page|clicked in the favorite button "add" and clicked again "remove" from favorites|all the recipes can be "added" or "removed" from the favorite pages and the two toggle button different display state works accordingly|
recipe page comments|the comment box and user comments are displayed on the bottom of the page after the recipe text. When write and submit a comment it should display the message "Your comment is awaiting approval" when your comment is approved it's published and visible to all user in addition you can edit and delete your comment any time; when the comment is edited it requires new approval|wrote and submitted a comment, edited, and deleted |the warning message:"Your comment is awaiting approval" is displayed; when the comment is approved by the administrator the warning message is removed and the comment is published to all users. When edited the warning message is displayed again until approval and deleted the comment an it worked accordingly.|
recipe page like a comment|click on the thumbs up icon and add 1 to the number of likes of the specific comment click again and it remove the like|clicked on the like icon two times|the number of likes increased +1 clicked again removed the like -1|
favorite page|you must be logged in to access the favorite page when not logged in the favorite navbar link is not displayed. The favorite page display all the favorite recipes cards that the user favorited when click on any recipe card it open its specific recipe|clicked on the favorite navbar link when logged in. clicked on a specific favorited recipe card|open the favorite page containing all the favorited recipes cards when clicked on a card it opens it respective recipe page. when logged out the favorite navbar access link is not displayed|
login page|when the user fill the username and password field and click on the login button it login and redirect to the home page if credential is wrong a warning message is displayed|filed wrong credentials and filed correct credentials|when filed the wrong credentials a warning message is displayed and when filled correct credential successfully logged in and redirected to the home page|
sign up page|when user fill username, password and confirm the password it creates user credentials log in and redirects to the home page|fill the required credential fields and use already taken username|when the user filled the required fields with valid data it creates an user account the user is logged in and redirected to the home page when the required field is filled with invalid or taken username a warning message is displayed and the user must try again|
Responsive Design|all the pages are bootstrap responsive to small, medium, and large screens devices|when opens the page on small, medium, and large screen the content is reorganized to fit the different screen sizes |Opened all the pages in different screen sizes on Chrome inspector and the content fits all the screen flawlessly (some examples can be found in the README.MD "Features" screen shots)|

## Languages Used
HTML, CSS, JS, Python

### Frame works
- Django
- Bootstrap

### Software and Tools
- GitHub
- VScode
- GitPod
- Balsamiq
- Thechsini
- Heroku
- ElephantSQL
- Claudinary

## Installed django apps 
- 'django.contrib.admin',
- 'django.contrib.auth',
- 'django.contrib.contenttypes',
- 'django.contrib.sessions',
- 'django.contrib.messages',
- 'cloudinary_storage',
- 'django.contrib.staticfiles',
- 'cloudinary',
- 'django_summernote',
- 'blog',
- 'allauth',
- 'allauth.account',
- 'allauth.socialaccount',

### Unfixed Bugs:
- There are no unfixed bugs, but I would like to mention what I consider a development mistake in my views.py:
In my recipe_detail view function, I integrated all the functionalities: recipe page, user rating, commenting, and favorites. It's messy, and I should have been using a modular approach, slicing it into different functions. When I tried to address it, I was not able to do so. Nothing worked anymore, so I made the decision to leave how it was.




