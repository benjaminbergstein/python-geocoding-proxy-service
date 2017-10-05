# Geocoding Service

Solution to Postmate's geocoding service challenge.

Live version running on AWS Lambda [here](https://529pxbvmri.execute-api.us-east-1.amazonaws.com/delivered?address=Sightglass%20Coffee)

## Installation

1. Install python3.
2. Clone the repo.
3. Copy `secrets.json.example` to `secrets.json`
4. Set up an account with [Here](https://developer.here.com/documentation/geocoder/topics/quick-start.html) and add your app id and app code to `secrets.json`
5. Set up an account with [Geonames](http://www.geonames.org/login) and add your geonames username to `secrets.json`
6. Done!

# Usage

Start the server:

```
=> ./server
Server is running at http://localhost:8000
```

Make a request:

```
=> curl http://localhost:8000?address=270%207th%20St,%20San%20Francisco,%20CA%2094103
{"lat": 37.7768998, "lng": -122.4086371}
```

# Deploy to AWS Lambda

This project includes an `index.py` which deploys to AWS Lambda.

1. Create a bucket in AWS S3 console for the zipped payload.
2. Create a lambda function in the AWS Lambda console.
4. Create an API in the AWS API Gateway console.
5. Create a GET method for your API. **Make sure to check "Use Lambda Proxy integration" when creating the method**.
6. Use the `deploy-to-lambda` script to zip the project, upload it to S3 and use it in AWS:

    ```
    ./deploy-to-lambda LAMBDA_NAME 1.0.0 S3_BUCKET PATH_TO_SECRETS_FILE
    ```    

6. Test the lambda in the AWS console with data such as:

    ```
    {
      "queryStringParameters": {
        "address": "Sightglass Coffee"
      }
    }
    ```
    
7. Test your API gateway with query string data such as:

    ```
 		address=Sightglass%Coffee
    ```

8. Deploy the API Gateway and test against the endpoint!

# Tests

1. Install ruby
2. Run`rake test`

