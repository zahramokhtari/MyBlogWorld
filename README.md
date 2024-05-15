# MyBlogWorld

MyBlogWorld is a Django-based web application for creating and managing blog posts. It allows users to register, create, view, and manage their blog posts. Each post can be categorized into different types for better organization.

## Features

- User registration and authentication
- Create, edit, and delete blog posts
- Categorize posts into different types (e.g., Entertainment, Lifestyle, Travel)
- View all posts or filter posts by type
- Responsive design for mobile and desktop devices

## Technologies Used

- Django
- HTML/CSS
- Bootstrap
- SQLite (default database for development)

## Installation

To run the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/zahramokhtari/MyBlogWorld.git
   ```

2. Navigate to the project directory:

   ```bash
   cd MyBlogWorld
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open http://localhost:8000 in your web browser to access the application.

## Usage

- Visit the homepage to view all blog posts.
- Sign up for an account to create your own blog posts.
- Use the navigation links to filter posts by type or create a new post.
- Click on a post title to view its details.

## Contributing

Contributions are welcome! If you'd like to contribute to MyBlogWorld, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
