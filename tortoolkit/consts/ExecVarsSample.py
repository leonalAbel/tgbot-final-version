try:
    from .ExecVars import ExecVars
except:
    class ExecVars:
        # TODO optimize for vps use fully - currently only heroku is focused
        # Set true if its VPS [currently not fully working]
        IS_VPS = False
        API_HASH = "d522013bbca2d46e256145b13f967aee"
        API_ID = 1517192
        BOT_TOKEN = "1644261366:AAEKpyN_ChcD3_JetgM5TSPatjYPgdIujUY"
        BASE_URL_OF_BOT = "https://nobitest005.herokuapp.com"
        # ALLOWED USERS [ids of user or supergroup] seperate by commas
        ALD_USR = [1458912827,1467018377,1546675358,1444150889,1482853408,1333689035,935041758,992574970,-100374414317,-1001479070385,-100320640070,-1001422326809,-1001267728460]
        
        # Google Drive Index Link should include the base dir also See readme for more info
        GD_INDEX_URL = "https://004.tortoolkitpro.workers.dev/0:/"

        # Time to wait before edit message
        EDIT_SLEEP_SECS = 40

        # Telegram Upload Limit (in bytes)
        TG_UP_LIMIT = 1700000000

        # Should force evething uploaded into Document
        FORCE_DOCUMENTS = False

        # Chracter to use as a completed progress 
        COMPLETED_STR = "▰"

        # Chracter to use as a incomplete progress
        REMAINING_STR = "▱"

        # DB URI for access
        DB_URI = "postgres://queksdkneisxxk:72948058f02554545e5c279d04fba86a8a63cb53611ee6f521715cdfc325d2bb@ec2-34-224-254-126.compute-1.amazonaws.com:5432/djb7uphi0ju8q"
        
        # UNCOMMENT THE BELOW LINE WHEN USING CONTAINER AND COMMENT THE UPPER LINE
        #DB_URI = "dbname=tortk user=postgres password=your-pass host=db port=5432"
        
        # The base direcory to which the files will be upload if using RCLONE
        RCLONE_BASE_DIR = "/"

        # This value will be considered only if Rclone is True - this may be defied now ;)
        # Cuz at least one needs to be Ture at a time either RCLONE or Leech.
        LEECH_ENABLED = True

        # Will be enabled once its set
        # For vps change it to True if config loaded
        RCLONE_ENABLED = False

        # If the user fails to select whether to use rclone or telegram to upload this will be the deafult.
        DEFAULT_TIMEOUT = "leech"

        # For vps set path here or you can use runtime too
        RCLONE_CONFIG = False
        
        # Name of the RCLONE drive from the config
        DEF_RCLONE_DRIVE = ""

        # Max size of a playlist that is allowed (Number of videos)
        MAX_YTPLAYLIST_SIZE = 200000
        
        # Max size of the torrent allowed
        MAX_TORRENT_SIZE = 250

        # This is to stop someone from abusing the system by imposing the limit
        # [<GBs of total torrent sapce>, <Number of youtube videos allowed to download>, <Number of youtube playlists allowed to download>]
        USER_CAP_ENABLE = False
        USER_CAP_LIMIT = [50,10,2]

        # No need to worry about these
        # CHANGE THESE AT YOUR RISK
        LOCKED_USERS = False
        RSTUFF = False
        FORCE_DOCS_USER = False
        FAST_UPLOAD = True
        METAINFO_BOT = False
        





