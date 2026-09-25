"""Visual-only PyObjC preview of a NoSleep settings window.

Run with ``.venv/bin/python settings_preview.py``. The controls intentionally do
not change system or application settings; add your own behavior to the named
action methods in ``SettingsWindowController`` when you are ready.
"""
#settings menu written with gpt6 sol 


import objc
from AppKit import (
    NSApp,
    NSApplication,
    NSApplicationActivationPolicyRegular,
    NSAppearance,
    NSAppearanceNameDarkAqua,
    NSBackingStoreBuffered,
    NSBezelStyleCircular,
    NSBezelStyleRounded,
    NSButton,
    NSButtonTypeSwitch,
    NSColor,
    NSControlStateValueOff,
    NSControlStateValueOn,
    NSFont,
    NSFontWeightMedium,
    NSFontWeightSemibold,
    NSImage,
    NSImageScaleProportionallyUpOrDown,
    NSImageView,
    NSMakePoint,
    NSMakeRect,
    NSMakeSize,
    NSObject,
    NSPopUpButton,
    NSScreen,
    NSScrollView,
    NSTextAlignmentCenter,
    NSTextAlignmentRight,
    NSTextField,
    NSView,
    NSViewHeightSizable,
    NSViewMinYMargin,
    NSViewWidthSizable,
    NSWindow,
    NSWindowStyleMaskClosable,
    NSWindowStyleMaskFullSizeContentView,
    NSWindowStyleMaskMiniaturizable,
    NSWindowStyleMaskResizable,
    NSWindowStyleMaskTitled,
    NSWindowTitleHidden,
)
from Quartz import CGColorCreateGenericRGB


def color(red, green, blue):
    return NSColor.colorWithCalibratedRed_green_blue_alpha_(
        red / 255, green / 255, blue / 255, 1
    )


HEADER = color(54, 56, 56)
BODY = color(43, 43, 43)
SELECTED_TAB = color(69, 71, 71)
TEXT = color(225, 225, 228)
SECONDARY_TEXT = color(183, 184, 187)
TAB_TEXT = color(171, 172, 175)
BLUE = color(43, 151, 255)

HEADER_HEIGHT = 150
CONTENT_HEIGHT = 680

TABS = (
    ("general", "General", "gearshape"),
    ("session_defaults", "Session Defaults", "clock.arrow.circlepath"),
    ("system_control", "System Control", "cursorarrow.rays"),
    ("triggers", "Triggers", "bolt"),
    ("drive_alive", "Drive Alive", "internaldrive"),
    ("hot_keys", "Hot Keys", "command.square"),
    ("notifications", "Notifications", "bell"),
    ("appearance", "Appearance", "paintbrush"),
    ("statistics", "Statistics", "chart.bar"),
)


def background(view, fill, radius=0):
    view.setWantsLayer_(True)
    view.layer().setBackgroundColor_(cg_color(fill))
    if radius:
        view.layer().setCornerRadius_(radius)


def cg_color(fill):
    return CGColorCreateGenericRGB(
        fill.redComponent(),
        fill.greenComponent(),
        fill.blueComponent(),
        fill.alphaComponent(),
    )


def label(text, size, weight, tint, alignment=None):
    field = NSTextField.labelWithString_(text)
    field.setFont_(NSFont.systemFontOfSize_weight_(size, weight))
    field.setTextColor_(tint)
    if alignment is not None:
        field.setAlignment_(alignment)
    return field


