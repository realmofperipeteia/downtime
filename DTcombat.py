!servalias DTcombat embed
<drac2>
args,n,p,e=&ARGS&,"\n",proficiencyBonus,"Experience"

C1=max(dexterityMod,strengthMod)+p+roll('1d20')
C2=get_raw().skills.acrobatics+roll('1d20')
S1=get('dexteritySave')+roll('1d20')
DC=12
S=0 if DC > C1 else 1
F1=1 if DC > C2 else 0
F2=(1 if F1==1 else 0) + (1 if DC > S1 else 0)
R=roll('4d8')
T=R * p if S==1 else 0

i = load_json(get_gvar("f688fe2b-5057-4900-beaa-e75121489e46"))
oldXP=get_cc(e)
mod_cc(e,T)
newXP=get_cc(e)

if get_cc('DT')==0:
	Msg = f' -desc "{name} does not have the required downtime."'
else:
	mod_cc('DT', -1) 
	Msg = f""" -desc 
	"
	Dodging the obstacles (DC {DC})
	**Acrobatics:** {C2}{n + n + "Encountering difficulties (DC " + str(DC) + ")" + n + "**Dexterity Save:** " + str(S1) if F1==1 else ""}{n + n + "While training you get injured!" + n +"You now have a **" + str(i[randint(20)]) + "** :PandaWorried:" if F2==2 else ""}
	
	Attacking the targets (DC {DC})
	**Attack:** {C1}
	
	{"**Success** - you completed the training! :PandaHappy:" + n + "You gain **" + str(T) + "xp**" if S==1 else "Further training is needed. :PandaPopcorn:"}
	{n + "**Experience: **" + n + str(oldXP) + "xp -> " + str(newXP) + "xp" if S==1 else ""}
	**DT Remaining:** {cc_str("DT")}
	"
	"""
return Msg
</drac2>
-title "**<name>** begins combat training!"
-footer "Downtime | Training | Peripéteia"
-thumb <image>
-color <color>
