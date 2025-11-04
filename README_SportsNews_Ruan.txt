Sports News Application (Capstone Project)
-------------------------------------------------------------

This project is a Django web application I built as part of my HyperionDev Software Engineering course. 
It’s called Sports News, and it focuses on displaying sports-related articles in a clean and easy-to-use layout. 
The goal was to create a simple news app where articles can be viewed, reviewed, and managed by the admin.

1. Project Overview
-------------------------------------------------------------
The app uses Django and Django REST Framework. 
It shows all approved sports articles on the homepage and includes a review page for articles that still need approval. 
The design follows a blue and green color theme to match the sporty look and feel.

2. Main Features
-------------------------------------------------------------
1. Displays all approved sports articles on the homepage.
2. Allows viewing full article details.
3. Includes a review section for pending articles.
4. Admin panel to manage users, articles, and newsletters.
5. API endpoints for articles, publishers, and newsletters.

3. Project Structure
-------------------------------------------------------------
sports-news/
│
├── core/              # Django settings and main URLs
├── news/              # Main app with models, views, and templates
│   ├── templates/news/
│   │   ├── home.html
│   │   ├── article_detail.html
│   │   └── review_articles.html
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── static/css/        # Custom blue and green theme
│   └── style.css
├── templates/         # Shared base template
│   └── base.html
├── db.sqlite3         # Database file
└── manage.py

4. Technologies Used
-------------------------------------------------------------
- Python 3
- Django 5
- Django REST Framework
- Bootstrap 5
- HTML and CSS

5. How to Run the Project
-------------------------------------------------------------
1. Run migrations using:
   python manage.py migrate

2. Create a superuser (if needed):
   python manage.py createsuperuser

3. Start the server:
   python manage.py runserver

4. Open the project in your browser:
   http://127.0.0.1:8000/

6. Reflection
-------------------------------------------------------------
Building this project helped me understand Django better, especially how views, models, and templates work together. 
I also learned how to use Django REST Framework to build APIs and how to style a site using Bootstrap and CSS. 
I really liked experimenting with the blue and green color scheme since it made the app feel like a real sports news website.

7. Author
-------------------------------------------------------------
Ruan
Student Software Developer — HyperionDev
