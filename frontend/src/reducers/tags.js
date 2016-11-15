import {
  SET_TAGS
} from '../constants/Tags'

const initialState = {
  tags:[]
}

export default function tags(state = initialState, action) {

  switch (action.type) {
    case SET_TAGS:
      return { ...state, tags: action.payload};

    default:
      return state;
  }

}
