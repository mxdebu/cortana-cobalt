#!/usr/bin/python

import os
import sys, traceback

def main():
	try:
		print ('''
yyy                                                
                                                oMN+                                                
                                               :MMMm/                                               
                                              .mMMMNd-                                              
                                             `dMMMMMmh.                                             
                                             yMMMMMMMmy`                                            
                                            +MMMMMMMMNmo                                            
                                           :NMMMMMMMMMmmo                                           
                                          .NMMMMMMMMMMMmm/                                          
                                         `dMMMMMMMMMMMMNmd/                                         
                                        `hMMMMMMMMMMMMMMNmd-                                        
                                        sMMMMMMMMMMMMMMMMmmh-                                       
                                       oNNMMMMMMMMMMMMMMMNmmh`                                      
                                      /NNNNNNNNNMMMMMMMMMMNmmy`                                     
                                     `mNNNNNNNNNNNNNNNMMMMMNmdy`                                    
                                    ` -ymNNNNNNNNNNNNNNNNNNNNddy`                                   
                                   :ho-`-ymNNNNNNNNNNNNNNNNNNmdds                                   
                                  :mNNmho-:odNNNNNNNNNNNNNNNNNmddo                                  
                                 -mmmNNNNmho/odmNNNNNNNNNNNNNNNmdd+                                 
                                .hmmmmmmmmmNmdhhNNNNNNNNNNNNNNNNmddo                                
                               `hmmmmmmmmmmmmmmmmNNNNNNNNNNNNNNNNmdd+                               
                              `hmmmmmmmmmmmmmmmmmmmmmmmNNNNNNNNNNNmdd+                              
                             .hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNNNNmdd+                             
                            .dmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdd/                            
                           .hddddmmmmmmmmmmmmmNNNNNNMMMMMMMNNNNNNNNmmmdh+                           
                          .hdddddddddmmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdo                          
                         .hdddddddmmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMms                         
                        -hdddddmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmo                        
                       -hddmNNMMMMMMMMMNoooyMMMMooooMMMMMMMMMMMMMyooyMMMMMMNy`                      
                      -hmNMMMMMMMMMMMMMm   :MMMM`  `MMMMMMMMMMMMM-  :MMMMMMMMy`                     
                     /mMMMMMMMMMMMMMMMMm   :MMMM`  `MMMMMMMMMMMMM-  :MMMMMMMMMh`                    
                    /NMMMMMMMMMMMMMMMMMm   :MMMM`  `MMMMMMMMMMMMM-  :MMMMMMMMMMy`                   
                   +NMMMMMMMMMMmdddddddy   -dddd    ddddddddNMMMM-  :MMMMMMMMMMMd`                  
                  oMMMMMMMMMMMM:````````    ````    ````````oMMMM-  :MMMMMMMMMMMMd`                 
                 +MMMMMMMMMMMMM+-------.   `----    --------sMMMM-  :MMMMMMMMMMMMMh`                
                sMMMMMMMMMMMMMMNNNNNNNNd   -NNNN`  `NNNNNNNNMMMMM-  :MMMMMMMMMMMMMMm.               
               sMMMMMMMMMMMMMMMNNNNNNNNd   -NNNN`  `NNNNNNNNNMMMM-  :MMMMMMMMMMMMMMMm.              
             `sMMMMMMMMMMMMMMMM/........   `....    ........sMMMM-  :MMMMMMMMdddNMMMMm.             
            `hMMMMMMMMMMMMMMMMM/````````    ````    ````````oMMMM:``/MMMMMMMMMmhs/oymNd-            
           .hMMMMMMMMMMMMMMMMMMmmmmmmmmh   -mmmm`  `mmmmmmmmNMMMMmmmmMMMMMMMMMMMMmy/--/s`           
          .dMMMMMMMMMMMMMMMMMMMMMMMMMMMm   :MMMM`  `MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMms-`            
         .dMMMMMMMMMMMMMMMMMMMMMMMMMMMMm   -NNNN`  `NNNNMMMMMMMMMs++sMMMMMMMMMMMMMMMMMNh/.          
        -NMMMMMMMMMMMMMMMMMMMMMMMNNmmyy/    ....    ...-::/+oyhmm-  :MMMMMMMMMMMMMMMMMMMMNo-        
       :mMMMMMMMMMMMMMMMMMMNNmhs+:-`                            `   .hmNMMMMMMMMMMMMMMMMMMMN/       
      :NMMMMMMMMMMMMMMMNms+:.                                          ./+ymNMMMMMMMMMMMMMMMM+      
     +NMMMMMMMMMMMNmh+:.                                                    `:ohmNMMMMMMMMMMMM+     
    +MMMMMMMMMNmy+-`                                                            `-+smMMMMMMMMMMo    
   oMMMMMMMmy/.                                                                      -ohNMMMMMMMs   
  sMMMMNho:                                                                             `:ohNMMMMs  
`yMMms/.                                                                                    `:smMMh`
yho.                                                                                            .ohy
                  .__              .__  .__                     
_____ _______   ____ |  |__           |  | |__| ____  __ _____  ___
\__  \\_  __ \_/ ___\|  |  \   ______ |  | |  |/    \|  |  \  \/  /
 / __ \|  | \/\  \___|   Y  \ /_____/ |  |_|  |   |  \  |  />    < 
(____  /__|    \___  >___|  /         |____/__|___|  /____//__/\_ \
     \/            \/     \/                       \/            \/
                                                                                    
							  _____                                       
							_/ ____\___________   _______  __ ___________ 
							\   __\/  _ \_  __ \_/ __ \  \/ // __ \_  __ \
							 |  | (  <_> )  | \/\  ___/\   /\  ___/|  | \/
							 |__|  \____/|__|    \___  >\_/  \___  >__|   
							                         \/          \/     
                                                                                                    
                                                                                                                                    
									                      __                   __  .__                
									______   ____   _____/  |_  ____   _______/  |_|__| ____    ____  
									\____ \_/ __ \ /    \   __\/ __ \ /  ___/\   __\  |/    \  / ___\ 
									|  |_> >  ___/|   |  \  | \  ___/ \___ \  |  | |  |   |  \/ /_/  >
									|   __/ \___  >___|  /__|  \___  >____  > |__| |__|___|  /\___  / 
									|__|        \/     \/          \/     \/               \//_____/                                                            
                                               
 \033[1;32m+ -- -- +=[ Autor [mx-debug]]=+
 \033[1;32m+ -- -- +=[ mais de 1500 ferramentas de pentest \033[1;m

		''')
		def inicio1():
			while True:
				print ('''
1) colocar  o repositorio do blackarch eatualizar 
2) ver categorias
3) Install classicmenu indicator
4) Install navegadores
5) Help

			''')

				opcion0 = raw_input("\033[1;36mtools-set>\033[1;m")
			
				while opcion0 == "1":
					print ('''
1) colocar o repositorio blackarch
2) Update
3) instalar o conk e cairo-dock
4) ver os pacotes do black arch / ver o pacman.conf
5) use back para voltar
					''')
					repo = raw_input("\033[1;32oque voce quer meu jovem? >> \033[1;m")
					if repo == "1":
						cmd1 = os.system(" mkdir mx-debug ")
						cmd2 = os.system("cd mx-debug && curl -O https://blackarch.org/strap.sh && chmod +x strap.sh && ./strap.sh")
					elif repo == "2":
						cmd3 = os.system("pacman -Syy")
					elif repo == "3":
						cmd4 = os.system("pacman -S conky cairo-dock ")
					elif repo == "back":
						inicio1()
					elif repo == "gohome":
						inicio1()
					elif repo == "4":
						cmd5 = os.system("sudo pacman -Sg | grep blackarch")
						file = open('/etc/pacman.conf', 'r')
						print (file.read())

					else:
						print ("\033[1;31mDesculpa comando errado\033[1;m") 					
						

				if opcion0 == "3":
					print (''' 
meu feito pelos usuarios do arch linux e ele pode ser usando e varios ambientes , eu indico coloca colocar ele e rezerar o seus desktop , deixando 
so o conk , dock e o menu instalado , que elefica suer top  (ps dica :)

''')
					repo = raw_input("\033[1;32mvoce quer instalar o menu do black arch> \033[1;m")
					if repo == "y":
						cmd1 = os.system("")
						cmd = os.system("yaourt -S blackarch-menus-extended")

				elif opcion0 == "4"	:
					repo = raw_input("\033[1;32mvoce quer colocar uns navegadores na sua distro ? [y/n]> \033[1;m")
					if repo == "y":
						cmd1 = os.system("pacman -S  opera firefox ")
						print ("o google nao pode rodar como root , se for rodar como root , ccoloque --user-date-dir")
						cmd2 = os.system("yaourt -S google ")
				elif opcion0 == "5":
					print (''' 
****************** +comandos de volta+ ******************


\033[1;32mback\033[1;m 	\033[1;33mvolta uma categoria\033[1;m

\033[1;32mgohome\033[1;m	\033[1;33mvolta para o menu iniciar\033[1;m

		''')


				def inicio():
					while opcion0 == "2":
						print ('''
\033[1;36m**************************** principais categorias de ferramentas*****************************\033[1;m

1) Information Gathering			8) Exploitation Tools
2) Vulnerability Analysis			9) Forensics Tools
3) Wireless Attacks				10) Stress Testing
4) Web Applications				11) Password Attacks
5) Sniffing & Spoofing				12) Reverse Engineering
6) Maintaining Access				13) Hardware Hacking
7) Reporting Tools 				14) Extra

0) All ps[tem mais do que 14 categorias , entao se vc quiser instalar todas aperte 0 ]
		ps2[eu so coloquei as principais ferramentas , no comando 0 vai ter muito mais uehueheu]				

			 ''')
						print ("\033[1;32mselecione alguma categoria ou coloque 0 para instalar todas as ferramentas do black arch .\n\033[1;m")

						opcion1 = raw_input("\033[1;36mtools-set>\033[1;m")
						if opcion1 == "back":
							inicio1()
						elif opcion1 == "gohome":
							inicio1()
						elif opcion1 == "0":
							cmd = os.system("pacman -S blackarch")	
						while opcion1 == "1":
							print ('''
\033[1;36m=+[ Information Gathering\033[1;m

 1) acccheck					30) lbd
 2) ace-voip					31) Maltego Teeth
 3) Amap					32) masscan
 4) Automater					33) Metagoofil
 5) bing-ip2hosts				34) Miranda
 6) braa					35) Nmap
 7) CaseFile					36) ntop
 8) CDPSnarf					37) p0f
 9) cisco-torch					38) Parsero
10) Cookie Cadger				39) Recon-ng
11) copy-router-config				40) SET
12) DMitry					41) smtp-user-enum
13) dnmap					42) snmpcheck
14) dnsenum					43) sslcaudit
15) dnsmap					44) SSLsplit
16) DNSRecon					45) sslstrip
17) dnstracer					46) SSLyze
18) dnswalk					47) THC-IPV6
19) DotDotPwn					48) theHarvester
20) enum4linux					49) TLSSLed
21) enumIAX					50) twofi
22) exploitdb					51) URLCrazy
23) Fierce					52) Wireshark
24) Firewalk					53) WOL-E
25) fragroute					54) Xplico
26) fragrouter					55) iSMTP
27) Ghost Phisher				56) InTrace
28) GoLismero					57) hping3
29) goofile

0) Install all Information Gathering tools
ps[tem mais do que 14 categorias , entao se vc quiser instalar todas aperte 0 ]
ps2[eu so coloquei as principais ferramentas , no comando 0 vai ter muito mais uehueheu]
				 
						''')
							print ("\033[1;32mescolha qual ferramenta quer instalar  .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mtools-set>\033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S  acccheck")

							elif opcion2 == "2":
								cmd = os.system("pacman -S  ace-voip")

							elif opcion2 == "3":
								cmd = os.system("pacman -S  amap")
							elif opcion2 == "4":
								cmd = os.system("pacman -S  automater")
							elif opcion2 == "5":
								cmd = os.system("wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
							elif opcion2 == "6":
								cmd = os.system("pacman -S  braa")
							elif opcion2 == "7":
								cmd = os.system("pacman -S  casefile")
							elif opcion2 == "8":
								cmd = os.system("pacman -S  cdpsnarf")
							elif opcion2 == "9":
								cmd = os.system("pacman -S  cisco-torch")
							elif opcion2 == "10":
								cmd = os.system("pacman -S  cookie-cadger")
							elif opcion2 == "11":
								cmd = os.system("pacman -S  copy-router-config")
							elif opcion2 == "12":
								cmd = os.system("pacman -S  dmitry")
							elif opcion2 == "13":
								cmd = os.system("pacman -S  dnmap")
							elif opcion2 == "14":
								cmd = os.system("pacman -S  dnsenum")
							elif opcion2 == "15":
								cmd = os.system("pacman -S  dnsmap")
							elif opcion2 == "16":
								cmd = os.system("pacman -S  dnsrecon")
							elif opcion2 == "17":
								cmd = os.system("pacman -S  dnstracer")
							elif opcion2 == "18":
								cmd = os.system("pacman -S  dnswalk")
							elif opcion2 == "19":
								cmd = os.system("pacman -S  dotdotpwn")
							elif opcion2 == "20":
								cmd = os.system("pacman -S  enum4linux")
							elif opcion2 == "21":
								cmd = os.system("pacman -S  enumiax")
							elif opcion2 == "22":
								cmd = os.system("pacman -S  exploitdb")
							elif opcion2 == "23":
								cmd = os.system("pacman -S  fierce")
							elif opcion2 == "24":
								cmd = os.system("pacman -S  firewalk")
							elif opcion2 == "25":
								cmd = os.system("pacman -S  fragroute")
							elif opcion2 == "26":
								cmd = os.system("pacman -S  fragrouter")
							elif opcion2 == "27":
								cmd = os.system("pacman -S  ghost-phisher")
							elif opcion2 == "28":
								cmd = os.system("pacman -S  golismero")
							elif opcion2 == "29":
								cmd = os.system("pacman -S  goofile")
							elif opcion2 == "30":
								cmd = os.system("pacman -S  lbd")
							elif opcion2 == "31":
								cmd = os.system("pacman -S  maltego-teeth")
							elif opcion2 == "32":
								cmd = os.system("pacman -S  masscan")
							elif opcion2 == "33":
								cmd = os.system("pacman -S  metagoofil")
							elif opcion2 == "34":
								cmd = os.system("pacman -S  miranda")
							elif opcion2 == "35":
								cmd = os.system("pacman -S  nmap")
							elif opcion2 == "36":
								print ('ntop is unavailable')
							elif opcion2 == "37":
								cmd = os.system("pacman -S  p0f")
							elif opcion2 == "38":
								cmd = os.system("pacman -S  parsero")
							elif opcion2 == "39":
								cmd = os.system("pacman -S  recon-ng")
							elif opcion2 == "40":
								cmd = os.system("pacman -S  set")
							elif opcion2 == "41":
								cmd = os.system("pacman -S  smtp-user-enum")
							elif opcion2 == "42":
								cmd = os.system("pacman -S  snmpcheck")
							elif opcion2 == "43":
								cmd = os.system("pacman -S  sslcaudit")
							elif opcion2 == "44":
								cmd = os.system("pacman -S  sslsplit")
							elif opcion2 == "45":
								cmd = os.system("pacman -S  sslstrip")
							elif opcion2 == "46":
								cmd = os.system("pacman -S  sslyze")
							elif opcion2 == "47":
								cmd = os.system("pacman -S  thc-ipv6")
							elif opcion2 == "48":
								cmd = os.system("pacman -S  theharvester")
							elif opcion2 == "49":
								cmd = os.system("pacman -S  tlssled")
							elif opcion2 == "50":
								cmd = os.system("pacman -S  twofi")
							elif opcion2 == "51":
								cmd = os.system("pacman -S  urlcrazy")
							elif opcion2 == "52":
								cmd = os.system("pacman -S  wireshark")
							elif opcion2 == "53":
								cmd = os.system("pacman -S  wol-e")
							elif opcion2 == "54":
								cmd = os.system("pacman -S  xplico")
							elif opcion2 == "55":
								cmd = os.system("pacman -S  ismtp")
							elif opcion2 == "56":
								cmd = os.system("pacman -S  intrace")
							elif opcion2 == "57":
								cmd = os.system("pacman -S  hping3")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()		
							elif opcion2 == "0":
								cmd = os.system("pacman -S  blackarch-fingerprint")				
							else:
								print ("\033[1;31mDesculpa comando errado\033[1;m")



						while opcion1 == "2":
							print ('''
\033[1;36m=+[ Vulnerability Analysis\033[1;m

 1) BBQSQL				18) Nmap
 2) BED					19)ohrwurm
 3) cisco-auditing-tool			20) openvas-administrator
 4) cisco-global-exploiter		21) openvas-cli
 5) cisco-ocs				22) openvas-manager
 6) cisco-torch				23) openvas-scanner
 7) copy-router-config			24) Oscanner
 8) commix				25) Powerfuzzer
 9) DBPwAudit				26) sfuzz
10) DoonaDot				27) SidGuesser
11) DotPwn				28) SIPArmyKnife
12) Greenbone Security Assistant 	29) sqlmap
13) GSD					30) Sqlninja
14) HexorBase				31) sqlsus
15) Inguma				32) THC-IPV6
16) jSQL				33) tnscmd10g
17) Lynis				34) unix-privesc-check
					35) Yersinia

0) Install all Vulnerability Analysis tools
ps[tem mais do que 14 categorias , entao se vc quiser instalar todas aperte 0 ]
ps2[eu so coloquei as principais ferramentas , no comando 0 vai ter muito mais uehueheu]
				 
						''')
							print ("\033[1;32mescolha qual ferramenta quer instalar  .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mtools-set>\033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S  bbqsql")

							elif opcion2 == "2":
								cmd = os.system("pacman -S  bed")

							elif opcion2 == "3":
								cmd = os.system("pacman -S  cisco-auditing-tool")
							elif opcion2 == "4":
								cmd = os.system("pacman -S  cisco-global-exploiter")
							elif opcion2 == "5":
								cmd = os.system("pacman -S  cisco-ocs")
							elif opcion2 == "6":
								cmd = os.system("pacman -S  cisco-torch")
							elif opcion2 == "7":
								cmd = os.system("pacman -S  copy-router-config")
							elif opcion2 == "8":
								cmd = os.system("pacman -S  git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
							elif opcion2 == "9":
								cmd = os.system("echo 'download page : http://www.cqure.net/wp/tools/database/dbpwaudit/'")
							elif opcion2 == "10":
								cmd = os.system("pacman -S  doona")
							elif opcion2 == "11":
								cmd = os.system("pacman -S  dotdotpwn")
							elif opcion2 == "12":
								cmd = os.system("pacman -S  greenbone-security-assistant")
							elif opcion2 == "13":
								cmd = os.system("pacman -S  git && git clone git://git.kali.org/packages/gsd.git")
							elif opcion2 == "14":
								cmd = os.system("pacman -S  hexorbase")
							elif opcion2 == "15":
								print ("Please download inguma from : http://inguma.sourceforge.net")
							elif opcion2 == "16":
								cmd = os.system("pacman -S  jsql")
							elif opcion2 == "17":
								cmd = os.system("pacman -S  lynis")
							elif opcion2 == "18":
								cmd = os.system("pacman -S  nmap")
							elif opcion2 == "19":
								cmd = os.system("pacman -S  ohrwurm")
							elif opcion2 == "20":
								cmd = os.system("pacman -S  openvas-administrator")
							elif opcion2 == "21":
								cmd = os.system("pacman -S  openvas-cli")
							elif opcion2 == "22":
								cmd = os.system("pacman -S  openvas-manager")
							elif opcion2 == "23":
								cmd = os.system("pacman -S  openvas-scanner")
							elif opcion2 == "24":
								cmd = os.system("pacman -S  oscanner")
							elif opcion2 == "25":
								cmd = os.system("pacman -S  powerfuzzer")
							elif opcion2 == "26":
								cmd = os.system("pacman -S  sfuzz")
							elif opcion2 == "27":
								cmd = os.system("pacman -S  sidguesser")
							elif opcion2 == "28":
								cmd = os.system("pacman -S  siparmyknife")
							elif opcion2 == "29":
								cmd = os.system("pacman -S  sqlmap")
							elif opcion2 == "30":
								cmd = os.system("pacman -S  sqlninja")
							elif opcion2 == "31":
								cmd = os.system("pacman -S  sqlsus")
							elif opcion2 == "32":
								cmd = os.system("pacman -S  thc-ipv6")
							elif opcion2 == "33":
								cmd = os.system("pacman -S  tnscmd10g")
							elif opcion2 == "34":
								cmd = os.system("pacman -S  unix-privesc-check")
							elif opcion2 == "35":
								cmd = os.system("pacman -S  yersinia")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()						
							elif opcion2 == "0":
								cmd = os.system("pacman -S  blackarch-scanner")						
							else:
								print ("\033[1;31mDesculpa comando errado\033[1;m")

						while opcion1 == "3":
							print ('''
		\033[1;36m=+[ Wireless Attacks\033[1;m

 1) Aircrack-ng				17) kalibrate-rtl
 2) Asleap				18) KillerBee
 3) Bluelog				19) Kismet
 4) BlueMaho				20) mdk3
 5) Bluepot				21) mfcuk
 6) BlueRanger				22) mfoc
 7) Bluesnarfer				23) mfterm
 8) Bully				24) Multimon-NG
 9) coWPAtty				25) PixieWPS
10) crackle				26) Reaver
11) eapmd5pass				27) redfang
12) Fern Wifi Cracker			28) RTLSDR Scanner
13) Ghost Phisher			29) Spooftooph
14) GISKismet				30) Wifi Honey				31) Wifitap
16) gr-scan				32) Wifite 
ps[tem mais do que 14 categorias , entao se vc quiser instalar todas aperte 0 ]
ps2[eu so coloquei as principais ferramentas , no comando 0 vai ter muito mais uehueheu]
0) Install all Wireless Attacks tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mtools-set>\033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S  aircrack-ng")

							elif opcion2 == "2":
								cmd = os.system("pacman -S  asleap")

							elif opcion2 == "3":
								cmd = os.system("pacman -S  bluelog")
							elif opcion2 == "4":
								cmd = os.system("pacman -S  git && git clone git://git.kali.org/packages/bluemaho.git")
							elif opcion2 == "5":
								cmd = os.system("pacman -S  git && git clone git://git.kali.org/packages/bluepot.git")
							elif opcion2 == "6":
								cmd = os.system("pacman -S  blueranger")
							elif opcion2 == "7":
								cmd = os.system("pacman -S  bluesnarfer")
							elif opcion2 == "8":
								cmd = os.system("pacman -S  bully")
							elif opcion2 == "9":
								cmd = os.system("pacman -S  cowpatty")
							elif opcion2 == "10":
								cmd = os.system("pacman -S  crackle")
							elif opcion2 == "11":
								cmd = os.system("pacman -S  eapmd5pass")
							elif opcion2 == "12":
								cmd = os.system("pacman -S  fern-wifi-cracker")
							elif opcion2 == "13":
								cmd = os.system("pacman -S  ghost-phisher")
							elif opcion2 == "14":
								cmd = os.system("pacman -S  giskismet")
							elif opcion2 == "16":
								cmd = os.system("pacman -S  git && git clone git://git.kali.org/packages/gr-scan.git")
							elif opcion2 == "17":
								cmd = os.system("pacman -S  kalibrate-rtl")
							elif opcion2 == "18":
								cmd = os.system("pacman -S  killerbee")
							elif opcion2 == "19":
								cmd = os.system("pacman -S  kismet")
							elif opcion2 == "20":
								cmd = os.system("pacman -S  mdk3")
							elif opcion2 == "21":
								cmd = os.system("pacman -S  mfcuk")
							elif opcion2 == "22":
								cmd = os.system("pacman -S  mfoc")
							elif opcion2 == "23":
								cmd = os.system("pacman -S  mfterm")
							elif opcion2 == "24":
								cmd = os.system("pacman -S  multimon-ng")
							elif opcion2 == "25":
								cmd = os.system("pacman -S  pixiewps")
							elif opcion2 == "26":
								cmd = os.system("pacman -S  reaver")
							elif opcion2 == "27":
								cmd = os.system("pacman -S  redfang")
							elif opcion2 == "28":
								cmd = os.system("pacman -S  rtlsdr-scanner")
							elif opcion2 == "29":
								cmd = os.system("pacman -S  spooftooph")
							elif opcion2 == "30":
								cmd = os.system("pacman -S  wifi-honey")
							elif opcion2 == "31":
								cmd = os.system("pacman -S  wifitap")
							elif opcion2 == "32":
								cmd = os.system("pacman -S  wifite")
							elif opcion2 == "0":
								cmd = os.system("pacman -S  blackarch-wireless")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()						
							else:
								print ("\033[1;31mDesculpa comando errado\033[1;m")
						while opcion1 == "4":
							print ('''
\033[1;36m=+[ Web Applications\033[1;m

 1) apache-users			21) Parsero
 2) Arachni				22) plecost
 3) BBQSQL				23) Powerfuzzer
 4) BlindElephant			24) ProxyStrike
 5) Burp Suite				25) Recon-ng
 6) commix				26) Skipfish
 7) CutyCapt				27) sqlmap
 8) DAVTest				28) Sqlninja
 9) deblaze				29) sqlsus
