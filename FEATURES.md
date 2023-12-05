    ## Features

      - Shop Nature website is structured in a user-friendly and easy to navigate way.

    - Home Page:
        When the index first loads, the user is presented with a page that succinctly conveys the fundamental purpose of the site through a single image on the home page, accompanied by a "Shop Now" button.The button leads to all products ,where customers can start to search our plnats.
        The navigation bar presents the site name, logo, search field, account and basket icons, and selectors for all products, categories, deals, about and contact sections.
        Right above the navbar, there is an animated marquee banner that blinks special offers.
        The footer contains business email and physical address, popular categories, about and social media links, as well as a newsletter subscription button that opens a subscription-dedicated page.
        Using an MVT-based framework (Model, View, Template), the base template is created with the head, navigation, and footer being the same on all pages, adding specific page content to it.

    - Navbar:
        The first navbar dropdown menu consists of sorting options for products, by price,by rating and 'All Products' nav link.
        The second dropdown menu is for exploring Categories.
        The Deals dropdown menu contains Holiday Deals.
        The About link leads to About page ,where customer can learn more about the store.
        The Contact link leads to Contact page. where customer can contact direct the store's owner.
        The My Account link and Font Awesome icon are for handling user's login, logout, registering, My Profile page, and admin's access and Products Management page.

    - Footer:
        The footer contains business email and physical address, popular categories, about and social media links (opening in separate tabs).
        At the top of the footer area, there is a newsletter subscription button that opens a subscription-dedicated page.

    - Registering, logging in/out:
        A first-time/unregistered user can successfully make a purchase without registering.
        A first-time user can register on the register page. The page contains redirect links to login if the user is mistakenly on the register page and a link to the login page if the user is already registered.
        Upon registering, the 'Register' link is replaced by 'Logout' link, allowing the user to sign out from the site.
        If the registered user makes a purchase, the personal and delivery details as well as the past order and its details are visible on 'My Profile' link in the My Account nav dropdown.
        A logged-in admin user will also have additional links in the navbar - 'Products Management,' for adding products for sale, and 'Admin Page,' which opens the admin site in a separate tab.
        When logging in, the user is brought to the index page.
        When logging out, the user is asked 'Are you sure' before signing out.
        When signed out, the user is brought to the index page.

    - Products Page (this includes all the categories, and sorting options):
        The user is presented with a paginated view of products for sale. Each product card consists of an image, price, rating, information on whether the product is pet-friendly, its availability in stock, category name, and a brief description. If the user clicks on a product, the details of the product, including specifications, features, and customer reviews, are presented.

        All of the products are categorized, providing a structured navigation experience for users. This categorization is crucial for enhancing the user experience, as it allows customers to easily locate and explore products within their specific areas of interest. Whether someone is searching for pet-friendly items, checking stock availability, or seeking detailed information, the categorized structure ensures a seamless and user-friendly shopping experience.


    - Product-detail Page:
        This page shows a larger image of the product, as well as its full name, size, price, add to cart button, if the user is authenticated a button for add to a wishlist and keep shopping button.
        The customer can choose the quantity of the product, which affects the price at the checkout.


    - Cart Page:
        Consists of the list of products the user has placed in the cart, the currently selected prduct with quantity, Subtotal calculations on the right side.
        There is a remove button so the user can remove products from the cart easily.
        If the user is under the free delivery threshold, the message is displayed below the grand total saying that the user can spend just (amount) to get free delivery.
        Cart total is calculated excluding delivery.

    - Checkout Page:
        Checkout page consists of the product image, title, quantity and the full total of the product.
        The form for delivery details can be found on the left, after a successful purchase the user is presented with the checkout success page, holding all of the info from the purchase, product/s, delivery, and personal details, and the email confirmation sent message.
        Order is saved to 'My Profile' page if the user is registered with the site.

    - About Pages:
        As you navigate through our "About Us" section, you'll learn about the core values that drive us, the dedicated team behind the scenes, and the principles that guide our sustainable and eco-friendly practices. Discover the unique stories of the passionate individuals who contribute to the growth of Shop Nature, whether it's our expert horticulturists, customer support team, or the visionary minds shaping our plant collections.

    - Contact Page:
        Contact page is for any questions about products, orders, or delivery services,costumer can feel free to reach out to the store/owner. Costumers can seek more information about a specific plant, tracking order, or have a general inquiry.
        

    - Error Pages:
        Two error pages are supported, 404 (page not found) and 500 (internal server error), both with buttons that guide the user back to the home page.

