!servalias DTfind embed
<drac2>
args,n= &ARGS&,"\n"

C1=max(get_raw().skills.persuasion,get_raw().skills.investigation)+roll('1d20')
DC=roll('2d4+5')
S=(0 if DC > C1 else 1)
J=["cook", "scribe", "healer", "guard", "performer"]

eM=f""" -desc 
"
**Command:**
`!DTfind [Job]`

**Jobs**
Cook, Scribe, Healer, Guard, Performer
"
"""

if get_cc('DT') > 0:
	if len(&ARGS&)==1:
		if '&1&'.lower() in J:
			j = '&1&'
			mod_cc('DT', -1) 
			Msg=f""" -desc 
			"
			Asking around (DC {DC})
			**Check:** {C1}
			
			{"**Success** - you found a job as a **" + str(j) + "**! :PandaHappy:" if S==1 else "Unfortunately you were unable to find a job this time. :PandaWorried:"}
			
			**DT Remaining:** {cc_str("DT")}
			"
			"""
		else:
			Msg=eM
	else:
		Msg=eM
else:
	Msg=f' -desc "{name} does not have the required downtime."'

return Msg
</drac2>
-title "**<name>** looks around the city!"
-footer "Downtime | Find | Peripéteia"
-thumb <image>
-color <color>
