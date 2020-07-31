!servalias DTrest embed
<drac2>
args,n=&ARGS&,"\n"

if get_cc('DT')==0:
	Msg = f' -desc "{name} does not have the required downtime."'
else:
	mod_cc('DT', -1)
	Msg = f""" -desc 
	"
	Feeling a lot better now. :PandaHappy:
	
	**DT Remaining:** {cc_str("DT")}
	"
	"""
return Msg
</drac2>
-title "**<name>** goes to rest their injuries!"
-footer "Downtime | Rest | Peripéteia"
-thumb <image>
-color <color>
