# -- coding: utf-8 --
# Copyright (c)  2012
# Fabian "fabiantheblind" Morón Zirfas
# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to  permit persons to
# whom the Software is furnished to do so, subject to
# the following conditions:
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF  CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTIO
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# see also http://www.opensource.org/licenses/mit-license.php

#wuhahahah more license than code :D
#this plugin opens all urls in the selection in the standard browser
#the magic regex is taken from Brett Terpstra
#http://brettterpstra.com/openurls-popclip-extension/
#https://github.com/ttscoff/popclipextensions/tree/master/OpenURLS.popclipext
# import sublime
import sublime_plugin
import webbrowser
import re
# view.run_command('example')


class OpenUrlCommand(sublime_plugin.TextCommand):
    def run(self, view):
        for region in self.view.sel():
            if not region.empty():
                patt = re.compile("\w+?:[^\n ]+[^\.,!&gt;\)\n ]")
                s = self.view.substr(region)
                urls = patt.findall(s)
                # webbrowser.open(s)
                for url in urls:
                    # print url
                    webbrowser.open(url)
