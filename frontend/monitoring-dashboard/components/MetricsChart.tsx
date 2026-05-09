"use client";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";

type Metric = {
  cpu: number;
  ram: number;
  timestamp: string;
};

export default function MetricsChart({
  data,
}: {
  data: Metric[];
}) {

  return (
    <div className="bg-zinc-900 p-6 rounded-2xl mt-10">

      <h2 className="text-2xl font-bold mb-6">
        System Metrics History
      </h2>

      <div className="h-[400px]">

        <ResponsiveContainer width="100%" height="100%">

          <LineChart data={data}>

            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="timestamp" />

            <YAxis />

            <Tooltip />

            <Line
              type="monotone"
              dataKey="cpu"
              stroke="#3b82f6"
              strokeWidth={3}
            />

            <Line
              type="monotone"
              dataKey="ram"
              stroke="#22c55e"
              strokeWidth={3}
            />

          </LineChart>

        </ResponsiveContainer>

      </div>

    </div>
  );
}