# import os

# DEFAULT_CONFIG = {
#     "project_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
#     "results_dir": os.getenv("TRADINGAGENTS_RESULTS_DIR", "./results"),
#     "data_dir": "/Users/yluo/Documents/Code/ScAI/FR1-data",
#     "data_cache_dir": os.path.join(
#         os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
#         "dataflows/data_cache",
#     ),
#     # LLM settings
#     "llm_provider": "openai",
#     "deep_think_llm": "gpt-40-mini",
#     "quick_think_llm": "gpt-4o-mini",
#     "backend_url": "https://api.openai.com/v1",
#     # Debate and discussion settings
#     "max_debate_rounds": 1,
#     "max_risk_discuss_rounds": 1,
#     "max_recur_limit": 100,
#     # Tool settings
#     "online_tools": True,
# }

import os

DEFAULT_CONFIG = {
    "project_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
    "results_dir": os.getenv("TRADINGAGENTS_RESULTS_DIR", "./results"),
    "data_dir": "/Users/yluo/Documents/Code/ScAI/FR1-data",
    "data_cache_dir": os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
        "dataflows/data_cache",
    ),
    # LLM settings - Change "llm_provider" to switch between providers
    "llm_provider": "openai",  # Options: "openai", "groq", "ollama", "openrouter"
    
    # OpenAI settings
    "deep_think_llm": "o1-mini",
    "quick_think_llm": "gpt-4o-mini",
    "backend_url": "https://api.openai.com/v1",
    "openai_api_key": os.getenv("OPENAI_API_KEY"),
    
    # Groq settings (used when llm_provider="groq")
    "groq_deep_think_llm": "llama-3.3-70b-versatile",
    "groq_quick_think_llm": "llama-3.1-8b-instant",
    "groq_api_key": os.getenv("GROQ_API_KEY"),
    
    # Debate and discussion settings
    "max_debate_rounds": 1,
    "max_risk_discuss_rounds": 1,
    "max_recur_limit": 100,
    # Tool settings
    "online_tools": True,
}
