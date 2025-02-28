import React, { useState } from "react";
import axios from "axios";
import ReactMarkdown from "react-markdown";
import CircularProgress from "@mui/material/CircularProgress";

const App = () => {
  const [userCode, setUserCode] = useState("");
  const [fixedCode, setFixedCode] = useState("");
  const [loading, setLoading] = useState(false);
  const [copySuccess, setCopySuccess] = useState("");

  const handleSubmit = async () => {
    setLoading(true);
    try {
      const response = await axios.post("http://127.0.0.1:8000/analyze", {
        code: userCode,
      });
      if (response.data.fixed_code) {
        setLoading(false);
        setUserCode("");
      }
      setFixedCode(response.data.fixed_code);
    } catch (error) {
      console.error("Error fetching AI response:", error);
    }
  };

  const handleCopy = () => {
    navigator.clipboard
      .writeText(fixedCode)
      .then(() => {
        setCopySuccess("Copied!");
        setTimeout(() => setCopySuccess(""), 2000); // Hide message after 2 seconds
      })
      .catch((err) => {
        console.error("Failed to copy code:", err);
      });
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h2>AI Code Reviewer</h2>
      <textarea
        rows={6}
        cols={50}
        placeholder="Paste your Python code here..."
        value={userCode}
        onChange={(e) => setUserCode(e.target.value)}
      />
      <br />
      <button
        onClick={handleSubmit}
        style={{ marginTop: "10px", minWidth: "100px" }}
      >
        {loading ? <CircularProgress size={16} /> : "Submit Code"}
      </button>

      {fixedCode && (
        <div>
          <h3>Fixed Code:</h3>
          <div
            style={{
              background: "#f4f4f4",
              padding: "10px",
              borderRadius: "5px",
              marginTop: "10px",
              maxWidth: "100%",
              overflow: "hidden",
              wordBreak: "break-word",
              position: "relative",
            }}
          >
            <ReactMarkdown>{fixedCode}</ReactMarkdown>
            <button
              onClick={handleCopy}
              style={{
                position: "absolute",
                top: "10px",
                right: "10px",
                padding: "5px 10px",
                fontSize: "12px",
                cursor: "pointer",
                border: "none",
                background: "#007bff",
                color: "#fff",
                borderRadius: "4px",
              }}
            >
              Copy
            </button>
            {copySuccess && (
              <span
                style={{ fontSize: "12px", color: "green", marginLeft: "10px" }}
              >
                {copySuccess}
              </span>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default App;
