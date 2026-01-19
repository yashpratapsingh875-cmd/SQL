from instagrapi import Client
import time, random, os

USERNAME = os.getenv("IG_USERNAME")

REPLIES = [
    "please follow us 🙏",
    "thanks for watching ❤️",
    "thanks to view 🙏"
]

FILTER_WORDS = ["nice", "bro", "op", "fire", "love"]

cl = Client()

if os.path.exists("session.json"):
    cl.load_settings("session.json")
    cl.login(USERNAME, relogin=False)
else:
    print("Session file not found. Run login.py first.")
    exit()

print("Bot started successfully 🚀")

replied = set()

while True:
    try:
        medias = cl.user_medias(cl.user_id, 5)

        for media in medias:
            comments = cl.media_comments(media.id, 20)

            for comment in comments:
                text = comment.text.lower()

                if comment.pk in replied:
                    continue

                if not any(word in text for word in FILTER_WORDS):
                    continue

                cl.comment_like(comment.pk)

                reply = random.choice(REPLIES)
                cl.comment_reply(media.id, comment.pk, reply)

                print("Replied to:", comment.text)

                replied.add(comment.pk)
                time.sleep(random.randint(8, 15))

        time.sleep(60)

    except Exception as e:
        print("Error:", e)
        time.sleep(30)