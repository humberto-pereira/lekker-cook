# LekkerCook: A Culinary Journey Awaits
![Home Page](lekkercook/documentation/images/device-mockup.png)
- LekkerCook is a dynamic cooking platform designed for food enthusiasts who seek a blend of flavor, and creativity. It's more than just a recipe site; it's a culinary community where passion for cooking is shared and celebrated.

## UI | UX

### Site Goals

- LekkerCook aims to achieve several key goals to enhance the culinary experience of its users:
Celebrating Culinary Diversity
We strive to represent a wide array of culinary styles, encouraging users to explore and celebrate diverse cuisines from around the world.

- Building a Cooking Community:
Our platform is designed to foster a supportive and engaging community. We aim to connect cooks of all skill levels, from beginners to experts, creating a space where knowledge and experiences are shared.

- User-Driven Experience:
We prioritize user engagement and interaction. The ability to rate, comment, and like a comment allows for a dynamic and responsive culinary experience. User feedback directly shapes the evolution of our site, ensuring a platform that resonates with our community’s needs and preferences.

- Culinary Learning and Inspiration:
We are committed to being a source of culinary inspiration. Whether it’s through detailed recipes, cooking tips, our goal is to empower users to expand their culinary skills and knowledge.

- Accessibility and Ease of Use:
LekkerCook aims to be accessible and user-friendly, offering an intuitive interface that makes discovering, and managing recipes simple and enjoyable.

### Wireframes

#### Mobile Wireframes
![Mobil Wireframes](lekkercook/documentation/images/wireframes/smartphone_group.png)
- These were the initial wireframes on what the mobile version was based on.

### Desktop Wireframes
![Desktop Wireframes](lekkercook/documentation/images/wireframes/desktop_group.png)
-These were the initial wireframes on what the desktop version was based on.

## Design
### Color Palette
![color palette](lekkercook/documentation/images/design/palette.png) 
- Background color: `#f3f5f9`
- Navbar and footer: `#ffffff` 
- Logo, footer, and body text: `#4a4a4f`
- logo: `#e82d10`
- stars: `#ffdd00`

### Typography
- Oswald

## User Stories:
- Create wireframes

- create DB diagram

- View the categories list: As a Site User, I can view a list of recipe categories so that I can choose one category of recipes.

- View the recipes list: As a Site User, I can view a list of recipes from a category so that I can select one recipe. 

- Open a recipe post: As a Site User, I can click on a recipe post so that I can read the full recipe.

- View likes: As a Site User / Admin, I can view the number of likes on each comment so that I can read the highest-rated comments

- View comments: As a Site User / Admin, I can view comments on an individual post so that I can read the conversation and read the recipe feedback from other cooking chefs

- Rate a recipe: As a Site User, I can view the recipe rating given by other users so that I can see which recipe tastes better.

- View a list of the highest-rated recipes: As a Site User / Admin, I can view a list of the highest-rated recipe posts so that I can see which is the most popular and tasty in the navigation bar.

- My favorite recipes: As a Site User, I can add a recipe to my favorites page so that I can have a list of my favorite recipes

- Account registration: As a Site User, I can register an account so that I can comment, rate recipes, and like comments from other users

- Rate a recipe: As a Site User, I can rate a recipe so that I can help other users find the best recipe

- Update and delete a post: As a Site User I can update and delete my comments so that I can correct typos or delete them if I change my mind.

- Like / Unlike: As a Site User, I can like or unlike other users comments so that I can interact with the community.

- Manage posts and images: As a Site Admin, I can create, read, update, and delete posts and images so that I can manage my blog content.

- Create drafts: As a Site Admin, I can create draft posts so that I can finish writing the content later.

- Approve comments: As a Site Admin, I can approve or disapprove comments so that I can filter out the comments.

- create README.md

- Create TESTING.md

## AGILE Development

#### LekkerCook was developed using AGILE method on git hub: 
- 1 - A user story template was created and added to the repository
- 2 - A project "LekkerCook user stories" was created
- 3 - Go to the Project tab in your repo
- 4 Click Add Project, then Go to your profile to create a new project.
- 5 - Create a new project using the Board template
- 6 - Rename the new board by clicking the name in the top left.
- 7 - Navigate to the Projects tab again in your repo. Click Add Project again and search your new board to add it
- 8 - Four boards where created: Todo, In Progress, Done, and Future Features
- 9 - Click in issue in your repo, then new select the "User Story" template and then create your issue "User Story" for the board
- 10 - Then go to projects in the right side, select LekkerCook user stories and submit the new issue, the new issue will be added to the first board "Todo"
- 11 - Select the user stories to be implemented move it to the "In Progress" board go to the IDE implement the code, when done move the implemented user stories "Issue" to the "Done" board
- 12 - Repeated the process until all the "Todo" user stories where moved to the "In Progress" implemented and then moved to the "Done board" then the project was finished with all the user stories "Issues" requirements implemented


