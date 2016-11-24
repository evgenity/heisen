import React from 'react';


export default class Filter extends React.Component{
    constructor(props) {
      super(props);
    this.handleChange = this.handleChange.bind(this);
    }
      handleChange(event) {
        // console.log(event.target.value, event.target.checked)
        if (event.target.checked )
        {this.props.addTag(event.target.value);}
        else {this.props.removeTag(event.target.value)}

      }
      render() {
        const {tags} = this.props

        let lambda = this.handleChange;
        return (
        <div className="row team-filter">
          {tags.map(function(filter, i) {
          //   return (<div className='three columns filter'><input className='tag input' type="checkbox" key={i} value={filter} onChange={lambda}/> {filter} </div>)
          return (<div className='three columns filter'>
          <input className='checkbox-custom' type="checkbox" id={filter} name="cc" key={i} value={filter} onChange={lambda}/>
          <label className='checkbox-custom-label' htmlFor={filter}>{filter}</label>
          </div>)
      })}
      </div>

        );
      }

    }
