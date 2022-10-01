# PDF-Search-Engine
PDF search engine allows you to find free PDF books and files and download them to your computer. Search through millions of online pdfs.

![image](https://user-images.githubusercontent.com/60779510/193424728-6b503bd4-41eb-4b43-beaa-dcebc726e64b.png)


#### Prerequisites

## Installation

Install with pip:

```
$ pip install -r requirements.txt
```

## Flask Application Structure 
```
.
|-----app/
| |-----static
| | |-----assets
| | |-----css
| | |-----images
| | |-----js
| |-----templates
| | |-----index.html
| | |-----pdfurl.html
| |----index.py


```


## Flask Configuration

#### Example

```
app = Flask(__name__)
app.config['DEBUG'] = True
```
### Configuring From Files

#### Example Usage

```
app = Flask(__name__ )
app.config.from_pyfile('config.Development.cfg')
```

#### cfg example

```

##Flask settings
DEBUG = True  # True/False
TESTING = False

##SWAGGER settings
SWAGGER_DOC_URL = '/api'
....
```
##### Thats all now Setup Vercel for deployment
###### Step 1 
- Create an account with Vercel if you don't already have one.
- Vercel is a cloud platform for static sites and Serverless Functions that fits perfectly with your workflow. It enables developers to host Jamstack websites and web services that deploy instantly, scale automatically, and requires no supervision, all with no configuration.
###### Step 2 
- Use npm to install Vercel globally on your computer https://www.npmjs.com/package/vercel
- ```npm i -g vercel```
###### Step 3
- Make sure that you have the latest version of Python3 installed and the Flask framework with pip3
- ```pip install Flask```
#### Setup the project
- Setup the development environment by running these commands in your terminal.
- ``` SET FLASK_APP=index.py```
- ```SET FLASK_ENV=development```
##### Run the command below to see your Python/Flask app working locally in the browser
- ```flask run```

##### Deploying to Vercel
- Make sure that you are in the root folder for your project so inside of the venv folder and then run the command vercel in your terminal.
- Use the project setup settings to setup your own project with Vercel.

- Now run the command ```vercel --prod``` to deploy your app. Open the Production link and your app should be working online with full working routes.
