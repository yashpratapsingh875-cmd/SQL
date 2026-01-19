from instagrapi import Client
import time
import os
import random

USERNAME = "ypeditix"
PASSWORD = "yash2026"

REPLIES = [
    "please follow us 🙏",
    "thanks for watching ❤️",
    "thanks to view 🙏"
]

cl = Client()
cl.login(USERNAME, PASSWORD)

print("Login successful")

replied = set()

while True:
    try:
        medias = cl.user_medias(cl.user_id, 5)

        for media in medias:
            comments = cl.media_comments(media.id, 20)

            for comment in comments:
                if comment.pk not in replied:

                    cl.comment_like(comment.pk)

                    reply_text = random.choice(REPLIES)
                    cl.comment_reply(media.id, comment.pk, reply_text)

                    print("Liked & replied:", comment.text)

                    replied.add(comment.pk)
                    time.sleep(random.randint(8, 15))

        time.sleep(60)

    except Exception as e:
        print("Error:", e)
        time.sleep(60)