import React from "react";

export default function PRTable({ prs }) {
  return (
    <table>
      <thead>
        <tr>
          <th>PR #</th>
          <th>Repo</th>
          <th>Files Analyzed</th>
          <th>Timestamp</th>
        </tr>
      </thead>
      <tbody>
        {prs.map((pr, idx) => (
          <tr key={idx}>
            <td>{pr.pr_number}</td>
            <td>{pr.repo}</td>
            <td>{pr.files.length}</td>
            <td>{new Date(pr.timestamp).toLocaleString()}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}