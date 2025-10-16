const API_URL = 'http://localhost:5000';

export const apiCall = async (endpoint, options = {}) => {
  const url = `${API_URL}${endpoint}`;
  const response = await fetch(url, {
    headers: {
      'Content-Type': 'application/json',
      ...options.headers
    },
    ...options
  });
  
  if (!response.ok) throw new Error('API call failed');
  return response.json();
};

export const login = (credentials) => 
  apiCall('/auth/login', {
    method: 'POST',
    body: JSON.stringify(credentials)
  });

export const getStudents = () => 
  apiCall('/students');