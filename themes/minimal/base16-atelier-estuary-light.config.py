# base16-qutebrowser (https://github.com/theova/base16-qutebrowser)
# Base16 qutebrowser template by theova and Daniel Mulford
# Atelier Estuary Light scheme by Bram de Haan (http://atelierbramdehaan.nl)

base00 = "#f4f3ec"
base01 = "#e7e6df"
base02 = "#929181"
base03 = "#878573"
base04 = "#6c6b5a"
base05 = "#5f5e4e"
base06 = "#302f27"
base07 = "#22221b"
base08 = "#ba6236"
base09 = "#ae7313"
base0A = "#a5980d"
base0B = "#7d9726"
base0C = "#5b9d48"
base0D = "#36a166"
base0E = "#5f9182"
base0F = "#9d6c7c"

# set qutebrowser colors

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
c.colors.completion.fg = base05

# Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = base00

# Background color of the completion widget for even rows.
c.colors.completion.even.bg = base00

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = base0D

# Background color of the completion widget category headers.
c.colors.completion.category.bg = base00

# Top border color of the completion widget category headers.
c.colors.completion.category.border.top = base00

# Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = base00

# Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = base00

# Background color of the selected completion item.
c.colors.completion.item.selected.bg = base0D

# Top border color of the completion widget category headers.
c.colors.completion.item.selected.border.top = base0D

# Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = base0D

# Foreground color of the matched text in the selected completion item.
c.colors.completion.item.selected.match.fg = base00

# Foreground color of the matched text in the completion.
c.colors.completion.match.fg = base09

# Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = base05

# Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = base00

# Background color for the download bar.
c.colors.downloads.bar.bg = base00

# Color gradient start for download text.
c.colors.downloads.start.fg = base00

# Color gradient start for download backgrounds.
c.colors.downloads.start.bg = base0D

# Color gradient end for download text.
c.colors.downloads.stop.fg = base00

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = base0C

# Foreground color for downloads with errors.
c.colors.downloads.error.fg = base08

# Font color for hints.
c.colors.hints.fg = base00

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
c.colors.hints.bg = base0A

# Font color for the matched part of hints.
c.colors.hints.match.fg = base05

# Text color for the keyhint widget.
c.colors.keyhint.fg = base05

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = base05

# Background color of the keyhint widget.
c.colors.keyhint.bg = base00

# Foreground color of an error message.
c.colors.messages.error.fg = base00

# Background color of an error message.
c.colors.messages.error.bg = base08

# Border color of an error message.
c.colors.messages.error.border = base08

# Foreground color of a warning message.
c.colors.messages.warning.fg = base00

# Background color of a warning message.
c.colors.messages.warning.bg = base0E

# Border color of a warning message.
c.colors.messages.warning.border = base0E

# Foreground color of an info message.
c.colors.messages.info.fg = base05

# Background color of an info message.
c.colors.messages.info.bg = base00

# Border color of an info message.
c.colors.messages.info.border = base00

# Foreground color for prompts.
c.colors.prompts.fg = base05

# Border used around UI elements in prompts.
c.colors.prompts.border = base00

# Background color for prompts.
c.colors.prompts.bg = base00

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = base0A

# Foreground color of the statusbar.
c.colors.statusbar.normal.fg = base05

# Background color of the statusbar.
c.colors.statusbar.normal.bg = base00

# Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = base0C

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = base00

# Foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = base0A

# Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = base00

# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = base0E

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = base00

# Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = base04

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = base01

# Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = base0E

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = base01

# Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = base0D

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = base00

# Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = base0D

# Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = base00

# Background color of the progress bar.
c.colors.statusbar.progress.bg = base0D

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = base05

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = base08

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = base09

# Foreground color of the URL in the statusbar on successful load
# (http).
c.colors.statusbar.url.success.http.fg = base0B

# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = base0B

# Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = base0E

# Background color of the tab bar.
c.colors.tabs.bar.bg = base00

# Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = base0D

# Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = base0C

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = base08

# Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = base05

# Background color of unselected odd tabs.
c.colors.tabs.odd.bg = base00

# Foreground color of unselected even tabs.
c.colors.tabs.even.fg = base05

# Background color of unselected even tabs.
c.colors.tabs.even.bg = base00

# Background color of pinned unselected even tabs.
c.colors.tabs.pinned.even.bg = base0B

# Foreground color of pinned unselected even tabs.
c.colors.tabs.pinned.even.fg = base00

# Background color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.bg = base0B

# Foreground color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.fg = base00

# Background color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.bg = base0D

# Foreground color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.fg = base00

# Background color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.bg = base0D

# Foreground color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.fg = base00

# Foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = base00

# Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = base0D

# Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = base00

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = base0D

# Background color for webpages if unset (or empty to use the theme's
# color).
c.colors.webpage.bg = base00
