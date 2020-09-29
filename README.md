[View the live project here.](https://barbiebooth.herokuapp.com/)

<h2 align="center"><img src="https://github.com/MarthGimenzo/barbiebooth/blob/master/static/images/readme/barbieboothlogo.jpg?raw=true"></h2>

As a response to an - almost traumatic - event in which my mother lost her very first Barbie Doll (it was actually the very first doll that was given away to the crowd during a huge Barbie launch event in Amsterdam, 1961), she started collecting all Barbie Dolls that were released between 1961 and 1980.</br></br>
After years of diligent tracing at collector’s events and markets, her collection was almost complete. She has collected hundreds of authentic Barbie dolls, Skippers, and Kens. All mended, and with their original clothing and outfits. Aside from that, she has a massive collection of clothing and accessories for the dolls.</br></br>
But after years of enjoying the collection, she feels it’s time to let it go. It’s also an emotional process, so why not do it step by step, in her own online store. I promised her once that if I would be able to, I would build the online store for her. So here I am taking the first step.</br></br>
The community of Barbie collectors is huge and this store needs to be a popular point for Barbie collectors all over the world. That is why every product needs a detailed description, with the original title of the Barbie/accessory along with its release year, and state of condition.</br></br>
Some dolls are extremely rare and expensive. Finding an exact copy of it will be hard. Since it is her collection she is selling, all dolls are unique, so the buyer won’t be able to change the quantity of a product. Once a product has been bought, it is marked as ‘sold’ in the database.</br></br>

## User Experience (UX)

### User stories

<h2 align="center"><img src="https://github.com/MarthGimenzo/barbiebooth/blob/master/static/images/readme/userstories.jpg?raw=true"></h2>

### Design

#### Colour Scheme

Barbie Booth utilises a colour scheme of 8 different colours. Pink and yellow colours are the mainly used colours. The pink colours are used because, of course, these are the colours of the Barbie brand. To complement this colour, mint and yellow are used. This gives the website a playful, seventies style feeling.
<div align="center">
    <img src="https://github.com/MarthGimenzo/barbiebooth/blob/master/static/images/readme/colourscheme.jpg?raw=true">
</div>

- Purple: #9a5266
- Pink: #f4b5c6
- Light Pink: #feeaf3
- White: #ffffff
- Mint: #dbe7e7
- Light Yellow: #fffda6
- Yellow: #fef568
- Dark Mint: #597a69

#### Typography

<div align="center">
    <img src="https://github.com/MarthGimenzo/barbiebooth/blob/master/static/images/readme/fonts.jpg?raw=true">
</div>

- The primary font used for Barbie Booth is called ‘Ubuntu’ and it is used in the body of all pages. The font is used because it is recognized for its easy readability, and because it has small curves, it matches the seventies feeling of the website.
- The secondary font used for Barbie Booth is called ‘Dollie Script’. It is used in the logo and most of the headers on the website. This font is chosen because it shows strong similarities with the original Barbie logo and is therefore recognizable for visitors of the website. Dollie Script has a strong seventies feeling to it, which adds to the overall feeling of the website. The logo utilizes Dollie Script with a white colour and black shadow (outlines). All headers use Dollie Script with a purple colour and every first letter of every word capitalized.

#### Imagery

- Much time has been spent on the imagery of the website. The main goal was to give the website a seventies style feeling, as it matches time period of the products on the website. Therefore, a lot of seventies style organic figures were used.
- The header of the home page uses a pink and yellow spiral which goal it is to emphasize the Barbies that slide in- and out on the left side of the page. It creates a quirky seventies style ‘showcase’ of the products on the website.
- To give the website continuity in its imagery, the spiral returns on other pages of the website as well, albeit with a much softer colour scheme so it does not distract from the content of the page.
- The spiral returns once again on the ‘Processing Transaction’ overlay when a visitor checks out. This time, the spiral image has four different versions that are part of an animation consisting of four frames. The strings of the spiral are divided into four colours of the colour scheme and with every frame each string colour jumps to the string next to it. When animated, it creates a spinning effect and adds to the impression that background processes are running.
- The main, informative section of the homepage uses a mainly light pink coloured background to distinct it from the header above it. If you look closely, you can see some stylized Barbie legs in light yellow. In the middle there’s a big, mint coloured ‘B’ in the middle of this background. It is hard to style this image as it should not be too noisy, but using a plain colour would make it too boring and would not add to a seventies feeling of the website.
- For the product images, pictures of the dolls, clothing and accessories were manually taken using a photo studio lightbox. This way, all products are lighted equally and this adds to the continuity of the imagery on the products page. The pictures are taken with a white background and plain white light, which gives a clean feeling to them.

### Mockups

In this pdf file you can find the mockups that were created for Barbie Booth using Balsamiq.</br>
It contains mockups for the following pages:

- Home
- About
- Contact
- FAQS
- Products
- Product Details
- My Profile
- Cart
- Checkout

[PDF of Mockups of Barbie Booth](https://github.com/MarthGimenzo/barbiebooth/blob/master/static/pdf/barbiebooth_mockups.pdf)

## Existing Features

### Features for visitors on every page

#### The Navbar

- On the left side, the navbar contains the logo of Barbie Booth. As is convention on websites, when clicked, the visitor is taken back to the home page.
- The ‘Dolls’ link in the navbar triggers a dropdown menu with links to different categories of barbies and a link with ‘All dolls’. Clicking on these links will take the visitor to their respective product pages. For example, when ‘Barbie’ is clicked, it will take the user to the Products page and shows only dolls in the category ‘Barbie’.
- The ‘Accessories’ link in the navbar triggers a dropdown menu with links to different categories of accessories such as shoes and bags. There is also a link with ‘All accessories’. Clicking on these links will take the visitor to their respective product pages. For example, when ‘Clothing’ is clicked, it will take the user to the Products page and shows only products in the category ‘Clothing’.
- The ‘Search’ item in the navbar triggers a dropdown search bar which the visitor can use to find all sorts of products.
- The ‘About’ link takes the visitor to the About page.
- The ‘Sign In’ link in the navbar triggers a dropdown menu with links to sign in or register as a new user. The ‘Sign In’ link is only visible when no user is logged in to the website.
- The ‘<USERNAME’> link in the navbar triggers a dropdown menu with links the signed in user’s profile and a link to log out. The link in the navbar shows the currently logged user’s username and is not visible when no user has logged in.
- The ‘Cart’ link in the navbar shows the total price of all products that are currently in their cart and when clicked takes the visitor to the ‘Cart’ page.
- The navbar collapses on devices up to medium screen size and will turn it into a dropdown menu that can be triggered using the button on the right size.

#### Authorization

- The user is able to register to the website on a separate page. A confirmation email is sent to the user.
- The user is able to retrieve his password when forgotten.
- The user is able to log in and out.
- The user is able to set up a personal profile that is connected to their account to make the checking out process easy.

#### Messages (Toasts)

- When the user performs certain actions, a message will display on the top right of the page that gives the user information about their action. When the user adds a product to their cart, it also shows a small overview of what the user currently has in their cart.

#### Footer

- The most noteworthy feature of the footer is the ‘Popular Links’ section which gives the user convenient shortcuts to different parts of the website, such as Home, About, Contact, FAQS, Privacy Policy, Terms & Conditions.

### Features for visitors

#### Homepage

- A quirky seventies style ‘showcase’ of the products on the website, with a button that leads to the products page when clicked.
- A quick introduction to the website and a link to the ‘About’ page.

#### About Page

- An introduction about my mother (the admin) and the purpose, and the ‘why’ of this project.
- Some convenient links to other parts of the website, such as Home, About, Contact, FAQS, Privacy Policy, Terms & Conditions.

#### Contact Page

- The feature to send a form with the user’s details and question or feedback. The form is sent with the submit button. The user’s feedback can be seen by the admin at the back-office of Django.
- A convenient link to go back to the homepage.

#### FAQS

- The page contains some frequently asked questions and answers.
- Convenient links to go back to the homepage or contact page.

#### Privacy Policy

- An extensive privacy policy. Though at the moment still a concept version as the website is not officially launched yet.
- Convenient links to go back to the homepage or contact page.

#### Terms & Conditions

- An extensive terms & conditions page. Though at the moment still a concept version as the website is not officially launched yet.
- Convenient links to go back to the homepage or contact page.

#### Products Page

- A list of the current products.
- Convenient category buttons at the top of the page view only products in a certain category.
- A selector to sort all products by name, price, condition, year or category, alle ascending or descending.
- A button to filter out sold products, so only available products will be viewed.
- For every product, details are shown regarding its name, year, category, condition and price.
- When a product is sold, its picture appears in grayscale with green letters: ‘Sold!’
- A small button with an arrow on the right bottom of page. When clicked the page navigates to the top.
- When ‘I need this’ is clicked the product is added to the cart and the cart contents are shown in the top right corner of the page using messages (toast).
- When clicked on the picture of a product the user is redirected to the product’s details page.

#### Product Details Page

- Full details of the product regarding the name, category condition, times viewed, the price and the description.
- A large picture of the product. It can be viewed in full detail when clicked.
- When ‘Put it in my cart!' is clicked the product is added to the cart and the cart contents are shown in the top right corner of the page using messages (toast).
- A comment section where users can place comments underneath a product and ask questions. Comments can only be placed when the user is logged in. Comments of the superuser (GeiskeZijlstra) are viewed in pink on the left side. Comments of other users are viewed on the right side in yellow.

#### Cart Page

- Full details of the product regarding the name, SKU, year, category, condition, price.
- A button with every product that removes the product from the cart when clicked.
- An overview of the total costs of the products, the delivery costs and the grand total.
- A button that leads to the checkout page when clicked.

#### Checkout Page

- An overview of the order the user is about to checkout.
- Forms where the user can enter his or her personal information and delivery information.
- A checkbox to ensure the user’s information is saved to the user’s profile.
- A stripe payment card input form.
- A button that leads the user back to the cart page so the user can adjust his or her cart.
- A button that initiates the checkout background process and leads the user to the checkout success page when the transaction succeeded.
- A loading overlay with a spinning spiral to indicate that the transaction is processing.

#### Other Features

- The website is completely responsive.
- The website contains interactive elements such as animation when hovering over the navbar buttons and other buttons throughout the site. 
- The website uses icons that were retrieved from font awesome.

### Features for the admin

- The admin or superuser can log into to the Django back-office of the website.
- The admin has the ability to view and edit the list of users and their emails and status.
- The admin has the ability to view all placed orders so they can be sent to their address.
- The admin has the ability to view the forms that were submitted by users through the contact page.
- The admin has the ability to add, delete or edit categories of products
- The admin has the ability to view, edit and delete the comments of users that were left on the product details page.
- The admin has the ability to add, delete and edit products and change their status. 

## Features for future releases

- The ability to log in to the site using social accounts.
- The ability to add more options to pay with Stripe, including iDeal.
- The ability for users to add favourites to their account.
- The ability for users to sign in for a mailing list and get updates about new products that are added to the site.

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/CSS)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1.  [GitPod](https://gitpod.io/workspaces/)
    - Gitpod was used as the IDE to develop the website in.
1.  [Google Chrome Developer Tools](https://www.google.com/intl/nl_nl/chrome/)
    - Google Developer Tools were used for checking the console and tracing issues on the website.
1.  [Django](https://www.djangoproject.com/)
    - Django was used as the python framework used to efficiently create the website.
1.  [Stripe](https://stripe.com/)
    - Stripe was used as the payment system to validate and accept the payments of the user when checking out.
1.  [AWS S3 Bucket](https://aws.amazon.com/s3/)
    - AWS S3 Bucket was used to store the images of the website.
1.  [Bootstrap 4.4.1](https://getbootstrap.com/)
    - Bootstrap 4.4.1 was used to aid with the responsiveness of the website and to utilize pre-built classes to style the website.
1.  [PIP](https://pypi.org/project/pip/)
    - PIP was used for installation of the tools that were needed for developing the website.
1.  [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
    - Boto3 was used for configuration and management of AWS S3.
1.  [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
    - Django Crispy Forms was used to easily create forms using the Bootstrap4 styles.
1.  [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
    - Django Allauth was used to enable user login, registering and password retrieval.
1.  [Django-Countries](https://pypi.org/project/django-countries/)
    - Django Countries was used to easily create a select list for selecting countries in forms.
1.  [Psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
    - Psycopg2-binary was used as a database adaptor for Python.
1.  [Gunicorn](https://gunicorn.org/)
    - Gunicorn was used to aid in deployment of the project to Heroku.
1.  [Pillow](https://pillow.readthedocs.io/en/stable/)
    - Pillow was used as a Python imaging library to process storing images into the database.
1.  [PopperJS](https://popper.js.org/)
    - PopperJS was used to aid with sliding in and out the Barbies on the homepage.
1.  [Font Awesome](https://fontawesome.com/)
    - Font Awesome was used to add icons for aesthetic and UX purposes.
1.  [jQuery](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive and to add effects by manipulating the DOM.
1.  [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal.
1.  [GitHub](https://github.com/)
    - GitHub was used to store the projects code after being pushed from Git.
1.  [Photoshop](https://www.adobe.com/nl/products/photoshop.html)
    - Photoshop was used to create backgrounds, resizing images and editing photos for the website.
1.  [Illustrator](https://www.adobe.com/nl/products/illustrator.html)
    - Illustrator was used to create backgrounds and edit pictures.
1.  [Balsamiq](https://balsamiq.com/)
    - Balsamiq was used to create the [mockups](https://github.com/MarthGimenzo/barbiebooth/blob/master/static/pdf/barbiebooth_mockups.pdf) during the design process.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.</br></br>
Some errors occured when using Flake8, but these were acceptable errors that mainly occurred in the root Django code.</br></br>

- [W3C Markup Validator](https://validator.w3.org/)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- [JJavascript Validator](http://beautifytools.com/javascript-validator.php)
- [Flake8](https://flake8.pycqa.org/en/latest/)

### Testing User Stories from User Experience (UX) Section

#### 1. As a Barbie Collector I want to be able to view a list of all available products so that I can select products from the collection to purchase.
1. When clicked on ‘DOLLS’ or ‘ACCESSORIES’ a dropdown menu appears which provides all categories and ‘ALL DOLLS’ and ‘ALL ACCESSORIES’.

#### 2. As a Barbie Collector I want to be able to view individual details of a product so that I can see the price, description, year, image and condition of the product.
1.	When clicked on a picture of a product on the product page the user is directed to the product details page of that specific product successfully. 
2.	A large image of the product is viewed along with its price, description, year and condition.
3.	When the image is clicked, a new tab is launched within the browser that views the image in full size.

#### 3. As a Barbie Collector I want to be able to view the total of my purchases so that I can see how much I will spend.
1.	The grand total of all products in the cart are displayed correctly on the right side of the navbar.
2.	When the user is on the products page, and clicks on the ‘I need this’ button, the product is added to the cart and a message (toast) appears at the top right corner of the website that displays an overview of all added products and its grand total.
3.	When the user is on the product details page, and clicks on the ‘Put it in my cart!’ button, the product is added to the cart and a message (toast) appears at the top right corner of the website that displays an overview of all added products and its grand total.
4.	When clicked on the ‘Buy this!’ button in the message (toast) that appears when a product is added, the user is directed to the Cart page.
5.	On the Cart page, the total of all products is defined, along with the delivery costs, resulting in a Grand Total, which are all correctly displayed.

#### 4. As a Barbie Collector I want to be able to ask specific questions about a product so that I can decide whether I like this product.
1.	On the product details page, a user is able to submit a comment about the specific product.
2.	The user is only able to place a comment if he is logged in. If not, the comment form is replaced with a message that tells the user to login in order to submit comments. A button is provided that gives a convenient link to the login page.
3.	If no comments have been submitted for a certain product, a message will tell that no comments have been submitted yet.
4.	All comments made by the admin/superuser are displayed in pink on the left side.
5.	All comments made by other users are displayed in yellow on the right side.

#### 5. As a Site User I want to be able to contact the store owner of the website so that I can ask about various issues that I need information about.
1.	On the contact page, a user is able to fill in a feedback form.
2.	All form fields are successfully validated and submitted when clicked on the ‘Submit!’ button.
3.	Company details are also provided so the visitor can call the store owner.

#### 6. As a Site User I want to be able to register for an account so that I can have a personal account and view my profile.
1.	When the user is not logged in, a ‘SIGN IN’ option is displayed in the navbar.
2.	When clicked on the ‘SIGN IN’ item, a dropdown menu appears that gives the user the ability to either sign up, or sign in.
3.	When clicked on the ‘Sign Up’ item, the user is redirected to the Sign Up page.
4.	The user is able to fill in a form asking twice for an e-mail, a username, and twice for a password.
5.	When clicked on the ‘Sign Up’ button, the user is automatically signed in and a confirmation e-mail is sent to the user. Messages (toasts) display on the top right corner of the page to inform the user about this.
6.	When the user is logged in, the username is displayed on the right side of the navbar.
7.	When clicked on the username, a dropdown menu appears that gives the user the option to view his or her profile, or sign out.
8.	When clicked on ‘My Profile’, the user is directed to the ‘My Profile’ page, where delivery information can be entered and stored, and the order history can be viewed.

#### 7. As a Site User I want to be able to login and logout so that I can access personal account information.
1.	When the user is logged in, the username is displayed on the right side of the navbar.
2.	When clicked on the username, a dropdown menu appears that gives the user the option to view his or her profile, or sign out.
3.	When clicked on ‘My Profile’, the user is directed to the ‘My Profile’ page, where delivery information can be entered and stored, and the order history can be viewed.

#### 8. As a Site User I want to be able to have a personalized user profile so that I can view order history and save payment information.
1.	When the user is logged in, the username is displayed on the right side of the navbar.
2.	When clicked on the username, a dropdown menu appears that gives the user the option to view his or her profile, or sign out.
3.	When clicked on ‘My Profile’, the user is directed to the ‘My Profile’ page, where delivery information can be entered and stored, and the order history can be viewed.

#### 9. As a Site User I want to be able to recover my password in case I forgot it so that I can re-gain access to my account.
1.	When the user is not logged in, a ‘SIGN IN’ option is displayed in the navbar.
2.	When clicked on the ‘SIGN IN’ item, a dropdown menu appears that gives the user the ability to either sign up, or sign in.
3.	When clicked on ‘Sign In’, the user is directed to the ‘Sign In’ page.
4.	When clicked on ‘Forgot Password?’, the user is directed to the ‘Password Reset’ page.
5.	When the user enters his or her e-mail in the form and clicks the ‘Reset My Password’ button, an e-mail is sent to the user.
6.	When clicked on the link in the e-mail, the user is redirected to the ‘Change Password’ page.
7.	The user is provided with two form fields to enter a new password. When clicked on ‘Change My Password’, the password is successfully changed.

#### 10. As a Barbie Collector want to be able to sort the list of available dolls and accessories so that I can identify best condition, best priced and categorically sorted products.
1.	When clicked on ‘DOLLS’ or ‘ACCESSORIES’ a dropdown menu appears which provides all categories and ‘ALL DOLLS’ and ‘ALL ACCESSORIES’.
2.	When clicked on a certain category the user is directed to the products page on which the products of a selected category (or all products) are successfully displayed.
3.	When clicked on the ‘SORT BY’ selector, users are able to sort products by price, condition, year, name and category, all ascending or descending. This sorting selector works correctly and works immediately.

#### 11. As a Barbie Collector want to be able to sort on specific categories of dolls/accessories so that I can see what dolls and accessories are available in certain categories.
1.	When clicked on ‘DOLLS’ or ‘ACCESSORIES’ a dropdown menu appears which provides all categories and ‘ALL DOLLS’ and ‘ALL ACCESSORIES’.
2.	When clicked on a certain category the user is directed to the products page on which the products of a selected category (or all products) are successfully displayed.
3.	When clicked on a certain category at the top of the products page, the user is redirected to the same page, but only with products in that specific category.

#### 12. As a Barbie Collector want to be able to search for a doll/accessory by name, description or year so that I can look for a specific type of doll or accessory.
1.	When clicked on the ‘SEARCH’ item in the navbar, a dropdown search bar appears.
2.	The user is able to enter a specific term and click on the magnifying glass to submit the search query.

#### 13. As a Barbie Collector want to be able to see what I’ve searched so that I can decide whether the product I want is in the collection.
1.	When the user enters a term in the search form and clicks on the magnifying glass icon, the user is directed to the products page.
2.	Only products are viewed within the search terms based on name, description and year successfully.

#### 14. As a Barbie Collector want to be able to filter products that are available so that I can view only products that are available to buy.
1.	On the products page, when a user toggles the ‘Only Available’ checkbox, products that are not available (sold) are immediately filtered out and not displayed within the product list.

#### 15. As a Barbie Collector want to be able to view the items in my cart to be purchased so that I can see the total cost of my purchase and the items I will buy.
1.	On the ‘Checking Out’ page, an overview of the products in the cart is displayed, along with the order total, delivery costs and the grand total.

#### 16. As a Barbie Collector want to be able to enter my payment information so that I can check out.
1.	On the ‘Checking Out’ page, the user is able to enter his or her information details and delivery information in a form. The user is also able to enter credit card credentials.
2.	When the user is logged in, a checkbox is displayed that saves the user’s information to his or her account when the user checks out.

#### 17. As a Barbie Collector want to be able to feel my payment information is secure so that I can provide the information to make a purchase.
1.	Credit card information is successfully validated by Stripe.
2.	Transactions will fail should webhooks detect any issues.
3.	While processing the transaction, a loading overlay with a spinning spiral is displayed that gives the user a true impression that background processes are running.
4.	Should anything go wrong during transaction processing, the user is informed with a message displayed beneath the credit card input form field
5.	If the payment was successful, the user is directed to the ‘Checkout Success’ page.

#### 18. As a Barbie Collector want to be able to get a confirmation (by mail) after a purchase so that I can verify no mistakes were made.
1.	If the payment was successful, the user is directed to the ‘Checkout Success’ page and a confirmation e-mail is sent to the user regarding the order number, date, order total, delivery costs, grand total and delivery address.

#### 19. As a Store Owner I want to be able to add a product so that I can add new dolls and accessories to my store.
1.	The admin is able to login to the Django back-office environment by adding ‘/admin’ to the base url of the website and log in using the admin’s username and password.
2.	When clicked on ‘Products’, the admin is able to see an overview of all products.
3.	When clicked on ‘add product’, the admin is able to add a product by inputting the following details: category, sku, name, description, views, price, condition, an image and availability.
4.	When clicked on ‘save’, the product is successfully added.

#### 20. As a Store Owner I want to be able to edit/update a product so that I can change the product prices, descriptions, availability and image.
1.	The admin is able to login to the Django back-office environment by adding ‘/admin’ to the base url of the website and log in using the admin’s username and password.
2.	When clicked on ‘Products’, the admin is able to see an overview of all products.
3.	When clicked on the sku of a specific product, the admin is redirected to that products back-office page.
4.	The admin is able to edit the details and save successfully.

#### 21. As a Store Owner I want to be able to delete a product so that I can remove dolls and accessories that I don’t want to view in my store anymore.
1.	The admin is able to login to the Django back-office environment by adding ‘/admin’ to the base url of the website and log in using the admin’s username and password.
2.	When clicked on ‘Products’, the admin is able to see an overview of all products.
3.	The admin is able to select certain products.
4.	The admin is able to select an action in the dropdown input at the top of the page and select ‘delete selected products’.
5.	When clicked on ‘Go’ the selected products are successfully deleted.

#### 22. As a Store Owner I want to be able to view feedback of users so that I can respond to the feedback and get in touch with my customers.
1.	The admin is able to login to the Django back-office environment by adding ‘/admin’ to the base url of the website and log in using the admin’s username and password.
2.	When clicked on ‘Contact’, the admin is able to see an overview of all submitted contact forms.
3.	When clicked on a specific name, the admin can see the full details of that contact feedback, including an e-mail address, so the admin can respond.

#### 23. As a Store Owner I want to view and edit comments for products so that I can control what comments are being submitted and delete inappropriate comments.
1.	The admin is able to login to the Django back-office environment by adding ‘/admin’ to the base url of the website and log in using the admin’s username and password.
2.	When clicked on ‘Comments’, the admin is able to see an overview of all submitted comments.
3.	When clicked on a specific name, the admin can see the full details of that comment.
4.	When clicked on the ‘Delete’ button in the left bottom corner of the page, the admin is asked if she is sure she wants to delete this comment.
5.	When clicked on ‘Yes, I’m sure’, the comment is successfully deleted.

### Further Testing
- The Website was tested on Google Chrome, Microsoft Edge and Mozilla Firefox and everything works as it’s supposed to.
- Using responsinator.com, the website was viewed on a variety of devices.
- Asked friends to review the website and adjusted the site based on their feedback.

### Known Bugs
- On several mobile devices, when the website is viewed, the Barbie on the homepage is displayed lower than it’s supposed to. It overflows the header’s border but as of now I am not sure why this is happening.
- On the contact page, when submitting a form, the message (toast) at first appeared, but with a 0% opacity. I experienced this as a strange issue as the JavaScript for this is loaded in the base.html file and on other pages the message appears with full opacity. I found a solution for this by adding the JavaScript code separately on the bottom of the contact.html page which fixed the issue. Yet I am still not sure why this is needed only on this page.

## Deployment

### Heroku Deployment

Deployment of Barbie Booth to Heroku has been done by the following steps:

1.	A new app was created on the Heroku Dashboard.
2.	Added Heroku Postgress as addon in the Heroku Dashboard.
3.	Installed dj_database_url in GitPod.
4.	Installed psycopg2-binary in GitPod.
5.	Added the Postgress DATABASE_URL to settings.py.
6.	Made migrations.
7.	Installed gunicorn in GitPod.
8.	Created a Procfile.
9.	Added ‘barbiebooth.herokuapp.com’ to ALLOWED_HOSTS in settings.py
10.	Initialized Heroku Git remote using the command: Heroku git:remote -a barbiebooth.
11.	Pushed to Heroku.
12.	Added a bucket on AWS S3 for Barbie Booth.
13.	Setup AIM on AWS, setup policies, user group, users and acces keys.
14.	Installed boto3 in GitPod.
15.	Installed django_storages in GitPod.
16.	Added the AWS access keys to settings.py and added them to the config vars in Heroku.

### Run Project Locally

You can run the project locally in your IDE by following these instructions: PIP, Python3 and Git need to be installed on your computer.

1.	On the GitHub repository of Barbie Booth, click clone or download;
2.	Click ‘Download ZIP;
3.	Unpack the downloaded ZIP file;
4.	Open the index.html file with your preferred IDE;
5.	Keep in mind that the following following packages need to be installed (from the requirements.txt):
    1. asgiref==3.2.10
    2. boto3==1.14.51
    3. botocore==1.17.51
    4. dj-database-url==0.5.0
    5. Django==3.1
    6. django-allauth==0.42.0
    7. django-countries==6.1.3
    8. django-crispy-forms==1.9.2
    9. django-forms-bootstrap==3.1.0
    10. django-storages==1.9.1
    11. docutils==0.15.2
    12. gunicorn==20.0.4
    13. jmespath==0.10.0
    14. oauthlib==3.1.0
    15. Pillow==7.2.0
    16. psycopg2-binary==2.8.5
    17. python3-openid==3.2.0
    18. pytz==2020.1
    19. requests-oauthlib==1.3.0
    20. s3transfer==0.3.3
    21. sqlparse==0.3.1
    22. stripe==2.50.0

## Credits

### Code

Developing this website was based on lessons from Code Institute. The lessons were mainly used to setup the structure of the html and to create models and views. There is some JavaScript that was directly taken from these lessons. In particular:
-	The remove item and reload cart JavaScript on the ‘What You Picked’ page.
-	The scroll to top of page JavaScript on the ‘Products’ page.
-	The refresh page and sort products when the selector is changed JavaScript on the ‘Products’ page.

Also, code from Bootstrap 4 was used:
- Bootstrap4: Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.











