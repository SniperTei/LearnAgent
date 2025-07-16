from my_agent3 import agent
from dotenv import load_dotenv

def main():
    
    topic = "财经"
    result = agent.run_sync(topic)
    print(result.output)
    

if __name__ == "__main__":
    main()



