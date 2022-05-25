import json , sys , hashlib , os , time , marshal, getpass
try:
  import requests
except ImportError:
  print("\x1b[41;1m\x1b[37;1m[ ! ] MODULE REQUESTS NOT INSTALLED\x1b[0m")

import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
os.system("clear")
def banner():
  logo = """\x1b[37;1m
 _______                    _______  _______  _______ 
(  __   )|\     /||\     /|(  ___  )(       )(  ___  )
| (  )  |( \   / )| )   ( || (   ) || () () || (   ) |
| | /   | \ (_) / | (___) || (___) || || || || (___) |
| (/ /) |  ) _ (  |  ___  ||  ___  || |(_)| ||  ___  |
|   / | | / ( ) \ | (   ) || (   ) || |   | || (   ) |
|  (__) |( /   \ )| )   ( || )   ( || )   ( || )   ( |
(_______)|/     \||/     \||/     \||/     \||/     \|\x1b[0m"""
  print(logo)
local_token = []
def get(data):
  print("\x1b[37;1m[ A ] GENERATING ACCESS TOKEN ")
  b = open('ses/log', "w")
  try:
    r = requests.get('https://api.facebook.com/restserver.php',params=data)
    print(r.text)
    a = json.loads(r.text)
    b.write(a['access_token'])
    b.close()
    print("[ S ] SUCCESSFULLY LOGINED ")
    main()
  except KeyError:
    print("[ E ] EMAIL PASSWORD / WRONG ")
    os.remove('ses/log')
    main()
  except requests.exceptions.ConnectionError:
    print("[ i ] INTERNET CONNECTION LOST ")
    os.remove('ses/log')
    sys.exit() 
def id():
  print ('[*] login to your facebook account         ')
  id = raw_input('[?] Username : ')
  pwd = raw_input('[?] Password : ');
  API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
  data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
  sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
  x = hashlib.new('md5')
  x.update(sig)
  data.update({'sig':x.hexdigest()})
  get(data)
def main():
  banner()
  print("\x1b[37;1m[ 0xHaMa ] \x1b[0m")
  try:
    r = open("ses/log", "r").read()
    print("[ Log ] SUCCESSFULLY SEASON FOUND ")
  except:
    id()
  target = raw_input("[ ID ] : ")
  x = requests.get("https://graph.facebook.com/"+target+"?access_token="+r)
  z = x.json()
  print(z)
  try:
    name = z['name']
  except:
    name = "Null"
  try:
    birthday = z['birthday']
  except:
    birthday = "Null"
  try:
    username = z['username']
  except:
    usermame = "Null"
  try:
    phone = z['mobile_phone']
  except:
    phone = "Null"
  try:
    mail = z['email']
  except:
    mail = "Null"
  try:
    info_card = ("""
\x1b[40;1m\x1b[37;1m
----------Info----------
Name : """+name+"""
Username : """+username+"""
Birthday : """+birthday+"""
Phone : """+phone+"""
Mail : """+mail+"""
------------------------""")
    print(info_card)
  except:
    print("CHECKPOINT")
  sys.exit()
main()
