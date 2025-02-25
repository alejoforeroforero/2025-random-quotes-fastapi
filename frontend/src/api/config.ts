import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'https://quotesfastapi.alejoforero.com/api';
console.log(import.meta.env);
console.log('API Base URL:', API_URL);



const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;
