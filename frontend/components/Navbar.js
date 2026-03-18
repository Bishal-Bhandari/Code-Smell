import Link from "next/link";

export default function Navbar() {
  return (
    <div className="bg-slate-800 p-4 flex justify-between">
      <h2 className="font-semibold">Dashboard</h2>
      <button
        onClick={() => {
          localStorage.removeItem("token");
          window.location.href = "/login";
        }}
        className="bg-red-500 px-3 py-1 rounded"
      >
        Logout
      </button>
    </div>
  );
}