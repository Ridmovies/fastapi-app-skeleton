<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Fastapi_app_skeleton</h3>

  <p align="center">
    Simple fastapi app as carcass for future applications
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    &middot;
    <a href="https://github.com/github_username/repo_name/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/github_username/repo_name/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Here's a blank template to get started. To avoid retyping too much info, do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`, `project_license`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

## Installation
### Installation for Linux with Docker (sqlite database version)

*  #### Clone the repo
   ```bash
   git clone https://github.com/Ridmovies/fastapi-app-skeleton.git
   ```  
  
* ### Install Docker Engine
- https://docs.docker.com/engine/install/
- https://docs.docker.com/engine/install/ubuntu/

* #### Enter the application root folder: 
```bash
cd fastapi-app-skeleton 
```

* #### Change .env file
* Rename '.env.template' to '.env'
* uncomment line ```DATABASE_URL=sqlite+aiosqlite:///database.db```
* Replace the settings with your own


### Creating an image from a Dockerfile
```bash
docker build -t image_name .
```

### Run a container from an image
```bash
docker run -p 8000:8000 image_name
```

* ### Open in browser OpenAPI (Swagger UI) Documentation
        http://127.0.0.1:8000/docs


### Installation for Linux with docker-compose (postgres database version)

*  #### Clone the repo
   ```bash
   git clone https://github.com/Ridmovies/fastapi-app-skeleton.git
   ```  
  
* ### Install Docker Engine
- https://docs.docker.com/engine/install/
- https://docs.docker.com/engine/install/ubuntu/

* #### Enter the application root folder: 
```bash
cd fastapi-app-skeleton 
```

### Build a new image and run containers
```bash
docker-compose up --build
```

* ### Open in browser OpenAPI (Swagger UI) Documentation
        http://127.0.0.1:5000/docs



### Installation for Linux with Virtual Environment
*  #### Clone the repo
   ```bash
   git clone https://github.com/Ridmovies/fastapi-app-skeleton.git
   ```  
   
* #### Enter the application root folder: 
```bash
cd fastapi-app-skeleton 
```
   
* #### Create a virtual environment in the project's root folder:
```bash
python3 -m venv .venv 
```

* #### Activate the virtual environment:
```bash
source .venv/bin/activate 
```

* #### Install dependencies for the production environment: 
```bash
pip install -r requirements.txt 
```

* #### Change .env file
1. Create postgres database or launch postgres docker 
2. Rename '.env.template' to '.env'
3. Replace the settings with your own

* #### Start your application using Uvicorn in root folder :
 ``` 
uvicorn src.main:app --host 127.0.0.1 --port 8000 --reload 
```


<!-- USAGE EXAMPLES -->
## Usage

* ### OpenAPI (Swagger UI) Documentation
        http://127.0.0.1:8000/docs

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Poetry
- [x] Readme.md
- [x] .env Settings and Environment Variables 
- [x] async database
    - [x] Alembic
    - [x] database for tests
    - [x] sqlite+aiosqlite or postgresql+asyncpg
- [x] example app "posts"
- [x] fix pytest mode
- [x] Auth app
    - [x] bearer access jwt token
    - [x] hashed password + salt
    - [x] refresh token
- [x] Admin Panel
- [x] Docker
    - [x] Docker compose




See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/github_username/repo_name/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=github_username/repo_name" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the project_license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [github.com/othneildrew](https://github.com/othneildrew/Best-README-Template/) Thanks for README.md blank


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Develop 
### Poetry Dependency Management System
### Creating a New Project

```bash
poetry new my-project
```
This command will create a new project structure with a `pyproject.toml` file where dependencies are stored.

### Initializing an Existing Project
```bash
poetry init
```

This command initializes the project by asking for necessary parameters and creating a `pyproject.toml` file.

### Adding a Package
```bash
poetry add requests
```
Adds the `requests` package to your project's list of dependencies.
To add a package under the `[tool.poetry.dev-dependencies]` section in the `pyproject.toml` file, use the following command:
```bash
poetry add <package-name> --group dev
```
### Updating All Packages
```bash
poetry update
```
Updates all packages to their latest compatible versions.

### Synchronizing Poetry with Virtual Environment
```bash
poetry install --sync
```
### Showing the Package Tree
```bash
poetry show --tree
```
### Removing a Package
```bash
poetry remove <package_name>
```


## PostgreSQL
## Creating a PostgreSQL database via console
### 1: Connecting to PostgreSQL shell
```bash
sudo -u postgres psql
```

### 2: Creating a new database
```bash
CREATE DATABASE database_name;
```

## Alembic

### Creating async an Environment
```bash
alembic init --template async alembic
```

### change env.py
?async_fallback=True param for async database
```
config = context.config
# if don't use --template async
# config.set_main_option("sqlalchemy.url", f"{settings.DATABASE_URL}?async_fallback=True")
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)
target_metadata = Base.metadata
```
Import models
```
from src.backend.dev.models import Song # noqa
from src.backend.products.models import Product # noqa
```

### Generate first migration
```bash
alembic revision --autogenerate -m "initial migration"
```

### Apply generated migration to the database:
```bash
alembic upgrade head
```

### Rolls back the last applied migration.
```bash
alembic downgrade -1
```


## Commands for working with Docker and Docker Compose
These commands will help you manage containers and images in your project, providing a convenient development and testing process.

### Creating an image from a Dockerfile
```bash
docker build -t image_name .
```

### Run a container from an image
```bash
docker run -p 8000:8000 image_name
```

### Remove all containers
```bash
docker rm $(docker ps -aq)
```

### Remove all images
```bash
docker rmi $(docker images -q)
```

### Stop and remove all services and images

```bash
docker-compose down --rmi all
```

### To start a console inside a running Docker container, use the docker exec command
```bash
docker exec -it container_name bash
```

### Run the container in interactive mode to gain shell access inside the container:
```bash
docker run -it --rm -p 9000:8000 container_name sh
```



This command stops and removes all services created with `docker-compose`, and removes the images used by these services.

### Build a new image and run containers

```bash
docker-compose up --build
```
This command builds a new image based on the instructions in `docker-compose.yml`.


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 