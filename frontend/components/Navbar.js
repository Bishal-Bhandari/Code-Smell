import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="bg-black text-white px-8 py-4 flex justify-between">
      <h1 className="text-xl font-bold">AI Code Reviewer</h1>
      <div className="space-x-6">
        <Link href="/">Dashboard</Link>
        <Link href="/api-keys">API Keys</Link>
        <Link href="/settings">Subscription</Link>
        <Link href="/login">Login</Link>
      </div>
    </nav>
  );
}