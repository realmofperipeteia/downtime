!servalias RPend embed
<drac2>
n = "\n"

if uvar_exists("RP_START_TIME"):
	seconds = int(float(time())-float(RP_START_TIME))
	h=str(seconds//3600)
	m=str((seconds%3600)//60)
	s=str((seconds%3600)%60)
	exp = round(float((seconds) * 40 / 60 / 60 * proficiencyBonus))
else:
	eM = f' -desc "{name} did not start the RPXP counter."'
	return eM

if not cc_exists('RPXP'):
	Msg = f' -desc "{name} does not have RPXP counters setup."'
else:
	mod_cc('RPXP', exp) 
	Msg = f""" -desc 
	"
	**Time:**
	**{h}** hours
	**{m}** minutes
	**{s}** seconds

	**Experience:**
	RPXP: **+{exp}**
	Weekly Total: **{cc_str("RPXP")}**
	"
	"""
	delete_uvar("RP_START_TIME")
return Msg
</drac2>
-title "**<name>** finishes roleplaying."
-footer "Roleplay | End | Peripéteia"
-thumb <image>
-color <color>
