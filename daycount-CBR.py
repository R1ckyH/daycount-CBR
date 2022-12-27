# -*- coding: utf-8 -*-
import datetime

from cbr.plugin.cbrinterface import CBRInterface
from cbr.plugin.info import MessageInfo

METADATA = {
    'id': 'daycount',
    'version': '0.0.1',
    'name': 'daycount-CBR',
    'description': '##day to get server days',
    'author': 'Ricky',
    'link': 'https://github.com/R1ckyH/daycount-CBR'
}

START_DAY = datetime.datetime.strptime('2020-04-06', '%Y-%m-%d')
SERVER_NAME = "§bT§dF§eC§r"

def on_message(server: CBRInterface, info: MessageInfo):
    if info.content.startswith('##day'):
        server.reply(info, f'§r今天是{SERVER_NAME}开服的第§e' + get_day() + '§r天')


def get_day():
    now = datetime.datetime.now()
    output = now - START_DAY
    return str(output.days)


def on_load(server):
    server.register_help_message('##day', '显示今天是开服第几天')
