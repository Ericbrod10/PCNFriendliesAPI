import axios from 'axios';
import React, { useState } from 'react';

function CreateMyModelForm() {
  const [formData, setFormData] = useState({
    player_name: '',
    team_name: '',
    team_league: '',
    player_numb: '',
    match_pref: '',
    player_pref: '',
    ip: '',
    device_info: ''
  });

  const handleSubmit = event => {
    event.preventDefault();
    axios.post('http://localhost:8000/api/myendpoint/', formData)
      .then(response => {
        console.log(response.data);
        console.log(response.status);
        //redirect to the new page
        //window.location.href = "http://localhost:8000/api/myendpoint/"; //This line of code will redirect you once the submission is succeed


        // Add any success message or redirect here
      })
      .catch(error => {
        console.log(error);
        // Add any error message or handling here
      });
  };

  const handleChange = event => {
    setFormData({
      ...formData,
      [event.target.name]: event.target.value
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Player Name:
        <input type="text" name="player_name" value={formData.player_name} onChange={handleChange} />
      </label>
      <br />
      <label>
        Team Name:
        <input type="text" name="team_name" value={formData.team_name} onChange={handleChange} />
      </label>
      <br />
      <label>
        Team League:
        <input type="text" name="team_league" value={formData.team_league} onChange={handleChange} />
      </label>
      <br />
      <label>
        Player Number:
        <input type="text" name="player_numb" value={formData.player_numb} onChange={handleChange} />
      </label>
      <br />
      <label>
        Match Preference:
        <input type="text" name="match_pref" value={formData.match_pref} onChange={handleChange} />
      </label>
      <br />
      <label>
        Player Preference:
        <input type="text" name="player_pref" value={formData.player_pref} onChange={handleChange} />
      </label>
      <br />
      <label>
        IP:
        <input type="text" name="ip" value={formData.ip} onChange={handleChange} />
      </label>
      <br />
      <label>
        Device Info:
        <input type="text" name="device_info" value={formData.device_info} onChange={handleChange} />
      </label>
      <br />
      
      <button type="submit">Submit</button>
    </form>
  );
}

export default CreateMyModelForm;