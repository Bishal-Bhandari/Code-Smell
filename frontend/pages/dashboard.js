import { useEffect, useState } from "react";
import Layout from "../components/Layout";
import API from "../services/api";
import ProtectedRoute from "../components/ProtectedRoute";
import Card from "../components/Card";
import { motion } from "framer-motion";

export default function Dashboard() {
  const [data, setData] = useState({ prs: [], usage: 0, limit: 0 });

  useEffect(() => {
    API.get("/dashboard/my-prs").then((res) => setData(res.data));
  }, []);

  return (
    <ProtectedRoute>
      <Layout>
        <motion.h1
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="text-3xl font-bold mb-6"
        >
          Dashboard
        </motion.h1>

        {/* Usage Cards */}
        <div className="grid grid-cols-3 gap-6 mb-6">
          <Card>
            <h2 className="text-gray-400">Total PRs</h2>
            <p className="text-2xl font-bold">{data.prs.length}</p>
          </Card>

          <Card>
            <h2 className="text-gray-400">Usage</h2>
            <p className="text-2xl font-bold">
              {data.usage} / {data.limit}
            </p>
          </Card>

          <Card>
            <h2 className="text-gray-400">Plan</h2>
            <p className="text-2xl font-bold text-blue-400">Free</p>
          </Card>
        </div>

        {/* Table */}
        <Card>
          <table className="w-full">
            <thead>
              <tr className="text-left text-gray-400 border-b border-gray-700">
                <th>PR #</th>
                <th>Repo</th>
                <th>Files</th>
              </tr>
            </thead>
            <tbody>
              {data.prs.map((pr, i) => (
                <tr key={i} className="border-b border-gray-800">
                  <td>{pr.pr_number}</td>
                  <td>{pr.repo}</td>
                  <td>{pr.results.length}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </Card>
      </Layout>
    </ProtectedRoute>
  );
}