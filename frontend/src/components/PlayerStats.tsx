import React, { useEffect, useState } from 'react';
import { getPlayers, getPlayerStats } from '../services/api';

export const PlayerStats: React.FC = () => {
  const [players, setPlayers] = useState<any[]>([]);
  const [selected, setSelected] = useState('');
  const [stats, setStats] = useState<any | null>(null);

  useEffect(() => {
    getPlayers().then(res => setPlayers(res.data));
  }, []);

  const handleSelect = async (e: React.ChangeEvent<HTMLSelectElement>) => {
    const name = e.target.value;
    setSelected(name);
    if (name) {
      const res = await getPlayerStats(name);
      setStats(res.data);
    } else {
      setStats(null);
    }
  };

  return (
    <div>
      <h2>Player Stats</h2>
      <select value={selected} onChange={handleSelect} style={{ marginBottom: 16 }}>
        <option value="">Select player...</option>
        {players.map((p: any) => <option key={p.name} value={p.name}>{p.name}</option>)}
      </select>
      {stats && (
        <div style={{ marginTop: 16 }}>
          <div><strong>Games Played:</strong> {stats.games_played}</div>
          <div><strong>Wins:</strong> {stats.wins}</div>
          <div><strong>Losses:</strong> {stats.losses}</div>
          <div><strong>Win Rate:</strong> {stats.win_rate}%</div>
        </div>
      )}
    </div>
  );
}; 