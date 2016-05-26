#!/usr/bin/python 

import os 

print '''
versao: 1.0
autor mxdebug
instalar todas as ferramentas do rapid7 :3
mx debug sempre ajudandon voces 
                             .___    ___.                 
  _____ ___  ___           __| _/____\_ |__  __ __  ____  
 /     \\  \/  /  ______  / __ |/ __ \| __ \|  |  \/ ___\ 
|  Y Y  \>    <  /_____/ / /_/ \  ___/| \_\ \  |  / /_/  >
|__|_|  /__/\_ \         \____ |\___  >___  /____/\___  / 
      \/      \/              \/    \/    \/     /_____/  

'''
acao = int(input("digite '1' para sim e '2' para nao"))
if(acao==1):
	print("voce disse que sim")
	
	print("pode demorar um pouco para baixar os arquivos")
	
	print("iniciando.........")
	
	install = int(input("qual e a versao do seu sistema 64ou32"))
	
	if(install==64):
	
		print("baixando os progrmas do rapid7 vs 64bits")
	
		print("iniciando........")
	
		os.system("mkdir rapid7")
		
		os.system("cd rapid7")
		
		print("baixando o msfpro")	
		
		os.system("wget http://downloads.metasploit.com/data/releases/metasploit-latest-linux-x64-installer.run")
		
		print("baixando o NEXPOSE")
		
		print ("baixand o Software Installation ( Linux)")
		
		os.system("wget http://download2.rapid7.com/download/NeXpose-v4/NeXposeSetup-Linux64.bin")
	else:
		
		print("aixando os progrmas do rapid7 vs 32bits")	 
		
		os.system("mkdir rapid7")
		
		os.system("cd rapid7")
		
		print("baixando msfpro")
		
		os.system("wget http://downloads.metasploit.com/data/releases/metasploit-latest-linux-installer.run")
		
else:
	
	
	print("vpce disse que nao ")
	
	print("voce nao instalou as ferrametas do rapid7")
	
print("achou que tinha terminado nada nada kkkk")
print("vamos para os repos do git agora :3")

