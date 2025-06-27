import React from 'react';

interface LayoutProps {
  children: React.ReactNode;
  setSection: (section: string) => void;
  section: string;
}

const sections = [
  { key: 'players', label: 'Players' },
  { key: 'teams', label: 'Team Balancer' },
  { key: 'games', label: 'Game History' },
  { key: 'stats', label: 'Player Stats' },
];

export const Layout: React.FC<LayoutProps> = ({ children, setSection, section }) => (
  <div style={{ display: 'flex', minHeight: '100vh' }}>
    <nav style={{ width: 200, background: '#f5f5f5', padding: 24 }}>
      <h2>⚽ The Ferndale Massive<br/>Team Selekta<br/><small>Inside the ride</small></h2>
      <ul style={{ listStyle: 'none', padding: 0 }}>
        {sections.map(s => (
          <li key={s.key}>
            <button
              style={{
                background: section === s.key ? '#1976d2' : 'transparent',
                color: section === s.key ? '#fff' : '#222',
                border: 'none',
                padding: '8px 16px',
                margin: '4px 0',
                width: '100%',
                textAlign: 'left',
                borderRadius: 4,
                cursor: 'pointer',
                fontWeight: section === s.key ? 'bold' : 'normal',
              }}
              onClick={() => setSection(s.key)}
            >
              {s.label}
            </button>
          </li>
        ))}
      </ul>
    </nav>
    <main style={{ flex: 1, padding: 32 }}>{children}</main>
  </div>
); 