import {
  SET_TEAM
} from '../constants/Team'

export function setTeam(teamlist) {
  return {
      type: SET_TEAM,
      payload: teamlist
    }
}
