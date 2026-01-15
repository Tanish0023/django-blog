# Django Blog Project

A Django-based web application featuring blog posts, user profiles, and a review system with session-based interactions.

## Features

### Blog Application
- Blog post management with read later functionality using Django sessions [1](#1-0) 

### Profiles Application  
- User profile creation with image upload capabilities
- Generic class-based views for CRUD operations [2](#1-1) 
- Integration with AWS S3 for media storage in production

### Reviews Application
- Review submission system with form validation
- Review listing and detailed views
- Session-based favoriting system for reviews [3](#1-2) 

## Architecture

The project follows Django's MVT (Model-View-Template) pattern with a focus on generic class-based views to minimize boilerplate code.

### Key Components

#### Views Layer
- **CreateView**: Used for profile and review creation [4](#1-3) [5](#1-4) 
- **ListView**: Used for displaying profiles and reviews [6](#1-5) [7](#1-6) 
- **DetailView**: Used for individual review display [8](#1-7) 
- **TemplateView**: Used for static pages like thank you messages [9](#1-8) 

#### Session Management
The application leverages Django's session framework for user-specific features:
- **Review Favorites**: Stores favorite review ID in session [10](#1-9) 
- **Read Later Posts**: Stores list of post IDs for later reading [11](#1-10) 

## Project Structure

```
django-blog/
├── profiles/          # User profile management
│   ├── models.py      # UserProfile model
│   ├── views.py       # Profile creation and listing views
│   └── forms.py       # Profile form (legacy)
├── reviews/           # Review system
│   ├── models.py      # Review model
│   ├── views.py       # Review CRUD and favoriting views
│   └── urls.py        # Review URL routing
├── blog/              # Blog functionality
│   ├── views.py       # Blog post views and read later
│   └── models.py      # Post model
├── my_site/           # Project configuration
│   ├── settings.py    # Django settings
│   └── urls.py        # Root URL configuration
└── custom_storages.py # AWS S3 storage backends
```

## Environment Variables

The project uses `python-dotenv` to load configuration from a `.env` file in the project root [12](#1-11) . Create a `.env` file with the following variables:

### Required Variables

```bash
# Development/Production Environment
IS_DEVELOPMENT=True                    # Set to False for production
APP_HOST=localhost                     # Your domain for production

# PostgreSQL Database Configuration
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# AWS S3 Configuration (for production)
AWS_STORAGE_BUCKET_NAME=your-s3-bucket
AWS_S3_REGION_NAME=us-east-1
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_S3_CUSTOM_DOMAIN=your-cloudfront-domain.cloudfront.net
```

### Variable Usage

- `IS_DEVELOPMENT`: Controls Django's `DEBUG` setting [13](#1-12) 
- `APP_HOST`: Sets `ALLOWED_HOSTS` for the application [14](#1-13) 
- PostgreSQL variables configure the database connection [15](#1-14) 
- AWS variables configure S3 storage for static and media files [16](#1-15) 

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Tanish0023/django-blog.git
   cd django-blog
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Copy the example variables from the section above
   - Create a `.env` file in the project root
   - Fill in your actual values for each variable

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser account**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main site: `http://localhost:8000`
   - Admin panel: `http://localhost:8000/admin`

## Key Technologies

- **Django 6.0**: Web framework
- **PostgreSQL**: Database
- **AWS S3**: Media storage (production)
- **python-dotenv**: Environment variable management
- **django-storages**: S3 integration
- **Generic Class-Based Views**: For rapid development
- **Session Framework**: For user-specific state management

## Notes

The project demonstrates Django's "batteries included" philosophy with extensive use of generic views and session-based features. The codebase includes legacy implementations that show the evolution from function-based views to class-based generic views [17](#1-16) .

The storage configuration uses custom S3 backends for both static files and media uploads in production [18](#1-17) .
