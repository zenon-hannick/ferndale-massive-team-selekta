import React, { useEffect, useState } from 'react';
import { getPlayers, balanceTeams } from '../services/api';

export const TeamBalancer: React.FC = () => {
  const [players, setPlayers] = useState<any[]>([]);
  const [selected, setSelected] = useState<string[]>([]);
  const [teams, setTeams] = useState<any | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getPlayers().then(res => setPlayers(res.data));
  }, []);

  const handleSelect = (name: string) => {
    setSelected(sel => sel.includes(name) ? sel.filter(n => n !== name) : [...sel, name]);
  };

  const handleBalance = async () => {
    setError(null);
    const selectedPlayers = players.filter(p => selected.includes(p.name));
    try {
      const res = await balanceTeams(selectedPlayers);
      setTeams(res.data);
    } catch (e: any) {
      setTeams(null);
      setError(e?.response?.data?.detail || 'Error balancing teams');
    }
  };

  return (
    <div>
      <h2>Team Balancer</h2>
      <div style={{ marginBottom: 16 }}>
        <strong>Select 10 or 12 available players:</strong>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8, marginTop: 8 }}>
          {players.map(p => (
            <label key={p.name} style={{ border: '1px solid #ccc', borderRadius: 4, padding: 8, background: selected.includes(p.name) ? '#1976d2' : '#fff', color: selected.includes(p.name) ? '#fff' : '#222', cursor: 'pointer' }}>
              <input type="checkbox" checked={selected.includes(p.name)} onChange={() => handleSelect(p.name)} style={{ marginRight: 4 }} />
              {p.name}
            </label>
          ))}
        </div>
        <button onClick={handleBalance} style={{ marginTop: 12 }}>Balance Teams</button>
      </div>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      {teams && (
        <div style={{ display: 'flex', gap: 32 }}>
          <div>
            <h3>Red Team</h3>
            <ul>
              {teams.red_team.players.map((p: any) => <li key={p.name}>{p.name}</li>)}
            </ul>
          </div>
          <div>
            <h3>Yellow Team</h3>
            <ul>
              {teams.yellow_team.players.map((p: any) => <li key={p.name}>{p.name}</li>)}
            </ul>
          </div>
        </div>
      )}
    </div>
  );
}; 