import infoGath,admin,CJ,port,banner,csrf,click

@click.group(help='A set of pentesting tools')
def cli():
    pass

@cli.command(help='Admin page finder')
@click.argument('url',type=click.STRING)
def findadminpage(url):
    admin.admin(url)

@cli.command(help='Click jacking poc maker')
@click.argument('url',type=click.STRING)
def clickjacking(url):
    CJ.CJ(url)

@cli.command(help='Information gethering')
def getinfo():
    infoGath.InfoGath()

@cli.command(help='To get Banner information')
@click.argument('url',type=click.STRING)
def getbanner(url):
    banner.banner(url)

@cli.command(help='CSRF Poc maker')
def csrfpoc():
    csrf.csrf()

@cli.command(help='Port Scanner')
@click.argument('url',type=click.STRING)
def scanport(url):
    port.port(url)
'''print("\n1. Admin page finder"+"\n2. Clickjacking"+"\n3. Port Scanning"+"\n4. Information Gathering+"+"\n5. Banner"+"\n6. CSRF")

choice = int(input("\n Enter your Choice\n"),10)


if(choice == 1):
    admin.admin()
elif(choice == 2):
    CJ.CJ()
elif(choice == 3):
    port.port()
elif(choice == 4):
    infoGath.InfoGath()
elif(choice == 5):
    banner.banner()
elif(choice == 6):
    csrf.csrf()
else:print("\n Invalid Choice")'''