### Database Diagram Relationship 
![Database Diagram](lekkercook/documentation/images/database-diagram/database_diagram.png)


## Features:

### Home Page "Landing Page"

### logged in nav-bar
 ![NavBar Logged-in](lekkercook/documentation/images/features/home/logged-in-navbar.png)
- When logged in, the nav bar shows the LekkerCook logo that, when clicked, redirects to the home page, the same behavior as the Home item; next, we have the categories dropdown menu containing all the recipes categories of the site. Next, we have the favorites
item that redirect to the user-favorites recipes page, and the log-out how the name suggests logs the user out.

### Logged out nav-bar
 ![NavBar Logged-out](lekkercook/documentation/images/features/home/logged-out-navbar.png)
 - When logged-out, the navbar shows the login and signUp options. The favorites item is not displayed when you are not logged-in because this feature is available only to logged-in users, and all the other nav bar features behave as logged-in.

### Hamburger menu
 ![Hamburger Menu](lekkercook/documentation/images/features/home/hamburger-menu.png)
- Medium to small screens, we have the hamburger menu with the same features.

### Home Carousel
![Home carousel](lekkercook/documentation/images/features/home/carousel.png)
- The carousel displays sliding images with subtitles. It's intended to give the user a grasp of what is available on the site. Its content is CRUD manageable on the admin panel. The carousel is only displayed on 'Home' (landing page) and on large screens.

### Welcome message 
![Welcome message](lekkercook/documentation/images/features/home/welcome-text.png)
- The welcome message is a short description of LekkerCook's philosophy, features, and goals and motivates the users to sign up and join the LekkerCook community. 

### Category Cards
![Category Cards](lekkercook/documentation/images/features/home/category-cards.png)
- The categorys cards divide recipes into categories, for example, meat, fish, dessert... and so on. It has an appealing image and an inspiring text that intends to instigate user curiosity and cook passion. The layout is Bootstrap responsive on small medium and large screens. The category cards are CRUD manageable on the admin panel, so new categories can be created, updated, or deleted, and the administrator has complete control over this feature.

### Category Cards Small Screens
![Category Cards Small](lekkercook/documentation/images/features/home/category-cards-small.png)
- An example of the cards on a small screen device

### Footer
![Footer](lekkercook/documentation/images/features/home/footer.png)
- The footer is simple; it has social media links where users can interact and make contact, letting us know what is in the user's mind and helping us to develop an even better solution.

### Category Page
- Desktop
![Meat Category Recipe Cards](lekkercook/documentation/images/features/recipe-cards/meat-category-recipe-cards.png)
- Medium Screen
![Meat Category Recipe Cards Medium Screens](lekkercook/documentation/images/features/recipe-cards/meat-category-recipe-cards-medium.png)

- The Meat category was chosen as a recipe category example. It shows a list of recipes based on meat. Each recipe is a card, like the category, with an image rating average and a favorite toggle button that adds the recipe to the user's favorite page, filing the heart icon with the red color when activated, press again the heart icon will be hollow with a blue outline and the recipe will be removed from the favorites; the favorite button is present on the recipe page as well; if you want to change the category, a category dropdown menu is displayed on the navbar for easy access to the category content, avoiding the necessity of returning to the category cards on the home page. Obs. The Category dropdown menu is not displayed on the home-page "landing page" to encourage the user to scroll down to the cards and navigate the content, but it is displayed on all other site pages. All the categories' content is CRUD manageable on the admin panel and is displayed dynamically when you create, update, or delete category content.

### Recipe Page
![Recipe Hero Image](lekkercook/documentation/images/features/recipe-page/recipe-hero-image.png)
![Recipe page Moblie](Lekkercook/documentation/images/features/recipe-page/recipe-page-mobile.png)
- To access any of the recipes and their functionalities described in this section, the user must sign up and log in. If the user tries to access without logging in, the user is redirected to the log-in page. At the top of the page, we have the recipe title, and below, we Have a high-definition recipe hero image that illustrates the recipe.

#### Recipe Rating and Recipe Text
![Recipe Rating](lekkercook/documentation/images/features/recipe-page/recipe-rating.png)
- Below the recipe image, we have the average rating score followed by the rating star icons that color it dynamically by the user click; when the number of stars that the user wishes to give to the recipe is selected, the next step is to click in the blue "rate button," and the average rating is calculated and updated without reloading the page thanks to the javascript code. And below the rating, we find the actual recipe text content.

