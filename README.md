# Coiling Clay

Coiling Clay is an independant ceramics ecommerce store, that is focused on delivering unique, handmade ceramics that bring a touch of artistry and charm to the customers home. This website is targeted towarads individuals that value the beauty and quality of handmade products.

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

The websites header and footer is consistent through out the whole website. The header consists of a logo which links back to the homepage, menu dropdown for naviagtion and searching funcitionality, a my account dropdown with all account funcitionality and a cart icon that will take the user to preview their cart.

![Header](https://github.com/user-attachments/assets/186cbe05-a5ba-4b7e-8672-522fbd2ad0c5)

![Navigation dropdown](https://github.com/user-attachments/assets/fd125768-ee58-45bb-ba5d-afadac9a193b)

The footer is simple but contains some key aspects of the website. It is made up of a link to the stores Facebook page for advertising, and a form for users to sign up to the stores newsletter created and using mailchimp.

![footer](https://github.com/user-attachments/assets/256cc4ac-2e36-4bd8-a8f6-c00d88f7c715)

#### Account Functionality
All account funcitonality for signing up and logging in is done using allauth!

For new site users the account dropdown will contain two links: one for logging in and one for signing up. These links will take the user to the relevant forms.

![New user account drop down](https://github.com/user-attachments/assets/3de07023-7a01-4826-a984-4348b6e371f6)

### Log in page
![Log in form](https://github.com/user-attachments/assets/1063292e-f5ea-439d-b297-a146202c5e31)

Once a user has logged in to their account, the account dropdown would have changed. They will have access to the My Profile link, wishlist link and sign out link. Using the My profile link will take the user to a page that contains a form for them to fill in their defualt shipping information to their account, aswell as a section for their order history.
Using the wishlist link will take the user to a page that will hold a list of the users created wishlist aswell as a button to add new wishlists. When clicking the add wishlist link a popup form will be displayed.

![Logged in user account dropdown](https://github.com/user-attachments/assets/e3e5fc7a-f19a-4291-9612-3519cfc88815)

### My profile page
![My profile page](https://github.com/user-attachments/assets/e5990efb-93a9-488a-9e5b-59a6e07dfaf7)

### Wishlists page
![Wishlist page](https://github.com/user-attachments/assets/4ff70652-4b4f-4b54-83e4-a3aaad38099f)

![Wishlist popup form](https://github.com/user-attachments/assets/c4b608d3-c30c-4743-931b-ff2718aa6d52)

Clicking on the view button on a wishlist will take the user to a page that contains all products they have added to that particular wishlist. From there, they can remove the item form the wishlist, click the link to see the reviews on that product and quickly add it to their basket for an efficient checkout. Along with the a small header section containing a button to take them back to their wishlist page, the wishlist title, a wishlist comment if the user added one and the date the wishlist was created.

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

This page can be filtered in different ways. The first way is by using the sort by dropdown on the page itself. Using this, users can sort the products by name, price and rating. The second way user can filter this page is by using the category links in the header menu section. Clicking on a particular category will take the user to the prodcut page but with only the products from that category. The last way to filter this page is via the search bar in the header menu section. From here, users can search for a specific item (e.g. blue mug) and only the results from that search will be shown.

#### Sort by dropdown
![Page filter dropdown](https://github.com/user-attachments/assets/04d483f3-4b12-4fed-8df8-448fe0cb177c)

#### Navigation links
![Navigation links](https://github.com/user-attachments/assets/02818106-ac00-46c0-8c7c-21c5f1f2c3d4)

#### Search bar
![Search bar](https://github.com/user-attachments/assets/2e8751c0-a682-4622-9358-4e5ab06d919d)

#### Super user additions

For a logged in super user, the product cards on the product page will have two additional links one for editing and one for deleting, allowing the superuser to easily manage products for the site.

![super user product card](https://github.com/user-attachments/assets/d1eaa760-21f5-4b2a-9752-20e35f9e64db)

### Product detail page

When a user clicks on a product on the products page, they will be taken to new page for that specific product. This page contains some additonal information about the product aswell as functionality to add the product to their cart. Under the product detail section is a small section for related products. These products are chosen at random and are from the same category as the product being viewed. Under the related products section is the review section. This section holds all reviews left on the product begin viewed aswell as a form for logged in users to leave their own review.

#### Product details
![Product details](https://github.com/user-attachments/assets/8cb2aa50-b4c2-4405-8eb2-452fa5e4b36a)

#### Related products
![Related products](https://github.com/user-attachments/assets/2099659d-7a94-4739-b934-5261499f59d2)

#### Reviews
![Reviews](https://github.com/user-attachments/assets/e0f7c2af-a8e5-4780-869c-0620e7b9317b)

If the logged in user is the reviewer then they have the options to delete or edit their review as seen above. However if the logged in user is not the reviewer, they will have the option to comment on the review. Clicking the comment button will bring up a popup comment form to fill in. Once created the commenter will then also have the option to edit or delete their comment.

#### Comment on review
![comment on review](https://github.com/user-attachments/assets/1280ee94-ee87-46b0-bcad-acf30f27840b)

#### Commment popup form
![Comment form](https://github.com/user-attachments/assets/52b8fc63-f4b0-464a-8e80-99482a5af6e3)

#### Comment edit or delete buttons
![Comment edit or delete](https://github.com/user-attachments/assets/f17af9bb-93c8-4620-b949-5e407d8a40de)

### Cart Preview page

The cart preview page can be accessed by clicking on the cart icon in the header. The purpose of this page is for users to ensure that what is in their cart is correct before proceeding to checkout. If the user doesn't have anything in their cart when they access the page, they will have a message telling them nothing is in their cart and a button to take them to the products page.

When the user does have items in their cart, there will be a list of their products with an image for each product: the product name, product sku, price, quantity and subtotal price. Users will also be able to update their cart using the quantity field and link. They will be able to change the quantity of each individual item or remove it from their cart completely.

At the bottom of the page, the user will be able to see their cart total and shipping costs if they have any and a grandtotal, aswell as buttons to securely checkout or keep shopping. If the user does have shipping costs, there will be a red message telling them how much they need to spend to get free shipping.

#### Nothing in cart
![Nothing in cart](https://github.com/user-attachments/assets/c75e7b7d-07af-49b5-9770-e179b0defe44)

#### Items in cart
![Cart page](https://github.com/user-attachments/assets/4860a729-9bb9-493d-bb78-d72a85da935e)

#### Bottom of cart page
![Cart page footer](https://github.com/user-attachments/assets/628a4eb3-77f8-40d7-b40c-c3a81b9e0ff7)

### Checkout page

The checkout page consists of two sections. A section for the order summary, where the user can see the products they have in thier order, quantities and prices. The other section is the shipping and payment details form. If the user has saved shipping info on their profile, then the shipping details will already be filled in. Otherwise they can opt to save the info once they have filled the form in. Under these two sections are two buttons, one to complete order and the other to go back to the cart preview page. There is also a red message informing the user how much they will be charged.

![Checkout page](https://github.com/user-attachments/assets/d19b9beb-ee31-4647-a7f4-10bafab11a21)

### Order confirmation page

Once a user has completed their order, the order will be processed and the user will be taken to the order confirmation page. This will display a breakdown of their order and a copy of this will also be sent to their email. Under the order detials is a button to take the user back to the homepage.

![Order confirmation page](https://github.com/user-attachments/assets/a6d0a7af-b998-44bd-8931-861ac52fd36e)

### Error pages

On the website there are custom 404 error and 500 error pages, both consisting of a message explaining the issue to the user, along with a button to take them back to the homepage. This ensures there is a consistent theme throught the whole wesbite and to keep users engaged.

#### 404 Error
![404 error](https://github.com/user-attachments/assets/95aea7c1-3950-46ed-a5ae-acd8992175df)

#### 500 Error
![500 error](https://github.com/user-attachments/assets/c31eae1d-c2e7-42c7-8e77-9e9a4cf0c345)

## Additional Features

### Messages

Throughout the website, the user will see pop up messages from the cart icon. These messages are related to the type of messages they are (success, error, warning and info), by the colour of the banner at the top of the message. Not only do user get messages but when a user adds an item to their cart they will get a success message and within the message will be a preview of their cart.

![Cart preview message](https://github.com/user-attachments/assets/475ead68-4293-4795-a101-0ceff680b18e)

### Cart icon

When a user first visits the site the cart icon will be black and show the cost as zero. However when they start adding products to the cart, the icon will change colour and the price will update to the total of those products. This allows users to keep up with how much they will have to spend without going to the cart preview page.

#### Before products are added
![Cart icon with no items](https://github.com/user-attachments/assets/eaab47b6-0991-440f-99ef-82b8784ff7be)

#### After products are added
![Cart icon with itemsd](https://github.com/user-attachments/assets/d7420548-5f1c-4d7c-b8de-f5f6bcff30bb)

### Ratings

By defualt, when a product is added to the store the rating is set to none, but when users start to leave reviews on it the rating will start to change. The rating will be an average of all reviews left on that product, and it will automatically update when reviews are created and removed. This ensures that site users are always up to date with products.

#### Defualt rating
![No rating](https://github.com/user-attachments/assets/e10fa792-4f7b-4b4c-a830-cedc8765ed37)

#### With reviews
![Rating](https://github.com/user-attachments/assets/f037ec0e-3cd2-4e86-a953-cedb25f4e26b)

### Facebook page

In the footer of the website is a link to the Coiling Clay Facebook page, the purpose of the store having a Facebook page is to boost digital marketing.

![Facebook page](https://github.com/user-attachments/assets/6c914908-3d75-47eb-915e-89ae00abdda3)

![Facebook page](https://github.com/user-attachments/assets/94885ca3-3714-4cad-b80b-3db4086ca19d)

## Design Features
The design of this website stays consistent throughtout, which keeps the user enganged.

The font used throught the website is 'Comfortaa'.

![Comfortaa font](https://github.com/user-attachments/assets/64c9a982-cdda-46a6-a87d-1c50882b14f5)

The main colours for the site where found using [Coolors](https://coolors.co/):
![coolors colour pallet](https://github.com/user-attachments/assets/691ae267-318f-4c14-a15c-2c86ac5c136c)
 - #3D3D3D (Onyx) ~ Was used for the main font colour.

 - #A39B8B (Kahki) ~ Was used for the header and footer background aswell as buttons defualt colour.

 - #F6F5F4 (White smoke) ~ was used for the main body background colour.

 - #6C757D (Slate grey) ~ was used for buttons when the user hovers over them.

## Deployment

This website was developed using gitpod workspaces and has been deployed via heroku using the following steps:

- Log in to Heroku and create an app with the name of the website.

- Go to the settings tab and create the neccessary configuration variables.

- Connect the app to the relevant GitHub repository in the deploy tab.

- Once connected ensure the app is begin deployed by the main branch of the repository.

- Then enable automatic deployments.

- Once that is set up click deploy and heroku will build the application using the specified buildpack and dependencies.

- Once the build process is complete, the URL can be used to access the deployed application.

## Testing

### Manual Testing

#### Testing Links:

- Coiling Clay logo ~ Ensured it takes the user to the homepage.

- Shop Now button ~ Ensures the button takes the user to the products page with all products shown.

- Navigation links ~ Esnured the shop navigation links take the user to the specific page related to the link (Example: Mugs link takes the user to the products page with only the products in the mugs category preseneted).

- Log in, sign up, log out ~ Tested that all these links take the user to the correct page with the correct form presented.

- My profile ~ Ensured that when the user uses this link the correct page is shown with the correct information related to their acocunt.

- Wishlist ~ Ensured this link shows the correct wishlist page with all the wishlist's related to the users account.

- Product Managment ~ Ensured that this link is only present to the superuser and takes the superuser to the correct page with the correct form.

#### Functionality Testing:

- Adding products to cart ~ Tested that the correct product was added to the users cart along with the correct quantity.

- Removing or updating products in cart ~ Tested that the user can easily edit the quantity of products or reemove the product from their cart with ease.

- Leaving a review ~ Tested that when a user creates a review the correct information is shown with their username, aswell as the rating on the product was updated correctly.

- Editing and deleting reviews ~ Tested that when a user edits thier review the information is correctly updated, also that when a user deletes a review the rating of the product is updated correctly. Ensured that only the reviewer of the review has access to the edit or delete funcitonality.

- Commenting on a review ~ Ensured that all logged in users that are not the reviewer have access to leave a review on a comment and that when done so, the correct information is shown only on that specific review.

- Editing or deleting a review ~ Ensured that only the owner of the comment has access to these funcitonalities and that when a comment is edited the comment is updated and the correct information is shown, aswell the comment is effectively removed from the comment.

- Adding shipping information/ Saving shipping information at checkout ~ Ensured that when a user has saved shipping information to their account via the my profile page that when they go to checkout the information is correctly filled in. Additionally checked that when a user opts to save shipping information at checkout that this information is correctly saved and displayed in their my profile page.

- Creating wishlist ~ Ensured that when a user creates a wishlist it is only created on their account.

- Adding to wishlist ~ Tested that when a product is added to a users wishlist it is only added to the wishlist they have specified.

- Editing or deleting wishlist's ~ When a user removes a produc from a wishlist it is effectively removed. Checkout that when a user deletes a wishlist it is effecitvely removed along with any products that where saved to it.

- Adding products ~ Esnured that only the superuser has access to add products and when a product is added it is correctly dispalyed on the products page.

- Editing or deleting products ~ Ensured that only the superuser has access to these links and that when a product is edited the information is updated correctly, aswell as enssured that when a product is deleted it is instantly removed from the site so users cannot see it.

#### Responsive Testing: 

To test how repsonsive the site is multiple devices where used:

- PC: Mac Mini, M2 chip, Runnning chrome, 27" monitor (1920x1080) ~ Tested that all pages are displayed correctly on desktop aswell as used chrome dev-tools to test the responsiviness on all sized screens.
- Tablet: Ipad Air, M1 chip, Running Safari, 10.9" display (2360x1640) ~ Tested all pages are displayed correctly on tablet in both portrait and landscape modes.
- Phone: Iphone 15 pro, running safari, 6.1" display (2532x1170) ~ Tested all pages are displayed correctly on phone and it is easy to navigate the site on smaller screens.

### Automatic Testing:

Automatic testing has been used to test the Products app, checkout app and profiles app forms.

#### Products app Forms:

    from django.test import TestCase

    from .forms import ProductForm, ReviewForm, CommentForm
    from .models import Category

    class TestProductForm(TestCase):
        """ Test the product form for validation. """
        def test_form_is_valid(self):
            """ Test the Product form when valid. """
            category = Category.objects.create(name='Mugs', friendly_name='Mugs')

            product_form = ProductForm({
                'category': category.id,
                'sku': 'pp10',
                'name': 'Blue mug',
                'description': 'This is a blue mug',
                'price': 10.00,
                'image_url': '',
                'image': '',
            })
            print(product_form.errors)
            self.assertTrue(product_form.is_valid(), msg='Product form is invalid.')

        def test_form_is_invalid(self):
            """ Test the Product form when invalid. """
            product_form = ProductForm({
                'category': '',
                'sku': 'pp10',
                'name': '',
                'description': 'This is a blue mug',
                'price': 10.00,
                'image_url': '',
                'image': '',
            })
            self.assertFalse(product_form.is_valid(), msg='Product form is valid.')

    class TestReviewForm(TestCase):
        """ Test the review form for validation. """

        def test_form_is_valid(self):
            """ Test the review form when valid """
            review_form = ReviewForm({
                'rating': 3,
                'review_body': 'I love this mug',
            })
            self.assertTrue(review_form.is_valid(), msg='Review form is invalid.')

        def test_form_is_invalid(self):
            """ Test the review form when invalid """
            review_form = ReviewForm({
                'rating': 3,
                'review_body': '',
            })
            self.assertFalse(review_form.is_valid(), msg='Review form is valid.')

    class TestCommentForm(TestCase):
        """ Test the comment form for validation. """

        def test_form_is_valid(self):
            """ Test the comment form when valid. """
            comment_form = CommentForm({
                'comment_body': 'I also love this mug.',
            })
            self.assertTrue(comment_form.is_valid(), msg='Comment form is invalid.')

        def test_form_is_invalid(self):
            """ Test the comment form when invalid. """
            comment_form = CommentForm({
                'comment_body': '',
            })
            self.assertFalse(comment_form.is_valid(), msg='Comment form is valid.')

#### Checkout app forms:

    from django.test import TestCase

    from .forms import OrderForm

    class TestOderForm(TestCase):
    """ Test Order form for validation. """

        def test_form_is_valid(self):
            """ Test order form when valid. """

            order_form = OrderForm({
                'full_name': 'John Doe',
                'email': 'johndoe@test.com',
                'phone_number': '1234567890',
                'street_address1': 'street',
                'street_address2': '',
                'town_or_city': 'anywhere',
                'postcode': '',
                'country': 'GB',
                'county': '',
            })
            self.assertTrue(order_form.is_valid(), msg='Order form is invlaid.')

    def test_form_is_invalid(self):
        """ Test order form when invalid. """

        order_form = OrderForm({
            'full_name': '', #Required
            'email': '', #Required
            'phone_number': '', #Required
            'street_address1': '', #Required
            'street_address2': 'anywhere',
            'town_or_city': 'anywhere',
            'postcode': '12345',
            'country': '', #Required
            'county': ' anywhere',
        })
        self.assertFalse(order_form.is_valid(), msg='Order form is vlaid.')

#### Profiles app forms:

    from django.test import TestCase

    from .forms import CreateWishlistForm

    class TestCreateWishlistForm(TestCase):
        """ Test create wishlist form for validation. """

        def test_form_is_valid(self):
            """ Test create wishlist form when valid. """
            create_wishlist_form = CreateWishlistForm({
                'wishlist_name': 'Gift Ideas',
                'wishlist_note': 'Potentail gift ideas for friends.'
            })
            self.assertTrue(create_wishlist_form.is_valid(), msg='Create wishlist form is invalid.')

        def test_form_is_invalid(self):
            """ Test create wishlist form when invalid. """
            create_wishlist_form = CreateWishlistForm({
                'wishlist_name': '', #Required
                'wishlist_note': 'Potentail gift ideas for friends.'
            })
        self.assertFalse(create_wishlist_form.is_valid(), msg='Create wishlist form is valid.')

Automatic testing has also been used to test the all_products view and the product_details view.

#### all_products view:

    from django.test import TestCase

    from django.contrib.auth.models import User
    from django.urls import reverse
    from django.contrib.messages import get_messages

    from .models import Product, Category, Review
    from.forms import ReviewForm, CommentForm


    class TestAllProductView(TestCase):
        """ Testing the all_products view. """

        def setUp(self):
            """ Create mock data for testing. """

            self.category1 = Category.objects.create(name='Mugs')
            self.category2 = Category.objects.create(name='vases')

            self.product1 = Product.objects.create(
                name='Blue Mug', description='A ncie blue mug.', price=12.50, category=self.category1
            )
            self.product2 = Product.objects.create(
                name='Red Vase', description='A nice red vase.', price=28.00, category=self.category2
            )

        def test_render_products_page(self):
            """ Test the rendering of the default products page. """

            response = self.client.get(reverse('products'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'products/products.html')
            self.assertEqual(len(response.context['products']), 2)

#### product_detials view:

    from django.test import TestCase

    from django.contrib.auth.models import User
    from django.urls import reverse
    from django.contrib.messages import get_messages

    from .models import Product, Category, Review
    from.forms import ReviewForm, CommentForm

    class TestProductDetailView(TestCase):
    """ Test the product_detail view. """

    def setUp(self):
        """ Create mock data for testing. """

        self.user = User.objects.create_user(username='testuser', password='testpassword')

        self.category = Category.objects.create(name='Mugs')

        self.product = Product.objects.create(
            name='Blue Mug', description='A ncie blue mug.', price=12.50, category=self.category
        )
        self.related_product = Product.objects.create(
            name='Red Mug', description='A ncie red mug.', price=12.50, category=self.category
        )
        self.review = Review.objects.create(
            product=self.product, rating=4, reviewer=self.user, review_body='A very nice mug!' 
        )

    def test_product_detail_view(self):
        """ Test rendering the product detail page. """
        response = self.client.get(reverse('product_detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertEqual(response.context['product'], self.product)
        self.assertIn('reviews', response.context)
        self.assertEqual(len(response.context['reviews']), 1)
        self.assertIsInstance(response.context['review_form'], ReviewForm)
        self.assertIsInstance(response.context['comment_form'], CommentForm)
        self.assertIn(self.related_product, response.context['random_related_products'])


When using the command 'python3 manage.py test' in the terminal all tests passed:

![Automatic testing](https://github.com/user-attachments/assets/53514ae7-d469-4fd3-b7da-c4072abdfadc)

## Validation

### The W3C Markup validation service
![W3C HTML validation](https://github.com/user-attachments/assets/728ab8a7-c29a-44c2-ac9f-b657980c57dd)

### The W3C CSS validation service
![W3C CSS validation](https://github.com/user-attachments/assets/edbe1048-934a-4e4d-973e-637e3d5c5464)

### CI python linter

Tested all python files and ensured they all passed!
![CI python linter](https://github.com/user-attachments/assets/92760649-076b-4839-8118-5b96c15f3543)

### JSHint
All javascript code has been tested using JSHint and no errors were present.

![JSHint](https://github.com/user-attachments/assets/abad01f3-2be7-483f-838e-cb1440b5bbdc)

## Credits
I have used the knowledge I have learnt from the Boutique ado course content, and have taken inspiration for the base of my project from the code used throught the walkthough.

For the transtions given to the cards on the products page and buttons throught the website I used the ByteGrad youtube channel:

[ByteGrad YouTube channel](https://www.youtube.com/@ByteGrad)

#### The video I used for inspiration
[Card zoom hover effect in Bootstrap 5](https://www.youtube.com/watch?v=KAHjf1Xj0SU)

## Acknowledgement
I would like to express my gratitude to Spencer Barriball for guiding me during this project and offering me endless support to overcome challenges I endured.