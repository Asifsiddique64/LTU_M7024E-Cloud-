import requests
from matplotlib import pyplot as plt


url = "https://asifmuiz.s3.eu-north-1.amazonaws.com/weatherApp/index.html"
num_iterations = 40
request_times = []

for _ in range(num_iterations):
    total_time = requests.get(url, headers={'Cache-Control': 'no-cache'}).elapsed.total_seconds()
    request_times.append(total_time*1000)

print(request_times)

plt.plot([i for i in range(num_iterations)],request_times)
plt.title('Response Time vs Iteration')
plt.xlabel('Iteration')
plt.ylabel('Response Time (ms)')
plt.show()
plt.savefig('AWS5.png')