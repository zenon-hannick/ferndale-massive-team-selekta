import React, { useEffect, useState } from 'react';
import { getPlayers, createPlayer, updatePlayer } from '../services/api';

const columnStyles = [
  { width: '25%' }, // Name
  { width: '18.75%' }, // Attacking
  { width: '18.75%' }, // Defending
  { width: '18.75%' }, // Goalkeeping
  { width: '18.75%' }, // Energy
];

export const PlayerList: React.FC = () => {
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
          <table style={{ width: '100%', borderCollapse: 'collapse', background: '#fff', borderRadius: 8, boxShadow: '0 2px 8px rgba(0,0,0,0.08)' }}>
            <colgroup>
              {columnStyles.map((col, idx) => (
                <col key={idx} style={col} />
              ))}
            </colgroup>
            <thead>
              <tr style={{ background: '#f5f5f5', color: '#1976d2', fontWeight: 600 }}>
                <th style={{ padding: 10 }}>Name</th>
                <th>Att</th>
                <th>Def</th>
                <th>GK</th>
                <th>Energy</th>
                <th style={{ width: '100px' }}>Actions</th>
              </tr>
            </thead>
            <tbody>
              {players.map((p) => (
                <tr key={p.name} style={{ borderBottom: '1px solid #eee' }}>
                  {editingPlayer === p.name ? (
                    // Edit mode
                    <>
                      <td style={{ padding: 8 }}>
                        <input
                          name="name"
                          value={editForm.name}
                          onChange={handleEditChange}
                          style={{ padding: 4, borderRadius: 4, border: '1px solid #ccc', width: '100%' }}
                        />
                      </td>
                      <td style={{ textAlign: 'center', padding: 8 }}>
                        <input
                          name="attacking"
                          type="number"
                          min={1}
                          max={10}
                          value={editForm.attacking}
                          onChange={handleEditChange}
                          style={{ padding: 4, borderRadius: 4, border: '1px solid #ccc', width: '60px', textAlign: 'center' }}
                        />
                      </td>
                      <td style={{ textAlign: 'center', padding: 8 }}>
                        <input
                          name="defending"
                          type="number"
                          min={1}
                          max={10}
                          value={editForm.defending}
                          onChange={handleEditChange}
                          style={{ padding: 4, borderRadius: 4, border: '1px solid #ccc', width: '60px', textAlign: 'center' }}
                        />
                      </td>
                      <td style={{ textAlign: 'center', padding: 8 }}>
                        <input
                          name="goalkeeping"
                          type="number"
                          min={1}
                          max={10}
                          value={editForm.goalkeeping}
                          onChange={handleEditChange}
                          style={{ padding: 4, borderRadius: 4, border: '1px solid #ccc', width: '60px', textAlign: 'center' }}
                        />
                      </td>
                      <td style={{ textAlign: 'center', padding: 8 }}>
                        <input
                          name="energy"
                          type="number"
                          min={1}
                          max={10}
                          value={editForm.energy}
                          onChange={handleEditChange}
                          style={{ padding: 4, borderRadius: 4, border: '1px solid #ccc', width: '60px', textAlign: 'center' }}
                        />
                      </td>
                      <td style={{ padding: 8, textAlign: 'center' }}>
                        <button
                          onClick={handleSaveEdit}
                          style={{
                            background: '#4caf50',
                            color: '#fff',
                            border: 'none',
                            borderRadius: 4,
                            padding: '4px 8px',
                            marginRight: 4,
                            cursor: 'pointer',
                            fontSize: 12,
                          }}
                        >
                          Save
                        </button>
                        <button
                          onClick={cancelEditing}
                          style={{
                            background: '#f44336',
                            color: '#fff',
                            border: 'none',
                            borderRadius: 4,
                            padding: '4px 8px',
                            cursor: 'pointer',
                            fontSize: 12,
                          }}
                        >
                          Cancel
                        </button>
                      </td>
                    </>
                  ) : (
                    // View mode
                    <>
                      <td style={{ padding: 8 }}>{p.name}</td>
                      <td style={{ textAlign: 'center', padding: 8 }}>{p.attributes.attacking}</td>
                      <td style={{ textAlign: 'center', padding: 8 }}>{p.attributes.defending}</td>
                      <td style={{ textAlign: 'center', padding: 8 }}>{p.attributes.goalkeeping}</td>
                      <td style={{ textAlign: 'center', padding: 8 }}>{p.attributes.energy}</td>
                      <td style={{ padding: 8, textAlign: 'center' }}>
                        <button
                          onClick={() => startEditing(p)}
                          style={{
                            background: '#1976d2',
                            color: '#fff',
                            border: 'none',
                            borderRadius: 4,
                            padding: '4px 8px',
                            cursor: 'pointer',
                            fontSize: 12,
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

      {/* Add New Player Section */}
      <div style={{
        background: '#fff',
        borderRadius: 8,
        boxShadow: '0 2px 8px rgba(0,0,0,0.08)',
        padding: 24,
      }}>
        <h3 style={{ marginTop: 0, marginBottom: 16 }}>Add New Player</h3>
        <form onSubmit={handleSubmit}>
          <div style={{
            display: 'grid',
            gridTemplateColumns: columnStyles.map(c => c.width).join(' '),
            gap: 8,
            alignItems: 'center',
            marginBottom: 8,
            fontWeight: 600,
            color: '#1976d2',
            fontSize: 15,
          }}>
            <div>Name</div>
            <div>Attacking</div>
            <div>Defending</div>
            <div>Goalkeeping</div>
            <div>Energy</div>
          </div>
          <div style={{
            display: 'grid',
            gridTemplateColumns: columnStyles.map(c => c.width).join(' '),
            gap: 8,
            alignItems: 'center',
            marginBottom: 8,
          }}>
            <input name="name" value={form.name} onChange={handleChange} placeholder="Name" required style={{ padding: 8, borderRadius: 4, border: '1px solid #ccc', width: '100%' }} />
            <input name="attacking" type="number" min={1} max={10} value={form.attacking} onChange={handleChange} style={{ padding: 8, borderRadius: 4, border: '1px solid #ccc', width: '100%' }} />
            <input name="defending" type="number" min={1} max={10} value={form.defending} onChange={handleChange} style={{ padding: 8, borderRadius: 4, border: '1px solid #ccc', width: '100%' }} />
            <input name="goalkeeping" type="number" min={1} max={10} value={form.goalkeeping} onChange={handleChange} style={{ padding: 8, borderRadius: 4, border: '1px solid #ccc', width: '100%' }} />
            <input name="energy" type="number" min={1} max={10} value={form.energy} onChange={handleChange} style={{ padding: 8, borderRadius: 4, border: '1px solid #ccc', width: '100%' }} />
          </div>
          <div style={{ textAlign: 'right' }}>
            <button type="submit" style={{
              background: '#1976d2',
              color: '#fff',
              border: 'none',
              borderRadius: 4,
              padding: '8px 24px',
              fontWeight: 600,
              cursor: 'pointer',
              transition: 'background 0.2s',
              marginTop: 8,
            }}>Add</button>
          </div>
        </form>
      </div>
    </div>
  );
}; 