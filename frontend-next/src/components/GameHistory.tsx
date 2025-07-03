"use client";
import React, { useEffect, useState } from 'react';
import { getGames } from '../services/api';

const GameHistory: React.FC = () => {
  const [games, setGames] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(true);
    getGames().then(res => {
      setGames(res.data);
      setLoading(false);
    });
  }, []);

  return (
    <div>
      <h2>Game History</h2>
      {loading ? <div>Loading...</div> : (
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr>
              <th>Date</th>
              <th>Red Team</th>
              <th>Yellow Team</th>
              <th>Score</th>
            </tr>
          </thead>
          <tbody>
            {games.map((g, i) => (
              <tr key={i}>
                <td>{g.date}</td>
                <td>{g.red_team.players.map((p: any) => p.name).join(', ')}</td>
                <td>{g.yellow_team.players.map((p: any) => p.name).join(', ')}</td>
                <td>{g.score.red_score} - {g.score.yellow_score}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default GameHistory; 