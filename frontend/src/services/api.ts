import axios from 'axios';

const API_BASE = 'http://localhost:8000';

export const api = axios.create({
  baseURL: API_BASE,
});

// Player APIs
export const getPlayers = () => api.get('/players/');
export const createPlayer = (player: any) => api.post('/players/', player);
export const updatePlayer = (playerName: string, player: any) => api.put(`/players/${encodeURIComponent(playerName)}`, player);
export const getPlayerStats = (name: string) => api.get(`/players/${encodeURIComponent(name)}/stats`);

// Team Balancing
export const balanceTeams = (players: any[]) => api.post('/teams/balance', { players });

// Game APIs
export const recordGame = (game: any) => api.post('/games/', game);
export const getGames = () => api.get('/games/'); 