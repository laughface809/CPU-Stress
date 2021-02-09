import os

os.system(' ps aux| grep gnome-panel | awk \'{if($3>80) print $2}\' |xargs kill -9 ')