!servalias DTmerch embed
<drac2>
h,nd='%1%'.lower()=='help',get_cc('DT')<4
args=&ARGS&

lveh=proficiencyBonus if "Land Vehicles" in get("pTools","[]") else proficiencyBonus if "Cartographer's Tools" in get("pTools","[]") else 0

wveh=proficiencyBonus if "Navigator's Tools" in get("pTools","[]") else proficiencyBonus if "Water Vehicles" in get("pTools","[]") else 0

one=max(lveh,wveh)+roll('1d20')
two=max(get_raw().skills.persuasion,get_raw().skills.deception)+roll('1d20')
save=get('strengthSave')+roll('1d20')
dc1=roll('2d4+7')
dc2=roll('2d4+7')
dc3=roll('2d4+7')

suc=0 if dc2 > two else 1
fail=1 if dc1 > one else 0
fate=(1 if fail ==1 else 0) + (1 if dc3 > save else 0)

mod_cc('DT', -4) if fate ==2 else mod_cc('DT', -3) if not (nd or h) else None
rew=(suc+1)*(4+proficiencyBonus)
total=rew

a = load_json(bags)
[a[x][1].update({"gp":a[x][1].gp+total}) for x in range(len(a)) if a[x][0] == 'Coin Pouch'][0]
set_cvar("bags",dump_json(a))

n = "\n"

sMsg=f' -desc "You traverse the environment! (DC {dc1})\n**Vehicle check:** {one}\n\n{"You encounter difficulties! (" + str(dc3) + ")" + n + "**Strength save:** " + str(save) + n + n if fail==1 else ""}You trade goods! (DC {dc2})\n**Charisma check:** {two}\n\n{"**Success!** You make a profit!" + n + "You gain **" + str(total) + "gp**" if suc==1 else "You make a decent trade." + n + "You gain **" + str(total) + "gp**"}\n{n + "On your travels you encounter delays." + n + n if fate==2 else n}**DT Remaining:** "{cc_str("DT")}'

ndMsg=f' -desc "{name} does not have the required downtime to perform this work.\n\nFor this activity you must have 4 DT to plan for unexpected delays."'

hMsg=f' -desc "**HELP**\n\nPlease check downtime rules to set counters!"'

return hMsg if h else ndMsg if nd else sMsg
</drac2>
-title "**<name>** starts their work as a Merchant!"
-footer "Downtime | Merchant | Peripéteia"
-thumb <image>
-color <color>
