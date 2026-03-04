import { useEffect, useState } from "react";
import API from "../services/api";
import Layout from "../components/Layout";
import ProtectedRoute from "../components/ProtectedRoute";

export default function ApiKeys() {
  const [apiKey, setApiKey] = useState("");

  const generateKey = async () => {
    const res = await API.post("/auth/generate-api-key");
    setApiKey(res.data.api_key);
  };

  return (
    <ProtectedRoute>
      <Layout>
        <h1 className="text-3xl font-bold mb-6">API Key</h1>

        <button
          onClick={generateKey}
          className="bg-indigo-600 text-white px-6 py-3 rounded-lg"
        >
          Generate API Key
        </button>

        {apiKey && (
          <div className="mt-6 p-4 bg-gray-200 rounded-lg">
            <p className="font-mono">{apiKey}</p>
          </div>
        )}
      </Layout>
    </ProtectedRoute>
  );
}