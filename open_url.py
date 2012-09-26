#this plugin opens a the selection as url in a browser
import sublime
import sublime_plugin
import webbrowser
# view.run_command('example')


class OpenUrlCommand(sublime_plugin.TextCommand):
    def run(self, view):
        for region in self.view.sel():
            if not region.empty():
                s = self.view.substr(region)
                webbrowser.open(s)
