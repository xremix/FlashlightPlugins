import i18n

def dark_mode():
    import Foundation
    return Foundation.NSUserDefaults.standardUserDefaults().persistentDomainForName_(Foundation.NSGlobalDomain).objectForKey_("AppleInterfaceStyle") == "Dark"

def results(parsed, original):
  import json
  path = "sharkobot.html";
  html = open(i18n.find_localized_path(path)).read().replace("var nullValue = null;", "var nullValue = \"{0}\";").replace('{0}', parsed['~query']).replace("light-mode", "dark-mode" if dark_mode() else "light-mode")
  return {
    "title": u"\"{0}\" GIFs (Press enter to copy)".format(parsed['~query']),
    "html": html,
    "pass_result_of_output_function_as_first_run_arg": True,
    "run_args": ["abc"],
    "webview_transparent_background": True,
    "webview_links_open_in_browser": True
  }