### Add to Favorites
![Favorite button](lekkercook/documentation/images/features/recipe-page/favorite-button.png)
- Bellow the recipe and above the comments, we find the favorite button; the functionality has been described in the (Category Page section) resuming it is a toggle button that ads and removes the recipe from the user's favorite page

### Recipe Comment
![Recipe Comment](lekkercook/documentation/images/features/recipe-page/recipe-comments.png)
- Below the recipe, we find the comments section with the user's comments for this specific recipe; when the user submits a new comment, a message is displayed. Warning: The comment is awaiting the administrator's approval; when the approval is given, any user can leave a like in the comment.

### Recipe Edit and Delete Comment
![Recipe Edit Comment](lekkercook/documentation/images/features/recipe-page/edit-comment.png)
- If the user wishes, he can delete or edit the comment at any time. If the comment is edited, it has to be approved by the administrator again, even if the comment was previously approved.

### User Favorites
![Recipe Favorites](lekkercook/documentation/images/features/user-favorites/user-favorites.png)
- The user favorites is a page where the user can add or remove his favorite recipes represented by the "recipe cards" that have been described in the (Category Page); When the user clicks one of the recipe cards, it opens the page with the respective recipe, when you want to remove from favorites there is a "Remove from favorites" button.

### Mobile Favorites
![Mobile Favorites](lekkercook/documentation/images/features/user-favorites/small-favorites.png)
- The favorite page, like all LekkerCook pages, are fully bootstrap responsive in small, medium, and large screens

### Log in | signUp
![Log in](lekkercook/documentation/images/features/login-signup/login.png)
- Here, we have a simple, straightforward login page with a welcome message and a link to signUp

#### Sign Up
![signUp](lekkercook/documentation/images/features/login-signup/signup.png)
- Here is the Mobile signUp page 

## Testing
- [TESTING.md link](TESTING.md)



## Deployment

### Forking a Repository on GitHub
- Log In to GitHub: If you don't have a GitHub account, sign up.
- Find the Repository: Go to the GitHub page of the project you want to fork.
- Fork the Repository: Click the "Fork" button in the top right corner of the page.

### Cloning a Repository from GitHub
- Log In to GitHub: Make sure you are signed in.
- Access the Repository: Navigate to the project's GitHub repository page.
- Prepare to Clone: Click on the "Code" button, select one of the options (HTTPS, SSH, or GitHub CLI), and copy the link.
- Open Your Terminal: In your code editor, open the terminal.
- Set the Location: Change the current working directory to where you want the cloned directory.
- Clone: Type 'git clone', paste the link you copied, and press enter.

### Deploying to Heroku
- Setting Up an ElephantSQL Database (or Similar Service)
- Create an Account: Sign up for ElephantSQL or a similar database service.
- Set Up the Database:
- Log into ElephantSQL.
- Click "Create New Instance".
- Choose a plan, give your database a name, and select a data center.
- Review the details and create the instance.
- Copy the database URL from the dashboard.
### Creating a Heroku App
- Heroku Account: Sign up for Heroku if you haven't already.
- Create a New App:
- Go to the Heroku dashboard.
- Click "Create new app".
- Name your app (must be unique) and select a region.
- Click "Create app".
#### Configuring the Environment and Database on Heroku
- Environment File: In your IDE, create a new env.py file.
- Set Environment Variables: In env.py, import the os library and set environment variables for the database URL, a secret key,
Cloudinary Setup: If using Cloudinary, copy the API Environment variable into env.py.
Heroku Config Vars:
In the Heroku app settings, click "Reveal Config Vars".
Add key-value pairs for 
- PORT 8000
- DATABASE_URL
- SECRET_KEY
- CLOUDINARY_URL.
- Deploying the App on Heroku
- Go to the Deploy Tab: In your Heroku app's dashboard.
- Set Up GitHub Deployment:
- Choose GitHub as the deployment method.
- Connect to GitHub and select the repository.
- Deploy: Scroll down and click "Deploy Branch".

## Citation Sources

#### Credits
- HTML templates: Code Institute "I Think Therefore I Blog" project
I used the templates as an base and customized it for my needs
- Django framework: I used the code institute project as "I Think Therefore I Blog" inspiration for my project.
- Other django project sources:
- https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django
- https://www.youtube.com/watch?v=rHux0gMZ3Eg&ab_channel=ProgrammingwithMosh
- https://www.youtube.com/watch?v=PtQiiknWUcI&t=4106s&ab_channel=TraversyMedia
- https://docs.allauth.org/en/latest/
- https://docs.djangoproject.com/en/stable/topics/db/models/
- https://docs.djangoproject.com/en/stable/topics/http/views/
- https://docs.djangoproject.com/en/stable/topics/forms/
- Javascript sources:
- https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model
- https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
- https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html
- https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Manipulating_the_DOM
- https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie
- https://www.youtube.com/watch?v=cuEtnrL9-H0&ab_channel=WebDevSimplified
- bootstrap 
- https://getbootstrap.com/docs/5.3/getting-started/introduction/