git = int(input("voce quer instalar os repos do git ? sim '1' nao '2'"))
if(git==1):
	print("vamos la......")
	print("instalando the-backdoor-factory")
	os.system("git clone https://github.com/secretsquirrel/the-backdoor-factory /opt/the-backdoor-factory")	
	print("instalando HTTPScreenShot")
	os.system("git clone https://github.com/breenmachine/httpscreenshot.git /opt/httpscreenshot")
	os.system("pip install selenium")
	os.system("cd /opt/httpscreenshot")
	os.system("chmod +x install-dependencies.sh && ./install-dependencies.sh")
	os.system("cd /etc/opt")
	os.system("git clone https://github.com/pentestgeek/smbexec.git /opt/smbexec")
	os.system("cd /opt/smbexec && ./install.sh")
	os.system("./install.sh")
	print("instalando o Masscan")
	os.system(" apt-get install git gcc make libpcap-dev")
	os.system("git clone https://github.com/robertdavidgraham/masscan.git /opt/masscan")
	os.system("cd /opt/masscan")
	os.system("make")
	os.system("make install")
	print("instalando Gitrob")
	os.system(" git clone https://github.com/michenriksen/gitrob.git /opt/gitrob")
	os.system("gem install bundler")
	os.system("service postgresql start")
	os.system("su postgres")
	os.system("createuser -s gitrob --pwprompt")
	os.system("createdb -O gitrob gitrob")
	os.system("exit")
	os.system("cd /opt/gitrob/bin")
	os.system("gem install gitrob")
	print("instalando o CMSmap")
	os.system("git clone https://github.com/Dionach/CMSmap /opt/CMSmap")
	print("instalando o WPScan")
	os.system("git clone https://github.com/wpscanteam/wpscan.git /opt/wpscan")
	os.system("cd /opt/wpscan && ./wpscan.rb --update")
	print("instalando o Eyewitness")
	os.system("git clone https://github.com/ChrisTruncer/EyeWitness.git /opt/EyeWitness")
	print("instalando o Printer Exploits")
	os.system("git clone https://github.com/MooseDojo/praedasploit /opt/praedasploit")
	print("instalando o SQLMap")
	os.system("git clone https://github.com/sqlmapproject/sqlmap /opt/sqlmap")
	print("instalando o Recon-ng")
	os.system("git clone https://bitbucket.org/LaNMaSteR53/recon-ng.git /opt/recon-ng")
	print ("instalando o Discover Scripts")
	os.system("git clone https://github.com/leebaird/discover.git /opt/discover")
	os.system("cd /opt/discover && ./update.sh")
	print("BeEF Exploitation Framework")
	os.system("cd /opt/")
	os.system("wget https://raw.github.com/beefproject/beef/a6a7536e/install-beef")
	os.system("chmod +x install-beef")
	os.system("./install-beef")
	print("instalando o Responder")
	os.system("git clone https://github.com/SpiderLabs/Responder.git /opt/Responder")
	os.system("git clone https://github.com/cheetz/Easy-P.git /opt/Easy-P")
	os.system("git clone https://github.com/cheetz/Password_Plus_One /opt/Password_Plus_One")
	os.system("git clone https://github.com/cheetz/PowerShell_Popup /opt/PowerShell_Popup")
	os.system("git clone https://github.com/cheetz/icmpshock /opt/icmpshock")
	os.system("git clone https://github.com/cheetz/brutescrape /opt/brutescrape")
	os.system("git clone https://www.github.com/cheetz/reddit_xss /opt/reddit_xss")
	os.system("git clone https://github.com/cheetz/PowerSploit /opt/HP_PowerSploit")
	os.system("git clone https://github.com/cheetz/PowerSploit /opt/HP_PowerSploit")
	os.system("git clone https://github.com/cheetz/nishang /opt/nishang")
	print("instalando o DSHashes")
	os.system("wget http://ptscripts.googlecode.com/svn/trunk/dshashes.py -O /opt/NTDSXtract/dshashes.py")
	print("instalando o SPARTA")
	os.system("git clone https://github.com/secforce/sparta.git /opt/sparta")
	os.system("apt-get install python-elixir")
	os.system("apt-get install ldap-utils rwho rsh-client x11-apps finger")
	print("instalando o NoSQLMap")
	os.system("git clone https://github.com/tcstool/NoSQLMap.git /opt/NoSQLMap")
	print("instalando Spiderfoot ")
	os.system("mkdir /opt/spiderfoot/ && cd /opt/spiderfoot")
	os.system("wget http://sourceforge.net/projects/spiderfoot/files/spiderfoot-2.3.0-src.tar.gz/download")
	os.system("tar xzvf download")
	os.system("pip install lxml")
	os.system("pip install netaddr")
	os.system("pip install M2Crypto")
	os.system("pip install cherrypy")
	os.system("pip install mako")
	print("instalando o WCE")
	os.system("wget www.ampliasecurity.com/research/wce_v1_4beta_universal.zi")
	os.system("mkdir /opt/wce && unzip wce_v1* -d /opt/wce && rm wce_v1*.zip")
	print("instalando o Mimikatz")
	os.system("cd /opt/ && wget http://blog.gentilkiwi.com/downloads/mimikatz_trunk.zip")
	os.system("unzip -d ./mimikatz mimikatz_trunk.zip")
	print("instalando o SET")
	os.system("git clone https://github.com/trustedsec/social-engineer-toolkit/ /opt/set/")
	os.system("cd /opt/set && ./setup.py install")
	print("instalando o PowerSploit (PowerShell)")
	os.system("git clone https://github.com/mattifestation/PowerSploit.git /opt/PowerSploit")
	os.system("cd /opt/PowerSploit && wget https://raw.githubusercontent.com/obscuresec/random/master/StartListener.py && wget https://raw.githubusercontent.com/darkoperator/powershell_scripts/master/ps_encoder.py")
	print("instalando o Nishang (PowerShell)")
	os.system("git clone https://github.com/samratashok/nishang /opt/nishang")
	print("instalando o Veil-Framework ")
	os.system("git clone https://github.com/Veil-Framework/Veil /opt/Veil")
	os.system("cd /opt/Veil/ && ./Install.sh -c")
	print("instalando o Fuzzing Lists (SecLists")
	os.system("git clone https://github.com/danielmiessler/SecLists.git /opt/SecLists")
	print("instalando o Net-Creds Network Parsing ")
	os.system("git clone https://github.com/DanMcInerney/net-creds.git /opt/net-creds")
	print("Installing Wifite")
	os.system("git clone https://github.com/derv82/wifite /opt/wifite")
	print("instalando o WIFIPhisher ")
	os.system("git clone https://github.com/sophron/wifiphisher.git /opt/wifiphisher")
	print("Phishing (Optional):")
	os.system("git clone https://github.com/pentestgeek/phishing-frenzy.git /var/www/phishing-frenzy")
	os.system("git clone https://github.com/macubergeek/gitlist.git /opt/gitlist")
