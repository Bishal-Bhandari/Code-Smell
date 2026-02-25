import axios from "axios";
import { useEffect, useState } from "react";
import PRTable from "../components/PRTable";

export default function Dashboard() {
  const [owner, setOwner] = useState("bishal");
  const [repo, setRepo] = useState("ai-code-reviewer");
  const [prs, setPRs] = useState([]);

  const fetchData = async () => {
    try {
      const res = await axios.get(
        `http://localhost:8000/dashboard/pr-history/${owner}/${repo}`
      );
      setPRs(res.data.prs);
    } catch (err) {
      console.error("Error fetching PRs:", err);
      setPRs([]);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div>
      <h1>PR Dashboard</h1>
      <div style={{ marginBottom: "1rem" }}>
        <input
          type="text"
          placeholder="Owner"
          value={owner}
          onChange={(e) => setOwner(e.target.value)}
        />
        <input
          type="text"
          placeholder="Repo"
          value={repo}
          onChange={(e) => setRepo(e.target.value)}
        />
        <button onClick={fetchData}>Load PRs</button>
      </div>
      <PRTable prs={prs} />
    </div>
  );
}