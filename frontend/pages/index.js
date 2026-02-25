import axios from "axios";
import { useEffect, useState } from "react";
import PRTable from "../components/PRTable";

export default function Dashboard() {
  const [prs, setPRs] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const res = await axios.get(
        "http://localhost:8000/dashboard/pr-history/owner/repo"
      );
      setPRs(res.data.prs);
    }
    fetchData();
  }, []);

  return (
    <div>
      <h1>PR Dashboard</h1>
      <PRTable prs={prs} />
    </div>
  );
}