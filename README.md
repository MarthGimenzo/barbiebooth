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