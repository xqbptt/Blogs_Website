import "./App.css";
import Home from "./Home";
import NavigationBar from "./Navbar";
import { BrowserRouter as Router,Route, Switch} from 'react-router-dom';
import Communities from "./Communities";
import Timelines from "./Timelines";
import Explore from "./Explore";
import Channels from "./Channels";
import Bookmarks from "./Bookmarks";
import { Container } from "@material-ui/core";
import Login from "./Login";
import Logout from "./Logout";
import SignIn from "./components/auth/login";

function App() {
  return (
    <Router> 
    <div className="App">
      
      <div style={{width:"300px", height:"700px", position:"fixed", top:"0", left:"0"}}>
      <SignIn />
      <NavigationBar />
      
      <Logout />

      </div>
      
      <div className="content">
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/communities">
            <Communities />
          </Route>
          <Route path="/explore">
            <Explore />
          </Route>
          <Route path="/channels">
            <Channels />
          </Route>
          <Route path="/timelines">
            <Timelines />
          </Route>
          <Route path="/bookmarks">
            <Bookmarks />
          </Route>
        </Switch>
      </div>
      
    </div>
    </Router>
  );
}

export default App;