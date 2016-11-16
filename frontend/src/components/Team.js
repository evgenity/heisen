import React, {Component } from 'react'

class Person extends Component{
    render() {
        return (
          <div className='two columns member'>
            <a href={this.props.url}>
              <img className='u-max-full-width avatar' src={this.props.slack_avatar} /> </a>
            <p className='first_name'> {this.props.first_name} </p>
          </div>
        );
    }
}


export default class Team extends Component {
    componentDidMount(){
        // var url = 'http://127.0.0.1:8000/team/filter';
        //superagent
    }
    team_filter(team, filter){
    return (team.filter(
        function(person){
          for(var skill in filter){
            if (person.skills.indexOf(filter[skill])<=-1) return false;}
              return true;
          }
    ))
    }
    render() {
        const { team, filter } = this.props
        var team_list = this.team_filter(team,filter).map(function(p, i){
            return <Person first_name={p.name} url={p.url} slack_avatar={p.avatar} key={i}/>
        });
        return (
              <div className='row names-team'>
                  {team_list.length > 0 ? team_list : <p>Нет людей, удовлетворяющих данному запросу.</p>}
              </div>
        );
    }
}
