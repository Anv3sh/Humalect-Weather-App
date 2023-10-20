import React from 'react';

const getWeatherIconUrl = (weatherIcon) => {
    const baseUrl = 'https://www.accuweather.com/images/weathericons/';
    let iconName;
  
    switch (weatherIcon) {
      case 1:
      case 2:
      case 3:
        iconName = '01';
        break;
      case 4:
      case 5:
        iconName = '02';
        break;
      case 6:
      case 7:
        iconName = '03';
        break;
      case 8:
      case 9:
        iconName = '04';
        break;
      case 10:
      case 11:
        iconName = '05';
        break;
      case 12:
      case 13:
      case 14:
      case 15:
      case 16:
        iconName = '06';
        break;
      case 17:
      case 18:
        iconName = '07';
        break;
      case 19:
        iconName = '08';
        break;
      case 20:
      case 21:
        iconName = '09';
        break;
      case 22:
        iconName = '10';
        break;
      case 23:
      case 24:
        iconName = '11';
        break;
      case 25:
      case 26:
      case 29:
      case 30:
        iconName = '12';
        break;
      case 27:
      case 28:
      case 31:
      case 32:
      case 33:
      case 34:
        iconName = '13';
        break;
      case 35:
        iconName = '14';
        break;
      case 36:
        iconName = '15';
        break;
      case 37:
        iconName = '16';
        break;
      case 38:
      case 39:
      case 40:
      case 41:
      case 42:
        iconName = '17';
        break;
      case 43:
      case 44:
        iconName = '18';
        break;
      default:
        iconName = '01';
    }
  
    return `${baseUrl}${iconName}.svg`;
  };
  
export const WeatherIcon = ({ weatherIcon }) => {
  const iconUrl = getWeatherIconUrl(weatherIcon);

  return <img src={iconUrl} alt="Weather Icon" />;
};
