// Privacy overrides
user_pref("privacy.resistFingerprinting", false);
user_pref("privacy.clearOnShutdown.cookies", false);
user_pref("privacy.clearOnShutdown.history", false);
user_pref("privacy.clearOnShutdown.sessions", false);
user_pref("privacy.resistFingerprinting.letterboxing", false);
user_pref("browser.display.use_system_colors", true);
user_pref("privacy.clearOnShutdown_v2.cookiesAndStorage", false); // was added recently in FF
user_pref("privacy.clearOnShutdown_v2.browsingHistoryAndDownloads", false); // was also added recently in FF

// Preferences
user_pref("browser.startup.page", 1);
user_pref("browser.startup.homepage", "https://www.google.com");
user_pref("browser.urlbar.suggest.topsites", false);
user_pref("privacy.clearOnShutdown.openWindows", false);
user_pref("browser.search.suggest.enabled", true);
user_pref("browser.urlbar.suggest.searches", true);
user_pref("browser.toolbars.bookmarks.visibility", "never");

// Weird fixes
user_pref("widget.chrome.allow-gtk-dark-theme", true); // dark mode fix

// OPSEC Preferences
user_pref("browser.urlbar.suggest.history", false);
user_pref("browser.urlbar.suggest.bookmark", false);
user_pref("browser.urlbar.suggest.openpage", false);