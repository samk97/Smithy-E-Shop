# Smithy-E-Shop

# Project Description:

The Blacksmith E-Shop is an online platform designed to showcase and sell handcrafted blacksmithing products. The platform serves as a marketplace for both blacksmith artisans and customers who appreciate high-quality, custom-made metalwork. The project aims to provide a user-friendly and visually appealing experience, allowing users to explore, purchase, and engage with unique blacksmithing creations.

# Technologies:

The Blacksmith E-Shop is built using the Django web framework for backend development. Frontend technologies such as HTML, CSS, JavaScript and Bootstrap are employed to create an intuitive user interface. The platform incorporates a relational database to manage product information, user profiles and orders.

# Installation:

To run  locally, follow these steps:

1. Clone the repository:

   git clone https://github.com/samk97/Smithy-E-Shop.git
   
2. Create a virtual environment and activate it:
           
   python -m venv venv
      
    source venv/bin/activate

   On Windows: venv\Scripts\activate
3. Install dependencies:

   pip install -r requirements.txt
4. Apply migrations:

   python manage.py createsuperuser
5. Create a superuser account:

    python manage.py createsuperuser
  
6. Run the development server:

    python manage.py runserver
