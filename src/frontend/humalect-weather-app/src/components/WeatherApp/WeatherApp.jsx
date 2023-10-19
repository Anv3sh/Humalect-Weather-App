import React from 'react'
import './WeatherApp.css'
import search_icon from '../../assets/search.png';
import clear_icon from '../../assets/clear.png';
import cloud_icon from '../../assets/cloud.png';
import drizzle_icon from '../../assets/drizzle.png';
import humidity_icon from '../../assets/humidity.png';
import rain_icon from '../../assets/rain.png';
import snow_icon from '../../assets/snow.png';
import wind_icon from '../../assets/wind.png';

const API_ENPOINT = import.meta.env.REACT_APP_BACKEND_API_ENDPOINT

export const WeatherApp = () => {

    const search = async () =>{
        // city to be searched
        const element = document.getElementsByClassName("cityInput")
        if(element[0].value==="")
        {
            return 0;
        }
        let city_name = element[0].value
        let url = API_ENPOINT+`/weather/${city_name}`
        const response = await fetch(url);
        const data = await response.json();
        console.log(response.status, data.title);
        // const sessionValue = sessionStorage.getItem('key');
        console.log("hello");
        console.log(data)
        // const humidity = document.getElementsByClassName("humidity-percentage")
        // const wind = document.getElementsByClassName("wind-speed")
        // const temprature = document.getElementsByClassName("weather-temp")
        // const location = document.getElementsByClassName("weather-location")

        // humidity[0].innerHTML
    }
  return (
    <div className='container'>
        <div className="top-bar">
            <input type='text' className='cityInput' placeholder='Search'/>
            <div className="search-icon" onClick={()=>{search()}}>
                <img src={search_icon} alt=''/>
            </div>
        </div>
        <div className="weather-image">
            <img src={cloud_icon} alt=''/>
        </div>
        <div className="weather-temp">24C</div>
        <div className="weather-location">London</div>
        <div className="data-container">
            <div className="element">
                <img src="" alt="" className="icon" />
                <div className="data">
                    <div className="humidity-percentage">64</div>
                    <div className='text'>Humidity</div>
                </div>
            </div>
            <div className="element">
                <img src={humidity_icon} alt="" className="icon" />
                <div className="data">
                    <div className="humidity-percentage">64</div>
                    <div className='text'>Humidity</div>
                </div>
            </div>
            <div className="element">
                <img src={wind_icon} alt="" className="icon" />
                <div className="data">
                    <div className="wind-speed">18 Km/h</div>
                    <div className='text'>Wind Speed</div>
                </div>
            </div>
        </div>
    </div>
  )
}
