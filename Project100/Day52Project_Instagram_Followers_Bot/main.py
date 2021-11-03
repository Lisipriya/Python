from instafollower import InstaFollower

INSTAGRAM_EMAIL = "aplisipriya1998@gmail.com"
INSTAGRAM_PASSWORD = "Rvisnu@2411"
SIMILAR_ACCOUNT = "studiovirupa"

chrome_drive_path = "C:\\Users\\lisipriya\Python\\Chrome\\chromedriver.exe"
insta = InstaFollower(chrome_drive_path)

insta.login()
insta.find_followers()
# insta.follow()
insta.log_out()
