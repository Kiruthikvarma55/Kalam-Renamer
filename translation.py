class Translation(object):
    START_TEXT = """Welcome {message.from_user.first_name}, 
    I am Telegram Renamer Bot with Custom Thumbnail support!!!

<b>1.Send me any Telegram File...
2. Reply to that message to /rename new name.extension</b>

/help for more Details about me...

<b>Developer : © @Kalam_Company</b>"""
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = "<b>If you Fail, Never give up because FAIL means 'First Attempt In Learning'</b>"
    UPGRADE_TEXT = "Join to my Developer channel © @Kalam_Company for upgrade your plan...  /help for more Details"
    DOWNLOAD_START = "🔰 DownloadiNg... to my Server 📥"
    UPLOAD_START = "📤 UploadiNg... to Telegram 📤"
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.5GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "<b>***Always Be Happy 😁***</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://telegram.dog/ThankTelegram'>@SpEcHlDe</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Custom File thumbnail saved. This image will be used in the File."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "❌️ No Custom ThumbNail found."
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    HELP_USER = """Hai, I am Telegram Renamer bot with Custom Thumbnail Support...
    
1. Send me any Telegram File..
2. Reply to that message to /rename new name.extension.
Example for Rename:- /rename Hii(New name).mkv(format)

👉 <a href="https://www.youtube.com/channel/UC1dgbRIE-X1viE8nG_3006w">Subscribe our official Music Channel</a> 👈

--------

<b>Developed by © @Kalam_Company</b>"""
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to (/rename New Name.extension) with custom thumbnail support.."
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    IFLONG_FILE_NAME = """File Name limit allowed by Telegram is {alimit} characters.
The given file name has {num} characters.

<b>Essays Not allowed in Telegram file name!</b>
©️ <code>@Kalam_Renamer_Bot</code>
Please short your file name and try again!"""
    DONATION_LINK = "Hii, sexy"