print '''
___  ___. ___   ___          _______   _______ .______    __    __    _______         _______. _______ .___  ___. .______   .______       _______         ___             __   __    __   _______       ___      .__   __.  _______    ______          ____       _______       ___          __    __  .___  ___.         _______.     ___       __       __       __      ____    ____  _______  _______  _______         ___       _______ 
|   \/   | \  \ /  /         |       \ |   ____||   _  \  |  |  |  |  /  _____|       /       ||   ____||   \/   | |   _  \  |   _  \     |   ____|       /   \           |  | |  |  |  | |       \     /   \     |  \ |  | |       \  /  __  \      _ |___ \     |       \     /   \        |  |  |  | |   \/   |        /       |    /   \     |  |     |  |     |  |     \   \  /   / |   ____||   ____||   ____|       /   \     |   ____|
|  \  /  |  \  V  /   ______ |  .--.  ||  |__   |  |_)  | |  |  |  | |  |  __        |   (----`|  |__   |  \  /  | |  |_)  | |  |_)  |    |  |__         /  ^  \          |  | |  |  |  | |  .--.  |   /  ^  \    |   \|  | |  .--.  ||  |  |  |    (_)  __) |    |  .--.  |   /  ^  \       |  |  |  | |  \  /  |       |   (----`   /  ^  \    |  |     |  |     |  |      \   \/   /  |  |__   |  |__   |  |__         /  ^  \    |  |__   
|  |\/|  |   >   <   |______||  |  |  ||   __|  |   _  <  |  |  |  | |  | |_ |        \   \    |   __|  |  |\/|  | |   ___/  |      /     |   __|       /  /_\  \   .--.  |  | |  |  |  | |  |  |  |  /  /_\  \   |  . `  | |  |  |  ||  |  |  |        |__ <     |  |  |  |  /  /_\  \      |  |  |  | |  |\/|  |        \   \      /  /_\  \   |  |     |  |     |  |       \      /   |   __|  |   __|  |   __|       /  /_\  \   |   __|  
|  |  |  |  /  .  \          |  '--'  ||  |____ |  |_)  | |  `--'  | |  |__| |    .----)   |   |  |____ |  |  |  | |  |      |  |\  \----.|  |____     /  _____  \  |  `--'  | |  `--'  | |  '--'  | /  _____  \  |  |\   | |  '--'  ||  `--'  |     _  ___) |    |  '--'  | /  _____  \     |  `--'  | |  |  |  |    .----)   |    /  _____  \  |  `----.|  `----.|  `----.   \    /    |  |____ |  |____ |  |____     /  _____  \  |  |____ 
|__|  |__| /__/ \__\         |_______/ |_______||______/   \______/   \______|    |_______/    |_______||__|  |__| | _|      | _| `._____||_______|   /__/     \__\  \______/   \______/  |_______/ /__/     \__\ |__| \__| |_______/  \______/     (_)|____/     |_______/ /__/     \__\     \______/  |__|  |__|    |_______/    /__/     \__\ |_______||_______||_______|    \__/     |_______||_______||_______|   /__/     \__\ |_______|
                                                                                                                                                                                                                                                                                                                                                                                                                                              

'''

	
