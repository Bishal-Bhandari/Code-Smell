import Link from "next/link";


export default function Sidebar() {
  return (
    <div className="w-64 bg-black/30 backdrop-blur-xl border-r border-white/10 p-6">
      <h1 className="text-2xl font-bold text-blue-400 mb-8">
        AI Reviewer
      </h1>

      <nav className="flex flex-col gap-4 text-gray-300">
        <Link href="/dashboard" className="hover:text-white">Dashboard</Link>
        <Link href="/repos" className="hover:text-white">Repositories</Link>
        <Link href="/analytics" className="hover:text-white">Analytics</Link>
        <Link href="/settings" className="hover:text-white">Settings</Link>
      </nav>
    </div>
  );
}