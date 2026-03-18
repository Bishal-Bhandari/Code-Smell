import Layout from "../components/Layout";
import API from "../services/api";

export default function Settings() {
  const generateKey = async () => {
    const res = await API.post("/auth/generate-api-key");
    alert(res.data.api_key);
  };

  return (
    <Layout>
      <h1 className="text-xl mb-4">Settings</h1>

      <button
        onClick={generateKey}
        className="bg-purple-500 px-4 py-2 rounded"
      >
        Generate API Key
      </button>
    </Layout>
  );
}