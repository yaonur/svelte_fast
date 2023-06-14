import requests
from concurrent.futures import ThreadPoolExecutor

# Define the URL you want to send requests to

# Define the number of concurrent requests you want to send
num_requests = 10

def send_request(url):
	response = requests.get(url)
	print(response.status_code)
with ThreadPoolExecutor(max_workers=num_requests) as executor:
	for _ in range(num_requests):
		# url = f"http://127.0.0.1:3000/process/?url=https://i0.wp.com/runthatline.com/wp-content/uploads/202{_}/12/vitest-mock-fetch-api.png?fit=1622%2C1080&ssl=1"
		url = f"http://127.0.0.1:3000/process/?url=https://darastastasasaf.com"
		executor.submit(send_request, url)
