manifest = '''{
    "app": {
        "background": {
            "scripts": [ "background.js" ]
        }
    },
    "manifest_version": 2,
    "name": "%s",
    "description": "%s",
    "version": "%s",
    "icons": {
    	"%d": "%s"
	}
}''' % (input("app name:\n "), input("description:\n "), input("version:\n "), int(input("icon size:\n ")), input("icon directory/filename:\n "))
background = '''chrome.app.runtime.onLaunched.addListener(function() {
  chrome.app.window.create('index.html', {
  	"id": "app",
    "bounds": {
      width: %d,
      height: %d
    },
    "frame": { color: "#%s" }
  });
});''' % (int(input("window width:\n ")), int(input("window height:\n ")), input("frame color (hex):\n #"))
manifest_file = open("manifest.json", "w")
manifest_file.write(manifest)
manifest_file.close()
background_file = open("background.js", "w")
background_file.write(background)
background_file.close()
print("Success! Go to chrome://extensions, check \"Developer Mode\", press \"Pack Extensions,\" and select this directory.")
