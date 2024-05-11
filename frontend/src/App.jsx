import "./App.css";
import { useEffect, useState } from "react";
import { apiService } from "./common/apiService";

function App() {
  const [user, setUser] = useState({});

  useEffect(async () => {
    const res = await apiService("/api/auth/me");
    setUser(res);
  }, []);

  let id_ = null;
  let email = null;
  let username = null;

  if (user) {
    id_ = user.pk;
    email = user.email;
    username = user.username;
  }

  return (
    <>
      <h1>Dashboard</h1>
      <div className="card">
        <h2>ID: {id_}</h2>
        <h2>User: {username}</h2>
        <h2>Email: {email}</h2>
      </div>
    </>
  );
}

export default App;
