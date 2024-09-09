from openai import OpenAI


with open('SECRETS.txt') as f:
    key = f.read()

client = OpenAI(
    api_key=key,
)


def create_run(asst_id, instr):

    thread = client.beta.threads.create()

    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=asst_id,
        instructions=instr
    )

    if run.status == 'completed': 
        messages = client.beta.threads.messages.list(thread.id)
        return messages

    else:
        print(run.last_error)
        print(run.status)