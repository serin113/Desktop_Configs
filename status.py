from i3pystatus import Status
from i3pystatus.group import Group
import sys

primaryColor = sys.argv[1]
compColor = sys.argv[2]
secondaryColor = sys.argv[3]
inactiveColor = sys.argv[4]

status = Status(logfile="$HOME/i3pystatus.log")

spacing = 14
innerSpacing = 8

def hintsSettings(color, sep=None, sepWidth=None, borTop=None, bg=None):
	if sep is None:
		sep=True
	if sepWidth is None:
		sepWidth=spacing
	if borTop is None:
		borTop=0
	if bg is None:
		bg=None
	return {
		"markup":"pango",
		"separator_block_width": sepWidth,
		"border": color,
		"color": color,
		"border_top": borTop,
#		"border_top": 0,
		"border_left": 0,
		"border_right": 0,
		"border_bottom": 0,
#		"border_bottom": borTop,
		"separator": sep,
		"background": bg
	}
	
def drawBorder(borSize=None, sepWid=None, borCol=None, inText=None):
	if borSize is None:
		borSize=1
	if sepWid is None:
		sepWid=spacing+5
	if borCol is None:
		borCol=inactiveColor
	if inText is None:
		inText=" "
	status.register("text",
		text=inText,
		hints={
			"markup":"pango",
			"separator_block_width":sepWid,
			"border": borCol,
			"border_top": 0,
			"border_left": 0,
			"border_right": borSize,
			"border_bottom": 0
		},)
	return

#clockColor 		= "#FFFFFF"
#batteryColor 	= "#44DD77"
#batteryColor_h 	= "#AAFF00"
#batteryColor_c	= "#FF2222"
#diskColor 		= "#DD7744"
#volumeColor		= "#EE5599"
#volumeColor_m	= "#777777"
#musicColor		= "#99FF44"
#lightColor		= "#DDDD99"
#titleColor		= clockColor
#titleColor_bg	= None
#networkColor 	= "#5599FF"
#networkColor_d	= "#777777"
#onlineColor		= networkColor
#onlineColor_o	= networkColor_d
#pingColor		= networkColor
#pingColor_b		= networkColor_d

#white = "#FFFFFF"
#gray = "#999999"

white = secondaryColor
gray = inactiveColor

iconColor		= primaryColor
boldColor		= compColor

appColor		= gray
clockColor 		= white
batteryColor 	= white
batteryColor_h 	= white
batteryColor_c	= gray
procColor 		= white
volumeColor		= white
volumeColor_m	= gray
musicColor		= white
lightColor		= white
scratchColor	= white
titleColor		= clockColor
titleColor_bg	= None
networkColor 	= white
networkColor_d	= gray
onlineColor		= networkColor
onlineColor_o	= networkColor_d
pingColor		= networkColor
pingColor_b		= networkColor_d
clockPrefix		= ""
clockFormat		= "<b><span color='"+boldColor+"'>%H:%M</span>   </b><small>%a</small> <b><span color='"+boldColor+"'>%-d</span></b> %b"


drawBorder(0, 0)
drawBorder(None, spacing-9)
#drawBorder(None, spacing)

status.register("clock",
    format=[(clockPrefix+clockFormat, "Asia/Manila"),
    (clockPrefix+"<small>BR</small> "+clockFormat, "America/Sao_Paulo"),
    (clockPrefix+"<small>EST</small> "+clockFormat, "America/Atikokan"),
    (clockPrefix+"<small>IT</small> "+clockFormat, "Europe/Rome"),
    (clockPrefix+"<small>UTC</small> "+clockFormat, "Etc/UTC")],
    hints=hintsSettings(clockColor,None,None,0),
    color=clockColor,
    on_upscroll=['scroll_format', -1],
    on_downscroll=['scroll_format', 1])

drawBorder()

status.register("battery",
    format="<b><span color='"+iconColor+"'>{status}</span><span color='"+boldColor+"'>{percentage:.0f}</span></b><small> {remaining:%E%h\'%M\"}</small>",
    status={
#        "DIS":  "⚡ ",
        "DIS":  " ",
        "CHR":  " ",
        "FULL": " ",
    },
    hints=hintsSettings(batteryColor),
    color=batteryColor,
    full_color=batteryColor,
    charging_color=batteryColor_h,
    critical_color=batteryColor_c,
    critical_level_percentage=5,
    critical_level_command="",
    alert_percentage=15,
    alert_timeout=5,
	alert=True,
	alert_format_title="Battery low",
	alert_format_body="{percentage:.1f}% ({remaining:%E%h\'%m\"}) remaining",)

status.register("backlight",
	format="<span color='"+iconColor+"'></span> <b><span color='"+boldColor+"'>{percentage}</span></b>",
	hints=hintsSettings(lightColor, False, innerSpacing),
	color=lightColor,)

status.register("pulseaudio",
    format="<span color='"+iconColor+"'>🔊</span> <b><span color='"+boldColor+"'>{volume}</span></b>",
    format_muted="<span color='"+iconColor+"'>🔊</span> <b><span color='"+boldColor+"'>{volume}</span></b>",
    hints=hintsSettings(volumeColor, False, innerSpacing),
    color_unmuted=volumeColor,
    color_muted=volumeColor_m,
    step=3,)