10) DIRB				30) ua-tester
11) DirBuster				31) Uniscan
12) fimap				32) Vega
13) FunkLoad				33) w3af
14) Grabber				34) WebScarab
15) jboss-autopwn			35) Webshag
16) joomscan				36) WebSlayer
17) jSQL				37) WebSploit
18) Maltego Teeth			38) Wfuzz
19) PadBuster				39) WPScan
20) Paros				40) XSSer
					41) zaproxy
ps[tem mais do que 14 categorias , entao se vc quiser instalar todas aperte 0 ]
ps2[eu so coloquei as principais ferramentas , no comando 0 vai ter muito mais uehueheu]
0) Install all Web Applications tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

							
							opcion2 = raw_input("\033[1;36mtools-set>\033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S  apache-users")

							elif opcion2 == "2":
								cmd = os.system("pacman -S  arachni")

							elif opcion2 == "3":
								cmd = os.system("pacman -S  bbqsql")
							elif opcion2 == "4":
								cmd = os.system("pacman -S  blindelephant")
							elif opcion2 == "5":
								cmd = os.system("pacman -S  burpsuite")
							elif opcion2 == "6":
								cmd = os.system("pacman -S  cutycapt")
							elif opcion2 == "7":
								cmd = os.system("pacman -S  git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
							elif opcion2 == "8":
								cmd = os.system("pacman -S  davtest")
							elif opcion2 == "9":
								cmd = os.system("pacman -S  deblaze")
							elif opcion2 == "10":
								cmd = os.system("pacman -S  dirb")
							elif opcion2 == "11":
								cmd = os.system("pacman -S  dirbuster")
							elif opcion2 == "12":
								cmd = os.system("pacman -S  fimap")
							elif opcion2 == "13":
								cmd = os.system("pacman -S  funkload")
							elif opcion2 == "14":
								cmd = os.system("pacman -S  grabber")
							elif opcion2 == "15":
								cmd = os.system("pacman -S  jboss-autopwn")
							elif opcion2 == "16":
								cmd = os.system("pacman -S  joomscan")
							elif opcion2 == "17":
								cmd = os.system("pacman -S  jsql")
							elif opcion2 == "18":
								cmd = os.system("pacman -S  maltego-teeth")
							elif opcion2 == "19":
								cmd = os.system("pacman -S  padbuster")
							elif opcion2 == "20":
								cmd = os.system("pacman -S  paros")
							elif opcion2 == "21":
								cmd = os.system("pacman -S  parsero")
							elif opcion2 == "22":
								cmd = os.system("pacman -S  plecost")
							elif opcion2 == "23":
								cmd = os.system("pacman -S  powerfuzzer")
							elif opcion2 == "24":
								cmd = os.system("pacman -S  proxystrike")
							elif opcion2 == "25":
								cmd = os.system("pacman -S  recon-ng")
							elif opcion2 == "26":
								cmd = os.system("pacman -S  skipfish")
							elif opcion2 == "27":
								cmd = os.system("pacman -S  sqlmap")
							elif opcion2 == "28":
								cmd = os.system("pacman -S  sqlninja")
							elif opcion2 == "29":
								cmd = os.system("pacman -S  sqlsus")
							elif opcion2 == "30":
								cmd = os.system("pacman -S  ua-tester")
							elif opcion2 == "31":
								cmd = os.system("pacman -S  uniscan")
							elif opcion2 == "32":
								cmd = os.system("pacman -S  vega")
							elif opcion2 == "33":
								cmd = os.system("pacman -S  w3af")
							elif opcion2 == "34":
								cmd = os.system("pacman -S  webscarab")
							elif opcion2 == "35":
								print ("Webshag is unavailable")
							elif opcion2 == "36":
								cmd = os.system("pacman -S  git && git clone git://git.kali.org/packages/webslayer.git")
							elif opcion2 == "37":
								cmd = os.system("pacman -S  websploit")
							elif opcion2 == "38":
								cmd = os.system("pacman -S  wfuzz")
							elif opcion2 == "39":
								cmd = os.system("pacman -S  wpscan")
							elif opcion2 == "40":
								cmd = os.system("pacman -S  xsser")
							elif opcion2 == "41":
								cmd = os.system("pacman -S  zaproxy")										
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()	
							elif opcion2 == "0":
								cmd = os.system("pacman -S blackarch-webapp ")												
							else:
								print ("\033[1;31mDesculpa comando errado\033[1;m")
						while opcion1 == "5":
							print ('''
\033[1;36m=+[ Sniffing & Spoofing\033[1;m

 1) Burp Suite				17) rtpmixsound
 2) DNSChef				18) sctpscan
 3) fiked				19) SIPArmyKnife
 4) hamster-sidejack			20) SIPp
 5) HexInject				21) SIPVicious
 6) iaxflood				22) SniffJoke
 7) inviteflood				23) SSLsplit
 8) iSMTP				24) sslstrip
 9) isr-evilgrade			25) THC-IPV6
10) mitmproxy				26) VoIPHopper
11) ohrwurm				27) WebScarab
12) protos-sip				28) Wifi Honey
13) rebind				29) Wireshark
14) responder				30) xspy
15) rtpbreak				31) Yersinia
16) rtpinsertsound			32) zaproxy 
ps[tem mais do que 14 categorias , entao se vc quiser instalar todas aperte 0 ]
ps2[eu so coloquei as principais ferramentas , no comando 0 vai ter muito mais uehueheu]
0) Install all Sniffing & Spoofing tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mtools-set>\033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S  burpsuite")

							elif opcion2 == "2":
								cmd = os.system("pacman -S  dnschef")

							elif opcion2 == "3":
								cmd = os.system("pacman -S  fiked")
							elif opcion2 == "4":
								cmd = os.system("pacman -S  hamster-sidejack")
							elif opcion2 == "5":
								cmd = os.system("pacman -S  hexinject")
							elif opcion2 == "6":
								cmd = os.system("pacman -S  iaxflood")
							elif opcion2 == "7":
								cmd = os.system("pacman -S  inviteflood")
							elif opcion2 == "8":
								cmd = os.system("pacman -S  ismtp")
							elif opcion2 == "9":
								cmd = os.system("pacman -S  git && git clone git://git.kali.org/packages/isr-evilgrade.git")
							elif opcion2 == "10":
								cmd = os.system("pacman -S  mitmproxy")
							elif opcion2 == "11":
								cmd = os.system("pacman -S  ohrwurm")
							elif opcion2 == "12":
								cmd = os.system("pacman -S  protos-sip")
							elif opcion2 == "13":
								cmd = os.system("pacman -S  rebind")
							elif opcion2 == "14":
								cmd = os.system("pacman -S  responder")
							elif opcion2 == "15":
								cmd = os.system("pacman -S  rtpbreak")
							elif opcion2 == "16":
								cmd = os.system("pacman -S  rtpinsertsound")
							elif opcion2 == "17":
								cmd = os.system("pacman -S  rtpmixsound")
							elif opcion2 == "18":
								cmd = os.system("pacman -S  sctpscan")
							elif opcion2 == "19":
								cmd = os.system("pacman -S  siparmyknife")
							elif opcion2 == "20":
								cmd = os.system("pacman -S  sipp")
							elif opcion2 == "21":
								cmd = os.system("pacman -S  sipvicious")
							elif opcion2 == "22":
								cmd = os.system("pacman -S  sniffjoke")
							elif opcion2 == "23":
								cmd = os.system("pacman -S  sslsplit")
							elif opcion2 == "24":
								cmd = os.system("pacman -S  sslstrip")
							elif opcion2 == "25":
								cmd = os.system("pacman -S  thc-ipv6")
							elif opcion2 == "26":
								cmd = os.system("pacman -S  voiphopper")
							elif opcion2 == "27":
								cmd = os.system("pacman -S  webscarab")
							elif opcion2 == "28":
								cmd = os.system("pacman -S  wifi-honey")
							elif opcion2 == "29":
								cmd = os.system("pacman -S  wireshark")
							elif opcion2 == "30":
								cmd = os.system("pacman -S  xspy")
							elif opcion2 == "31":
								cmd = os.system("pacman -S  yersinia")
							elif opcion2 == "32":
								cmd = os.system("pacman -S  zaproxy")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()


							elif opcion2 == "0":
								cmd = os.system("pacman -S blackarch-sniffer blackarch-spoof")  
							else:
								print ("\033[1;31mDesculpa comando errado\033[1;m")

						while opcion1 == "6":
							print ('''
\033[1;36m=+[ Maintaining Access\033[1;m

 1) CryptCat
 2) Cymothoa
 3) dbd
 4) dns2tcp
 5) http-tunnel	
 6) HTTPTunnel
 7) Intersect
 8) Nishang
 9) polenum
