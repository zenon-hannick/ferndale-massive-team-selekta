import React, { useEffect, useState } from 'react';
import { getPlayers, createPlayer } from '../services/api';

export const PlayerList: React.FC = () => {
  const [players, setPlayers] = useState<any[]>([]);
  const [form, setForm] = useState({ name: '', attacking: 5, defending: 5, goalkeeping: 5, energy: 5, available: true });
  const [loading, setLoading] = useState(false);

  const fetchPlayers = async () => {
    setLoading(true);
    const res = await getPlayers();
    setPlayers(res.data);
    setLoading(false);
  };

  useEffect(() => { fetchPlayers(); }, []);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value, type, checked } = e.target;
    setForm(f => ({ ...f, [name]: type === 'checkbox' ? checked : value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await createPlayer({
      name: form.name,
      attributes: {
        attacking: Number(form.attacking),
        defending: Number(form.defending),
        goalkeeping: Number(form.goalkeeping),
        energy: Number(form.energy),
      },
      available: form.available,
    });
    setForm({ name: '', attacking: 5, defending: 5, goalkeeping: 5, energy: 5, available: true });
    fetchPlayers();
  };

  return (
    <div>
      <h2>Players</h2>
      <form onSubmit={handleSubmit} style={{ marginBottom: 24, display: 'flex', gap: 8, flexWrap: 'wrap' }}>
        <input name="name" value={form.name} onChange={handleChange} placeholder="Name" required />
        <input name="attacking" type="number" min={1} max={10} value={form.attacking} onChange={handleChange} placeholder="Attacking" />
        <input name="defending" type="number" min={1} max={10} value={form.defending} onChange={handleChange} placeholder="Defending" />
        <input name="goalkeeping" type="number" min={1} max={10} value={form.goalkeeping} onChange={handleChange} placeholder="Goalkeeping" />
        <input name="energy" type="number" min={1} max={10} value={form.energy} onChange={handleChange} placeholder="Energy" />
        <label style={{ display: 'flex', alignItems: 'center', gap: 4 }}>
          <input name="available" type="checkbox" checked={form.available} onChange={handleChange} /> Available
        </label>
        <button type="submit">Add Player</button>
      </form>
      {loading ? <div>Loading...</div> : (
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr>
              <th>Name</th>
              <th>Att</th>
              <th>Def</th>
              <th>GK</th>
              <th>Energy</th>
              <th>Available</th>
            </tr>
          </thead>
          <tbody>
            {players.map((p) => (
              <tr key={p.name}>
                <td>{p.name}</td>
                <td>{p.attributes.attacking}</td>
                <td>{p.attributes.defending}</td>
                <td>{p.attributes.goalkeeping}</td>
                <td>{p.attributes.energy}</td>
                <td>{p.available ? '✅' : '❌'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}; 