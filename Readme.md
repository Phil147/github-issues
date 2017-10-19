### Simple django project to create github issues
This is my simple start for an application to post issues over the github api.

#### Set up
* Prerequistes: You need at least Python 3.4
* Optional: Create virtualenvironment (recommended)
* Run
    ```
    pip3 install -r requirements.txt
    ```
* Copy github_issues/secure_settings.example.py to github_issues/secure_settings.py and
fill in your values. If you use a [personal access token](https://github.com/settings/tokens/new) instead of your password the token needs at least
"public_repo" scope
* Run server with 
    ```
    python3 manage.py runserver
    ```
* Go to [http://localhost:8000/issues](http://localhost:8000/issues) and create issues
* Please don't spam repos other than your own with issues ;)

#### Important files/stuff for the task by SinnerSchrader
* secure_settings.example.py -> no sensitive data committed to git
* issues/utils/github.py -> simple utility function to create the issue
* issues/views.py -> response handling
* i could have used plain python or simpler modules instead of django yes but normally you would
have more requirements or future requirements will come in a project. so for me django is a solid ground to add more functionality
like maybe user login, more functions of the github api (list all issues, edit issues), logging etc.
* potentially we could also make a standalone django app out of this wanted to show you my whole project