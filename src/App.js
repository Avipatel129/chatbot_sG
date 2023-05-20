import logo from './logo.svg';
import './App.css';
import {useState , useEffect , useRef} from 'react'
import axios from 'axios';

function App() {

  const log = console.log
  
  const [inputField , setInputField] = useState("")

  const [response , setResponse] = useState("")
  
  const [ history , setHistory] = useState([])

  const sendInput = async (value) => {
    const response = await fetch('http://localhost:5000/input', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({value : value}),
    });

    if (response.ok) {
      const responseData = await response.json();
      console.log(responseData);
    } else {
      throw new Error('Request failed with status ' + response.status);
    }
  }
  
  return (
    <div className="App">
      <input type="text"
        onChange={(e) => {setInputField(e.target.value)}}
      />
      <button onClick={() => {sendInput(inputField)}}>send</button>
    </div>
  );
}

export default App;
