capture-left-click:
	cnee --record --mouse | awk  '/7,4,0,0,1/ { system("xdotool getmouselocation") } '

github-push:
	git push https://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@github.com/ebbitten/Automation.git
