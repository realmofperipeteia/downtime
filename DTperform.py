!servalias DTperform embed
<drac2>
h,nd='%1%'.lower()=='help',get_cc('DT')==0
mod_cc('DT', -1) if not (nd or h) else None
args=&ARGS&

one = get_raw().skills.insight+roll('1d20')
two = get_raw().skills.performance+roll('1d20')

dc1=roll('2d4+7')
dc2=roll('2d4+7')

suc=1 + (0 if dc1 > one else 1) + (0 if dc2 > two else 1)

rew=proficiencyBonus + roll('1d6') if suc==3 else roll('1d6')
total=0 if suc==1 else rew

a = load_json(bags)
[a[x][1].update({"gp":a[x][1].gp+total}) for x in range(len(a)) if a[x][0] == 'Coin Pouch'][0]
set_cvar("bags",dump_json(a))

n = "\n"

sMsg=f' -desc "You read the audience! (DC {dc1})\n**Insight:** {one}\n\nYou put on a performance! (DC {dc2})\n**Performance:** {two}\n\n{"You **failed** and your performance was not entertaining." if suc==1 else "**Success!** The crowd absolutely loves your performance!" + n + "You gain **" + str(total) + "gp**"}\n\n**DT Remaining:** "{cc_str("DT")}'

ndMsg=f' -desc "{name} does not have the required downtime to perform this work."'

hMsg=f' -desc "**HELP**\n\nPlease check downtime rules to set counters!"'

return hMsg if h else ndMsg if nd else sMsg
</drac2>
-title "**<name>** attempts to put on a show!"
-footer "Downtime | Perform | Peripéteia"
-thumb <image>
-color <color>
