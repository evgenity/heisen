import {
  REMOVE_TAG,
  ADD_TAG,
  GET_FILTER
} from '../constants/Filter'


export function addTag(tag) {
  return {
      type: ADD_TAG,
      payload: tag
    }
}

export function removeTag(tag) {
  return {
      type: REMOVE_TAG,
      payload: tag
    }
}
