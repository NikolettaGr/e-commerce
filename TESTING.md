
# **Shop Nature - Testing** 

[Main README.md file](/README.md)

Visit the live site - [Shop Nature](https://ecommerce-project-uch6.onrender.com "Link to Shop Nature website")

View GitHub [Repository](https://github.com/NikolettaGr/e-commerce)


## Automated Testing

### **W3C HTML Validator**

The [HTML W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) was used to validate the HTML code used, showing no errors.

<details>
<summary>HTML Validation:</summary>

 - Index
 <br>

![Index](documentation/html_validator/home-html-validator.png)

 - Products
 <br>

![Products](documentation/html_validator/products-html%20-valid.png)

  I removed spaces between the friendly name ,but still the validator detecting the same error.


 - Cart
 <br>

![Cart](documentation/html_validator/cart-html-validator.png)

 - Checkout
 <br>

![Checkout](documentation/html_validator/checkout-html-valid.png)

 - Checkout success
 <br>

![Checkout success](documentation/html_validator/success-valid.png)

  - Newsletter
 <br>

![Newsletter](documentation/html_validator/newsletter-valid.png)

  - About the Artist
 <br>

![About Page](documentation/html_validator/about-html-validator.png)

  - Contact Us
 <br>

![Contact Page](documentation/html_validator/contact-html-validator.png)


 - Log in
 <br>

![Log in](documentation/html_validator/login-html-validator.png)

 - Log out
 <br>

![Log out](documentation/html_validator/logout-html-validator.png)

 - Register
 <br>

![Register](documentation/html_validator/logout-html-validator.png)

 - My Profile
 <br>

![My Profile](documentation/html_validator/profile-html-validator.png)

 - Add Product
 <br>

![Add Product](documentation/html_validator/add-product-html-validator.png)

- Wishlist
 <br>

![Wishlist](documentation/html_validator/wishlist-html-validator.png)

</details>

---


### **W3C CSS Validator**

The [CSS Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) was used to validate the CSS code used, showing no errors.

<details>
<summary>CSS Validation:</summary>

![Base.css](documentation/css_and_js_validator/base-css-validator.png)


![Checkout.css](documentation/css_and_js_validator/checkout-css-validator.png)

</details>

---


### **JSHINT Javascript Validator**

The [JsHint](https://jshint.com/) was used to validate the Javascript code used, showing no errors.

<details>
<summary>Javascript Validation:</summary>

![Javascript Stripe Validator](documentation/css_and_js_validator/js-stripe-validator.png)

![Javascript Validator](documentation/css_and_js_validator/js-validator.png)

</details>

---


### **CI Python Linter**

The [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code used, showing no errors.

---

#### Cart App

<details>
<summary>Cart App Validation:</summary>

 - contexts.py
 <br>

![contexts](documentation/python_validator/cart/context-valid.png)

 - urls.py
 <br>

![urls](documentation/python_validator/cart/cart-url.png)

 - views.py
 <br>

![views](documentation/python_validator/cart/cart-vews.png)

</details>

---

#### Checkout App

<details>
<summary>Checkout App Validation:</summary>

 - admin.py
 <br>

![admin](documentation/python_validator/checkout/checkout-admin.png)

 - forms.py
 <br>

![forms](documentation/python_validator/checkout/checkout-forms.png)

 - models.py
 <br>

![models](documentation/python_validator/checkout/checkout-models.png)

 - signals.py
 <br>

![signals](documentation/python_validator/checkout/checkout-signals.png)

 - urls.py
 <br>

![urls](documentation/python_validator/checkout/checkout-urls.png)

 - views.py
 <br>

</details>

---


#### Home App

<details>
<summary>Home App Validation:</summary>

 - urls.py
 <br>

![urls](documentation/python_validator/home/home-urls.png)

 - views.py
 <br>

![views](documentation/python_validator/home/home-views.png)

</details>

---

#### Products App

<details>
<summary>Products App Validation:</summary>

 - admin.py
 <br>

![admin](documentation/python_validator/products/products-admin.png)

 - forms.py
 <br>

![forms](documentation/python_validator/products/products-forms.png)

 - models.py
 <br>

![models](documentation/python_validator/products/products-models.png)

 - urls.py
 <br>

![urls](documentation/python_validator/products/products-urls.png)

 - views.py
 <br>

![views](documentation/python_validator/products/products-views.png)


</details>

---

#### Profiles App

<details>
<summary>Profiles App Validation:</summary>

 - forms.py
 <br>

![forms](documentation/python_validator/profiles/profiles-forms.png)

 - models.py
 <br>

![models](documentation/python_validator/profiles/profiles-models.png)

 - urls.py
 <br>

![urls](documentation/python_validator/profiles/profiles-urls.png)

 - views.py
 <br>

![views](documentation/python_validator/profiles/profiles-views.png)

</details>

---

#### Support App

<details>
<summary>Support App Validation:</summary>

 - forms.py
 <br>

![forms](documentation/python_validator/support/support-forms.png)

 - models.py
 <br>

![models](documentation/python_validator/support/support-models.png)

 - urls.py
 <br>

![urls](documentation/python_validator/support/support-urls.png)

 - views.py
 <br>

![views](/
documentation/python_validator/support/support-views.png)

</details>

---

#### Wishlist App

<details>
<summary>Wishlist App Validation:</summary>

 - models.py
 <br>

![models](/documentation/python_validator/wishlist/wish;ist-models.png)

 - urls.py
 <br>

![urls](documentation/python_validator/wishlist/wishlist-urls.png)

 - views.py
 <br>

![views](documentation/python_validator/wishlist/wishlist-views.png)

</details>


---

## **Manual Testing**

### **Testing User Stories**

#### **First Time Visitor**

| User Story | Pass/Fail |
|------------|----------|
| I can open the home page so that I can see what this website is about. | PASS |
| I can effectively explore this website so that I can access all the info I need. | PASS |
| I can see a list of products so that I can select one or more to purchase. | PASS |
| I can find out more about the store so that I can find out more about them. | PASS |
| I can modify my shopping cart so that I can adjust my purchase. | PASS |
| I can see a notification upon successful modifying/removing so that I can know I'm doing things right. | PASS |
| I can connect with the store/business on Facebook so I can follow on any news/updates/special offers. | PASS |

#### **Returning Customer**

| User Story | Pass/Fail |
|------------|----------|
| I want to be able to register and log in/out without issues. | PASS |
| I want to get an email notification so that my registration is confirmed. | PASS |
| I can search or sort by category of paintings so that I can select one or more to purchase. | PASS |
| I can see if there is anything on special offer so that I can save some money. | PASS |
| I can add and see my wishlist so, that I can save products which I like. | PASS |
| I can remove products from my shopping cart so that I can adjust my purchase. | PASS |
| I can have personalized user profile so I can view my order history. | PASS |
| I can subscribe to the store newsletter so I can know about any news/updates/special offers. | PASS |

#### **Website Admin/Owner**

| User Story | Pass/Fail |
|------------|----------|
| I can add/remove products from the store so I can remove sold out products and add new ones. | PASS |
| I can modify products in the store so I can update them with the right details. | PASS |
| I can see what the customer ordered, how much was paid, and was the discount applied. | PASS |

---

## **Bugs**

### **Known Bugs**

* No known bugs present in the project (disclaimer; that doesn't mean there are none) at the time of writing this readme/testing.

There were many 'small' bugs that had to be dealt with during the development of the project. Most of them were squashed by doing a quick [Google](https://google.com/ "Google home page") search and using [Stack Overflow](https://stackoverflow.com/ "Stack Overflow home page") to find relevant solutions.

One of the major hurdles faced during the development process stemmed from the use of a temporary email address for Stripe integration. This choice led to persistent issues with the checkout process, consistently resulting in errors related to an invalid API key. The intricacies of this problem were not extensively outlined, especially in the case of AWS connectivity, as it presented a significant source of concern and urgency nearing the submission deadline.

- First major bug was encountered while implementing Stripe. It took multiple days and tries for this to be solved, and it took away time from further development. The code was updated and reworked multiple times because there was lack of attention to details and testing scope on the developer's part. That bug lead directly to other one with the database. After overloading the code with `print()` statements, it was fixed.

- Forcing sku as unique identifier instead of painting_id was a mistake in retrospect, this caused additional time spent when reworking the code to use painting_id. This change necessity became apparent when trying to implement adding new paintings as admin. When using SKU-s, when SKU field was left empty when submitting new painting, nothing worked because SKU was missing and not automatically generated, and painting_id is.

- Search functionality was not working as it should, returning nothing if searched term was category which was solved and fixed quickly.

- Deployment Issue - Media Files Dysfunction

During the deployment phase, a critical challenge emerged related to the proper functioning of media files. Despite numerous attempts to rectify the situation, the images and media assets failed to load as expected on the deployed site. This issue became a source of frustration and consumed considerable time and effort in debugging and troubleshooting.

In the course of grappling with the problem, seeking guidance from the mentor, and consulting various resources, a breakthrough came with the suggestion to leverage Cloudinary for media storage. The decision to adopt Cloudinary as a solution for handling media assets proved to be pivotal in resolving the persistent issue and ensuring the seamless deployment of the project. This experience underscored the importance of exploring alternative strategies and seeking expert advice to overcome deployment hurdles effectively.

