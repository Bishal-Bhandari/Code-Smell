import Link from "next/link";

export default function Sidebar() {
  return (
    <div className="w-64 bg-slate-800 p-5 space-y-4">
      <h1 className="text-xl font-bold text-blue-400">AI Reviewer</h1>

      <nav className="flex flex-col gap-3">
        <Link href="/dashboard">Dashboard</Link>
        <Link href="/repos">Repositories</Link>
        <Link href="/analytics">Analytics</Link>
        <Link href="/settings">Settings</Link>
      </nav>
    </div>
  );
}