10) PowerSploit
11) pwnat
12) RidEnum
13) sbd
14) U3-Pwn
15) Webshells
16) Weevely
ps[tem mais do que 14 categorias , entao se vc quiser instalar todas aperte 0 ]
ps2[eu so coloquei as principais ferramentas , no comando 0 vai ter muito mais uehueheu]
0) Install all Maintaining Access tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mtools-set>\033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S  cryptcat")

							elif opcion2 == "2":
								cmd = os.system("pacman -S  cymothoa")

							elif opcion2 == "3":
								cmd = os.system("pacman -S  dbd")
							elif opcion2 == "4":
								cmd = os.system("pacman -S  dns2tcp")
							elif opcion2 == "5":
								cmd = os.system("pacman -S  http-tunnel")
							elif opcion2 == "6":
								cmd = os.system("pacman -S  httptunnel")
							elif opcion2 == "7":
								cmd = os.system("pacman -S  intersect")
							elif opcion2 == "8":
								cmd = os.system("pacman -S  nishang")
							elif opcion2 == "9":
								cmd = os.system("pacman -S  polenum")
							elif opcion2 == "10":
								cmd = os.system("pacman -S  powersploit")
							elif opcion2 == "11":
								cmd = os.system("pacman -S  pwnat")
							elif opcion2 == "12":
								cmd = os.system("pacman -S  ridenum")
							elif opcion2 == "13":
								cmd = os.system("pacman -S  sbd")
							elif opcion2 == "14":
								cmd = os.system("pacman -S  u3-pwn")
							elif opcion2 == "15":
								cmd = os.system("pacman -S  webshells")
							elif opcion2 == "16":
								cmd = os.system("pacman -S  weevely")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("pacman -S  -y blackarch-tunnel")
							else:
								print ("\033[1;31mDesculpa comando errado\033[1;m")
						while opcion1 == "7":
							print ('''
\033[1;36m=+[ Reporting Tools\033[1;m

1) CaseFile
2) CutyCapt
3) dos2unix
4) Dradis
5) KeepNote	
6) MagicTree
7) Metagoofil
8) Nipper-ng
9) pipal
ps[tem mais do que 14 categorias , entao se vc quiser instalar todas aperte 0 ]
ps2[eu so coloquei as principais ferramentas , no comando 0 vai ter muito mais uehueheu]
0) Install all Reporting Tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mtools-set>\033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S  casefile")

							elif opcion2 == "2":
								cmd = os.system("pacman -S  cutycapt")

							elif opcion2 == "3":
								cmd = os.system("pacman -S  dos2unix")
							elif opcion2 == "4":
								cmd = os.system("pacman -S  dradis")
							elif opcion2 == "5":
								cmd = os.system("pacman -S  keepnote")
							elif opcion2 == "6":
								cmd = os.system("pacman -S  magictree")
							elif opcion2 == "7":
								cmd = os.system("pacman -S  metagoofil")
							elif opcion2 == "8":
								cmd = os.system("pacman -S  nipper-ng")
							elif opcion2 == "9":
								cmd = os.system("pacman -S  pipal")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("pacman -S  -y casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal")  
							else:
								print ("\033[1;31mDesculpa comando errado\033[1;m")

						while opcion1 == "8":
							print ('''
\033[1;36m=+[ Exploitation Tools\033[1;m

 1) Armitage
 2) Backdoor Factory
 3) BeEF
 4) cisco-auditing-tool
 5) cisco-global-exploiter	
 6) cisco-ocs
 7) cisco-torch
 8) commix
 9) crackle
