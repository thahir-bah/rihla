import { TRACK_USER_EVENT } from '../actions/types';

const initialState = {
  // Autres états initiaux...
  userEvents: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    // Autres cas...
    case TRACK_USER_EVENT:
      return {
        ...state,
        userEvents: [...state.userEvents, action.payload]
      };
    default:
      return state;
  }
}
