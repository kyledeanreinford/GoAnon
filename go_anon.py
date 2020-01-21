#! /usr/bin/python3

import webbrowser, subprocess

subprocess.call(['/usr/local/bin/piactl', 'connect'])
webbrowser.open_new('https://thepiratebay.org')
subprocess.call('deluge')