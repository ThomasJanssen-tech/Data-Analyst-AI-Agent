<h1>Build an AI Agent Data Analyst</h1>

<h2>Watch the full tutorial on my YouTube Channel</h2>
<div>

<a href="https://www.youtube.com/watch?v=3ZDeqTIXBPM">
    <img src="thumbnail.png" alt="Thomas Janssen Youtube" width="200"/>
</a>
</div>

<h2>Prerequisites</h2>
<ul>
  <li>Python 3.11+</li>
</ul>

<h2>Installation</h2>
<h3>1. Clone the repository:</h3>

```
git clone https://github.com/ThomasJanssen-tech/Data-Analyst-AI-Agent.git
cd Data Analyst AI Agent
```

<h3>2. Create a virtual environment</h3>

```
python -m venv venv
```

<h3>3. Activate the virtual environment</h3>

```
venv\Scripts\Activate
(or on Mac): source venv/bin/activate
```

<h3>4. Install libraries</h3>

```
pip install -r requirements.txt
```

<h3>5. Create accounts</h3>

- Create an API key for OpenAI: https://platform.openai.com/api-keys

<h3>6. Add API keys to .env file</h3>

- Rename .env.example to .env
- Add the API keys for Supabase and OpenAI to the .env file

<h2>Executing the scripts</h2>

- Open a terminal in VS Code

- Execute the following command:

```
streamlit run main.py
```

<h2>Sources</h2>

While making this video, I used the following sources:

<ul>
<li>https://www.kaggle.com/code/iyadmahdy/identifying-key-features-for-diabetes-prediction</li>
<li>https://www.digilab.co.uk/posts/build-an-ai-data-assistant-with-streamlit-langchain-and-openai</li>
<li>https://python.langchain.com/api_reference/experimental/agents/langchain_experimental.agents.agent_toolkits.pandas.base.create_pandas_dataframe_agent.html</li>
</ul>
