from instagrapi import Client
import os

USERNAME = "ypeditix"
PASSWORD = "yash2026"

cl = Client()
cl.login(USERNAME, PASSWORD)
cl.dump_settings("session.json")

print("Session saved successfully ✅")