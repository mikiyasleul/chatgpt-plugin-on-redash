# Redash Chatbot Add-on
The Redash Chatbot Plugin is a powerful tool that integrates a chatbot powered by Large Language Models (LLMs) into Redash. This allows users to extract deep insights from dashboards and databases using simple, natural language queries. The add-on democratizes data analytics, making it accessible to non-technical users.

## Installation
To install the Redash Chatbot Add-on, follow these steps:
    1. Install Docker Desktop on your machine.
    2. Clone this repository to your local machine. (https://github.com/getredash/redash)
    3. Navigate to the project directory and run the following command to start Redash using Docker:

   ````
   docker-compose up
   ```

   This will download the necessary dependencies and start the Redash server.
- Once the server is up and running, open your web browser and navigate to `http://localhost:5000` to access the Redash application.
- Create the necessary database schema for the time-series data. Refer to the Redash documentation for detailed instructions on setting up the database schema.
- Prepare the frontend chatbot plugin using React. This plugin will handle the user interface for the chatbot functionality. Implement the necessary components and integrate them into Redash's front end.
- Prepare the backend API to handle the chatbot functionality. This will involve creating routes and controllers to handle user queries, interact with the LLM models, and retrieve data from the connected 
  databases.
- Obtain API keys from OpenAI to access their language models. These keys will be used to interact with the LLM models and generate responses based on user queries.
- Integrate the OpenAI API keys into the backend code, allowing the chatbot to use the LLM models for natural language processing and generating insightful responses.

## Usage
Once the Redash Chatbot Add-on is installed and configured, users can interact with the chatbot by accessing Redash's interface.
    - They can input natural language queries related to the dashboards and databases to extract valuable insights.
    - The chatbot will process the queries
    - interact with the LLM models
    - provide relevant responses and visualizations.
