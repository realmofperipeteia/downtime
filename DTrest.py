!alias DTrest embed
{{h,nd='%1%'.lower()=='help',get_cc('DT')==0}}
{{mod_cc('DT', -1) if not (nd or h) else None}}
{{args=&ARGS&}} 

{{sMsg=f"**{name}** goes to rest their injuries!\n\n**DT Remaining:** {cc_str('DT')}"}}

{{ndMsg=f"{name} does not have the required downtime to perform this action."}}

{{hMsg=f"**HELP**\n\nPlease check downtime rules to set counters!"}}

-title "**Downtime Activity: Rest**" 
-desc "{{hMsg if h else ndMsg if nd else sMsg}}"
-footer "Downtime | Rest | Peripéteia"
