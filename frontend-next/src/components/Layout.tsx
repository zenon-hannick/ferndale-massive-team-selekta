"use client";
import React from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';

const sections = [
  { key: '/', label: 'Players' },
  { key: '/teams', label: 'Team Balancer' },
  { key: '/games', label: 'Game History' },
  { key: '/stats', label: 'Player Stats' },
];

const Layout: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const pathname = usePathname();
  return (
    <div style={{ display: 'flex', minHeight: '100vh' }}>
      <nav style={{ width: 200, background: '#f5f5f5', padding: 24 }}>
        <h2>⚽ The Ferndale Massive<br/>Team Selekta<br/><small>Inside the ride</small></h2>
        <ul style={{ listStyle: 'none', padding: 0 }}>
          {sections.map(s => (
            <li key={s.key}>
              <Link href={s.key}>
                <span
                  style={{
                    display: 'block',
                    background: pathname === s.key ? '#1976d2' : 'transparent',
                    color: pathname === s.key ? '#fff' : '#222',
                    border: 'none',
                    padding: '8px 16px',
                    margin: '4px 0',
                    width: '100%',
                    textAlign: 'left',
                    borderRadius: 4,
                    cursor: 'pointer',
                    fontWeight: pathname === s.key ? 'bold' : 'normal',
                    textDecoration: 'none',
                  }}
                >
                  {s.label}
                </span>
              </Link>
            </li>
          ))}
        </ul>
      </nav>
      <main style={{ flex: 1, padding: 32 }}>{children}</main>
    </div>
  );
};

export default Layout; 