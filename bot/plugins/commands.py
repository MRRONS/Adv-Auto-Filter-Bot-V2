#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
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
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'Movie REQ 💥', url="https://t.me/filmcityhd1"
                                ),
                            InlinekeyboardButton
                                (
                                    '♻️Webseries♻️', url="https://t.me/fchweb"
                                ),
                            InlinekeyboardButton
                                (
                                    '♻️Animes♻️', url="https://t.me/fchanime"
                                ),
                            InlinekeyboardButton
                                (
                                    'Group✨', url="https://t.me/fchchatgroup"
                                ),
                            InlinekeyboardButton
                                ( 
                                    'SHARE🌐', url="https://t.me/share/url?url=https%3A//t.me/share/url%3Furl%3Dhttps%253A//t.me/FiLmCiTyHd1"
                                ),
                            InlinekeyboardButton
                                (
                                    'CLOSE 🔐', callback_data='close'
                                )
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
                            InlineKeyboardButton
                                (
                                    'Movie REQ💥', url="https://t.me/filmcityhd1"
                                ),
                            InlinekeyboardButton
                                (
                                    '♻️Webseries♻️', url="https://t.me/fchweb"
                                )
                            InlinekeyboardButton
                                (
                                    '♻️Animes♻️', url="https://t.me/fchanime"
                                ),
                            InlinekeyboardButton
                                (
                                    'Group✨', url="https://t.me/fchchatgroup"
                                ),
                            InlinekeyboardButton
                                ( 
                                    'SHARE🌐', url="https://t.me/share/url?url=https%3A//t.me/share/url%3Furl%3Dhttps%253A//t.me/FiLmCiTyHd1"
                                ),
                            InlinekeyboardButton
                                (
                                    'CLOSE 🔐', callback_data='close'
                                )

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
                            InlineKeyboardButton
                                (
                                    'Movie REQ💥', url="https://t.me/filmcityhd1"
                                ),
                            InlinekeyboardButton
                                (
                                    '♻️Webseries♻️', url="https://t.me/fchweb"
                                ),
                            InlinekeyboardButton
                                (
                                    '♻️Animes♻️', url="https://t.me/fchanime"
                                ),
                            InlinekeyboardButton
                                (
                                    'Group✨', url="https://t.me/fchchatgroup"
                                ),
                            InlinekeyboardButton
                                ( 
                                    'SHARE🌐', url="https://t.me/share/url?url=https%3A//t.me/share/url%3Furl%3Dhttps%253A//t.me/FiLmCiTyHd1"
                                ),
                            InlinekeyboardButton
                                (
                                    'CLOSE 🔐', callback_data='close'
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('Movie REQ', url='https://t.me/filmcityhd1'),
        InlineKeyboardButton('Webseries', url ='https://t.me/fchweb')
    ],[
        InlineKeyboardButton('animes', url='https://t.me/fchanime'),
        InlinekeyboardButton('Group',  url='https://t.me/fchchatgroup')
    ],[

        InlineKeyboardButton('Help ⚙', callback_data="help")
    ]] 
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_photo(
        chat_id=update.chat.id,
        photo = 'https://telegra.ph/file/2e9d20f371bb1ac305015.jpg',
        caption=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
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


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
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
