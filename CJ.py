from urllib.request import urlopen
from sys import argv, exit

class CJ:

	def check(self,url):
		''' check given URL is vulnerable or not '''

		try:
			if "http" not in url: url = "http://" + url

			data = urlopen(url)
			headers = data.info()

			if not "X-Frame-Options" in headers: return True

		except: return False


	def create_poc(self,url):
		''' create HTML page of given URL '''

		code = """
	<html>
	   <head><title>Clickjack test page</title></head>
	   <body>
		 <p>Website is vulnerable to clickjacking!</p>
		 <iframe src='"""+"http://"+url+"""' width="1247" height="800"></iframe>
	   </body>
	</html>
		""".format(url)

		with open(url + ".html", "w") as f:
			f.write(code)
			f.close()


	def __init__(self,sites):

		#try: sites = input("Enter the url \n")
		#except: print("[*] Incorrect input"); exit(0)

		print("\n[*] Checking " + sites)
		status = self.check(sites)

		if status:
			print(" [+] Website is vulnerable!")
			self.create_poc(sites.split('\n')[0])
			print(" [*] Created a poc and saved to <URL>.html")

		elif not status: print(" [-] Website is not vulnerable!")