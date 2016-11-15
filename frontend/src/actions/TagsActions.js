import {
  SET_TAGS
} from '../constants/Tags'


export function setTags(taglist) {
  return {
      type: SET_TAGS,
      payload: taglist
    }
}
