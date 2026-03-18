import { useEffect, useState } from "react";
import Layout from "../components/Layout";
import API from "../services/api";

export default function Analytics() {
  const [data, setData] = useState(null);

  useEffect(() => {
    API.get("/dashboard/analytics").then((res) => setData(res.data));
  }, []);

  return (
    <Layout>
      <h1 className="text-xl mb-4">Analytics</h1>

      {data && (
        <div className="bg-slate-800 p-6 rounded">
          Total Reviews: {data.total_reviews}
        </div>
      )}
    </Layout>
  );
}