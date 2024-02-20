import requests
import csv

def search_and_store_data():
    # Search for data about Canoo using the keywords "Canoo" and "GOEV"
    search_keywords = "Canoo GOEV"
    search_urls = [
        "https://www.barrons.com/market-data/stocks/goev={search_keywords}",
        "https://www.bloomberg.com/quote/GOEV:US={search_keywords}",
        "https://www.nasdaq.com/articles/5-things-to-know-about-canoo-stock={search_keywords}"
    ]

    csv_file = "canoo_data.csv"
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Company", "Ticker", "Data"])

        for url in search_urls:
            response = requests.get(url)
            data = process_search_results(response.text)

            for item in data:
                writer.writerow(["Canoo", "GOEV", item])

    print("Data stored successfully in canoo_data.csv")

# Process each search URL and store the data in a CSV file
def process_search_results(data):
    # Implement the logic to process the data
    search_keywords = "Canoo GOEV"  # Define the search_keywords variable

    search_urls = [
        "https://www.barrons.com/market-data/stocks/goev={search_keywords}",
        "https://www.bloomberg.com/quote/GOEV:US={search_keywords}",
        "https://www.nasdaq.com/articles/5-things-to-know-about-canoo-stock={search_keywords}"
    ]

    for url in search_urls:
        # Format the URL with the search query
        formatted_url = url.format(search_keywords=search_keywords)

        # Send a GET request to the URL
        data_list = []  # Define the data_list variable

        response = requests.get(formatted_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the data from the response
        data = response.text

        # Append the data to the list
        data_list.append(data)
    else:
        print(f"Error: Failed to retrieve data from {formatted_url}")

    

search_and_store_data()
