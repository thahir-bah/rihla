import axios from 'axios';
import { TRACK_USER_EVENT } from './types';
import { host_url } from '../data';
// import { toast } from "react-toastify";

// Autres actions ici...

// track user event
export const trackUserEvent = (eventType, data) => (dispatch, getState) => {
  const body = JSON.stringify({ eventType, data });
  axios.post(`${host_url}/api/useractions/`, body, tokenConfig(getState))
    .then(res => {
      dispatch({
        type: TRACK_USER_EVENT,
        payload: res.data
      });
    })
    .catch(err => console.log(err));
};

// Setup config with token - helper function
export const tokenConfig = (getState) => {
  // Get token from state
  const token = getState().auth.token;

  // Headers
  const config = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  // If token, add to headers config
  if (token) {
    config.headers['Authorization'] = `Token ${token}`;
  }

  return config;
};