10) jboss-autopwn
11) Linux Exploit Suggester
12) Maltego Teeth
13) SET
14) ShellNoob
15) sqlmap
16) THC-IPV6
17) Yersinia
ps[tem mais do que 14 categorias , entao se vc quiser instalar todas aperte 0 ]
ps2[eu so coloquei as principais ferramentas , no comando 0 vai ter muito mais uehueheu]
0) Install all Exploitation Tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S  armitage")

							elif opcion2 == "2":
								cmd = os.system("pacman -S  backdoor-factory")

							elif opcion2 == "3":
								cmd = os.system("pacman -S  beef-xss")
							elif opcion2 == "4":
								cmd = os.system("pacman -S  cisco-auditing-tool")
							elif opcion2 == "5":
								cmd = os.system("pacman -S  cisco-global-exploiter")
							elif opcion2 == "6":
								cmd = os.system("pacman -S  cisco-ocs")
							elif opcion2 == "7":
								cmd = os.system("pacman -S  cisco-torch")
							elif opcion2 == "8":
								cmd = os.system("pacman -S  git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
							elif opcion2 == "9":
								cmd = os.system("pacman -S  crackle")
							elif opcion2 == "10":
								cmd = os.system("pacman -S  jboss-autopwn")
							elif opcion2 == "11":
								cmd = os.system("pacman -S  linux-exploit-suggester")
							elif opcion2 == "12":
								cmd = os.system("pacman -S  maltego-teeth")
							elif opcion2 == "13":
								cmd = os.system("pacman -S  set")
							elif opcion2 == "14":
								cmd = os.system("pacman -S  shellnoob")
							elif opcion2 == "15":
								cmd = os.system("pacman -S  sqlmap")
							elif opcion2 == "16":
								cmd = os.system("pacman -S  thc-ipv6")
							elif opcion2 == "17":
								cmd = os.system("pacman -S  yersinia")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("pacman -S    blackarch-exploitation armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss")  						
							else:
								print ("\033[1;31mDesculpa comando errado\033[1;m")

						while opcion1 == "9":
							print ('''
\033[1;36m=+[ Forensics Tools\033[1;m

 1) Binwalk				11) extundelete
 2) bulk-extractor			12) Foremost
 3) Capstone				13) Galleta
 4) chntpw				14) Guymager
 5) Cuckoo				15) iPhone Backup Analyzer
 6) dc3dd				16) p0f
 7) ddrescue				17) pdf-parser
 8) DFF					18) pdfid
 9) diStorm3				19) pdgmail
10) Dumpzilla				20) peepdf
					21) RegRipper
					22) Volatility
					23) Xplico
ps[tem mais do que 14 categorias , entao se vc quiser instalar todas aperte 0 ]
ps2[eu so coloquei as principais ferramentas , no comando 0 vai ter muito mais uehueheu]
0) Install all Forensics Tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mtools-set>\033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S  binwalk")

							elif opcion2 == "2":
								cmd = os.system("pacman -S  bulk-extractor")

							elif opcion2 == "3":
								cmd = os.system("pacman -S  git && git clone git://git.kali.org/packages/capstone.git")
							elif opcion2 == "4":
								cmd = os.system("pacman -S  chntpw")
							elif opcion2 == "5":
								cmd = os.system("pacman -S  cuckoo")
							elif opcion2 == "6":
								cmd = os.system("pacman -S  dc3dd")
							elif opcion2 == "7":
								cmd = os.system("pacman -S  ddrescue")
							elif opcion2 == "8":
								print ('dff is unavailable')
							elif opcion2 == "9":
								cmd = os.system("pacman -S  git && git clone git://git.kali.org/packages/distorm3.git")
							elif opcion2 == "10":
								cmd = os.system("pacman -S  dumpzilla")
							elif opcion2 == "11":
								cmd = os.system("pacman -S  extundelete")
							elif opcion2 == "12":
								cmd = os.system("pacman -S  foremost")
							elif opcion2 == "13":
								cmd = os.system("pacman -S  galleta")
							elif opcion2 == "14":
								cmd = os.system("pacman -S  guymager")
							elif opcion2 == "15":
								cmd = os.system("pacman -S  iphone-backup-analyzer")
							elif opcion2 == "16":
								cmd = os.system("pacman -S  p0f")
							elif opcion2 == "17":
								cmd = os.system("pacman -S  pdf-parser")
							elif opcion2 == "18":
								cmd = os.system("pacman -S  pdfid")
							elif opcion2 == "19":
								cmd = os.system("pacman -S  pdgmail")
							elif opcion2 == "20":
								cmd = os.system("pacman -S  peepdf")
							elif opcion2 == "21":
								print ("Regripper is unavailable")
							elif opcion2 == "22":
								cmd = os.system("pacman -S  volatility")
							elif opcion2 == "23":
								cmd = os.system("pacman -S  xplico")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("pacman -S  -blackarch-forensic binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico")						
							else:
								print ("\033[1;31mDesculpa comando errado\033[1;m")
						while opcion1 == "10":
							print ('''
\033[1;36m=+[ Stress Testing\033[1;m

 1) DHCPig
 2) FunkLoad
 3) iaxflood
 4) Inundator
 5) inviteflood	
 6) ipv6-toolkit
 7) mdk3
 8) Reaver
 9) rtpflood
