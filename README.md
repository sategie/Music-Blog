# Audoiotown Music Blog

The Audiotown Music Blog is a Django project which enables users read, like and comment on music blogs.

[View the live project here.](https://audiotown-music-blog-8325eb2cec3b.herokuapp.com/)

![Image of AudioTown Music Blog app on different screen sizes and showing the different screens of the app](blog/documentation/am-i-responsive.png)


## User Experience (UX)

### Project Goals:

The project is designed to enable CRUD functionality for blogs.
Staff members are the only persons authorized to create, update and delete blogs.
Non-staff members on the other hand can read, like or comment on a blog.

### User stories
    - As a Site User, I can view blog posts in order to select a post to read
    - As a Site User, I can click on a particular post in order to read the post's content
    - As a Site Admin, I can perform CRUD functions on posts in order to manage posts
    - As a Site or Admin User, I can view the number of likes on each blog post in order to see the most interesting post
    - As a Site User, I can register an account on the blog app in order to comment on or like a post
    - As a Site or Admin User, I can view the comments on a blog post in order to to know people's opinion about the post
    - As a Site Admin, I can approve or disapprove comments in order to ensure that only acceptable comments are displayed to the public
    - As a Site User, I can comment on a post in order to to give my opinion about the post
    - As a Site User, I can like or unlike a post in order to let the author know whether or not the post is eye catching
    - As a Site Admin, I can log in and create a profile page for myself.
    - As a Site Admin, I can create a blog in the app after signing in.
    - As a Site Admin, I can log in and see my profile and associated posts.
    - As a Site Admin, I can log in and view my profile and access the respective posts from there.
    - As a Site Admin, I can edit my full name and bio in the Profile page.
    - As a Site User or Site Admin, I can view the blogs on different pages.

## Features

### Existing Features

- **Color Scheme**

  - The color combinations were chosen to keep the blog app simple.

  - Contrast was the major factor considered when choosing the colors.

- **Font Sizes**

  - The font sizes for the project are displayed using rem units to improve the readability on various screen sizes.

- **Landing Page**

    - The page that appears as soon as the URL loads is the home screen.
      - The home screen is has a Navbar and Footer which is consistent across all other pages.
      - The landing page's hero image is a picture of a guitar which fits well to the purpose of the app.
      - When a user logs in, a welcome message displays on the home screen with the username of the user(irrespective of staff membership).
  
        ![Image of landing page showing the navbar and hero image](blog/documentation/landing-page.png)
        ![Image of landing page showing footer](blog/documentation/landing-page-footer.png)
        ![Image of welcome message that displays whenever a user logs in](blog/documentation/landing-page-non-staff.png)

- **Navbar**

  - The Navbar consists of the AudioTown Music Blog Logo, **Home**, **Blogs**, **Signup** and **Login**
  - If a non-staff member logs in, they are presented with only three options: **Home**, **Blogs** and **Logout**
  - If a staff member logs in, they are presented with five options: **Home**, **Blogs**, **Create Blog**, **Profile** and **Logout**

        ![Image of navbar options after non-staff logs in](blog/documentation/landing-page-non-staff.png)
        ![Image of navbar options after staff member logs in](blog/documentation/landing-page-staff.png)

- **Blogs**

  - Whenever a user clicks on **Blogs**, all the blogs are displayed in boxes of 3 per row and 6 per page.
  - The user has the option to navigate to the next/previous page to view more blogs.
  - A user who is not logged in can click on blogs to read a blog and view comments, but does not have authorisation to like or comment on the blog.
  - Logged in users have the authorisation to read a blog, view comments, like/unlike or add a comment on a blog.
  - Staff members who click on a blog which they created themselves, have the option to edit or delete the blog.
  
        ![Image of blogs list](blog/documentation/list-of-blogs.png)
        ![Image of option to go to the next page](blog/documentation/pagination.png)
        ![Image of blog detail](blog/documentation/blog-detail.png)
        ![Image of blog commenting feature](blog/documentation/blog-detail-comment.png)
        ![Image of comment awaiting approval](blog/documentation/comment-awaiting-approval.png)
        ![Image of blog comments](blog/documentation/list-of-comments.png)
        ![Image of blog creation](blog/documentation/create-blog.png)
        ![Image of modify post](blog/documentation/modify-post.png)
        ![Image of delete post](blog/documentation/delete-post.png)
        ![Image of blog written by logged in staff member](blog/documentation/staff-member-own-blog.png)

- **Profile**

    - Whenever a staff member logs in, they have the option to click on Profile if one has been created for them on the backend.
    - A staff member who has a profile also has the ability to edit the fullname and bio in the blog app.
    - A staff member who has written blog posts will see the list of written blog posts within their profile

        ![Image of profile page](blog/documentation/profile.png)
        ![Image of edit profile](blog/documentation/edit-profile.png)

- **Logout**

    - Whenever a user logs out, they are asked to confirm if they want to logout or cancel.

        ![Image of logout page](blog/documentation/logout.png)

- **Django Admin Page**

    - A django superuser account was created to administer the site on the backend.
    - Every subsequent staff-member needs to be created within the admin page
    - After a staff member account is created, the user can then access the admin page and carry out actions depending on the permissions assigned.


### Features Left to Implement

- **Icon for Logged-in user**
  
    - An icon to be displayed in the top right showing the currently logged in user.
  
- **Sharing Blogs**
  
  - The ability to share blog posts to social media after logging in.

## Project Design

### Database Models

- This project is hosted on Heroku and the PostgreSQL database is used.
- Cloudinary is used to store all blog images.
- Three custom models were created: **Post**, **Comment** and **Profile**
- All three models all have a Foreign Key relationship to the built in Django User model
  
        ![Image of Entity Relationship Diagram for models](blog/documentation/audiotown-erd.png)


## Technologies Used

### Languages

- HTML5
- CSS3
- JavaScript
- Python

### Frameworks/Libraries

- [Bootstrap:](https://getbootstrap.com/) Bootstrap CSS Framework for styling most parts of the project
- [Django:](https://www.djangoproject.com/) Main Python framework used
- [Django Allauth:](https://django-allauth.readthedocs.io/en/latest/index.html) Used for authentication
- [Cloudinary:](https://cloudinary.com/) Used to store all uploaded images
- [Coverage:](https://coverage.readthedocs.io/en/latest/index.html) Used to record the percentage of automated tests carried out
- [Django Crispy Forms:](https://django-crispy-forms.readthedocs.io/en/latest/) Used to simplify the rendering of Django forms.
- [Gunicorn:](https://gunicorn.org/) used as the web server to run Django on Heroku.
- [psycopg2:](https://pypi.org/project/psycopg2/) Used PostgreSQL database adapter.
- [Summernote:](https://github.com/summernote/django-summernote) Used to provide a WYSIWYG editor for blogs and uploading images.


### Technologies/Software

- [Am I Responsive:](http://ami.responsivedesign.is) Used to create the responsiveness image across different screen sizes
- [Chrome DevTools:](https://developer.chrome.com/docs/devtools/) Used for testing responsiveness and device compatibility
- [Font Awesome:](https://fontawesome.com/) Used to add icons in the project
- [Git:](https://git-scm.com/) Git was used for version control
- [GitHub:](https://github.com/) GitHub is used to store the project
- [Google Fonts:](https://fonts.google.com/) Used to import the Roboto and serif fonts for the project.
- [Heroku:](https://www.heroku.com/) Used for deployment and hosting of the application.
- [Elephant SQL:](https://customer.elephantsql.com/login) The database hosting service used in the project
- [HTML Validator:](https://validator.w3.org/) Used to validate the HTML
- [Lucidchart:](https://www.lucidchart.com/pages/) Used to create the Entity Relationship Diagram for the database models
- [W3 CSS Validator:](https://jigsaw.w3.org/css-validator/) Check your code for CSS validation.


## Testing

### Browser Compatibility

- The project was tested on the browsers listed below. The project worked as expected on all three browsers without any significant differences noticed.

  - Google Chrome Version 118.0.5993.117 (Official Build) (64-Bit)

  - Microsoft Edge Version 118.0.2088.76 (Official build) (64-bit)

  - Firefox Version 119.0 (64-Bit)








