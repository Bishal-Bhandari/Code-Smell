import { useEffect, useState } from "react";
import API from "../services/api";
import Layout from "../components/Layout";
import PRTable from "../components/PRTable";
import ProtectedRoute from "../components/ProtectedRoute";

export default function Dashboard() {
  const [prs, setPrs] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await API.get("/dashboard/my-prs");
        setPrs(res.data.prs);
      } catch (err) {
        console.log(err);
      }
    };

    fetchData();
  }, []);

  return (
    <ProtectedRoute>
      <Layout>
        <h1 className="text-3xl font-bold mb-6">My PR Dashboard</h1>
        <PRTable prs={prs} />
      </Layout>
    </ProtectedRoute>
  );
}