!servalias DTperform embed
<drac2>
args,n,p=&ARGS&,"\n",proficiencyBonus

C1=get_raw().skills.insight+roll('1d20')
C2=get_raw().skills.performance+roll('1d20')
DC1,DC2=roll('2d4+7'),roll('2d4+7')

S=1 + (0 if DC1 > C1 else 1) + (0 if DC2 > C2 else 1)
R=p + roll('1d6') if S==3 else p
T=0 if S==1 else R

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
	Reading the audience (DC {DC1})
	**Insight:** {C1}
	
	Putting on a performance (DC {DC2})
	**Performance:** {C2}
	
	{"**Success** - the crowd loves your performance! :PandaHappy:" + n + "You gain **" + str(T) + "gp**" if S==3 else "Made it through the day." + n + "You gain **" + str(T) + "gp**" if S==2 else "Nobody was impressed. :PandaPopcorn:"}
	{"" if S==1 else n + "**Gold Pieces: **" + str(oldGP) + "gp -> " + str(newGP) + "gp"}
	**DT Remaining:** {cc_str("DT")}
	"
	"""
return Msg
</drac2>
-title "**<name>** attempts to put on a show!"
-footer "Downtime | Perform | Peripéteia"
-thumb <image>
-color <color>
