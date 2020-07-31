!servalias DTcook embed
<drac2>
args,n=&ARGS&,"\n"

B=proficiencyBonus if "Cook's Utensils" in get("pTools","[]") else 0
C1=get_raw().skills.survival+roll('1d20')+B
S1=get('constitutionSave')+roll('1d20')
DC=8

S=0 if DC > C1 else 1
R=proficiencyBonus+2

F=2 if S==1 else 1 if DC > S1 else 2
T=R if S==1 else R - 2

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
	Make a fabulous meal (DC {DC})
	**Survival:** {C1}{n + n + "Taste testing (DC " + str(DC) + ")" + n + "**Constitution Save:** " + str(S1) if S==0 else ""}{n + n + "You get **food poisoning**! :PandaWorried:" if F==1 else ""}
	
	{"**Success** - everyone is happy with your service! :PandaHappy:" + n + "You gain **" + str(T) + "gp**" if S==1 else "Not your best day. :PandaPopcorn:" + n + "You gain **" + str(T) + "gp**"}
	
	{"**Gold Pieces: **" + str(oldGP) + "gp -> " + str(newGP) + "gp"}
	**DT Remaining:** {cc_str("DT")}
	"
	"""
return Msg
</drac2>
-title "**<name>** starts their job as a Cook!"
-footer "Downtime | Cook | Peripéteia"
-thumb <image>
-color <color>
