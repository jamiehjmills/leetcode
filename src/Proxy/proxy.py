import threading
import time


# https://www.geeksforgeeks.org/python-program-with-concurrency/
# https://stackoverflow.com/questions/54954075/how-to-multi-thread-with-for-loop

def save_domains(index, f):
	domains = (["test1.com", "test2.com", "test3.com"], ["test10.com", "test11.com", "test12.com"],
               ["test7.com", "test8.com", "test9.com"])
	curr_domains = domains[index]

	for domain in curr_domains:
		print(f"domain {domain} \n")
		f.write(domain + "\n")
		time.sleep(1)

f = open("/Users/hyojoomills/Development/pythonProject/leetcode/src/Proxy/proxy.txt", "a")

threads = []

for i in range(3):
	threads.append(threading.Thread(target=save_domains, args=(i, f)))
	threads[-1].start()

for thread in threads:
    thread.join()


f.close()

print("Both threads have finished.")


