#  This module is part of YuiiDev or Yuii Dev
#  Inspired from CinderellaProBot
#  Edited by aryazakaria01 or Badboyanim
#  github.com/aryazakaria01 or t.me/Badboyanim


import psutil
import platform
from datetime import datetime
from platform import python_version, uname
from telegram import Update, Bot, ParseMode
from telegram.ext import run_async, CommandHandler

from YuiiDev import dispatcher, DEV_USERS
from YuiiDev.modules.helper_funcs.cs import dev_plus
import YuiiDev.modules.helper_funcs.git_api as git
from YuiiDev.modules.helper_funcs.filters import CustomFilters


@dev_plus
@run_async
def status(bot: Bot, update: Update):
	chat = update.effective_chat
	
	stat = "--- System Status ---\n"
	stat += f"Asuna Version: `Beta.v96`""\n"
	stat += "Python Version: `"+python_version()+"`\n"
	stat += "GitHub API Version: `"+str(git.vercheck())+"`\n\n"
	#Software Info
	uname = platform.uname()
	softw = "--- Software Information ---\n"
	softw += f"System: `{uname.system}`\n"
	softw += f"Node Name: `{uname.node}`\n"
	softw += f"Release: `{uname.release}`\n"
	softw += f"Version: `{uname.version}`\n"
	softw += f"Machine: `{uname.machine}`\n"
	softw += f"Processor: `{uname.processor}`\n\n"
	#Boot Time
	boot_time_timestamp = psutil.boot_time()
	bt = datetime.fromtimestamp(boot_time_timestamp)
	softw += f"Boot Time: `{bt.year}`/`{bt.month}`/`{bt.day}`  `{bt.hour}`:`{bt.minute}`:`{bt.second}`\n\n"
	#CPU Cores
	cpuu = "--- CPU Info ---\n"
	cpuu += "Physical cores:`" + str(psutil.cpu_count(logical=False)) + "`\n"
	cpuu += "Total cores:`" + str(psutil.cpu_count(logical=True)) + "`\n\n"
	# CPU frequencies
	cpufreq = psutil.cpu_freq()
	cpuu += f"Max Frequency: `{cpufreq.max:.2f}Mhz`\n"
	cpuu += f"Min Frequency: `{cpufreq.min:.2f}Mhz`\n"
	cpuu += f"Current Frequency: `{cpufreq.current:.2f}Mhz`\n\n"
	# CPU usage
	cpuu += "--- CPU Usage Per Core ---\n"
	for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
	    cpuu += f"Core {i}: `{percentage}%`\n"
	cpuu += f"Total CPU Usage: `{psutil.cpu_percent()}%`\n\n"
	# RAM Usage
	svmem = psutil.virtual_memory()
	memm = "--- Memory Usage ---\n"
	memm += f"Total: `{get_size(svmem.total)}`\n"
	memm += f"Available: `{get_size(svmem.available)}`\n"
	memm += f"Used: `{get_size(svmem.used)}`\n"
	memm += f"Percentage: `{svmem.percent}%`\n"
	reply = str(stat)+ str(softw) + str(cpuu) + str(memm) + "\n"
	bot.send_message(chat.id, reply, parse_mode=ParseMode.MARKDOWN)        

STATUS_HANDLER = CommandHandler("system", status, filters=CustomFilters.sudo_filter)

dispatcher.add_handler(STATUS_HANDLER)