10) SlowHTTPTest
11) t50
12) Termineter
13) THC-IPV6
14) THC-SSL-DOS 		
ps[tem mais do que 14 categorias , entao se vc quiser instalar todas aperte 0 ]
ps2[eu so coloquei as principais ferramentas , no comando 0 vai ter muito mais uehueheu]
0) Install all Stress Testing tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mtools-set>\033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S  dhcpig")

							elif opcion2 == "2":
								cmd = os.system("pacman -S  funkload")

							elif opcion2 == "3":
								cmd = os.system("pacman -S  iaxflood")
							elif opcion2 == "4":
								cmd = os.system("pacman -S  git && git clone git://git.kali.org/packages/inundator.git")
							elif opcion2 == "5":
								cmd = os.system("pacman -S  inviteflood")
							elif opcion2 == "6":
								cmd = os.system("pacman -S  ipv6-toolkit")
							elif opcion2 == "7":
								cmd = os.system("pacman -S  mdk3")
							elif opcion2 == "8":
								cmd = os.system("pacman -S  reaver")
							elif opcion2 == "9":
								cmd = os.system("pacman -S  rtpflood")
							elif opcion2 == "10":
								cmd = os.system("pacman -S  slowhttptest")
							elif opcion2 == "11":
								cmd = os.system("pacman -S  t50")
							elif opcion2 == "12":
								cmd = os.system("pacman -S  termineter")
							elif opcion2 == "13":
								cmd = os.system("pacman -S  thc-ipv6")
							elif opcion2 == "14":
								cmd = os.system("pacman -S  thc-ssl-dos ")    				             										
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("pacman -S  -y dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos")
							else:
								print ("\033[1;31mDesculpa comando errado\033[1;m")
						while opcion1 == "11":
							print ('''
\033[1;36m=+[ Password Attacks\033[1;m

 1) acccheck				19) Maskprocessor
 2) Burp Suite				20) multiforcer
 3) CeWL				21) Ncrack
 4) chntpw				22) oclgausscrack
 5) cisco-auditing-tool			23) PACK
 6) CmosPwd				24) patator
 7) creddump				25) phrasendrescher
 8) crunch				26) polenum
 9) DBPwAudit				27) RainbowCrack
10) findmyhash				28) rcracki-mt
11) gpp-decrypt				29) RSMangler
12) hash-identifier			30) SQLdict
13) HexorBase				31) Statsprocessor
14) THC-Hydra				32) THC-pptp-bruter
15) John the Ripper			33) TrueCrack
16) Johnny				34) WebScarab 
17) keimpx				35) wordlists 
18) Maltego Teeth			36) zaproxy 
ps[tem mais do que 14 categorias , entao se vc quiser instalar todas aperte 0 ]
ps2[eu so coloquei as principais ferramentas , no comando 0 vai ter muito mais uehueheu]
0) Install all Password Attacks tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mtools-set>\033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S  acccheck")

							elif opcion2 == "2":
								cmd = os.system("pacman -S  burpsuite")

							elif opcion2 == "3":
								cmd = os.system("pacman -S  cewl")
							elif opcion2 == "4":
								cmd = os.system("pacman -S  chntpw")
							elif opcion2 == "5":
								cmd = os.system("pacman -S  cisco-auditing-tool")
							elif opcion2 == "6":
								cmd = os.system("pacman -S  cmospwd")
							elif opcion2 == "7":
								cmd = os.system("pacman -S  creddump")
							elif opcion2 == "8":
								cmd = os.system("pacman -S  crunch")
							elif opcion2 == "9":
								cmd = os.system("pacman -S  git && git clone git://git.kali.org/packages/dbpwaudit.git")
							elif opcion2 == "10":
								cmd = os.system("pacman -S  findmyhash")
							elif opcion2 == "11":
								cmd = os.system("pacman -S  gpp-decrypt")
							elif opcion2 == "12":
								cmd = os.system("pacman -S  hash-identifier")
							elif opcion2 == "13":
								cmd = os.system("pacman -S  hexorbase")
							elif opcion2 == "14":
								cmd = os.system("echo 'please visit : https://www.thc.org/thc-hydra/' ")
							elif opcion2 == "15":
								cmd = os.system("pacman -S  john")
							elif opcion2 == "16":
								cmd = os.system("pacman -S  johnny")
							elif opcion2 == "17":
								cmd = os.system("pacman -S  keimpx")
							elif opcion2 == "18":
								cmd = os.system("pacman -S  maltego-teeth")
							elif opcion2 == "19":
								cmd = os.system("pacman -S  maskprocessor")
							elif opcion2 == "20":
								cmd = os.system("pacman -S  multiforcer")
							elif opcion2 == "21":
								cmd = os.system("pacman -S  ncrack")
							elif opcion2 == "22":
								cmd = os.system("pacman -S  oclgausscrack")
							elif opcion2 == "23":
								cmd = os.system("pacman -S  pack")
							elif opcion2 == "24":
								cmd = os.system("pacman -S  patator")
							elif opcion2 == "25":
								cmd = os.system("echo 'please visit : http://www.leidecker.info/projects/phrasendrescher/index.shtml' ")
							elif opcion2 == "26":
								cmd = os.system("pacman -S  polenum")
							elif opcion2 == "27":
								cmd = os.system("pacman -S  rainbowcrack")
							elif opcion2 == "28":
								cmd = os.system("pacman -S  rcracki-mt")
							elif opcion2 == "29":
								cmd = os.system("pacman -S  rsmangler")
							elif opcion2 == "30":
								print ("Sqldict is unavailable")
							elif opcion2 == "31":
								cmd = os.system("pacman -S  statsprocessor")
							elif opcion2 == "32":
								cmd = os.system("pacman -S  thc-pptp-bruter")
							elif opcion2 == "33":
								cmd = os.system("pacman -S  truecrack")
							elif opcion2 == "34":
								cmd = os.system("pacman -S  webscarab")
							elif opcion2 == "35":
								cmd = os.system("pacman -S  wordlists")
							elif opcion2 == "36":
								cmd = os.system("pacman -S  zaproxy")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("pacman -S  blackarch-cracker  acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy")
							else:
								print ("\033[1;31mDesculpa comando errado\033[1;m")
						while opcion1 == "12" :
							print ('''
\033[1;36m=+[ Reverse Engineering\033[1;m

 1) apktool
 2) dex2jar
 3) diStorm3
 4) edb-debugger
 5) jad	
 6) javasnoop
 7) JD-GUI
 8) OllyDbg
 9) smali
