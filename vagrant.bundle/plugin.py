import urllib, json, os
import i18n
vagrantpath = "ENTERPATH"

# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

def results(parsed, original_query):
    return {
        "title":"Vagrant up and provision",
        "webview_transparent_background": True,
        "run_args": [""]
    }

def run(url):
    import subprocess
    # Change Dir
    os.chdir(vagrantpath)
    # Vagrant Up
    up = subprocess.Popen(["vagrant", "up"])
    up.wait()
    if up.returncode != 0:
        notify('Vagrant', 'Error', 'up failed')
    else:
        notify('Vagrant', 'Success', 'up finished')
    # Vagrant Provision
    provision = subprocess.Popen(["vagrant", "provision"])
    provision.wait()
    if provision.returncode != 0:
        notify('Vagrant', 'Error', 'provision failed')
    else:
        notify('Vagrant', 'Success', 'provision finish')