status.register("network",
    interface="wlp4s0",
    detect_active=True,
    next_if_down=True,
    format_up="<span color='"+iconColor+"'></span> <b><span color='"+boldColor+"'>↓{bytes_recv}</span></b> <small>↑{bytes_sent}</small>",
    format_down="<span color='"+iconColor+"'></span> <b><span color='"+boldColor+"'>down</span></b>",
    hints=hintsSettings(networkColor),
    dynamic_color=False,
    color_up=networkColor,
    color_down=networkColor,)
    
status.register("ping",
	color=pingColor,
	color_bad=pingColor_b,
	color_down=pingColor_b,
	color_disabled=pingColor_b,
	hints=hintsSettings(pingColor, False, 0),
	format="<small>{ping:.0f}</small> ",
	format_disabled="",
	format_down="",
	latency_threshold=300,
	host="8.8.8.8",
	on_leftclick="",
	interval=5,)
    
#status.register("online",
#	color=onlineColor,
#	color_offline=onlineColor_o,
#	hints=hintsSettings(onlineColor, False, 0),
#	format_online="<b>✔</b> ",
#	format_offline="<b>✗</b> ",
#	interval=5)

group = Group(
	hints=hintsSettings(procColor),
	on_upscroll=['cycle_module', -1],
	on_downscroll=['cycle_module', 1])

group.register("disk",
    path="/",
    format="<span color='"+iconColor+"'></span> <b><span color='"+boldColor+"'>{avail:0.1f}</span></b> <small>diskfree</small>",
    color=procColor,)
    
group.register("now_playing",
#     format="<b><small>{status}</small> {title} · </b><small>{artist}</small>",
	 format="<b><small><span color='"+iconColor+"'>{status}</span></small> <span color='"+boldColor+"'>{title}</span>   </b><small>{artist}</small>",
     on_leftclick=["player_command","PlayPause"],
     on_rightclick=["player_command","Next"],
     hints=hintsSettings(musicColor),
	 color=musicColor,
	 format_no_player="<span color='"+iconColor+"'></span> <small>no player</small>",
	 hide_no_player=False,
     status={
		"play": " ",
        "pause": " ",
        "stop": " ",
     },)
    
group.register("cpu_usage",
	format="<span color='"+iconColor+"'></span> <b><span color='"+boldColor+"'>{usage:0.1f}</span></b> <small>cpu</small>",
	format_all="<b>{usage:0.0f}</b> <small>{core}</small> ",
	exclude_average=False,
	color=procColor,)
	
group.register("cpu_freq",
	format="<span color='"+iconColor+"'></span> <b><span color='"+boldColor+"'>{avgg}</span></b> <small>cpufreq</small>",
	color=procColor,)
	
group.register("mem",
	format="<span color='"+iconColor+"'></span> <b><span color='"+boldColor+"'>{avail_mem:0.1f}</span></b> <small>memfree</small>",
	divisor=1073741824,
	color=procColor,)
	
group.register("uptime",
	format="<span color='"+iconColor+"'></span> <b><span color='"+boldColor+"'>{hours}:{mins}</span></b> <small>uptime</small>",
	color=procColor,)
     
status.register(group)

status.register("scratchpad",
	format="<span color='"+iconColor+"'></span> <b><span color='"+boldColor+"'>{number}</span></b>",
	hints=hintsSettings(scratchColor),
	always_show=False,
#	on_leftclick="i3-msg scratchpad show && i3-msg floating toggle")
	on_leftclick="i3-msg scratchpad show")

drawBorder()

#status.register("shell",
#	format="<small><b>[{output}]</b></small>",
#	command="$HOME/scripts/i3currws",
#	ignore_empty_stdout=True,
#	color=titleColor,
#	interval=0.25,
#	hints=hintsSettings(titleColor,None,None,0,titleColor_bg),)

# v Causes i3 to hang with 100% CPU usage
#status.register("window_title",
#     format="<b>{title}</b><small> · {class_name}</small>",
#     hints=hintsSettings(titleColor,None,None,0),
#     color=titleColor,
#     max_width=60,)

# xtitle -ei -t 50
status.register("shell",
	format="<small>{output}</small>",
#	command="xtitle -i -f '%u' | xargs -l1 xprop -id 2> /dev/null | grep 'WM_CLASS(STRING) = ' --line-buffered | cut --delimiter='\"' --fields=4",
	command="$HOME/scripts/activewindowclass 50",
	ignore_empty_stdout=True,
	color=titleColor,
	interval=0.25,
#	hints=hintsSettings(titleColor,None,5,0,titleColor_bg),)
	hints=hintsSettings(titleColor,None,None,0,titleColor_bg),)
	
status.register("shell",
#	format="<b>{output} · </b>",
	format="<b><span color='"+boldColor+"'>{output}</span>   </b>",
#	command="xtitle -i -t 50",
	command="$HOME/scripts/activewindowtitle 75",
	ignore_empty_stdout=True,
	color=titleColor,
	interval=0.25,
	hints=hintsSettings(titleColor,False,0,0,titleColor_bg),)

status.run()
