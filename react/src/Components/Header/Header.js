import styles from "./Header.module.css"
import {useState} from "react";
import axios from 'axios';

export default function Header({setData}) {
  const [query, setQuery] = useState("");
  const [form, setForm] = useState(false)

  const sendQuery = async (query) => {
    try {
      const response = await axios.post(`${process.env.REACT_APP_BACKEND_URL}/search`, {
        query: query
      });
      setData(response)  
    } catch (error) {
      console.log(error.response.data.message);
    }
  }

  return (
    <header>
        <div>
            <h1>zero</h1>
        </div>
        <div>
            <input type="search" placeholder="Search"
              onChange={(e)=>{
                setQuery(e.target.value);
              }}
              onKeyDown={(e)=>{
                if (e.key === "Enter") {
                  sendQuery(query);
                }
              }}
              />
        </div>        
        <div>
            <button onClick={() => {
              setForm(true);
            }}>+</button>
        </div>
        
    </header>
  )
}
