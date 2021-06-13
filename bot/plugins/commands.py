#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG & NO-ONE-KN0WS-ME & MRRONS

from pyrogram import filters
from pyrogram import Client as Mai_bOTs
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
#from bot import ADMINS

db = Database()

@Mai_bOTs.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption ="❤️ 𝚃𝚑𝚊𝚗𝚔𝚢𝚘𝚞 𝙵𝚘𝚛 𝚄𝚜𝚒𝚗𝚐 𝙾𝚞𝚛 𝚂𝚎𝚛𝚟𝚒𝚌𝚎 𝙿𝚕𝚎𝚊𝚜𝚎 𝚂𝚞𝚙𝚙𝚘𝚛𝚝 𝚄𝚜 𝙱𝚢 𝚂𝚑𝚊𝚛𝚒𝚗𝚐 𝙾𝚞𝚛 𝙲𝚑𝚊𝚗𝚗𝚎𝚕/𝙶𝚛𝚘𝚞𝚙 𝙻𝚒𝚗𝚔 𝚃𝚘 𝚈𝚘𝚞𝚛 𝙵𝚛𝚒𝚎𝚗𝚍𝚜 \n\n❁𝕁𝕠𝕚𝕟 𝕆𝕦𝕣 ℂ𝕙𝕒𝕟𝕟𝕖𝕝𝕤❁  \n\n⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱  \n\n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑: @fchweb➻ \n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑 : @fchanime➻ \n👥𝕲𝖗𝖔𝖚𝖕 : @filmcityhd1 ➻ \n👥𝕲𝖗𝖔𝖚𝖕 : @fchchatgroup",
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('𝑺𝑯𝑨𝑹𝑬🌐', url="https://t.me/share/url?url=https%3A//t.me/share/url%3Furl%3Dhttps%253A//t.me/FiLmCiTyHd1")
                ],
                [
                    InlineKeyboardButton('💥𝐌𝐎𝐕𝐈𝐄 𝐑𝐄𝐐💥', url="https://t.me/filmcityhd1"),
                    InlineKeyboardButton('♻️𝐖𝐄𝐁𝐒𝐄𝐑𝐈𝐄𝐒♻️', url="https://t.me/fchweb")
                ],
                [
                    InlineKeyboardButton('🔱𝐆𝐑𝐎𝐔𝐏🔱', url="https://t.me/fchchatgroup"),
                    InlineKeyboardButton('♻️𝐀𝐍𝐈𝐌𝐄♻️', url="https://t.me/fchanime")
                ]
            ]
        )
    )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('𝑺𝑯𝑨𝑹𝑬🌐', url="https://t.me/share/url?url=https%3A//t.me/share/url%3Furl%3Dhttps%253A//t.me/FiLmCiTyHd1")
                ],
                [
                    InlineKeyboardButton('💥𝐌𝐎𝐕𝐈𝐄 𝐑𝐄𝐐💥', url="https://t.me/filmcityhd1"),
                    InlineKeyboardButton('♻️𝐖𝐄𝐁𝐒𝐄𝐑𝐈𝐄𝐒♻️', url="https://t.me/fchweb")
                ],
                [
                    InlineKeyboardButton('🔱𝐆𝐑𝐎𝐔𝐏🔱', url="https://t.me/fchchatgroup"),
                    InlineKeyboardButton('♻️𝐀𝐍𝐈𝐌𝐄♻️', url="https://t.me/fchanime")
                ]
            ]
        )
    )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('𝑺𝑯𝑨𝑹𝑬 🌐', url="https://t.me/share/url?url=https%3A//t.me/share/url%3Furl%3Dhttps%253A//t.me/FiLmCiTyHd1")
                ],
                [
                    InlineKeyboardButton('💥𝐌𝐎𝐕𝐈𝐄 𝐑𝐄𝐐💥', url="https://t.me/filmcityhd1"),
                    InlineKeyboardButton('♻️𝐖𝐄𝐁𝐒𝐄𝐑𝐈𝐄𝐒♻️', url="https://t.me/fchweb")
                ],
                [
                    InlineKeyboardButton('🔱𝐆𝐑𝐎𝐔𝐏🔱', url="https://t.me/fchchatgroup"),
                    InlineKeyboardButton('♻️𝐀𝐍𝐈𝐌𝐄♻️', url="https://t.me/fchanime")
                ]
            ]
        )
    )

        else:
            print(file_type)
        
        return

    await bot.send_photo(
        chat_id=update.chat.id,
        photo = 'https://telegra.ph/file/23a25b4f0ec04aaf1946d.jpg',
        caption=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
                
                [
                    InlineKeyboardButton('💥𝐌𝐎𝐕𝐈𝐄 𝐑𝐄𝐐💥', url='https://t.me/filmcityhd1'),
                    InlineKeyboardButton('♻️𝐖𝐄𝐁𝐒𝐄𝐑𝐈𝐄𝐒♻️', url ='https://t.me/fchweb')
                ],
                [
                    InlineKeyboardButton('♻️𝐀𝐍𝐈𝐌𝐄♻️', url='https://t.me/fchanime'),
                    InlineKeyboardButton('🔱𝐆𝐑𝐎𝐔𝐏🔱', url='https://t.me/fchchatgroup')
                ]
            ]
        ), 
        parse_mode="html", 
        reply_to_message_id=update.message_id
    )


@Mai_bOTs.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Mai_bOTs.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

@Mai_bOTs.on_message(filters.text & ~ filters.command(["start", "help"]) & filters.private & ~ filters.me)
async def note(bot, update):
    buttons = [[
        InlinekeyboardButton ('MOVIE REQUEST 💥', url='https://t.me/FiLmCiTyHd1')
    ],[
        InlineKeyboardButton('🏡 WEBSERIES CHANNEL', url='https://t.me/fchweb'),
        InlineKeyboardButton('📽️ ANIME CHANNEL', url ='https://t.me/FCHANIME')
    ],[
        InlineKeyboardButton('🤔𝙷𝙾𝚆 𝚃𝙾 𝚁𝙴𝚀?', url='https://t.me/c/1387634315/4')
    ],[
        InlineKeyboardButton('𝚂𝙷𝙰𝚁𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙵𝚁𝙸𝙴𝙽𝙳𝚂😍', url='https://t.me/share/url?url=https%3A//t.me/share/url%3Furl%3Dhttps%253A//t.me/FiLmCiTyHd1')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text="എന്നെ ഉപയോഗിക്കുന്നതിനു നന്ദി😊.നിങ്ങൾക്ക് വേണ്ട പടങ്ങൾ @filmcityhd1 എന്ന ഗ്രൂപ്പിൽ ചോദിച്ചാൽ മാത്രമേ കിട്ടുകയുള്ളൂ.\nഇവിടെ ചോദിച്ചു സമയം കളയണ്ട!🚶\n\nThank you for using me ❤️\nPlease Don't Req For Movies Here.\nJoin Our @filmcityhd1 Group And Req Your Movies There...🚶 ",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
