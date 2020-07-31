!servalias DThunt embed
<drac2>
args,n=&ARGS&,"\n"

C1=get_raw().skills.athletics+roll('1d20')
C2=get_raw().skills.survival+roll('1d20')
S1=get('dexteritySave')+roll('1d20')
DC1,DC2,DC3=roll('2d4+7'),roll('2d4+7'),roll('2d4+7')

S=0 if DC2 > C2 else 1
F1=(1 if DC1 > C1 else 0)
F2=(1 if F1==1 else 0) + (1 if DC3 > S1 else 0)
R=proficiencyBonus+4 if S==1 else 0
T=R if S==1 else 0

i = load_json(get_gvar("f688fe2b-5057-4900-beaa-e75121489e46"))
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
	Traversing the environment (DC {DC1})
	**Athletics:** {C1}{n + n + "Encountering difficulties (DC " + str(DC3) + ")" + n + "**Dexterity Save:** " + str(S1) if F1==1 else ""}{n + n + "On your travels you get injured and now have a **" + str(i[randint(20)]) + "** :PandaWorried:" if F2==2 else ""}
	
	Landing a catch (DC {DC2})
	**Survival:** {C2}
	
	{"**Success** - you make a catch! :PandaHappy:" + n + "You gain **" + str(T) + "gp**" if S==1 else "No catch this time. :PandaPopcorn:"}
	{"" if S==0 else n + "**Gold Pieces: **" + str(oldGP) + "gp -> " + str(newGP) + "gp"}
	**DT Remaining:** {cc_str("DT")}
	"
	"""

return Msg
</drac2>
-title "**<name>** starts their work as a Hunter!"
-footer "Downtime | Hunt | Peripéteia"
-thumb <image>
-color <color>
