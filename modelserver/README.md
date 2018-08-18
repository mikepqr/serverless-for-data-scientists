# Model deployment on AWS Lambda with zappa

1. Follow the instructions in [../hyperparameters/](../hyperparameters/) to
   train and upload and model to S3.

2. Create and activate a virtual environment (note you must create a fresh
   virtual environment to use zappa), e.g.

        python -m virtualenv venv && source venv/bin/activate

2. Install the requirements:

        pip install -r requirements.txt

4. Run `zappa init` and accept all the defaults

5. Run `zappa deploy`. The output of this command (or `zappa status`) includes
   the public `amazonaws.com` URL of your deployed flask application. It will
   look something like
   `https://abcdef123.execute-api.us-east-1.amazonaws.com/dev/`

6. Visit `your_amazonaws_url/predict?feature_1=3&feature_2=6` to get a
   prediction.
