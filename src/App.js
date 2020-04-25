import React, { useState } from "react";
import logo from "./logo.svg";
import "./App.css";

const axios = require("axios");
const API_ROOT = "/api";

function App() {
  const [message, setMessage] = useState(null);

  const getMessage = async (e) => {
    e.preventDefault();
    await axios
      .get(API_ROOT + "/get_message")
      .then((res) => {
        let data = res.data;
        console.info(`Received response from API: ${JSON.stringify(data)}`);
        setMessage(data["message"]);
      })
      .catch((err) => console.error(err));
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Flask React Boilerplate</h1>
        {message ? (
          <div className="message">
            <button onClick={() => setMessage(null)}>Reset</button>
            <p>{message}</p>
          </div>
        ) : (
          <button onClick={getMessage}>Click to get message</button>
        )}
      </header>
    </div>
  );
}

export default App;
