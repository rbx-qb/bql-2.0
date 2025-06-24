import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [commands, setCommands] = useState("RUN_QISKIT\nRUN_STRAWBERRY");
  const [output, setOutput] = useState<any>(null);

  const runCommands = async () => {
    const cmds = commands.split('\n').map(c => c.trim()).filter(c => c);
    const res = await axios.post("http://localhost:8000/run/", { commands: cmds });
    setOutput(res.data.output);
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">BQL Hybrid Quantum 2.0</h1>
      <textarea
        className="w-full h-32 border p-2"
        value={commands}
        onChange={(e) => setCommands(e.target.value)}
      />
      <button
        className="mt-4 px-4 py-2 bg-blue-600 text-white rounded"
        onClick={runCommands}
      >
        Run
      </button>
      <div className="mt-6">
        <h2 className="text-xl font-semibold mb-2">Output:</h2>
        <pre className="bg-black text-green-300 p-4">{JSON.stringify(output, null, 2)}</pre>
      </div>
    </div>
  );
}

