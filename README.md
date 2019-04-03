# Website: <http://www.misinformationresearch.org>

### Development

Environment variables must be set, so create a file in the root directory: `.env`.
```
FLASK_ENV=development
FLASK_APP=app
APP_NAME="misinformationresearch.org"
SECRET_KEY="some_secret_key"
```
(See <http://flask.pocoo.org/docs/latest/quickstart/> for information about `SECRET_KEY`.)

- Create a virtual environment (use Python 3):
	- `virtualenv venv`
- Activate the virtual environment:
	- `source venv/bin/activate`
- Install python dependencies:
	- `pip install -r requirements.txt`
- Install node dependencies
	- `npm install`
- Webpack watch for changes:
	- `npm run dev`
- Run server (separate terminal, virtualenv activated):
	- `source .env && flask run`
- Open a web browser and navigate to <http://localhost:5000>

### Deploy

The site is served as a static website from an AWS S3 bucket. `Frozen-Flask` (<https://pythonhosted.org/Frozen-Flask/>) is used to generate a static site in the `app/build` directory.
- Freeze static site:
	- `python freeze.py`
- Sync static site to S3:
	- `aws s3 sync app/build/ s3://<BUCKET_NAME>/ --acl public-read`
