import React, { useState, useEffect, useReducer  } from 'react';
import axios from 'axios';
import Fingerprint2 from 'fingerprintjs2';
import { SHA256 } from 'crypto-js';
import './styles.css';

function CreateMyModelForm() {
  const [formData, setFormData] = useState({
    player_name: '',
    team_name: '',
    team_league: '',
    player_numb: '',
    match_pref: 'Any',
    player_pref: 'Any',
    ip: '',
    device_info: '',
  });

  const [showForm, setShowForm] = useState(true);
  const [InQueue, setInQueue] = useState(false);
  const [showmatched, setmatched] = useState(false);
  const [uniqueIdentifier, setUniqueIdentifier] = useState('');
  const [openCount, setOpenCount] = useState(0);
  // eslint-disable-next-line
  const [player_name, setPlayerName] = useState('');
  const [team_name, setTeamName] = useState('');
  const [team_league, setTeamLeague] = useState('');
  // eslint-disable-next-line
  const [player_numb, setPlayerNumb] = useState('');
  const [match_pref, setMatchPref] = useState('');
  const [player_pref, setPlayerPref] = useState('');
  // eslint-disable-next-line
  const [open_or_close, setOpenOrClosed] = useState('');
  const [opponent_manager, setopponent_manager] = useState('');
  const [opponent_team, setopponent_team ] = useState('');
  const [send_v_receive, setopponent_send_v_receive] = useState('');
  const [errors, setErrors] = useState({});
  
  
  const [elapsedTime, dispatch] = useReducer((state, action) => {
    switch (action.type) {
      case 'reset':
        return 0;
      case 'tick':
        return state + 1;
      default:
        return state;
    }
  }, 0);



  const handleChange = (event) => {
    setFormData({
      ...formData,
      [event.target.name]: event.target.value,
    });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://192.168.1.243:8000/api/myendpoint/', formData);
      console.log(response.data);
      console.log(response.data.success);
      if (response.data.success === true) {
      setShowForm(false); // Hide the form
      setInQueue(true); // Show the timer
      setUniqueIdentifier(response.data.Unique_Identifier);
      console.log(response.data.Unique_Identifier); // Set the unique identifier
    } else setErrors(response.data.message);
  } catch (error) {
      console.error(error);
    }
  };

  const handleLeaveQueue = () => {
    axios.put(`http://192.168.1.243:8000/api/myendpoint/${uniqueIdentifier}/close/`)
      .then(response => {
        console.log(response.data);
        setInQueue(false);
        setShowForm(true);
        setPlayerName('');
        setTeamName('');
        setTeamLeague('');
        setPlayerNumb('');
        setMatchPref('Any');
        setPlayerPref('Any');
        setOpenCount(0);        
        dispatch({ type: 'reset' });


      })
      .catch(error => {
        console.log(error);
      });
  };

  useEffect(() => {

    if (showForm) {
      Fingerprint2.get(function(result, components) {
        const hashedFingerprint = SHA256(result).toString();
        formData.device_info = {
          fingerprint: hashedFingerprint,
          components: components
        };
        formData.device_info = formData.device_info.fingerprint.toString();
      });

      axios.get('https://api.ipify.org?format=json')
      .then(response => {
        formData.ip = response.data.ip;
      })
      .catch(error => {
        console.error(error);
      });
      const fetchData = async () => {
        try {
          const response = await axios.get('http://192.168.1.243:8000/api/opencount/');
          setOpenCount(response.data.count); // Set the open count
        } catch (error) {
          console.error(error);
        }
      };
      fetchData();
      
      
    }
  
    if (InQueue) {
      const fetchData = async () => {
        try {
          const response1 = await axios.get(`http://192.168.1.243:8000/api/myendpoint/${uniqueIdentifier}/`);
          console.log(response1.data);
          // Set each field to variable 
          // eslint-disable-next-line
          setPlayerName(response1.data.player_name); 
          setTeamName(response1.data.team_name);
          setTeamLeague(response1.data.team_league);
          // eslint-disable-next-line
          setPlayerNumb(response1.data.player_numb);
          setMatchPref(response1.data.match_pref);
          setPlayerPref(response1.data.player_pref);
          // eslint-disable-next-line
          setOpenOrClosed(response1.data.open_or_close);
          // if response1.data.Opponent_Unique_Identifier is not null, then state = 'MatchedScreen'
          
          if (response1.data.opponent_team != null) {
            setInQueue(false);
            setmatched(true);
            setopponent_manager(response1.data.opponent_manager);
            setopponent_team(response1.data.opponent_team);
            setopponent_send_v_receive(response1.data.send_v_receive);

          }

          // Do something with the response data
        } catch (error) {
          console.error(error);
        }
        try {
          const response2 = await axios.get('http://192.168.1.243:8000/api/opencount/');
          console.log(response2.data);
          setOpenCount(response2.data.count); // Set the open count
        } catch (error) {
          console.error(error);
        }
      };
  
      fetchData();
      const interval = setInterval(() => {
        fetchData();
      }, 7500);
      const interval2 = setInterval(() => {
        dispatch({ type: 'tick' });
      }, 1000);
      // eslint-disable-next-line
      return () => {      
        clearInterval(interval);
        clearInterval(interval2);
      };
    }
    
    // eslint-disable-next-line
  }, [InQueue, uniqueIdentifier, dispatch]);
  
  
  const minutes = Math.floor(elapsedTime / 60);
  const seconds = elapsedTime % 60

  return (
    
<div>

    
<div className="header-mobile clearfix" id="header-mobile">
      <div className="header-mobile__logo">
        <a href="https://proclubsnation.com/" rel="home">
          <img src="https://proclubsnation.com/wp-content/uploads/2020/08/PCN_logo_Best.png" className="header-logo__img" alt="Pro Clubs Nation" />
        </a>
      </div>
    </div>

<div className="center2" style={{ textAlign: 'left', margin: 'auto', marginLeft: '20px'}}>
<h3>Pro Clubs Nation's Friendly Queue </h3>

{showForm && (
  <form onSubmit={handleSubmit}>
    <h4>Please fill out the information below to sign up for the queue:</h4>
    <label>
      Player Name:
      <br />
      <input type="text" name="player_name" value={formData.player_name} onChange={handleChange} />
      {errors.player_name && <span style={{ color: 'red' }}>{errors.player_name}</span>}
    </label>
    <br />
    <label>
      Team Name (Exactly as it appears in-game):
      <br />
      <input type="text" name="team_name" value={formData.team_name} onChange={handleChange} />
      {errors.team_name && <span style={{ color: 'red' }}>{errors.team_name}</span>}
    </label>

    <br />
    <label>
      <select name="team_league" value={formData.team_league} onChange={handleChange}>
        <option value="">Select your League</option>
        <option value="SL">Super League</option>
        <option value="L1">League 1</option>
      </select>
      {errors.team_league && <span style={{ color: 'red' }}>{errors.team_league}</span>}
    </label>

    <label>
      <select name="player_numb" value={formData.player_numb} onChange={handleChange}>
        <option value="">Select your # of Players</option>
        <option value="Full">Full 11</option>
        <option value="10GK">10 with a GK</option>
        <option value="10NoGK">10 without a GK</option>
        <option value="Less10">Less than 10</option>
      </select>
      {errors.player_numb && <span style={{ color: 'red' }}>{errors.player_numb}</span>}
    </label>
    <br />
    <br />
    <b>Queue Preferences:</b>
    <br />
    <label>
      <label>
  <input type="radio" name="match_pref" value="Any" checked={formData.match_pref === 'Any'|| formData.match_pref === ''} onChange={handleChange} />
  Match to Teams in any League<br />
</label>
<label>
  <input type="radio" name="match_pref" value="Match" checked={formData.match_pref === 'Match'} onChange={handleChange} />
   Only Match Teams in Current League<br /> &nbsp;&nbsp;&nbsp;&nbsp; - <b>May increase wait times</b>  <br /> 
</label>
      <br />
    </label>
    <label>
      <label>
        <input type="radio" name="player_pref" value="Any" checked={formData.player_pref === 'Any'|| formData.match_pref === ''} onChange={handleChange} />
        Match Teams with any # of Players
        <br />
      </label>
      <label>
        <input type="radio" name="player_pref" value="Match" checked={formData.player_pref === 'Match'} onChange={handleChange} />
        Only Match Teams with the Same # of Players <br /> &nbsp;&nbsp;&nbsp;&nbsp; - <b>May increase wait times</b> < br />
      </label>
    </label>
    <p>Current Number of Teams waiting in queue: <b>{openCount}</b></p>
    
    <button type="submit" className ="btn btn-success" style={{ backgroundColor: 'green', fontSize: '20px', color: 'white', fontWeight: 'bold', padding: '10px 20px' }}>Submit</button>
  </form>
)}
      {InQueue && (
        <div>
          <p><b>Elapsed Time: </b>{minutes}:{seconds < 10 ? `0${seconds}` : seconds}</p>
          <p>Team Name: {team_name}</p>
          <p>Team League: {team_league}</p>
          <p>Match Preference: {match_pref}</p>
          <p>Player Preference: {player_pref}</p>
          <p>Number of teams in queue: {openCount}</p>
          <button style={{ backgroundColor: 'red', color: 'white', padding: '10px 20px', fontWeight: 'bold' }} onClick={handleLeaveQueue}>Leave Queue</button>
          <p style={{ color: 'red' }}><b>Note:</b> If you find a match outside of the queue please Leave Queue ASAP, repeated failure to so may result in league punishments.</p>
        </div>
      )}
      {showmatched && (
        <div>
          <p style={{ fontSize: '20px' }}><b>Match Found!</b></p>
          {send_v_receive === 'Send' && (
        <p><b>Send</b> a friendly invite to: <b>{opponent_team}</b></p>
      )}
      {send_v_receive === 'Receive' && (
        <p><b>Accept</b> a friendly invite from: <b>{opponent_team}</b></p>
      )}
          <p>The other manager is: <b>{opponent_manager}</b></p>
          <p>Reach out to the other manager if there are any issues accepting or sending.</p>

    </div>
      )}
    </div>
    </div>
  );
}

export default CreateMyModelForm;