import React, { useState } from "react";
import ChatBox from "./components/Chatbox";
import InputBox from "./components/InputBox";
import axios from "axios";
import "./styles/Chat.css";

function App() {
  const [messages, setMessages] = useState([]);

  const sendMessage = async (text) => {
    const userMessage = { sender: "user", text };
    setMessages((prev) => [...prev, userMessage]);

    try {
      const response = await axios.post("http://127.0.0.1:8000/chat", {
        message: text,
      });

      const botMessage = {
        sender: "bot",
        text: response.data.reply,
      };

      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      console.error(error);
      setMessages((prev) => [
        ...prev,
        { sender: "bot", text: "Error connecting to server" },
      ]);
    }
  };

  return (
    <div className="app">
      <h1 className="title">AI Chatbot</h1>
      <ChatBox messages={messages} />
      <InputBox sendMessage={sendMessage} />
    </div>
  );
}

export default App;