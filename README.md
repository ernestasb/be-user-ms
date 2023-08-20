# be-user-ms
User and authentication microservice for personal project
App is written in Python language using FastAPI framework

# Packages
- alembic==1.11.3
  - (database migration handling)
- black==23.7.0        
  - (code formatting)
- coverage==7.3.0      
  - (test coverage)
- fastapi==0.101.1     
  - (API framework)
- pydantic==2.1.1      
  - (schema validations)
- PyJWT==2.8.0         
  - (work with JWTs)
- pylint==2.17.5       
  - (static code check)
- pytest==7.4.0        
  - (testing the App)
- python-dotenv==1.0.0 
  - (.env variable file handling)
- SQLAlchemy==2.0.20   
  - (ORM)
- uvicorn==0.23.2      
  - (ASGI web server)

# Run the app
To run the app Python 3.10 is required. The app can be run with 'pipenv' virtual env package.
Postgress server has to be started and described in .env file for the program to work.

- CD to the project
- Install dependencies using `pipenv`
  - `pipenv install`
- Enter virtual environment
  - `pipenv shell`
- run the app
  - `python run.py`

# Additional info
- Unit tests are curenntly not written separately, code is covered with functional tests for now
- .env.example contains values for testing purposes
