# Geocoding Service

Solution to Postmate's geocoding service challenge.

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

# Tests

1. Install ruby
2. Run`rake test`

