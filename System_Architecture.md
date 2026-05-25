# System Architecture & UI Design

This document visually represents the design and workflow of **CrisisSignal AI Lite**.

## 🎨 UI Mockup / Wireframe
The following is the initial UI concept for the Streamlit dashboard. It features a modern, dark-themed alert system that presents the classified category and confidence score directly to the user.

![UI Mockup](assets/crisissignal_ui_mockup.png)

## 🗺️ Machine Learning Workflow

The system takes user text input, cleans it using NLP techniques, passes it through a classification model, and outputs the result in real-time.

```mermaid
graph TD
    %% Styling
    classDef userFill fill:#2b313e,stroke:#3b82f6,stroke-width:2px,color:#fff
    classDef processFill fill:#1f2937,stroke:#10b981,stroke-width:2px,color:#fff
    classDef modelFill fill:#374151,stroke:#8b5cf6,stroke-width:2px,color:#fff
    classDef outputFill fill:#111827,stroke:#ef4444,stroke-width:2px,color:#fff

    %% Nodes
    A[👤 User Input: Text Message]:::userFill
    
    subgraph Data Preprocessing
        B[🔤 Lowercase & Cleaning]:::processFill
        C[✂️ Tokenization & Stop-words]:::processFill
        D[🔢 Text Vectorization]:::processFill
    end
    
    subgraph Machine Learning Core
        E[🧠 NLP Model: Logistic Regression]:::modelFill
    end
    
    subgraph Real-Time Output
        F[🚨 Emergency Category]:::outputFill
        G[💯 Confidence Score %]:::outputFill
    end

    %% Connections
    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    E --> G
```
