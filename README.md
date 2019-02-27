# Identity App - Flask

This is the backend/API for the identity app.

# Local Dependency Requirements

* Python@3.7 with Pip
* Postgres

## Steps to run locally

1. Clone the repo
1. Set up a virtual environment - E.g. `python3 -m venv venv`, then `source venv/bin/activate`
1. Install local dependencies: `pip install -r requirements.txt`
1. Run postgress locally
1. Create a .env file to use locally: `cp sample_env .env`
1. Manually populate that .env file with the correct variables according to your local setup
1. Run the app from the root directory using `python run.py` (this should run in debug mode currently)

## API Documentation

* If we do not return a response code, 200 is defaulted.  The methods are typed with Tuple[dict, int] to explicitly return codes for every return path.
* flask_restful expects a dict or dict, code as return type and automatically does the dict to JSON conversions.
* Note: Post requests need to include the header, `Content-Type: application/json`

**Response Codes used:**

* 200 - OK
* 201 - Created
* 202 - Accepted (Might be used if the API queues up an action for later completion)
* 400 - Bad Request
* 404 - Not Found

## Other Notes

1. Make sure you save new dependencies to the requirements.txt file: `pip freeze > requirements.txt`
