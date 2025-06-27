import React, { useState } from 'react';
import { Layout } from './components/Layout';
import { PlayerList } from './components/PlayerList';
import { TeamBalancer } from './components/TeamBalancer';
import { GameHistory } from './components/GameHistory';
import { PlayerStats } from './components/PlayerStats';

function App() {
  const [section, setSection] = useState('players');

  let content;
  switch (section) {
    case 'players':
      content = <PlayerList />;
      break;
    case 'teams':
      content = <TeamBalancer />;
      break;
    case 'games':
      content = <GameHistory />;
      break;
    case 'stats':
      content = <PlayerStats />;
      break;
    default:
      content = <PlayerList />;
  }

  return (
    <Layout setSection={setSection} section={section}>
      {content}
    </Layout>
  );
}

export default App;
