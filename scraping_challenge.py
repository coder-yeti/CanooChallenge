import requests
import csv

# Define the search query
search_query = "GOEV"

# Define the URLs for the search
urls = [
    "https://www.barrons.com/market-data/stocks/goev={search_query}",
    "https://www.bloomberg.com/quote/GOEV:US={search_query}",
    "https://www.nasdaq.com/articles/5-things-to-know-about-canoo-stock={search_query}"
]

# Store the data from all URLs in a list
data_list = []

# Iterate over the URLs
for url in urls:
    # Format the URL with the search query
    formatted_url = url.format(search_query=search_query)

    # Send a GET request to the URL
    response = requests.get(formatted_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the data from the response
        data = response.text

        # Append the data to the list
        data_list.append(data)
    else:
        print(f"Error: Failed to retrieve data from {formatted_url}")

# Store the data in a CSV file
with open("canoo_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Data"])
    writer.writerows(data_list)

print("Data stored in canoo_data.csv")