import { useState } from "react";
import Layout from "../components/Layout";
import API from "../services/api";

export default function Repos() {
  const [owner, setOwner] = useState("");
  const [repo, setRepo] = useState("");

  const addRepo = async () => {
  const token = localStorage.getItem("token");  // ✅ define here

  console.log("TOKEN:", token);

  await API.post(
    `/auth/register-repo?owner=${owner}&repo=${repo}`,
    {},
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  alert("Repo added!");
};

  return (
    <Layout>
      <h1 className="text-xl mb-4">Add Repository</h1>

      <input
        placeholder="Owner"
        className="p-2 bg-slate-700 mr-2"
        onChange={(e) => setOwner(e.target.value)}
      />
      <input
        placeholder="Repo"
        className="p-2 bg-slate-700 mr-2"
        onChange={(e) => setRepo(e.target.value)}
      />

      <button
        onClick={addRepo}
        className="bg-green-500 px-4 py-2 rounded"
      >
        Add
      </button>
    </Layout>
  );
}