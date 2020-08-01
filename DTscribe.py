!servalias DTscribe embed
<drac2>
args,n,p=&ARGS&,"\n",proficiencyBonus

B=proficiencyBonus if "Calligrapher's Supplies" in get("pTools","[]") else 0
C1=intelligenceMod+roll('1d20')+B
S1=get('intelligenceSave')+roll('1d20')
DC=8

S=(0 if DC > C1 else 1)+(0 if DC > S1 else 1)
R=2+p if S==2 else p
T=0 if S==0 else R

a = load_json(bags)
oldGP=[a[x][1].get("gp") for x in range(len(a)) if a[x][0] == 'Coin Pouch'][0]
[a[x][1].update({"gp":a[x][1].gp+T}) for x in range(len(a)) if a[x][0] == 'Coin Pouch'][0]
set_cvar("bags",dump_json(a))
newGP=[a[x][1].get("gp") for x in range(len(a)) if a[x][0] == 'Coin Pouch'][0]

if get_cc('DT')==0:
	Msg = f' -desc "{name} does not have the required downtime."'
else:
	mod_cc('DT', -1) 
	Msg = f""" -desc 
	"
	Writing detailed pages and maps (DC {DC})
	**Intelligence:** {C1}
	
	Mental fortitude (DC {DC})
	**Intelligence Save:** {S1}
	
	{"**Success** - everyone is happy with your service! :PandaHappy:" + n + "You gain **" + str(T) + "gp**" if S==2 else "Made it through the day." + n + "You gain **" + str(T) + "gp**" if S==1 else "The work was not completed. :PandaPopcorn:"}
	{"" if S==0 else n + "**Gold Pieces: **" + str(oldGP) + "gp -> " + str(newGP) + "gp"}
	**DT Remaining:** {cc_str("DT")}
	"
	"""
return Msg
</drac2>
-title "**<name>** starts work as a Scribe!"
-footer "Downtime | Scribe | Peripéteia"
-thumb <image>
-color <color>
