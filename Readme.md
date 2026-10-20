# 🤖 AI Research Agent

An AI-powered research assistant built with **LangGraph, Google Gemini, Tavily, Streamlit, and LangSmith** that automates web research and generates structured research reports from user queries.

🌐 **Live Demo:** [AI Research Agent](https://ai-research-agent-o25v.onrender.com/)

🐳 **Docker Hub:** [gauravpatil77/ai-research-agent](https://hub.docker.com/r/gauravpatil77/ai-research-agent)

The agent breaks complex research questions into smaller subtopics, searches the web for relevant information, processes the findings, and synthesizes them into a comprehensive research report.

---

## ✨ Features

* 🔍 **Automated Web Research:** Uses Tavily to search the web for relevant information.
* 🧠 **AI-Powered Reasoning:** Leverages Google Gemini to analyze research questions and synthesize findings.
* 🔗 **Agentic Workflow:** Uses LangGraph to orchestrate the multi-step research process.
* 📚 **Subtopic Generation:** Breaks complex research questions into manageable subtopics.
* 📝 **Report Generation:** Generates structured research reports based on gathered information.
* 📊 **LangSmith Tracing:** Supports tracing and debugging of LLM calls and workflow execution when enabled and configured.
* 🖥️ **Interactive Interface:** Provides a user-friendly Streamlit interface.
* 🐳 **Docker Support:** Containerizes the application for consistent execution across environments.
* ☁️ **Cloud Deployment:** Deployed on Render for online access.

---

## 🏗️ Architecture

```text
                   User Query
                       |
                       v
              Streamlit Frontend
                       |
                       v
              LangGraph Workflow
                       |
                       v
             Generate Subtopics
                       |
                       v
                Tavily Search
                       |
                       v
             Collect Search Results
                       |
                       v
            Analyze Research Findings
                       |
                       v
              Generate Final Report
                       |
                       v
               Display to User

        LangSmith: Workflow Tracing
          and Execution Debugging
```

---

## 🛠️ Tech Stack

| Technology     | Purpose                                 |
| -------------- | --------------------------------------- |
| Python         | Core application logic                  |
| LangGraph      | AI workflow orchestration               |
| Google Gemini  | Research analysis and report generation |
| Tavily         | Web search and information retrieval    |
| Streamlit      | Interactive user interface              |
| LangSmith      | LLM tracing, monitoring, and debugging  |
| Docker         | Application containerization            |
| Docker Compose | Container lifecycle management          |
| Render         | Cloud deployment                        |

---

## 🚀 Live Application

Try the deployed application:

**👉 https://ai-research-agent-o25v.onrender.com/**

Enter a research topic and let the agent generate subtopics, search for relevant information, and produce a structured research report.

*Availability depends on the hosting service's status and resource limits.*

---

## 📂 Project Structure

```text
AI-Research-Agent/
│
├── backend.py
├── frontend.py
├── requirements.txt
├── Dockerfile
├── compose.yaml
├── .dockerignore
├── .gitignore
├── .env.example
└── README.md
```

*Adjust the file tree to match the actual files in your repository.*

---

## ⚙️ Run Locally

### Prerequisites

* Python version supported by the project's dependencies.
* Git.
* Google Gemini API key.
* Tavily API key.
* LangSmith account and API key (optional, for tracing).

### 1. Clone the Repository

```bash
git clone https://github.com/GauravPatil777/AI-Research-Agent.git
cd AI-Research-Agent
```

### 2. Create a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key

# Optional: LangSmith tracing
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_PROJECT=AI-Research-Agent
```

Get your API keys from:

* **Google AI Studio:** https://aistudio.google.com/
* **Tavily:** https://tavily.com/
* **LangSmith:** https://smith.langchain.com/

Keep your API keys private. Never commit your `.env` file to GitHub.

### 5. Run the Application

If your Streamlit entry point is `frontend.py`, run:

```bash
streamlit run frontend.py
```

Open the local URL displayed in your terminal.

*If your frontend uses a different filename, replace `frontend.py` with the correct one.*

---

## 📊 LangSmith Tracing

LangSmith provides observability for LLM-powered applications, helping developers understand and debug their AI workflows.

When tracing is enabled and correctly configured, it can help with:

* **Execution Tracking:** Inspect the steps executed during the research workflow.
* **LLM Call Inspection:** Examine model invocations and execution details.
* **Latency Analysis:** Identify slower steps in the workflow.
* **Error Debugging:** Investigate failed model calls and workflow execution.
* **Workflow Observability:** Understand the sequence of operations in the research process.

### Enable LangSmith Tracing

Add the following variables to your `.env` file:

```env
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_PROJECT=AI-Research-Agent
```

Restart the application after changing the configuration.

Open your LangSmith workspace and select the configured project to inspect available traces.

**Note:** LangSmith tracing is optional. It works only when tracing is enabled and supported by the application's integrations and execution environment. If tracing has been disabled in the current deployment, the presence of these variables alone does not guarantee that traces will be generated.

---

## 🐳 Docker Deployment

The project supports Docker-based execution, and its image is published on Docker Hub.

**Docker Hub Image:** `gauravpatil77/ai-research-agent`

### Prerequisites

* Docker Desktop or Docker Engine.
* API keys for Google Gemini and Tavily.

### Option 1: Run Using Docker Compose

#### 1. Clone the Repository

```bash
git clone https://github.com/GauravPatil777/AI-Research-Agent.git
cd AI-Research-Agent
```

#### 2. Create the Environment File

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key

# Optional: LangSmith tracing
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_PROJECT=AI-Research-Agent
```

Use your own API keys. Do not upload this file to GitHub.

#### 3. Configure Docker Compose

To run the published Docker Hub image directly, use this `compose.yaml`:

```yaml
services:
  ai-research-agent:
    image: gauravpatil77/ai-research-agent:latest
    container_name: ai-research-agent

    ports:
      - "8502:8501"

    env_file:
      - .env

    restart: unless-stopped
```

This configuration pulls and runs the published image instead of building the application from local source code.

#### 4. Start the Application

```bash
docker compose up -d
```

Docker Compose downloads the image if necessary and starts the container.

#### 5. Access the Application

Open:

**http://localhost:8502**

#### 6. View Logs

```bash
docker compose logs -f
```

#### 7. Stop the Application

```bash
docker compose down
```

### Option 2: Run Directly from Docker Hub

You can run the published image without Docker Compose.

#### 1. Pull the Image

```bash
docker pull gauravpatil77/ai-research-agent:latest
```

#### 2. Run the Container

Ensure that a `.env` file exists in your current directory.

```bash
docker run -d \
  --name ai-research-agent \
  -p 8502:8501 \
  --env-file .env \
  --restart unless-stopped \
  gauravpatil77/ai-research-agent:latest
```

#### 3. Open the Application

Visit:

**http://localhost:8502**

### Option 3: Build the Docker Image Locally

If you want to modify the source code and build a new image from your local project, use:

```bash
docker build -t ai-research-agent .
```

Run it:

```bash
docker run -d \
  --name ai-research-agent \
  -p 8502:8501 \
  --env-file .env \
  --restart unless-stopped \
  ai-research-agent
```

This approach uses your local Dockerfile and source code rather than downloading the published image.

---

## 📝 Docker Configuration Explained

| Configuration             | Purpose                                                      |
| ------------------------- | ------------------------------------------------------------ |
| `image`                   | Specifies the Docker image to run                            |
| `build`                   | Builds an image from the local Dockerfile                    |
| `container_name`          | Assigns a name to the container                              |
| `8502:8501`               | Maps host port `8502` to container port `8501`               |
| `env_file`                | Loads environment variables from `.env`                      |
| `restart: unless-stopped` | Automatically restarts the container unless manually stopped |

**Image versus build:**

* Use `image` to run the published Docker Hub image.
* Use `build` to build an image from the local project.
* You can configure both when you want Compose to build the image and assign it a specific image name.

---

## 🔐 Environment Variables

| Variable            | Required? | Purpose                                  |
| ------------------- | --------- | ---------------------------------------- |
| `GOOGLE_API_KEY`    | Yes       | Authenticates Google Gemini API requests |
| `TAVILY_API_KEY`    | Yes       | Authenticates Tavily web searches        |
| `LANGSMITH_TRACING` | Optional  | Enables LangSmith tracing when supported |
| `LANGSMITH_API_KEY` | Optional  | Authenticates with LangSmith             |
| `LANGSMITH_PROJECT` | Optional  | Sets the tracing project name            |

Configure these variables in your deployment platform's environment settings when required. Never hardcode API credentials in your source code or publish them in your README.

---

## 🔮 Future Improvements

* 📄 Export research reports as PDF and Markdown.
* 🔗 Improve source citations and reference formatting.
* 💾 Add persistent research history.
* 🎚️ Introduce configurable research depth and search limits.
* ⚡ Implement caching to reduce repeated API calls.
* 🧪 Add automated tests and CI/CD workflows.
* 📊 Improve workflow monitoring and error handling.

---

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

* Building multi-step agentic workflows using LangGraph.
* Integrating LLMs with external web search tools.
* Automating research and report generation.
* Observability and debugging with LangSmith.
* Managing environment variables and API credentials.
* Containerizing Python applications with Docker.
* Running containerized applications through Docker Compose.
* Publishing Docker images to Docker Hub.
* Deploying AI applications to the cloud.

---

## 👨‍💻 Author

**Gaurav Patil**

B.E. Computer Engineering Student | AI/ML & Generative AI Enthusiast

* **GitHub:** https://github.com/GauravPatil777
* **LinkedIn:** https://www.linkedin.com/in/gaurav-patil45/

---
