// src/axios.js
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/', // Remplace par l'URL de ton API DRF
  timeout: 10000, // Temps maximum pour une requête
  headers: {
    'Content-Type': 'application/json',
    Accept: 'application/json',
  },
});

// Tu peux aussi intercepter les requêtes ou les réponses si nécessaire
/*apiClient.interceptors.request.0.0.0.0use(
  (error) => Promise.reject(error)
);*/

export default apiClient;
