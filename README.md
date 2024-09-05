# Coiling Clay

Coiling Clay is an indepentent boutique ceramics ecommerce store, that is focused on delivering unique, handmade ceramics that bring a touch of artistry and charm to the customers home. This website is targeted towarads individuals that value beauty and quality of handmade products.

Site users can easily add products to their cart and complete purchases. By creating an account, users unlock additional features, such as the ability to leave product reviews, comment on other users' reviews, and create wishlists for future purchases. Account holders can also view their purchase history and save shipping information, making the checkout process even smoother.

The live link for coiling clay can be found here ~ [Coiling Clay](https://coiling-clay-33e330e1c084.herokuapp.com/)

![Responsive mock up](https://github.com/user-attachments/assets/3c25dcb9-58e4-4ef0-91b8-ea4940b5d25b)

## Technologies used

- HTML
- CSS
- Javascript
- Bootstrap Framework
- Django Framework

## Tools used

- GitHub ~ App repository
- GitPod ~ Cloud-based development enviroment
- ElefantSQL ~ Postgres database
- Stipe ~ Handle payments
- AWS (Amazon Web Services) ~ Holds staic and media files for production


## Keyword research

Keyword research was conducted to gather a set of targeted keywords and long-tail keywords for this project, aimed to target and provide valuable insight for the target audience.

![keyword research](https://github.com/user-attachments/assets/949041a9-9682-45b8-b806-59b4ebf4866f)

## User Stories

A series of user stories where written and used to help guide the build process of this project. This table shows the projects user stories, split into shopper, site user and site admin based user stories:

![User Stories](https://github.com/user-attachments/assets/cd6a0be3-e75e-4077-a3b5-e308e713dc45)

A link to the repository project board can be found here ~ [Coiling Clay - Project board](https://github.com/users/Willr-hawkins/projects/12)

## Pages and Features

### Header and footer

The websites header and footer is consistent throught the whole website, the header consists of a logo which links back to the homepage, menu dropdown for naviagtion and searching funcitonality, a my account dropdown with all account funcitonality and a cart icon that will take the user to preview their cart.

![Header](https://github.com/user-attachments/assets/186cbe05-a5ba-4b7e-8672-522fbd2ad0c5)

![Navigation dropdown](https://github.com/user-attachments/assets/fd125768-ee58-45bb-ba5d-afadac9a193b)

The footer is simple but contains some key aspects of the website, it is made up of a link to the stores facebook page for advertising and a form for users to sign up to the stores newsletter created and using mailchimp.

![footer](https://github.com/user-attachments/assets/256cc4ac-2e36-4bd8-a8f6-c00d88f7c715)

#### Account Functionality
All account funcitonality for signing up and logging in is done using allauth!

For new site users the account dropdown will contain two links one for logging in and one for signing up. These links will take the user to the relevant forms.

![New user account drop down](https://github.com/user-attachments/assets/3de07023-7a01-4826-a984-4348b6e371f6)

### Log in page
![Log in form](https://github.com/user-attachments/assets/1063292e-f5ea-439d-b297-a146202c5e31)

Once a user has logged in to their account the account dropdown will have changed, they will have access to the My profile link, wishlist link and sign out link. Using the My profile link will take the user to a page that contains a form for them to fill in their defualt shipping information to their account, aswell as a section for their order history.
Using the wishlist link will take the user to a page that will hold a list of the users created wishlist aswell as a button to add new wishlists. When clicking the add wishlist link a popup form will be displayed.

![Logged in user account dropdown](https://github.com/user-attachments/assets/e3e5fc7a-f19a-4291-9612-3519cfc88815)

### My profile page
![My profile page](https://github.com/user-attachments/assets/e5990efb-93a9-488a-9e5b-59a6e07dfaf7)

### Wishlists page
![Wishlist page](https://github.com/user-attachments/assets/4ff70652-4b4f-4b54-83e4-a3aaad38099f)

![Wishlist popup form](https://github.com/user-attachments/assets/c4b608d3-c30c-4743-931b-ff2718aa6d52)

Clicking on the view button on a wishlist will take the user to a page that contains all products they have added to that particular wishlist, form there they can remove the item formthe wishlist, click the link to see the reviews on that product and quickly add it to their basket for an effecient and easy checkout. Along with the a small header section containing a button to take them back to their wishlist page, the wishlist title, a wishlist comment if the user added one and the date the wishlist was created.

![Wishlist detail page](https://github.com/user-attachments/assets/5e8b656e-16be-4eb4-aaaf-67c0dcbfe87d)

### Superuser account funcitonality
If the logged in user is the super user then they will also have gained the product management link. Using this link will take the super user to a page with a form allowing them to add new prodcuts to the store.

![Super user account dropdown](https://github.com/user-attachments/assets/1be6909e-1ba2-40e0-9df7-20b45c66ba51)

![Product management page](https://github.com/user-attachments/assets/b793aa0b-6591-4c2a-94f0-52c7ead0dd43)

### Sign up page
![Sign up page](https://github.com/user-attachments/assets/a34d0026-611e-457d-9c43-c8dc0e624f25)

Once a user has filled in the sign up form they will be taken to page asking them to confirm their email. They will be sent an email to the email used to sign up and from their they can use the link in the email which will take them back to the website on a new page allowing them to confirm the email.

![Confirm email page](https://github.com/user-attachments/assets/7f94c556-28dd-4eb3-8e0b-027547f0a0dc)

#### Confirmation email
![Confirmation email](https://github.com/user-attachments/assets/7f3b1ea0-4b8a-4650-bd7a-14d264174bbd)

#### Confirmation page from email
![Confirmed email page](https://github.com/user-attachments/assets/88defda5-a831-4044-b76e-b162caee9bab)

### Home page

The home page for this project consits of a hero image of one of the stores products which contains a button that user can click to take them to the stores collection of products, at the top of the page there is a banner lettting users know how much to spend to get free shipping. Below this is a brief description of the store and their values.

![Home page hero image](https://github.com/user-attachments/assets/ec88323b-8713-472a-b476-9afe80ef8ebd)

![Home page description](https://github.com/user-attachments/assets/ee54a796-07fc-49fe-a016-d0116b74273f)

### Products page

The products page for this webiste consists of a series of cards, with each card containing an individual product with its product image, product name, price and rating.

![Product page](https://github.com/user-attachments/assets/875d2b9c-6a6b-4904-964e-25230bfbf903)

This page can be filtered in different ways the first way is by using the sort by dropdown on the page itself, using this users can sort the products by name, price and rating. The second way user can filter this page is by using the category links in the header menu section, clicking on a particular category will take the user to the prodcut page but with only the products from that category. The last way to filter this page is via the search bar in the header menu section, from here users can search for a specific think (e.g. blue mug) and only the results from that search will be shown.

#### Sort by dropdown
![Page filter dropdown](https://github.com/user-attachments/assets/04d483f3-4b12-4fed-8df8-448fe0cb177c)

#### Navigation links
![Navigation links](https://github.com/user-attachments/assets/02818106-ac00-46c0-8c7c-21c5f1f2c3d4)

#### Search bar
![Search bar](https://github.com/user-attachments/assets/2e8751c0-a682-4622-9358-4e5ab06d919d)

#### Super user additions

For a logged in super user the product cards on the product page will have two additional links one for editing and one for deleting, allowing the superuser to easily manage products for the site.

![super user product card](https://github.com/user-attachments/assets/d1eaa760-21f5-4b2a-9752-20e35f9e64db)