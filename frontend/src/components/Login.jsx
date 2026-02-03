import React, { useState } from "react";

function Login({ onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    alert(`Logged in as ${username}`);
    onLogin();
  };

  return (
    <div>
      <h1>Login Page</h1>
      <form onSubmit={handleSubmit}>
        <input placeholder="Username" value={username} onChange={(e)=>setUsername(e.target.value)} required/><br/>
        <input placeholder="Password" type="password" value={password} onChange={(e)=>setPassword(e.target.value)} required/><br/>
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default Login;
