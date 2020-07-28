!alias DTcook embed
<drac2>
h,nd='%1%'.lower()=='help',get_cc('DT')==0
mod_cc('DT', -1) if not (nd or h) else None
args=&ARGS&

b=proficiencyBonus if "Cook's Utensils" in get("pTools","[]") else 0
one=get_raw().skills.survival+roll('1d20')
sur=one + b
con=get('constitutionSave')+roll('1d20')
dc=8

suc=0 if dc > sur else 1
rew=proficiencyBonus+2

fail=2 if suc==1 else 1 if dc > con else 2

total=rew if suc==1 else rew - 2

a = load_json(bags)
[a[x][1].update({"gp":a[x][1].gp+total}) for x in range(len(a)) if a[x][0] == 'Coin Pouch'][0]
set_cvar("bags",dump_json(a))

n = "\n"

sMsg=f' -desc "You make a fabulous meal! (DC {dc})\n**Survival:** {sur}\n\nYou make sure it was cooked just right! (DC {dc})\n**Constitution Save:** {con}\n\n{"Unfortunately while working you get **food poisoning**!" if fail==1 else "**Success!** Everyone is happy with your service!" + n + "You gain **" + str(total) + "gp**" if suc==1 else "You are able to make it through the day without incident." + n + "You gain **" + str(total) + "gp**"}\n\n**DT Remaining:** "{cc_str("DT")}'

ndMsg=f' -desc "{name} does not have the required downtime to perform this work."'

hMsg=f' -desc "**HELP**\n\nPlease check downtime rules to set counters!"'

return hMsg if h else ndMsg if nd else sMsg
</drac2>
-title "**<name>** starts their job as a Cook!"
-footer "Downtime | Cook | Peripéteia"
-thumb <image>
-color <color>
