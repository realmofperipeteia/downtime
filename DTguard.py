!servalias DTguard embed
<drac2>
args,n=&ARGS&,"\n"

C1=get_raw().skills.perception+roll('1d20')
S1=get('charismaSave')+roll('1d20')
DC=12

S=(0 if DC > C1 else 1)+(0 if DC > S1 else 1)
R=proficiencyBonus+4 if S==2 else 4
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
	Keeping a lookout for anyone in trouble (DC {DC})
	**Perception:** {C1}
	
	Dissuading criminals and being a presence (DC {DC})
	**Charisma Save:** {S1}
	
	{"**Success** - you kept the city safe! :PandaHappy:" + n + "You gain **" + str(T) + "gp**" if S==2 else "An average day, just getting by." + n + "You gain **" + str(T) + "gp**" if S==1 else "The guard captain is not impressed. :PandaPopcorn:"}{n + "" if S==0 else n + n + "**Gold Pieces: **" + str(oldGP) + "gp -> " + str(newGP) + "gp"}
	**DT Remaining:** {cc_str("DT")}
	"
	"""
return Msg
</drac2>
-title "**<name>** starts their patrol as a City Guard!"
-footer "Downtime | Guard | Peripéteia"
-thumb <image>
-color <color>
