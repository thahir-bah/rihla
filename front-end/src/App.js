import './App.css'
import React from 'react';
import { Provider } from 'react-redux';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { createBrowserHistory } from 'history';

import store from './store';
import Navbar from './components/navbar/Navbar';
import Login from './components/users/Login';
import Singup from './components/users/Singup';
import PrivateRoute from './components/common/PrivateRoute';
import { loadUser } from './actions/auth'
import { trackUserEvent } from './actions/actions';


import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Home from './pages/home/Home';
import Dashboard from './pages/dashboard/Dashboard';
import Blogs from './pages/blogs/Blogs';
import Article from './pages/blogs/Article';
import Footer from './components/footer/Footer';
import NotFound from './pages/notFound/NotFound';
import Trips from './pages/tripPlanning/Trips';
import Profile from './components/users/profile/Profile';


const history = createBrowserHistory();


class App extends React.Component {

  componentDidMount() {
    store.dispatch(loadUser());

    // Track initial page load
    store.dispatch(trackUserEvent('page_load', window.location.pathname));

    // Track navigation events
    this.unlisten = history.listen((location, action) => {
      store.dispatch(trackUserEvent('navigation', location.pathname));
    });

    this.getUserLocation();

  }

  componentWillUnmount() {
    if (this.unlisten) {
      this.unlisten();
    }
  }

  getUserLocation = () => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition((position) => {
        const { latitude, longitude } = position.coords;
        localStorage.setItem('userLocation', JSON.stringify({ latitude, longitude }));
        this.getCountryFromCoordinates(latitude, longitude);
      }, (error) => {
        console.error("Error getting location: ", error);
      });
    } else {
      console.error("Geolocation is not supported by this browser.");
    }
  };
  

  getCountryFromCoordinates = async (latitude, longitude) => {
    const apiKey = 'a0082460675647d6bf29aadfe752ac6f';  
    const url = `https://api.opencagedata.com/geocode/v1/json?q=${latitude}+${longitude}&key=${apiKey}&language=en`;
  
    try {
      const response = await fetch(url);
      const data = await response.json();
      const country = data.results[0].components.country;
      localStorage.setItem('userCountry', country);
      console.log(`User is located in: ${country}`);
    } catch (error) {
      console.error("Error fetching country information: ", error);
    }
  };
  

  render() {
    return (
      <Provider store={store}>
        <Router>
          <Navbar/>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/dashboard/*" element={<Dashboard />} />
            <Route path="/blog" element={<Blogs/>} />
            <Route path="/blog/:blogId" element={<Article />} />
            <Route path="/travel" element={
              <PrivateRoute>
                <Trips />
              </PrivateRoute>
            } />
            <Route path="/profile" element={<Profile/>}/>
            {/* <Route path="/profile" element={
              <PrivateRoute>
                <Profile />
              </PrivateRoute>
            } /> */}
            <Route path='/login' Component={Login} />
            <Route path='/register' Component={Singup} />
            <Route path='*' element={<NotFound/>} />
          </Routes>
          <Footer />
        </Router>
        <ToastContainer className="toast-position"
          position="top-center"></ToastContainer>
      </Provider>
    )
  }

}

export default App;
