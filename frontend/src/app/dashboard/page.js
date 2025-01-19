"use client";

import React, { useState } from "react";
import axios from "axios";

export default function Dashboard() {
  const [file, setFile] = useState(null);
  const [topic, setTopic] = useState("");
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");

  const handleFileUpload = async () => {
    if (!file) return alert("Please select a file to upload");
    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("http://127.0.0.1:8000/upload/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      alert(res.data.message);
    } catch (error) {
      console.error(error);
      alert("Failed to upload file");
    }
  };

  const handleQuizGeneration = async () => {
    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/generate-quiz/",
        { topic },
        { headers: { "Content-Type": "application/x-www-form-urlencoded" } }
      );
      alert(res.data.message);
    } catch (error) {
      console.error(error);
      alert("Failed to generate quiz");
    }
  };

  const handleQuery = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:8000/query/", {
        params: { question },
      });
      setResponse(res.data.answer);
    } catch (error) {
      console.error(error);
      alert("Failed to get response");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>User Dashboard</h1>

      <div>
        <h2>Upload Study Material</h2>
        <input type="file" onChange={(e) => setFile(e.target.files[0])} />
        <button onClick={handleFileUpload}>Upload</button>
      </div>

      <div>
        <h2>Generate Quiz</h2>
        <input
          type="text"
          placeholder="Enter a topic..."
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
        />
        <button onClick={handleQuizGeneration}>Generate</button>
      </div>

      <div>
        <h2>Ask a Question</h2>
        <input
          type="text"
          placeholder="Enter your question..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />
        <button onClick={handleQuery}>Ask</button>
        {response && <p>Response: {response}</p>}
      </div>
    </div>
  );
}
