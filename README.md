# Geocoding Service

Solution to Postmate's geocoding service challenge.

## Installation

1. Install python3.
2. Clone the repo.
3. Done!

# Usage

Start the server:

```
=> ./server
Server is running at http://localhost:8000
```

Make a request:

```
=> curl http://localhost:8000?address=270%207th%20St,%20San%20Francisco,%20CA%2094103
{"address": ["270 7th St, San Francisco, CA 94103"]}
```

# Tests

1. Install ruby
2. Run`rake test`
