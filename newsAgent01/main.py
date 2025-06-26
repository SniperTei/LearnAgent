#main.py
# from pydantic_ai.models.gemini import GeminiModel
# from pydantic_ai import Agent

# from dotenv import load_dotenv
# import tools

# load_dotenv()
# model = GeminiModel("gemini-2.5-flash-preview-04-17")

# agent = Agent(model,
#               system_prompt="You are an experienced programmer",
#               tools=[tools.read_file, tools.list_files, tools.rename_file])

# demo1
# agent = Agent(model, system_prompt="Be concise, reply with one sentence.")

# demo2
# agent = Agent(model,
#               system_prompt="You are a helpful customer support agent. Be concise and friendly.")

from my_agent3 import agent

def main():
    # result = tools.list_files()
    # print("result : ", result)
    history = []
    while True:
        user_input = input("Input: ")
        resp = agent.run_sync(user_input,
                              message_history=history)
        history = list(resp.all_messages())
        print(resp.output.model_dump_json(indent=2))


if __name__ == "__main__":
    main()


