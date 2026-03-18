import { useState } from "react";
import API from "../services/api";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const login = async () => {
    const res = await API.post("/auth/login", { email, password });

    localStorage.setItem("token", res.data.access_token);

    window.location.href = "/dashboard";
  };

  return (
    <div className="h-screen flex justify-center items-center">
      <div className="bg-slate-800 p-8 rounded-xl shadow-lg w-96 space-y-4">
        <h1 className="text-xl font-bold">Login</h1>

        <input
          className="w-full p-2 bg-slate-700 rounded"
          placeholder="Email"
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="password"
          className="w-full p-2 bg-slate-700 rounded"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
        />

        <button
          onClick={login}
          className="w-full bg-blue-500 p-2 rounded hover:bg-blue-600 transition"
        >
          Login
        </button>
      </div>
    </div>
  );
}