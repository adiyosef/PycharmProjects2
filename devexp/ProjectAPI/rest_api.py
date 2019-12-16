import urllib.request, json

# Opening a web request
url = urllib.request.urlopen("http://free.currconv.com/api/v7/convert?q=USD_ILS&compact=n&apiKey=91adfad7fb0c17319060")

# Decoding response to str
data = json.loads(url.read().decode()) # Decoding a web request

# Parsing results
results = data['results']
USD_ILS = results['USD_ILS']
currency = USD_ILS['val']

print("Welcome to currency converter")
try:
    amount = float(input("Please enter an amount of Shekeles to convert:"))
    print("Result is: ", round(float(amount / currency), 2), "USD")
    print("Thanks for using our currency converter")

except ValueError:
    print("Invalid Choice")