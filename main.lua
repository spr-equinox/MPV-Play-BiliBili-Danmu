-- assert lua script
-- ===================|
-- note to escape path for winodws (c:\\users\\user\\...)

local utils = require 'mp.utils'

-- Log function: log to both terminal and MPV OSD (On-Screen Display)
function log(string, secs)
	mp.msg.warn(string)
	mp.osd_message(string, 1)
end

function assprocess()
	local cid = mp.get_opt('cid')
	if (cid == nil)
	then
		return
	end
	
	local python_path = 'python' -- path to python bin

	-- get script directory 
	local dir = mp.get_script_directory()
	local py_path = ''..dir..'\\load_danmu.py'
	if string.find(dir, "\\")
	then
		string.gsub(dir, "/", "\\")
		py_path = ''..dir..'/load_danmu.py'
	end
	
	-- choose to use python or .exe
	local arg = { 'python', py_path, cid, dir }
	log('弹幕正在上膛')
	mp.command_native_async({
		name = 'subprocess',
		playback_only = false,
		capture_stdout = true,
		args = arg
	},function(res, val, err)
		if err == nil
		then
			log('开火')
			mp.set_property_native("options/sub-file-paths", dir)
			mp.set_property('sub-auto', 'all')
			mp.command('sub-reload')
			mp.commandv('rescan_external_files','reselect')
		else
			log(err)
		end
	end)

end


mp.add_key_binding('b',	assprocess)
mp.register_event("start-file", assprocess)
