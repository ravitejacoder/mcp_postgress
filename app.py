import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

async def run_memory_chat():
  load_dotenv()
  config_file="postgresql_server.json"
  client = MCPClient.from_config_file(config_file)
  llm = ChatGroq(
  qroq_api_key = "",
  model_name="",
  temperature=0.0.1)

agent = MCPAgent(
  llm,
  max_steps=15,
  memory_enable=True,
  system_prompt="If required")

try:
  while True:
    user_input= input("\nYou:")
    if useer_input.lower() in ["exit", "quit"]:
      print("Ending Conversation")
      break

    if user_input.lower()=="clear":
      agent.clear_conversation_history()
      print("Conversation history cleared")
      continue
    print("\nAssistant:", end="", flush=True)

    try:
      response = await agent.run(user_input)
      print(response)
    except Exception as e:
      print(f"\n Error:{e}")
finally:
  if client and client.sessions:
    await client.close_all_sessions()

if __name__ =="__main__":
  asyncio.run(run_memory_chat())
  
