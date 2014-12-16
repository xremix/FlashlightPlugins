import urllib, json, i18n

def results(parsed, original_query):
    return {
        "title": i18n.localstr("Excuse"),
        "run_args": ['http://www.programmerexcuses.com'],
        "html": """
        <script>
        setTimeout(function() {
            window.location = %s
        }, 500);
        </script>
        """%(json.dumps('http://www.programmerexcuses.com')),
        "webview_user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53",
        "webview_links_open_in_browser": True
    }

def run(url):
    import os
    os.system('open "{0}"'.format(url))
