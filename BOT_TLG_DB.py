import sqlite3
from pyrogram import *
from pyrogram.filters import *
from pyrogram.types import *
from pyromod import *
from pyromod.helpers import *
from apis import *
from keyboards import *
app = Client("Gojo", api_hash=api_hash, api_id=api_id, bot_token=token)

@app.on_message(filters.command("start"))
async def on_message(client, message):

    userid = message.from_user.id
    alias = message.from_user.username
    if alias is None:
        alias = message.from_user.first_name
    
    msg_id = message.id

    await app.send_animation(chat_id=userid, animation="https://i.pinimg.com/originals/a3/22/41/a3224124ee48cddde865ecff61c13fde.gif",
                         caption=f"""<b>[ 🎊 ] 𝒮𝒽𝑜𝓅 𝑀𝒶𝓈𝓉𝑒𝓇 𝐼𝒜 [ 🎊 ]

ꜱᴇʟʟᴇʀ     @MasterBinn3r |「💻」
ᴛᴜ ɪᴅ        <code>{userid}</code>
ᴛᴜ ᴀʟɪᴀꜱ     @{alias}
ᴀᴅᴍɪɴ ⤏    False

ᴄʀᴇᴀᴅᴏ ᴇɴ : <code>Python⇝🐍</code>
</b>""", reply_to_message_id=msg_id, reply_markup=keyboard_menu)

@app.on_callback_query()
async def on_callback_query(client, callback_query):

    call_userid = callback_query.from_user.id
    call_name = callback_query.from_user.first_name

    callback_data = callback_query.data

    if callback_data == "info":
        await callback_query.answer("About Us")
        
        await callback_query.edit_message_text("👨‍**💻 We are a group of developers who are passionate about creating bots and other software. We are always looking for new ideas and projects to work on. If you have any suggestions or ideas, feel free to contact us!**",
                                               reply_markup=keyboard_back)

    elif callback_data == "products":
        await callback_query.answer("Products")
        
        await callback_query.edit_message_text("""📦 Here are some of the products we offer:""",
                                               reply_markup=keyboard_prods)

    elif callback_data == "withdraw":
        await callback_query.answer("Withdraw")
        
        await callback_query.edit_message_text("💰 To buy our products, you can use Paypal, Binance and Transference. We also accept Bitcoin and USDT. If you have any questions, please contact us @MasterBinn3r",
                                               reply_markup=keyboard_back)

    elif callback_data == "back":
        await callback_query.answer("Regresando al menú principal")

        await callback_query.edit_message_text(f"<b>[ 🎊 ] 𝒮𝒽𝑜𝓅 𝑀𝒶𝓈𝓉𝑒𝓇 𝐼𝒜 [ 🎊 ]\n\n"
                                               "ꜱᴇʟʟᴇʀ     @MasterBinn3r |「💻」\n"
                                               f"ᴛᴜ ɪᴅ        <code>{call_userid}</code>\n"
                                               f"ᴛᴜ ᴀʟɪᴀꜱ     @{call_name}\n"
                                               "ᴀᴅᴍɪɴ ⤏    False\n\n"
                                               "ᴄʀᴇᴀᴅᴏ ᴇɴ : <code>Python⇝🐍</code>\n</b>",
                                               reply_markup=keyboard_menu)

if __name__ == "__main__":
    print("Initializing...")
    app.run()
