import { useEffect, useState } from "react";
import Layout from "../components/Layout";
import API from "../services/api";
import Card from "../components/Card";
import { BarChart, Bar, XAxis, YAxis, Tooltip } from "recharts";

export default function Analytics() {
  const [data, setData] = useState(null);

  useEffect(() => {
    API.get("/dashboard/analytics").then((res) => setData(res.data));
  }, []);

  const chartData = [
    { name: "Reviews", value: data?.total_reviews || 0 },
  ];

  return (
    <Layout>
      <h1 className="text-2xl mb-6">Analytics</h1>

      <Card>
        <BarChart width={400} height={300} data={chartData}>
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="value" />
        </BarChart>
      </Card>
    </Layout>
  );
}