!servalias DThunt embed
<drac2>
h,nd='%1%'.lower()=='help',get_cc('DT')==0
mod_cc('DT', -1) if not (nd or h) else None
args=&ARGS&

one=get_raw().skills.athletics+roll('1d20')
two=get_raw().skills.survival+roll('1d20')
dex=get('dexteritySave')+roll('1d20')
dc1=roll('2d4+7')
dc2=roll('2d4+7')
dc3=roll('2d4+7')

suc=0 if dc2 > two else 1
fail=(1 if dc1 > one else 0)
fate=(1 if fail==1 else 0) + (1 if dc3 > dex else 0)
rew=4+proficiencyBonus if suc==1 else 0
total=rew if suc==1 else 0

a = load_json(bags)
[a[x][1].update({"gp":a[x][1].gp+total}) for x in range(len(a)) if a[x][0] == 'Coin Pouch'][0]
set_cvar("bags",dump_json(a))

i = load_json(get_gvar("f688fe2b-5057-4900-beaa-e75121489e46"))
n = "\n"

sMsg=f' -desc "You traverse the environment! (DC {dc1})\n**Athletics:** {one}\n\n{"You encounter difficulties! (" + str(dc3) + ")" + n + "**Dexterity save:** " + str(dex) + n + n if fail==1 else ""}You land a catch! (DC {dc2})\n**Survival:** {two}\n\n{"**Success!** You managed to catch food!" + n + "You gain **" + str(total) + "gp**" if suc==1 else "You were unable to catch anything this time."}\n{n + "On your travels you get injured and now have a **" + str(i[randint(20)]) + "**" + n + n if fate==2 else n}**DT Remaining:** "{cc_str("DT")}'

ndMsg=f' -desc "{name} does not have the required downtime to perform this work."'

hMsg=f' -desc "**HELP**\n\nPlease check downtime rules to set counters!"'

return hMsg if h else ndMsg if nd else sMsg
</drac2>
-title "**<name>** starts their work as a Hunter!"
-footer "Downtime | Hunt | Peripéteia"
-thumb <image>
-color <color>
