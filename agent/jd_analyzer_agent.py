import json
from autogen import AssistantAgent, UserProxyAgent

# Paths to configuration files
PROMPT_PATH = "prompts/jd_analysis_prompt.txt"
JOB_DESCRIPTION_PATH = "data/job_description.txt"
RESUME_PATH = "data/resume.txt"
OUTPUT_FILE = "match_result.json"

def main():
    # Load prompt, job description, and resume
    with open(PROMPT_PATH, 'r') as prompt_file:
        prompt = prompt_file.read()
    with open(JOB_DESCRIPTION_PATH, 'r') as jd_file:
        job_description = jd_file.read().strip()
    with open(RESUME_PATH, 'r') as resume_file:
        resume = resume_file.read().strip()

    # Create agents based on AutoGen
    assistant = AssistantAgent(name="JDAnalyzerAgent")
    user = UserProxyAgent(name="User")

    # Prepare input for the assistant
    input_data = {
        "job_description": job_description,
        "resume": resume,
    }
    query = f"{prompt}\n\nJob Description:\n{job_description}\n\nResume:\n{resume}"
    print("Query Sent to Assistant:", query)

    # Query the assistant for analysis
    response = assistant.run(query=query)

    # Log the output to a JSON file
    result = {
        "response": response,
        "input_data": input_data  # For traceability, optional
    }
    with open(OUTPUT_FILE, 'w') as output_file:
        json.dump(result, output_file, indent=2)

    print("Analysis complete! Results saved to", OUTPUT_FILE)

if __name__ == "__main__":
    main()