#### Content
- All the Recipes text content was created by Chat gpt open AI
### Media
#### carousel images and category cards images credits
- meat-corousel-cards - https://www.pexels.com/pt-br/foto/bife-de-carne-bem-passado-e-vegetais-no-prato-299347/

- dessert-carousel-cards - https://www.pexels.com/pt-br/foto/panqueca-com-morango-fatiado-376464/

- dough-carousel-cards- https://www.pexels.com/pt-br/foto/assando-assar-coques-cozimento-9510/

- fish-carousel-cards- https://www.pexels.com/pt-br/foto/prato-de-salada-de-peixe-262959/

### recipes cards and recipe page images credits
#### meat category 

- meat balls - https://pixabay.com/illustrations/meatballs-tomato-sauce-snack-food-7517633/

- milanesa steak - https://blog.amigofoods.com/index.php/argentine-foods/milanesa/

- roast beef - https://www.delish.com/cooking/recipe-ideas/a23584914/perfect-roast-beef-recipe/


- roast-chicken - https://www.pexels.com/pt-br/foto/carne-frita-em-prato-branco-2338407/

#### dessert category

- petit gateau -https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fphotos%2Fpetit-gateau&psig=AOvVaw2B851-HRPN6TKy8cC1Aqf6&ust=1700755974899000&source=images&cd=vfe&opi=89978449&ved=0CBQQjhxqFwoTCKiz0u__14IDFQAAAAAdAAAAABAI

- cheese cake -https://kidsrezepte.de/new-york-cheesecake/

- chocolate muffins - https://www.istockphoto.com/de/search/2/image-film?phrase=chocolate+muffin

- strawberry cupcakes - https://www.google.com/url?sa=i&url=https%3A%2F%2Fpreppykitchen.com%2Fstrawberry-cupcakes%2F&psig=AOvVaw0zubud5DWrPZqXltzOtYrY&ust=1700756639837000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCNiJ4qyC2IIDFQAAAAAdAAAAABAE

#### dough category

- focaccia - https://www.google.com/url?sa=i&url=https%3A%2F%2Falexandracooks.com%2F2018%2F03%2F02%2Fovernight-refrigerator-focaccia-best-focaccia%2F&psig=AOvVaw0KxX6HYbHloKSE2-rB_h28&ust=1700757040684000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCJj23euD2IIDFQAAAAAdAAAAABAE

- pizza Margherita - https://meny.no/oppskrifter/pizza/klassisk-margherita/

- minced meat pie - https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.thebrewerandthebaker.com%2Farchives%2F1236&psig=AOvVaw3JkRjUMnbqJqIAUOI--Igw&ust=1700757595896000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCLCdy_SF2IIDFQAAAAAdAAAAABAE

- ciabatta bread - https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.italianrecipebook.com%2Fciabatta-bread%2F&psig=AOvVaw1YwsCrI3TnjdcLbBbmKOsW&ust=1700757701128000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCMjY76aG2IIDFQAAAAAdAAAAABAE

#### fish category

- steamed fish - https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.godairyfree.org%2Frecipes%2Fpan-steamed-fish-lemon-white-wine-sauce&psig=AOvVaw1m0Bsfr5BYEqyd1vimHgy5&ust=1700757823754000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOi8peGG2IIDFQAAAAAdAAAAABAE

- breaded prawns - https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.kagerer.de%2Febi-fry-garnelen-1645&psig=AOvVaw3cTRkwpPqGGvJHHPMs4OYO&ust=1700757975330000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCICsyqmH2IIDFQAAAAAdAAAAABAE

- bacalhau a bras - https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.photosandfood.ca%2F2022%2F12%2F12%2Fbacalhau-a-bras-portuguese-cod-fish-with-onions-eggs-and-fries-a-time-saving-hack%2F&psig=AOvVaw2qIvtU3Z_iOph85MetFwdi&ust=1700758054977000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCMjxts-H2IIDFQAAAAAdAAAAABAE

- tomato fish soup - https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bonappetit.com%2Frecipe%2Fbrothy-tomato-and-fish-soup-with-lime&psig=AOvVaw2IkhuvkT8oWihzTxzzdx2k&ust=1700758126688000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCLiZ-vGH2IIDFQAAAAAdAAAAABAE


