!servalias DTfind embed
{{h,nd='%1%'.lower()=='help',get_cc('DT')==0}}
{{mod_cc('DT', -1) if not (nd or h) else None}}
{{args=&ARGS&}} 

{{one=max(get_raw().skills.persuasion,get_raw().skills.investigation)+roll('1d20')}}
{{dc=roll('2d4+3')}}{{suc=(0 if dc > one else 1)}}{{job="%1%"}}

{{sMsg=f"**{name}** looks for work around town!\n\nYou ask around the city! (DC {dc})\n**Check:** {one}\n\n{'**Success!** You find a new job as a **' + str(job) + '**!' if suc==1 else 'Unfortunately you were unable to find a job this time.'}\n\n**DT Remaining:** {cc_str('DT')}"}}

{{ndMsg=f"{name} does not have the required downtime to perform this work."}}

{{hMsg=f"**HELP**\n\nPlease check downtime rules to set counters!\nRemember to say what work you are looking for!"}}

-title "**Downtime Activity: Find**" 
-desc "{{hMsg if h else ndMsg if nd else sMsg}}"
-footer "Downtime | Find | Peripéteia"
