from pyrogram.types import *

keyboard_menu = InlineKeyboardMarkup([
        [InlineKeyboardButton("📚 About US", callback_data="info"),
         InlineKeyboardButton("🤖 Products", callback_data="products"),
         InlineKeyboardButton("🏦 Withdraw", callback_data="withdraw")]
    ])

keyboard_back = InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅️ Regresar", callback_data="back")]
        ])

keyboard_prods = InlineKeyboardMarkup([
            [InlineKeyboardButton("🤖 Telegram Bots", callback_data="tlg")],
            [InlineKeyboardButton("💬 Discord Bots", callback_data="dc")],
            [InlineKeyboardButton("📊 Data Analysis", callback_data="data")],
            [InlineKeyboardButton("🤖 Machine Learning", callback_data="llm")],
            [InlineKeyboardButton("⬅️ Regresar", callback_data="back")]
        ])

