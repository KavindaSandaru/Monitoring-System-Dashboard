"use client";

import { useEffect, useState } from "react";

import MetricsChart from "@/components/MetricsChart";

export default function Home() {

  const [metrics, setMetrics] = useState({
    cpu: 0,
    ram: 0,
    status: "LOADING",
    timestamp: "",
  });

  const [history, setHistory] = useState([]);

  async function fetchMetrics() {

    try {

      const response = await fetch(
        "http://backend:8000/metrics"
      );

      const data = await response.json();

      setMetrics(data);

    } catch (error) {
      console.error(error);
    }
  }

  async function fetchHistory() {

    try {

      const response = await fetch(
        "http://backend:8000/history"
      );

      const data = await response.json();

      setHistory(data);

    } catch (error) {
      console.error(error);
    }
  }

  useEffect(() => {

    fetchMetrics();
    fetchHistory();

    const interval = setInterval(() => {

      fetchMetrics();
      fetchHistory();

    }, 3000);

    return () => clearInterval(interval);

  }, []);

  return (
    <main className="min-h-screen bg-black text-white p-10">

      <h1 className="text-4xl font-bold mb-10">
        Monitoring Dashboard
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

        <div className="bg-zinc-900 p-6 rounded-2xl shadow-lg">
          <h2 className="text-xl mb-2 text-zinc-400">
            CPU Usage
          </h2>

          <p className="text-5xl font-bold">
            {metrics.cpu}%
          </p>
        </div>

        <div className="bg-zinc-900 p-6 rounded-2xl shadow-lg">
          <h2 className="text-xl mb-2 text-zinc-400">
            RAM Usage
          </h2>

          <p className="text-5xl font-bold">
            {metrics.ram}%
          </p>
        </div>

        <div className="bg-zinc-900 p-6 rounded-2xl shadow-lg">
          <h2 className="text-xl mb-2 text-zinc-400">
            System Status
          </h2>

          <p className="text-3xl font-bold">
            {metrics.status}
          </p>
        </div>

      </div>

      <div className="mt-10 text-zinc-500">
        Last Updated: {metrics.timestamp}
      </div>

      <MetricsChart data={history} />

    </main>
  );
}