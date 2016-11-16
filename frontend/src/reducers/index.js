import { combineReducers } from 'redux'
import filter from './filter'
import team  from './team'
import tags  from './tags'

export default combineReducers({
  filter,
  tags,
  team,
})
