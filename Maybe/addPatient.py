import sqlite3
from openai import OpenAI
import os
import time

with open('SECRET_STASH//MY_FIRST_SECRET.txt') as f:
    key = f.read()

client = OpenAI(
    api_key=key,
)

thread = client.beta.threads.create()

run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id='asst_N8y3Cosh8Zw9ec5F4M5BNKqg',
    instructions="You have tuberculosis, but this is your first time seeing a doctor about it, SO YOU DO NOT KNOW YOU HAVE TUBERCULOSIS. This is a mild case"
)


if run.status == 'completed': 
  messages = client.beta.threads.messages.list(
    thread_id=thread.id
  )
  print(messages)
else:
  print(run.last_error)
  print(run.status)
