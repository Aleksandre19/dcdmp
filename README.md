<h1 align="center">Data Centric Development Milestone Project</h1>



The working website can be found [here.](https://dcdmp.herokuapp.com/)

 This site is a milestone project for the Data Centric Development section. For this purpose I choose a book storing theme.  On this website a user can very easily find and collect the books he or she wishes to read.

- #### Mine goals of the project were :

    - To have CRUD functionality
    - To be written on python + flask
    - And to have a MongoDB as a database


- #### External Users Goal :

    - Find and collect a books which she or he wants to read.


- #### Webpage Owner Goal :

    - Earn money from each purchase made from the site.


- #### Admin :

    - User Name: Aleksandre (Must be with capital A)
    - User Email: aleksandre.voronini@gmail.com


## User Experience (UX)

-   ### User stories

    - As a user visited on the webpage he or she should very quickly understand what is this site about and should have a ability to find and collect the books they wish to read.


-   ### Strategy

    - My goal was to give to users of this website a quick understanding of what is this site  about and that the website has a simply accessibility and functionality.


-   ### Wireframes

    - All pages wireframes can be found [here.](https://github.com/Aleksandre19/dcdmp-files/blob/master/pages_wireframe.pdf)
    - New MongoDB database wireframe can be found [here.](https://github.com/Aleksandre19/dcdmp-files/blob/master/new_mongoDB_wireframe.pdf/)
    - Old MongoDB database wireframe can be found [here.](https://github.com/Aleksandre19/dcdmp-files/blob/master/old_mongoDB_wireframe.pdf/)


-   ### Design

    - #### Colour Schema
        
        - I choose complimentary colours: Light little bright blue ( #2bf3ff ) and light little pale orange ( #ff9752 ).


     - #### Typography
        
        - Roboto is the main font on the site and Sans Serif is as a fallback font.


    - #### Design files
        
        - PDF design file for Desktop devices can be found [here.](https://github.com/Aleksandre19/dcdmp-files/blob/master/design_desktop_v.pdf/)
        - PDF design file for Mobile devices can be found [here.](https://github.com/Aleksandre19/dcdmp-files/blob/master/design_mobile_v.pdf/)     


## Features

1. [Materializecss Autocomplete:](https://materializecss.com/autocomplete.html/)
    - It is used to auto fill a search filed.
1. [Materializecss Media:](https://materializecss.com/media.html/)
    - Clicking on image it opens and shows the original size of image with nice effect.
1. [Materializecss Collapsible:](https://materializecss.com/collapsible.html/)
    - It is used to smoothly and nicely show and hide a content of the collections in the my list page.
1. [Materializecss Tooltips:](https://materializecss.com/tooltips.html/)
    -  It is used for textarea element. On entering in the textarea a tooltips appears and it says that by pressing on enter kay a user can make a new line in the textarea.
1. [Materializecss Pickers:](https://materializecss.com/pickers.html/)
    -  It is used to select a date from a calendar in add book page.
1. [Materializecss Range:](https://materializecss.com/range.html/)
    -  It is used for choosing a price on a add book page.  This future is modified from [noUiSlider][https://refreshless.com/nouislider/] by Materializecss.



## Technologies used

1. [HTML5:](https://en.wikipedia.org/wiki/HTML5/)
1. [CSS3:](https://en.wikipedia.org/wiki/CSS/)
1. [Materialize 0.100.2 / 1.0.0](https://materializecss.com/)
    -  It was used to assist with the responsiveness and styling of the website.
1. [JavaScript](https://www.javascript.com/)
    -  It was used to fix Data Picker’s bug and to make auto submission of a search input after it is being filed with data. Also grab the date from mongodb and set it to the Data Picker.
1. [jQuery](https://jquery.com/)
    -  It was used for Materializecss framework:
        - To collapse a menu on the tablet and lower devices. 
        - For zooming of images.
        - For data picker.
        - For a animation of a HTML select element.
        - For tooltips.
        - For autocomplete. 
        - For a animation of a HTML range element. 
1. [Flask - Python framework](https://flask.palletsprojects.com/en/1.1.x/)
    -  It was used for a coding and for a development of the website.
1. [MongoDB](https://www.mongodb.com/)
    -  I was used to create a document structured database and to store a data of a website.
1. [Heroku](https://www.heroku.com/)
    -  It was used to deploy a live website.
1. [Git](https://git-scm.com/)
    -  Git was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub and to Heroku.
1. [GitHub](https://github.com/)
    -  Git was used for storing the project source files and README.md.
1. [noUiSlider](https://refreshless.com/nouislider/)
    -  Materializecss uses modifise this script to make a [Materializecss Range:](https://materializecss.com/range.html/).
1. [Google Fonts](https://fonts.google.com/)
    -  It was used for importing a Roboto font.
1. [Photoshop](https://www.adobe.com/se/products/photoshop.html?sdid=8JD95K3M&mv=search&ef_id=EAIaIQobChMIi9eOi8zN6wIVDSwYCh2qYgpbEAAYASAAEgJKtvD_BwE:G:s&s_kwcid=AL!3085!3!340839219577!b!!g!!%2Badobephotoshop!1469953337!58630352524&gclid=EAIaIQobChMIi9eOi8zN6wIVDSwYCh2qYgpbEAAYASAAEgJKtvD_BwE/)
    -  Photoshop was used to create the design for a desktop and for a mobile devices. The logo of the website was created also in the Photoshop.



## Testing
- The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project. In W3C CSS Validator are Materializecss framework’s errors.
- In W3C Markup Validator there are ID (#s_form) Duplication error for: add_book, contact and singel_book_page pages. This is because I duplicate a form element and use a [Materializecss helpers][https://materializecss.com/helpers.html] - hide-on-med-and-down and  hide-on-large-only - to control a responsiveness of the search field.  
- This website was tasted only in Chrome and safari browsers. Chrome inspect was used to checkout  a layout, styles and functionality for a tablets and mobile devices.
- A large amount of testing was done to ensure that all pages were linking correctly and functioning appropriately.
- ### Known Bugs
    - HTML and CSS needs to be played around to correct small errors her and there.
    - The search field aligns toper on mobile devices. It should be middle.
    - The image’s size and responsiveness is not well controlled. It sometimes overlaps the content beside it and also it scratches in height on longer devices. 
    - On tablet devices the search form and it’s icons needs to be aligned properly. 
    - On tablet devices a buttons of edition and deletion in my list page needs to be aligned properly.
    - On tablet devices the hamburger menu is little down. It must be middle.
    - Colour of titles	 in new released book section are white and that is way are badly visible.
    - When zooming images in new released books section they align them selfs toper.The alignment should be centered.
    - If the searched book wasn’t found a website doesn’t say anything.
    - If there is more than one result of searched book than a filed in mongoDB named as “searched” doesn’t increment by one. If there is only one than it increments by one.


## Functionality

- ### Pages

    - #### Home Page

        - There are:
            - Main menu.
            - Website's logo.
            - A banner with a search field.
            - A new released books section.
            - A best selling books section.
            - A footer.

        - In a menu the link underlines	 corresponding to the current page. To underline majority of adding books it has red colour.
        - By clicking on a search filed and typing a some letter a list of autocomplete is appearing. By clicking on a some link from this list the search submits automatically.
        - The posts has a cross signed add to my list icons. By clicking on that if a user is authenticated and the post is not already in the list the post adds in the user’s “My List”.
        - By clicking on the post’s images a Materialize media feature is triggering  and the image pop ups with nice effect.
    

    - #### Add book page

        - No matter user is authenticated or no the user can add a new book on the site. If user is a new than a new user records automatically in a database.
        - All fields are required by assigning required attribute to HTML input fields.
        - Before adding a new book in database a app checks if the selected image has required size and format. If so process continues by successfully adding the book in the database. 
        - The maximum image size is 500MB and allowed exstentions are PNG, JPG, JPEG and GIF.
        - For better user experience this page uses a flask message function called Flash Messages to give to the users appropriate messages during process.
    

    - #### My List page

        - In order to access to my list page the users must authenticate themselves.
        - For logging and authentication this website doesn’t use Flask framework’s login functionality.
        - In order to authenticate one must enter a name and email in the authentication form. If current user exits in the database than it takes all data necessary to this page from mongoldb and if a user is a new one than the app adds he or she as a new user in the mongodb.
        - A authenticated user’s data stores in the flask session to control if the user is already logged in when navigating from other pages to the my list page.
        - The Flask session is cookie based. Because of that the session doesn’t delete when user close browser or tab.
        - To logout the user must use logout button which is only located on this page.
        - here are two types of users: Usually users and admin. Admin can control additional setting such are:
            - The book of the day.
            - The special offer.
            - The new released book.
            - The best selling book.
            - Show or no as a big post on a home page.
        - This setting can be controlled on edit book page.
        - On this page user can access the books which are in his/hers my list and the books which she or he added.
        - From this page a user can delete and edit a book’s details.
        - If user deletes the book from his or hers list than this books deletes only form list. And if user deletes the book from added books page than this books deletes completely including database and cover image.
        - This page also uses Flask framework’s Flash function to give to a user a appropriate messages during using of this page.


    - #### My List page 

        - his page is not coded. It is only html and css. It should use [Google Map’s Api][https://cloud.google.com/maps-platform/?hl=en/] and [EmailJS][https://www.emailjs.com/] to send emails.    
    


## Deployment

- The functional website is deployed on Heroku and the source code is deployed on GitHub  

    - Deployment on Heroku
        1. Creating account on heroku.
        1. Creating new heroku app.
        1. Login in Heroku from gitpod CLI using heroku login -i command.
        1. Linking git  to heroku using:

        ```
        git remote add heroku https://git.heroku.com/dcdmp.git

        ``` 
        1. Creating requirements.txt by using:

        ```
        sudo pip3 freeze --local > requirements.txt

        ```
        1. Creating Procfile by using:

        ```
        echo web: python app.py > Procfile

        ```
        1. Setting IP and PORT on heroku website in setting section.
        1. Adding files on staging area by using:

        ```
        git add .

        ```
        1. Committing by using:

        ```
        git commit -m “ Deploying website”

        ```
        1. Pushing to heroku by using:

        ```
        git push heroku master

        ```
        1. Starting web process in gitpod by using:

        ```
        heroku  ps:scale  web=1

        ```
        1. Opening deploy project in browser by clicking - Open app on heroku website. 


    - The source files of website was deploy on GitHub using following steps:
        1. Creating new repository on GitHub website. 
        1. Linking git to GitHub by using:

        ```
        git remote add origin https://github.com/Aleksandre19/dcdmp.git

        ```
        1. Pushing files to GitHub by using:

        ```
        git push

        ```
### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
``` 


### Credits
   - #### Content
       - Content including a book’s cover images was taken from this website [https://www.bookdepository.com][https://www.bookdepository.com]

   - #### Images
       - Images for banners and for website design was taken from this website [https://www.pexels.com][https://www.pexels.com]

   - #### Website’s design and a logo was created by developer in Photoshop. 


### Acknowledgements

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.






  