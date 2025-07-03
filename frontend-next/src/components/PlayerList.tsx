"use client";
import React, { useEffect, useState } from 'react';
import { getPlayers, createPlayer, updatePlayer } from '../services/api';

const columnStyles = [
  { width: '25%' }, // Name
  { width: '18.75%' }, // Attacking
  { width: '18.75%' }, // Defending
  { width: '18.75%' }, // Goalkeeping
  { width: '18.75%' }, // Energy
];

const PlayerList: React.FC = () => {
  const [players, setPlayers] = useState<any[]>([]);
  const [form, setForm] = useState({ name: '', attacking: 5, defending: 5, goalkeeping: 5, energy: 5 });
  const [editingPlayer, setEditingPlayer] = useState<string | null>(null);
  const [editForm, setEditForm] = useState({ name: '', attacking: 5, defending: 5, goalkeeping: 5, energy: 5 });
  const [loading, setLoading] = useState(false);

  const fetchPlayers = async () => {
    setLoading(true);
    const res = await getPlayers();
    setPlayers(res.data);
    setLoading(false);
  };

  useEffect(() => { fetchPlayers(); }, []);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setForm(f => ({ ...f, [name]: value }));
  };

  const handleEditChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setEditForm(f => ({ ...f, [name]: value }));
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
    });
    setForm({ name: '', attacking: 5, defending: 5, goalkeeping: 5, energy: 5 });
    fetchPlayers();
  };

  const startEditing = (player: any) => {
    setEditingPlayer(player.name);
    setEditForm({
      name: player.name,
      attacking: player.attributes.attacking,
      defending: player.attributes.defending,
      goalkeeping: player.attributes.goalkeeping,
      energy: player.attributes.energy,
    });
  };

  const cancelEditing = () => {
    setEditingPlayer(null);
    setEditForm({ name: '', attacking: 5, defending: 5, goalkeeping: 5, energy: 5 });
  };

  const handleSaveEdit = async () => {
    if (!editingPlayer) return;
    
    await updatePlayer(editingPlayer, {
      name: editForm.name,
      attributes: {
        attacking: Number(editForm.attacking),
        defending: Number(editForm.defending),
        goalkeeping: Number(editForm.goalkeeping),
        energy: Number(editForm.energy),
      },
      available: true,
    });
    
    setEditingPlayer(null);
    setEditForm({ name: '', attacking: 5, defending: 5, goalkeeping: 5, energy: 5 });
    fetchPlayers();
  };

  return (
    <div style={{ maxWidth: 700, margin: '0 auto' }}>
      <h2>Players</h2>
      {/* Players List */}
      {loading ? <div>Loading...</div> : (
        <div style={{ marginBottom: 32 }}>
          <table style={{ width: '100%', borderCollapse: 'separate', borderSpacing: 0, background: '#fff', borderRadius: 12, boxShadow: '0 2px 12px rgba(0,0,0,0.10)', overflow: 'hidden', border: '2px solid #1976d2' }}>
            <colgroup>
              <col style={{ width: '25%' }} />
              <col style={{ width: '18.75%' }} />
              <col style={{ width: '18.75%' }} />
              <col style={{ width: '18.75%' }} />
              <col style={{ width: '18.75%' }} />
              <col style={{ width: '100px' }} />
            </colgroup>
            <thead>
              <tr style={{ background: 'linear-gradient(90deg, #1976d2 60%, #42a5f5 100%)', color: '#fff', fontWeight: 900, fontSize: 17, letterSpacing: 1 }}>
                <th style={{ padding: 14, borderRight: '2px solid #1565c0' }}>Name</th>
                <th style={{ background: '#e3f2fd', color: '#1976d2', borderRight: '2px solid #1565c0' }}>Att</th>
                <th style={{ background: '#e8f5e9', color: '#388e3c', borderRight: '2px solid #1565c0' }}>Def</th>
                <th style={{ background: '#fffde7', color: '#fbc02d', borderRight: '2px solid #1565c0' }}>GK</th>
                <th style={{ background: '#fce4ec', color: '#c2185b', borderRight: '2px solid #1565c0' }}>Energy</th>
                <th style={{ background: 'transparent' }}></th>
              </tr>
            </thead>
            <tbody>
              {players.map((p, idx) => (
                <tr
                  key={p.name}
                  style={{
                    borderBottom: '2px solid #1976d2',
                    background: editingPlayer === p.name
                      ? '#fffde7'
                      : idx % 2 === 0
                        ? '#e3f2fd'
                        : '#fff',
                    transition: 'background 0.2s',
                  }}
                  onMouseOver={e => (e.currentTarget.style.background = editingPlayer === p.name ? '#fff9c4' : '#bbdefb')}
                  onMouseOut={e => (e.currentTarget.style.background = editingPlayer === p.name ? '#fffde7' : idx % 2 === 0 ? '#e3f2fd' : '#fff')}
                >
                  {editingPlayer === p.name ? (
                    <>
                      <td style={{ padding: 10, borderRight: '2px solid #1565c0' }}>
                        <input
                          name="name"
                          value={editForm.name}
                          readOnly
                          style={{ padding: 6, borderRadius: 6, border: '1.5px solid #90caf9', width: '100%', background: '#f5f5f5', color: '#222', fontWeight: 700, fontSize: 15 }}
                        />
                      </td>
                      <td style={{ textAlign: 'center', padding: 10, background: '#e3f2fd', borderRight: '2px solid #1565c0' }}>
                        <input
                          name="attacking"
                          type="number"
                          min={1}
                          max={10}
                          value={editForm.attacking}
                          onChange={handleEditChange}
                          style={{ padding: 6, borderRadius: 6, border: '1.5px solid #90caf9', width: '60px', textAlign: 'center', color: '#1976d2', background: '#fff', fontWeight: 600 }}
                        />
                      </td>
                      <td style={{ textAlign: 'center', padding: 10, background: '#e8f5e9', borderRight: '2px solid #1565c0' }}>
                        <input
                          name="defending"
                          type="number"
                          min={1}
                          max={10}
                          value={editForm.defending}
                          onChange={handleEditChange}
                          style={{ padding: 6, borderRadius: 6, border: '1.5px solid #81c784', width: '60px', textAlign: 'center', color: '#388e3c', background: '#fff', fontWeight: 600 }}
                        />
                      </td>
                      <td style={{ textAlign: 'center', padding: 10, background: '#fffde7', borderRight: '2px solid #1565c0' }}>
                        <input
                          name="goalkeeping"
                          type="number"
                          min={1}
                          max={10}
                          value={editForm.goalkeeping}
                          onChange={handleEditChange}
                          style={{ padding: 6, borderRadius: 6, border: '1.5px solid #ffe082', width: '60px', textAlign: 'center', color: '#fbc02d', background: '#fff', fontWeight: 600 }}
                        />
                      </td>
                      <td style={{ textAlign: 'center', padding: 10, background: '#fce4ec', borderRight: '2px solid #1565c0' }}>
                        <input
                          name="energy"
                          type="number"
                          min={1}
                          max={10}
                          value={editForm.energy}
                          onChange={handleEditChange}
                          style={{ padding: 6, borderRadius: 6, border: '1.5px solid #f06292', width: '60px', textAlign: 'center', color: '#c2185b', background: '#fff', fontWeight: 600 }}
                        />
                      </td>
                      <td style={{ padding: 10, textAlign: 'center', background: 'transparent' }}>
                        <button
                          onClick={handleSaveEdit}
                          style={{
                            background: 'linear-gradient(90deg, #1976d2 60%, #42a5f5 100%)',
                            color: '#fff',
                            border: 'none',
                            borderRadius: 6,
                            padding: '6px 14px',
                            marginRight: 6,
                            cursor: 'pointer',
                            fontSize: 14,
                            fontWeight: 700,
                            boxShadow: '0 1px 4px rgba(25, 118, 210, 0.10)',
                          }}
                        >
                          Save
                        </button>
                        <button
                          onClick={cancelEditing}
                          style={{
                            background: 'linear-gradient(90deg, #f44336 60%, #e57373 100%)',
                            color: '#fff',
                            border: 'none',
                            borderRadius: 6,
                            padding: '6px 14px',
                            cursor: 'pointer',
                            fontSize: 14,
                            fontWeight: 700,
                            boxShadow: '0 1px 4px rgba(244, 67, 54, 0.10)',
                          }}
                        >
                          Cancel
                        </button>
                      </td>
                    </>
                  ) : (
                    <>
                      <td style={{ padding: 10, color: '#0d1333', fontWeight: 700, fontSize: 15, borderRight: '2px solid #1565c0' }}>{p.name}</td>
                      <td style={{ textAlign: 'center', padding: 10, color: '#1976d2', background: '#e3f2fd', fontWeight: 600, borderRight: '2px solid #1565c0' }}>{p.attributes.attacking}</td>
                      <td style={{ textAlign: 'center', padding: 10, color: '#388e3c', background: '#e8f5e9', fontWeight: 600, borderRight: '2px solid #1565c0' }}>{p.attributes.defending}</td>
                      <td style={{ textAlign: 'center', padding: 10, color: '#fbc02d', background: '#fffde7', fontWeight: 600, borderRight: '2px solid #1565c0' }}>{p.attributes.goalkeeping}</td>
                      <td style={{ textAlign: 'center', padding: 10, color: '#c2185b', background: '#fce4ec', fontWeight: 600, borderRight: '2px solid #1565c0' }}>{p.attributes.energy}</td>
                      <td style={{ padding: 10, textAlign: 'center', background: 'transparent' }}>
                        <button
                          onClick={() => startEditing(p)}
                          style={{
                            background: 'linear-gradient(90deg, #1976d2 60%, #42a5f5 100%)',
                            color: '#fff',
                            border: 'none',
                            borderRadius: 6,
                            padding: '6px 14px',
                            cursor: 'pointer',
                            fontSize: 14,
                            fontWeight: 700,
                            boxShadow: '0 1px 4px rgba(25, 118, 210, 0.10)',
                          }}
                        >
                          Edit
                        </button>
                      </td>
                    </>
                  )}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {/* Add New Player */}
      <form onSubmit={handleSubmit} style={{ background: '#f9f9f9', borderRadius: 8, padding: 24, boxShadow: '0 2px 8px rgba(0,0,0,0.04)' }}>
        <h3>Add New Player</h3>
        <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr 1fr 1fr 1fr', gap: 12, alignItems: 'center', marginBottom: 12 }}>
          <input
            name="name"
            value={form.name}
            onChange={handleChange}
            placeholder="Name"
            required
            style={{ padding: 8, borderRadius: 4, border: '1px solid #ccc' }}
          />
          <input
            name="attacking"
            type="number"
            min={1}
            max={10}
            value={form.attacking}
            onChange={handleChange}
            placeholder="Att"
            required
            style={{ padding: 8, borderRadius: 4, border: '1px solid #ccc', textAlign: 'center' }}
          />
          <input
            name="defending"
            type="number"
            min={1}
            max={10}
            value={form.defending}
            onChange={handleChange}
            placeholder="Def"
            required
            style={{ padding: 8, borderRadius: 4, border: '1px solid #ccc', textAlign: 'center' }}
          />
          <input
            name="goalkeeping"
            type="number"
            min={1}
            max={10}
            value={form.goalkeeping}
            onChange={handleChange}
            placeholder="GK"
            required
            style={{ padding: 8, borderRadius: 4, border: '1px solid #ccc', textAlign: 'center' }}
          />
          <input
            name="energy"
            type="number"
            min={1}
            max={10}
            value={form.energy}
            onChange={handleChange}
            placeholder="Energy"
            required
            style={{ padding: 8, borderRadius: 4, border: '1px solid #ccc', textAlign: 'center' }}
          />
        </div>
        <button
          type="submit"
          style={{ background: '#1976d2', color: '#fff', border: 'none', borderRadius: 4, padding: '8px 16px', cursor: 'pointer', fontWeight: 600 }}
        >
          Add Player
        </button>
      </form>
    </div>
  );
};

export default PlayerList; 