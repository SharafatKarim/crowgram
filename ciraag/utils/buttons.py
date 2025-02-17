from telethon.tl.custom import Button

categories_menu = [
    [
        Button.inline("🧩 Misc", b'misc')
    ],
    [
        Button.url("💬 Chat", url="https://t.me/ciraag_chat"),
        Button.inline("❌ Exit", b'exit')
    ]
]

misc_menu = [
    [
        Button.inline("Ping", b'ping'),
        Button.inline("Timer", b'timer'),
        Button.inline("Gemini", b'gemini')
    ],
    [
        Button.inline("Bomb", b'bomb'),
        Button.inline("Raid", b'raid'),
        Button.inline("Spam", b'spam')
    ],
    [
        Button.inline("Main Menu", b'main_menu')
    ]
]

back_misc = [
    [
        Button.inline("Back", b'back_misc')
    ]
]

repo = [
    [
        Button.url("🔗 Repository", url="https://github.com/iniridwanul/Ciraag")
    ]
]