10) Valgrind
11) YARA
ps[tem mais do que 14 categorias , entao se vc quiser instalar todas aperte 0 ]
ps2[eu so coloquei as principais ferramentas , no comando 0 vai ter muito mais uehueheu]
0) Install all Reverse Engineering tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mtools-set>\033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S  apktool")

							elif opcion2 == "2":
								cmd = os.system("pacman -S  dex2jar")

							elif opcion2 == "3":
								cmd = os.system("pacman -S  python-diStorm3")
							elif opcion2 == "4":
								cmd = os.system("pacman -S  edb-debugger")
							elif opcion2 == "5":
								cmd = os.system("pacman -S  jad")
							elif opcion2 == "6":
								cmd = os.system("pacman -S  javasnoop")
							elif opcion2 == "7":
								cmd = os.system("pacman -S  JD")
							elif opcion2 == "8":
								cmd = os.system("pacman -S  OllyDbg")
							elif opcion2 == "9":
								cmd = os.system("pacman -S  smali")
							elif opcion2 == "10":
								cmd = os.system("pacman -S  Valgrind")
							elif opcion2 == "11":
								cmd = os.system("pacman -S  YARA")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("pacman -S  blackarch-reversing apktool dex2jar python-diStorm3 edb-debugger jad javasnoop JD OllyDbg smali Valgrind YARA")
							else:
								print ("\033[1;31mDesculpa comando errado\033[1;m")
						while opcion1 == "13" :
							print ('''
\033[1;36m=+[ Hardware Hacking\033[1;m

 1) android-sdk
 2) apktool
 3) Arduino
 4) dex2jar
 5) Sakis3G	
 6) smali
ps[tem mais do que 14 categorias , entao se vc quiser instalar todas aperte 0 ]
ps2[eu so coloquei as principais ferramentas , no comando 0 vai ter muito mais uehueheu]
0) Install all Hardware Hacking tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mtools-set>\033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S  android-sdk")

							elif opcion2 == "2":
								cmd = os.system("pacman -S  apktool")

							elif opcion2 == "3":
								cmd = os.system("pacman -S  arduino")
							elif opcion2 == "4":
								cmd = os.system("pacman -S  dex2jar")
							elif opcion2 == "5":
								cmd = os.system("pacman -S  sakis3g")
							elif opcion2 == "6":
								cmd = os.system("pacman -S  smali")

							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("pacman -S  blackarch-hardware android-sdk apktool arduino dex2jar sakis3g smali")
							else:
								print ("\033[1;31mDesculpa comando errado\033[1;m")
						while opcion1 == "14" :
							print ('''
\033[1;36m=+[ Extra\033[1;m

1) Wifresti
2) Squid3
3) grande pacote de ferramenta escolidos por min [mx-debug]
				''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mtools-set>\033[1;m")
							if opcion2 == "1":
								cmd = os.system("git clone https://github.com/LionSec/wifresti.git && cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti")
								print (" ")
							elif opcion2 == "2":
								cmd = os.system("pacman -S  squid3")
								print (" ")
							elif opcion2 == "3":
								cmd = os.system("wget https://raw.githubusercontent.com/mxdebu/cortana-cobalt/master/install.py")
								print("va ate o diretorio onde vc rodo esse script e rode python2 install.py")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()

				inicio()
		inicio1()
	except KeyboardInterrupt:
		print ("esse script foi feito para ajudar a configurar a sua distro arch-linux")
		print ("feita pelo mx-debug")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()
