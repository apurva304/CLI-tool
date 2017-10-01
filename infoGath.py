import requests

class InfoGath:
  def __init__(self):

      print("\n 1. DNS lookup"+"\n 2. Who is lookup" + "\n 3. Geo IP lookup"+"\n 4. HTTP headers")

      choice = int(input("\n Enter your choice\n"),10)
      valid = False

      if(choice == 1):
        apiUrl = "http://api.hackertarget.com/dnslookup/?q="
        query = input("\nEnter url\n")
        valid = True
      elif(choice == 2):
        apiUrl = "http://api.hackertarget.com/whois/?q="
        query = input("\nEnter url\n")
        valid =  True
      elif(choice == 3):
        apiUrl = "http://api.hackertarget.com/geoip/?q="
        query = input("\nEnter IP address\n")
        valid = True
      elif(choice == 4):
        apiUrl = "http://api.hackertarget.com/httpheaders/?q="
        query = input("\n Enter url\n")
        valid = True
      else:print("\nInvalid choice\n")

      if(valid):
        finalUrl = apiUrl +query
        res = requests.get(finalUrl)
        print(res.text)