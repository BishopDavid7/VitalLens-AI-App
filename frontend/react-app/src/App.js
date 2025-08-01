import React, { useState } from 'react';

const App = () => {
  const [form, setForm] = useState({ age: '', weight: '', temperature: '' });
  const [prediction, setPrediction] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch('https://your-api-id.execute-api.region.amazonaws.com/Prod/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form)
    });
    const data = await res.json();
    setPrediction(`Prediction: ${data.prediction}`);
  };

  return (
    <div>
      <h2>VitalLens AI</h2>
      <form onSubmit={handleSubmit}>
        <input type="number" placeholder="Age" value={form.age} onChange={(e) => setForm({ ...form, age: e.target.value })} /><br />
        <input type="number" placeholder="Weight" value={form.weight} onChange={(e) => setForm({ ...form, weight: e.target.value })} /><br />
        <input type="number" placeholder="Temperature" value={form.temperature} onChange={(e) => setForm({ ...form, temperature: e.target.value })} /><br />
        <button type="submit">Submit</button>
      </form>
      <p>{prediction}</p>
    </div>
  );
};

export default App;
