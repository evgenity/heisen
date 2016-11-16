import {
  REMOVE_TAG,
  ADD_TAG,
  GET_FILTER
} from '../constants/Filter'

const initialState = {
  filter:[]
}

export default function filter(state = initialState, action) {

  switch (action.type) {
    case REMOVE_TAG:
      if (state.filter.indexOf(action.payload)>-1) state.filter.splice(state.filter.indexOf(action.payload), 1)
      return { ...state, filter: state.filter }



    case ADD_TAG:
      //state.filter.push(action.payload)
      state.filter.push(action.payload)
      return { ...state, filter: state.filter }

    case GET_FILTER:
      return { state }

    default:
      return state;
  }

}
