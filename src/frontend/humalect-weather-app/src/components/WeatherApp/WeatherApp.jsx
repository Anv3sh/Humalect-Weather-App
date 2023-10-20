import React, { useState } from 'react';
import './WeatherApp.css'
import search_icon from '../../assets/search.png';
import clear_icon from '../../assets/clear.png';
import cloud_icon from '../../assets/cloud.png';
import drizzle_icon from '../../assets/drizzle.png';
import humidity_icon from '../../assets/humidity.png';
import rain_icon from '../../assets/rain.png';
import snow_icon from '../../assets/snow.png';
import wind_icon from '../../assets/wind.png';
// import { TemperatureGraph } from '../TemperatureGraph/TemperatureGraph';

const API_ENDPOINT = import.meta.env.VITE_REACT_APP_BACKEND_API_ENDPOINT
const icons = {"clear":clear_icon,"drizzle":drizzle_icon,"rain":rain_icon,"snow":snow_icon,"cloud":cloud_icon}

export const WeatherApp = () => {
    const [forecastData, setForecastData] = useState(null);

    const search = async () =>{
        // city to be searched
        const element = document.getElementsByClassName("cityInput")
        if(element[0].value==="")
        {
            return 0;
        }
        let city_name = element[0].value
        let url = API_ENDPOINT+`/weather/${city_name}`
        console.log(url)
        const response = await fetch(url);
        const data = await response.json();
        console.log(data)
        if (response.status !== 200) {
            console.error('Error fetching weather data:', response.status);
            // Handle the error, return an error message, or show a user-friendly error.
            return 0;
          }
        // console.log(response.status, data.title);
        // const sessionValue = sessionStorage.getItem('key');
        console.log(data)
        setForecastData(data.body.forecast_data)
        const humidity = document.getElementsByClassName("humidity-percentage")
        const wind = document.getElementsByClassName("wind-speed")
        const temprature = document.getElementsByClassName("weather-temp")
        const location = document.getElementsByClassName("weather-location")
        const icons = document.getElementsByClassName("icon")
        // console.log(data.body.data.)
        location[0].innerHTML = data.body.name
        temprature[0].innerHTML = data.body.data.Temperature.Metric.Value+" °C"
        wind[0].innerHTML = data.body.data.Wind.Speed.Metric.Value+" km/h"
        humidity[0].innerHTML = data.body.data.RelativeHumidity+" %"
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
        <div className="chart">
        {/* {forecastData ? (
        <TemperatureGraph data={forecastData} />
      ) : (
        <p>Loading forecast data...</p>
      )} */}
        </div>
    </div>
  )
}
