text="http://data.kew.org/sid/SidServlet?Clade=UNCERTAIN&Order=&Family=&APG=off&Genus=&Species=&StorBehav=0&WtFlag=on"

text_crean1=(text.replace("http://data.kew.org/sid/SidServlet?Clade=","")).replace("&Order=&Family=&APG=off&Genus=&Species=&StorBehav=0&WtFlag=on","")
print(text_crean1)