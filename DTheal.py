!servalias DTheal embed
<drac2>
args,n=&ARGS&,"\n"

B=proficiencyBonus if "Herbalism Kit" in get("pTools","[]") else 0
C1=get_raw().skills.medicine+roll('1d20')+B
S1=get('constitutionSave')+roll('1d20')
DC1,DC2=roll('2d4+7'),roll('2d4+7')

S=0 if DC1 > C1 else 1
R=proficiencyBonus+4

F=2 if S==1 else 1 if DC2 > S1 else 2
T=R if S==1 else R - 2

i = load_json(get_gvar("c7da8c4c-f030-4f2e-931d-cd8367bddc4b"))
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
	Treating wounds, and curing diseases (DC {DC1})
	**Medicine:** {C1}{n + n + "Staying healthy (DC " + str(DC2) + ")" + n + "**Constitution Save:** " + str(S1) if S==0 else ""}{n + n + "While working you catch a **" + str(i[randint(20)]) + "** :PandaWorried:" if F==1 else ""}
	
	{"**Success** - you make the world a better place! :PandaHappy:" + n + "You gain **" + str(T) + "gp**" if S==1 else "Not your best day. :PandaPopcorn:" + n + "You gain **" + str(T) + "gp**"}
	
	{"**Gold Pieces: **" + str(oldGP) + "gp -> " + str(newGP) + "gp"}
	**DT Remaining:** {cc_str("DT")}
	"
	"""
return Msg
</drac2>
-title "**<name>** starts their work as a Healer!"
-footer "Downtime | Healer | Peripéteia"
-thumb <image>
-color <color>
