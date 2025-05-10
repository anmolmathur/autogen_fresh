"""
Simple test script to verify AutoGen and Ollama connectivity
"""

import sys
from autogen import AssistantAgent, UserProxyAgent

def check_autogen_version():
    """Print AutoGen version information"""
    import autogen
    print(f"AutoGen version: {autogen.__version__}")
    print(f"Python version: {sys.version}")

def test_ollama_connection():
    """Test connection to Ollama using a minimal agent setup"""
    # Simple Ollama config
    ollama_config = {
        "config_list": [
            {
                "model": "deepseek-coder-v2:latest",
                "base_url": "http://localhost:11434/v1",
                "api_key": "ollama",
            }
        ]
    }
    
    try:
        print("Creating assistant agent...")
        assistant = AssistantAgent(
            name="TestAgent",
            llm_config=ollama_config,
            system_message="You are a helpful assistant."
        )
        
        print("Creating user proxy agent...")
        user = UserProxyAgent(
            name="TestUser",
            human_input_mode="NEVER"
        )
        
        print("Testing with a simple query...")
        user.initiate_chat(
            assistant,
            message="Hello, please respond with a very short message to test connectivity."
        )
        
        # Get the response
        messages = user.chat_messages[assistant.name]
        last_message = messages[-1] if messages else "No response"
        
        print(f"Response received: {last_message[:100]}...")
        print("Connection test successful!")
        
    except Exception as e:
        print(f"Error during test: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("Running AutoGen compatibility test...")
    check_autogen_version()
    test_ollama_connection()