import React, { Component } from 'react'
import { bindActionCreators } from 'redux'
import { connect } from 'react-redux'
import Team from '../components/Team.js'
import Filter from '../components/Filter.js'
import * as teamActions from '../actions/TeamActions'
import * as filterActions from '../actions/FilterActions'
import * as tagsActions from '../actions/TagsActions'

// require("../styles/App.css")
import request from 'superagent'

class App extends Component {
  componentDidMount(){
      // var url = 'http://127.0.0.1:8000/team/filter';
      //superagent
      const { setTeam } = this.props.teamActions
      const {setTags} = this.props.tagsActions
      const { team,tags} = this.props
      request.get('/team/filter').end(function(err, res){
          var t = JSON.parse(res.text)
          setTeam(t)
      });
      request.get('/team/tags').end(function(err, res){
          var t = JSON.parse(res.text)
          setTags(t)
      });
      console.log(team, tags)

  }
  render() {
    const { team, filter, tags } = this.props
    const { setTeam } = this.props.teamActions
    const { addTag, removeTag } = this.props.filterActions
    const { setTags } = this.props.tagsActions
    return <div className='row'>
      <Filter filter={filter.filter} tags={tags.tags} addTag={addTag} removeTag={removeTag} />
      <Team team={team.team} filter={filter.filter} setTeam={setTeam} />
    </div>
  }
}

function mapStateToProps(state) {
  return {
    team: state.team,
    filter: state.filter,
    tags: state.tags
  }
}

function mapDispatchToProps(dispatch) {
  return {
    filterActions: bindActionCreators(filterActions, dispatch),
    teamActions: bindActionCreators(teamActions, dispatch),
    tagsActions: bindActionCreators(tagsActions, dispatch)

  }
}

export default connect(mapStateToProps, mapDispatchToProps)(App)
