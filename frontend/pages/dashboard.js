import { useEffect, useState } from "react";
import Layout from "../components/Layout";
import API from "../services/api";
import ProtectedRoute from "../components/ProtectedRoute";

export default function Dashboard() {
  const [data, setData] = useState([]);

  useEffect(() => {
    API.get("/dashboard/my-prs").then((res) => setData(res.data));
  }, []);

  return (
    <ProtectedRoute>
      <Layout>
        <h1 className="text-2xl font-bold mb-4">PR Dashboard</h1>

        <table className="w-full bg-slate-800 rounded">
          <thead>
            <tr className="text-left border-b border-gray-700">
              <th>PR #</th>
              <th>Repo</th>
              <th>Files</th>
            </tr>
          </thead>
          <tbody>
            {data.map((pr, i) => (
              <tr key={i} className="border-b border-gray-700">
                <td>{pr.pr_number}</td>
                <td>{pr.repo}</td>
                <td>{pr.results.length}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </Layout>
    </ProtectedRoute>
  );
}