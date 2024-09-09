#!/Users/zach/Documents/denv/bin/repos/news/.venv/bin/python

from webbrowser import open_new_tab

from bullet import Bullet


cli = Bullet(
        choices = ["weekday", "weekend", "pods"],
        indent = 0,
        align = 5,
        margin = 2,
        shift = 0,
        bullet = "",
        pad_right = 5,
        return_index = True
    )
result = cli.launch()

if result[0] == "weekday":
    open_new_tab("https://www.semafor.com")
    open_new_tab("https://www.wsj.com")
    open_new_tab("https://www.youtube.com/playlist?list=WL")
if result[0] == "weekend":
    open_new_tab("https://www.x.com")
    open_new_tab("https://www.marginalrevolution.com")
    open_new_tab("https://www.espn.com")
if result[0] == "pods":
    open_new_tab("https://player.fm/series/the-bill-simmons-podcast-1512037")
    open_new_tab("https://player.fm/series/boxing-with-chris-mannix")
    open_new_tab("https://www.youtube.com/@allin/videos")
