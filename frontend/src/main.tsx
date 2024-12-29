import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import "./style.css";
import Navbar from "./Navbar";
import Login from "./Login";
import Register from "./Register";
import Auth from "./Auth";

const rootElement = document.getElementById("app");
if (rootElement) {
  ReactDOM.createRoot(rootElement).render(
    <React.StrictMode>
      <Router>
        {/* Navbar appears on all pages */}
        <Navbar />
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/auth" element={<Auth />} />
          <Route
            path="/"
            element={
              <>
                <h1>Welcome to the Home Page</h1>
              </>
            }
          />
          {/* Default route */}
        </Routes>
      </Router>
    </React.StrictMode>
  );
} else {
  console.error("Root element not found");
}
