Website: <http://www.misinformationresearch.org>

Create a virtual environment:
`virtualenv venv`
Activate the virtual environment:
`source venv/bin/activate`
Install python dependencies:
`pip install -r requirements.txt`
Install node dependencies
`npm install`
Webpack watch for changes:
`npm run dev`
Run server (separate terminal, virtualenv activated):
`flask run`
Open a web browser and navigate to <http://localhost:5000>

The site is served as a static website from an AWS S3 bucket. `Frozen-Flask` (<https://pythonhosted.org/Frozen-Flask/>) is used to generate a static site in the `app/build` directory.
Freeze static site:
`python freeze.py`
Sync static site to S3:
`aws s3 sync app/build/ s3://<BUCKET_NAME>/ --acl public-read`
