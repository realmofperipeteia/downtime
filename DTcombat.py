!servalias DTcombat embed
<drac2>
h,nd='%1%'.lower()=='help',get_cc('DT')==0
mod_cc('DT', -1) if not (nd or h) else None
args=&ARGS&

one=max(dexterityMod,strengthMod)+proficiencyBonus+roll('1d20')
two=get_raw().skills.acrobatics+roll('1d20')
dex=get('dexteritySave')+roll('1d20')
dc=12
suc=0 if dc > one else 1
fail=1 if dc > two else 0
fate=(1 if fail==1 else 0) + (1 if dc > dex else 0)
rew=roll('4d8')
total=rew * proficiencyBonus if suc==1 else 0
mod_cc("Experience",total)

i = load_json(get_gvar("f688fe2b-5057-4900-beaa-e75121489e46"))
n = "\n"

sMsg=f' -desc "You make an attack! (DC {dc})\n**Attack:** {one}\n\nYou dodge the obstacles! (DC {dc})\n**Acrobatics:** {two}\n\n{"You encounter difficulties! (DC " + str(dc) + ")" + n + "**Dexterity save: **" + str(dex) + n + n if fail==1 else ""}{"**Success!** You completed the training!" + n + "You gain **" + str(total) + "xp**" if suc==1 else "Further training is needed"}{n + n + "While training you get injured! You now have a **" + str(i[randint(20)]) + "**" if fate==2 else ""}\n\n**Current Experience:** "{cc_str("Experience")}"\n**DT Remaining:** "{cc_str("DT")}'

ndMsg=f' -desc "{name} does not have the required downtime to perform this work."'

hMsg=f' -desc"**HELP**\n\nPlease check downtime rules to set counters!"'

return hMsg if h else ndMsg if nd else sMsg
</drac2>
-title "**<name>** begins combat training!"
-footer "Downtime | Training | Peripéteia"
-thumb <image>
-color <color>
