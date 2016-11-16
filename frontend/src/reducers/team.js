import {
  SET_TEAM,
} from '../constants/Team'

const initialState = {
  team:[]
}

export default function team(state = initialState, action) {

  switch (action.type) {
    case SET_TEAM:
      return { ...state, team: action.payload };


    default:
      return state;
  }

}
