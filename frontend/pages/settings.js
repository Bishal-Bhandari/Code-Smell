import Layout from "../components/Layout";
import ProtectedRoute from "../components/ProtectedRoute";

export default function Settings() {
  return (
    <ProtectedRoute>
      <Layout>
        <h1 className="text-3xl font-bold mb-6">Subscription</h1>

        <div className="grid grid-cols-2 gap-6">
          <div className="p-6 bg-white shadow-xl rounded-2xl">
            <h2 className="text-xl font-bold mb-4">Free Plan</h2>
            <p>✔ 50 PR reviews per month</p>
            <p>✔ Basic AI Analysis</p>
          </div>

          <div className="p-6 bg-indigo-600 text-white shadow-xl rounded-2xl">
            <h2 className="text-xl font-bold mb-4">Pro Plan</h2>
            <p>✔ Unlimited PR reviews</p>
            <p>✔ Advanced AI Analysis</p>
            <button className="mt-4 bg-white text-indigo-600 px-4 py-2 rounded-lg">
              Upgrade
            </button>
          </div>
        </div>
      </Layout>
    </ProtectedRoute>
  );
}