class SettingsWindowController(NSObject):
    """Owns the preview window and exposes controls for future settings code."""

    def init(self):
        self = objc.super(SettingsWindowController, self).init()
        if self is None:
            return None

        self.selected_tab = "general"
        self.quit_on_close = False
        self.tab_views = {}
        self.controls = {}
        self._build_window()
        return self

    @objc.python_method
    def _build_window(self):
        visible = NSScreen.mainScreen().visibleFrame()
        width = min(1280, visible.size.width * 0.94)
        height = min(890, visible.size.height * 0.96)
        frame = NSMakeRect(0, 0, width, height)
        style = (
            NSWindowStyleMaskTitled
            | NSWindowStyleMaskClosable
            | NSWindowStyleMaskMiniaturizable
            | NSWindowStyleMaskResizable
            | NSWindowStyleMaskFullSizeContentView
        )
        self.window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
            frame, style, NSBackingStoreBuffered, False
        )
        self.window.setTitle_("Settings")
        self.window.setTitleVisibility_(NSWindowTitleHidden)
        self.window.setTitlebarAppearsTransparent_(True)
        self.window.setAppearance_(NSAppearance.appearanceNamed_(NSAppearanceNameDarkAqua))
        self.window.setBackgroundColor_(BODY)
        self.window.setReleasedWhenClosed_(False)
        self.window.setMinSize_(NSMakeSize(980, 650))
        self.window.center()
        self.window.setDelegate_(self)

        self.root = self.window.contentView()
        background(self.root, BODY)

        self.header = NSView.alloc().initWithFrame_(
            NSMakeRect(0, height - HEADER_HEIGHT, width, HEADER_HEIGHT)
        )
        self.header.setAutoresizingMask_(NSViewWidthSizable | NSViewMinYMargin)
        background(self.header, HEADER)
        self.root.addSubview_(self.header)

        self.title_label = label(
            "Settings", 21, NSFontWeightSemibold, SECONDARY_TEXT, NSTextAlignmentCenter
        )
        self.header.addSubview_(self.title_label)

        self.separator = NSView.alloc().initWithFrame_(NSMakeRect(0, 0, width, 1))
        self.separator.setAutoresizingMask_(NSViewWidthSizable)
        background(self.separator, color(28, 29, 29))
        self.header.addSubview_(self.separator)

        self._build_tabs()

        self.scroll = NSScrollView.alloc().initWithFrame_(
            NSMakeRect(0, 0, width, height - HEADER_HEIGHT)
        )
        self.scroll.setAutoresizingMask_(NSViewWidthSizable | NSViewHeightSizable)
        self.scroll.setHasVerticalScroller_(True)
        self.scroll.setHasHorizontalScroller_(False)
        self.scroll.setBorderType_(0)
        self.scroll.setDrawsBackground_(True)
        self.scroll.setBackgroundColor_(BODY)
        self.root.addSubview_(self.scroll)

        self.general_view = NSView.alloc().initWithFrame_(
            NSMakeRect(0, 0, width, CONTENT_HEIGHT)
        )
        background(self.general_view, BODY)
        self._build_general()
        self.scroll.setDocumentView_(self.general_view)
        self._layout(width, height)

    @objc.python_method
    def _build_tabs(self):
        for index, (identifier, title, symbol) in enumerate(TABS):
            tile = NSView.alloc().initWithFrame_(NSMakeRect(0, 0, 100, 90))
            background(tile, SELECTED_TAB if index == 0 else HEADER, 11)
            self.header.addSubview_(tile)

            image = NSImage.imageWithSystemSymbolName_accessibilityDescription_(
                symbol, title
            )
            if image is None:
                image = NSImage.imageWithSystemSymbolName_accessibilityDescription_(
                    "square", title
                )
            icon = NSImageView.alloc().initWithFrame_(NSMakeRect(0, 0, 38, 38))
            icon.setImage_(image)
            icon.setImageScaling_(NSImageScaleProportionallyUpOrDown)
            icon.setContentTintColor_(BLUE if index == 0 else TAB_TEXT)
            tile.addSubview_(icon)

            text = label(
                title,
                16,
                NSFontWeightMedium,
                BLUE if index == 0 else TAB_TEXT,
                NSTextAlignmentCenter,
            )
            tile.addSubview_(text)

            hit_target = NSButton.alloc().initWithFrame_(NSMakeRect(0, 0, 100, 90))
            hit_target.setBordered_(False)
            hit_target.setTitle_("")
            hit_target.setTag_(index)
            hit_target.setTarget_(self)
            hit_target.setAction_("selectTab:")
            hit_target.setToolTip_(title)
            tile.addSubview_(hit_target)
            self.tab_views[identifier] = (tile, icon, text, hit_target)

    @objc.python_method
    def _build_general(self):
        self.quick_label = label(
            "Quick-Start a Session:",
            21,
            NSFontWeightMedium,
            TEXT,
            NSTextAlignmentRight,
        )
        self.general_view.addSubview_(self.quick_label)

        self.quick_start_popup = NSPopUpButton.alloc().initWithFrame_pullsDown_(
            NSMakeRect(0, 0, 430, 38), False
        )
        self.quick_start_popup.addItemsWithTitles_(
            [
                "Right click (left click shows menu)",
                "Left click (right click shows menu)",
                "Off",
            ]
        )
        self.quick_start_popup.selectItemAtIndex_(0)
        self.quick_start_popup.setIdentifier_("quick_start")
        self.quick_start_popup.setFont_(NSFont.systemFontOfSize_(20))
        self.quick_start_popup.setTarget_(self)
        self.quick_start_popup.setAction_("quickStartChanged:")
        self.quick_start_popup.setToolTip_("Choose a quick-start gesture")
        self.general_view.addSubview_(self.quick_start_popup)
        self.controls["quick_start"] = self.quick_start_popup

        self.quick_caption = self._caption("↳ Uses Default Duration")
        self.launch_heading = self._heading("Launch and Wake Behavior:")

        self.launch_at_login_checkbox = self._checkbox(
            "Launch NoSleep at login", "launch_at_login", False
        )
        self.start_on_launch_checkbox = self._checkbox(
            "Start session when NoSleep launches", "start_on_launch", False
        )
        self.launch_caption = self._caption("↳ Uses Default Duration")
        self.start_on_wake_checkbox = self._checkbox(
            "Start session after waking from sleep", "start_on_wake", False
        )
        self.wake_caption = self._caption("↳ Uses Default Duration")

        self.other_heading = self._heading("Other:")
        self.hide_in_dock_checkbox = self._checkbox(
            "Hide NoSleep in the Dock", "hide_in_dock", True
        )
        self.dock_caption = self._caption(
            "↳ Takes effect after closing all open windows"
        )
        self.reduce_motion_checkbox = self._checkbox(
            "Reduce motion", "reduce_motion", False
        )

        self.reset_warnings_button = self._button(
            "Reset warnings and dialogs", "resetWarningsAndDialogs:"
        )
        self.reset_settings_button = self._button(
            "Reset all settings", "resetAllSettings:"
        )
        self.controls["reset_warnings"] = self.reset_warnings_button
        self.controls["reset_settings"] = self.reset_settings_button

        self.help_button = NSButton.alloc().initWithFrame_(NSMakeRect(0, 0, 36, 36))
        self.help_button.setTitle_("?")
        self.help_button.setBezelStyle_(NSBezelStyleCircular)
        self.help_button.setFont_(NSFont.systemFontOfSize_weight_(22, NSFontWeightMedium))
        self.help_button.setTarget_(self)
        self.help_button.setAction_("showHelp:")
        self.help_button.setToolTip_("Help")
        self.general_view.addSubview_(self.help_button)
        self.controls["help"] = self.help_button

    @objc.python_method
    def _heading(self, title):
        field = label(title, 21, NSFontWeightMedium, TEXT, NSTextAlignmentRight)
        self.general_view.addSubview_(field)
        return field

    @objc.python_method
    def _caption(self, title):
        field = label(title, 18, NSFontWeightMedium, SECONDARY_TEXT)
        self.general_view.addSubview_(field)
        return field

    @objc.python_method
    def _checkbox(self, title, identifier, checked):
        button = NSButton.alloc().initWithFrame_(NSMakeRect(0, 0, 650, 34))
        button.setButtonType_(NSButtonTypeSwitch)
        button.setTitle_(title)
        button.setFont_(NSFont.systemFontOfSize_weight_(21, NSFontWeightMedium))
        button.setState_(
            NSControlStateValueOn if checked else NSControlStateValueOff
        )
        button.setIdentifier_(identifier)
        button.setTarget_(self)
        button.setAction_("settingChanged:")
        button.setToolTip_(title)
        self.general_view.addSubview_(button)
        self.controls[identifier] = button
        return button

    @objc.python_method
    def _button(self, title, action):
        button = NSButton.alloc().initWithFrame_(NSMakeRect(0, 0, 335, 36))
        button.setTitle_(title)
        button.setBezelStyle_(NSBezelStyleRounded)
        button.setFont_(NSFont.systemFontOfSize_weight_(20, NSFontWeightMedium))
        button.setTarget_(self)
        button.setAction_(action)
        self.general_view.addSubview_(button)
        return button

    @objc.python_method
    def _layout(self, width, height):
        self.header.setFrame_(NSMakeRect(0, height - HEADER_HEIGHT, width, HEADER_HEIGHT))
        self.title_label.setFrame_(NSMakeRect(width / 2 - 140, 118, 280, 27))
        self.separator.setFrame_(NSMakeRect(0, 0, width, 1))

        tab_width = min(138, (width - 26) / len(TABS))
        tab_start = (width - tab_width * len(TABS)) / 2
        for index, (identifier, _, _) in enumerate(TABS):
            tile, icon, text, hit_target = self.tab_views[identifier]
            tile.setFrame_(NSMakeRect(tab_start + index * tab_width, 14, tab_width, 90))
            icon.setFrame_(NSMakeRect((tab_width - 38) / 2, 36, 38, 40))
            text.setFrame_(NSMakeRect(0, 8, tab_width, 24))
            text.setFont_(
                NSFont.systemFontOfSize_weight_(
                    16 if tab_width >= 130 else 14 if tab_width >= 115 else 12,
                    NSFontWeightMedium,
                )
            )
            hit_target.setFrame_(NSMakeRect(0, 0, tab_width, 90))

        self.scroll.setFrame_(NSMakeRect(0, 0, width, height - HEADER_HEIGHT))
        self.general_view.setFrame_(NSMakeRect(0, 0, width, CONTENT_HEIGHT))
        control_x = max(390, width / 2 - 135)
        control_width = width - control_x - 30
        heading_x = control_x - 335
        heading_width = 315

        def frame_from_top(view, x, top, frame_width, frame_height):
            view.setFrame_(
                NSMakeRect(x, CONTENT_HEIGHT - top - frame_height, frame_width, frame_height)
            )

        frame_from_top(self.quick_label, heading_x, 36, heading_width, 36)
        frame_from_top(self.quick_start_popup, control_x, 34, min(430, control_width), 40)
        frame_from_top(self.quick_caption, control_x + 12, 81, control_width - 12, 27)

        frame_from_top(self.launch_heading, heading_x, 166, heading_width, 36)
        frame_from_top(self.launch_at_login_checkbox, control_x, 165, control_width, 36)
        frame_from_top(self.start_on_launch_checkbox, control_x, 208, control_width, 36)
        frame_from_top(self.launch_caption, control_x + 16, 250, control_width - 16, 26)
        frame_from_top(self.start_on_wake_checkbox, control_x, 292, control_width, 36)
        frame_from_top(self.wake_caption, control_x + 16, 334, control_width - 16, 26)

        frame_from_top(self.other_heading, heading_x, 406, heading_width, 36)
        frame_from_top(self.hide_in_dock_checkbox, control_x, 405, control_width, 36)
        frame_from_top(self.dock_caption, control_x + 16, 447, control_width - 16, 26)
        frame_from_top(self.reduce_motion_checkbox, control_x, 490, control_width, 36)

        frame_from_top(self.reset_warnings_button, control_x, 548, 335, 38)
        frame_from_top(self.reset_settings_button, control_x, 596, 335, 38)
        frame_from_top(self.help_button, width - 64, 628, 36, 36)
        clip = self.scroll.contentView()
        clip.scrollToPoint_(
            NSMakePoint(0, max(0, CONTENT_HEIGHT - clip.bounds().size.height))
        )
        self.scroll.reflectScrolledClipView_(clip)

    def selectTab_(self, sender):
        self.selected_tab = TABS[sender.tag()][0]
        for identifier, (tile, icon, text, _) in self.tab_views.items():
            selected = identifier == self.selected_tab
            tile.layer().setBackgroundColor_(
                cg_color(SELECTED_TAB if selected else HEADER)
            )
            icon.setContentTintColor_(BLUE if selected else TAB_TEXT)
            text.setTextColor_(BLUE if selected else TAB_TEXT)
        self.scroll.setHidden_(self.selected_tab != "general")

    def quickStartChanged_(self, sender):
        # Native popup keeps its selected item in memory. Add behavior here.
        pass

    def settingChanged_(self, sender):
        # Native checkboxes keep their checked state in memory. Add behavior here.
        pass

    def resetWarningsAndDialogs_(self, sender):
        # Deliberately does not reset anything.
        pass

    def resetAllSettings_(self, sender):
        # Deliberately does not reset anything.
        pass

    def showHelp_(self, sender):
        # Deliberately does not open anything.
        pass

    def windowDidResize_(self, notification):
        size = self.root.frame().size
        self._layout(size.width, size.height)

    def windowWillClose_(self, notification):
        if self.quit_on_close:
            NSApp.terminate_(None)


def main():
    app = NSApplication.sharedApplication()
    app.setActivationPolicy_(NSApplicationActivationPolicyRegular)
    controller = SettingsWindowController.alloc().init()
    controller.quit_on_close = True
    controller.window.makeKeyAndOrderFront_(None)
    app.activateIgnoringOtherApps_(True)
    app.run()


if __name__ == "__main__":
    main()
