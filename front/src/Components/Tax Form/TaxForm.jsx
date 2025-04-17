import React from 'react'
import { useState } from "react";
import './TaxForm.css'
import axios from 'axios'
//import 'semantic-ui-css/semantic.min.css'
//import { Container, Header, Divider } from 'semantic-ui-react'

const TaxForm = () => {
  /*const fetchFuntion = async () => {
    //const url = "/"
    const url = '/http://localhost:8000/form'
    const response = await axios.get(url)
    console.log(response)
    return response.data
  }*/

  const [inputs, setInputs] = useState({});
  //const [action, setAction] = useState({});

  /*const handleDelete = () => {
    //axios.delete('http://localhost:8000/form/deloitte', {data:{company:inputs.company, revenue:inputs.revenue, costs:inputs.costs}, headers:{Authorization: "token"}})
    //axios.delete('http://localhost:8000/form/', inputs.company);
    axios.delete('http://localhost:8000/form/deloitte');
    }*/

    async function getData() {
      try {
        const response = await axios.get('http://localhost:8000/form');
        console.log(response.data);
      } catch (error) {
        console.error(error);
      }
    }

    const handleClick = () => {
    /*const oldForm = {
        company: inputs.company,
        revenue: inputs.revenue,
        costs: inputs.costs,
    }*/
    axios.delete('http://localhost:8000/form');
  }

  const handleChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setInputs(values => ({...values, [name]: value}))
  }

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(inputs);
    const newForm = {
        company: inputs.company,
        revenue: inputs.revenue,
        costs: inputs.costs,
    }
    axios.post('http://localhost:8000/form/', newForm);
    /*alert(`Company: ${inputs.company}, Revenue: ${inputs.revenue}, Costs: ${inputs.costs}`
    );*/
  }

  return (
    <div className='container'>
        <div className='header'>
            <div className='text'>Tax Form</div>
            <div className='underline'> </div>
        </div>
        <div className='inputs'>
            <form onSubmit={handleSubmit}>
                <div class='form-table'>
                    <label for='company'>Company name</label>
                    <input type='text' id='company' name='company' 
                    value={inputs.company || ""} 
                    onChange={handleChange}/>
                </div>
                <div class='form-table'>
                    <label for='revenue'>Revenue</label>
                    <input type='number' id='revenue' name='revenue' 
                    value={inputs.revenue || ""} 
                    onChange={handleChange}/>
                </div>
                <div class='form-table'>
                    <label for='costs'>Costs</label>
                    <input type='number' id='costs' name='costs' 
                    value={inputs.costs || ""} 
                    onChange={handleChange}/>
                </div>
                <div class='form-table'>
                    <input type="submit"/>
                </div>
            </form>
        </div>
        <div className='button-container'>
        <noscript class="comment">axios get tester button</noscript>
          <div className='button' onClick={getData}>Get
          </div>
          <noscript class="comment">axios delete tester button</noscript>
          <div className='button' onClick={handleClick}>Delete
          </div>
        </div>
    </div>
  )
}

export default TaxForm
