import styles from "./Header.module.css"
import {useState} from "react";
import axios from 'axios';

export default function Header({setData, setForm}) {
  const [query, setQuery] = useState("");

  const sendQuery = async (query) => {
    try {
      const {data} = await axios.post(`${process.env.REACT_APP_BACKEND_URL}/search`, {
        product: query,
      });
      console.log(data);
      setData(data)  
    } catch (error) {
      console.log(error.response);
    }
  }

  return (
    <header>
        <div>
            <img src="https://i.ibb.co/9yJSrW9/zero-high-resolution-logo-transparent.png"></img>
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
