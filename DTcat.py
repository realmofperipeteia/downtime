!servalias DTcat embed
{{h,nd='%1%'.lower()=='help',get_cc('DT')==0}}
{{mod_cc('DT', -1) if not (nd or h) else None}}
{{args=&ARGS&}} 

{{one=get_raw().skills.athletics+roll('1d20')}}
{{two=get_raw().skills.animalHandling+roll('1d20')}}
{{dex=get('dexteritySave')+roll('1d20')}}
{{dc1=roll('2d4+7')}}{{dc2=roll('2d4+7')}}{{dc3=roll('2d4+7')}}
{{suc=0 if dc2 > two else 1}} {{fail=1 if dc1 > one else 0}}
{{fate=fail + (1 if dc3 > dex else 0)}}{{total=5 if suc==1 else 0}}

{{a = load_json(bags)}}{{[a[x][1].update({"gp":a[x][1].gp+total}) for x in range(len(a)) if a[x][0] == 'Coin Pouch'][0]}}{{set_cvar("bags",dump_json(a))}}

{{i=["Concussion", "Concussion", "Concussion", "Concussion", "Concussion", "Concussion", "Concussion", "Concussion", "Concussion", "Concussion", "Concussion", "Concussion", "Concussion", "Concussion", "Concussion", "Concussion", "Concussion", "Concussion", "Concussion", "Concussion"]}}

{{sMsg=f"**{name}** attempts to save the cat! \n\nYou climb the tree! (DC{dc1})\n**Athletics:** {one}!\n\n{'You fall out of the tree! (DC' + str(dc3) + ')' if fail==1 else ''}\n{'**Dexterity Save:** ' + str(dex) if fail==1 else ''}\n\nYou tell the cat to come to you! (DC{dc2})\n**Animal Handling:** {two}!\n\n{'**Success!** You have saved the cat! You are rewarded with **5gp**' if suc==1 else 'You **failed** to save the cat!'}\n{'You fall and get injured! You now have a **' + str(i[randint(20)]) + '**' if fate==2 else 'You are able to make it through the day without incident!'}\n\n**DT Remaining:** {cc_str('DT')}"}}

{{ndMsg=f"{name} does not have the required downtime to perform this work."}}

{{hMsg=f"**HELP**\n\nPlease check downtime rules to set counters!"}}

-title "**Downtime Activity: Saving the cat!**" 
-desc "{{hMsg if h else ndMsg if nd else sMsg}}"
-footer "Downtime | Cat | ShadowPrince#8900"
