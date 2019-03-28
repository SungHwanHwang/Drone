import React, { Component } from 'react';
import ViewerTemplate from './Components/ViewerTemplate';
import ControllSession from './Components/ControllSession';
import StatusViewer from './Components/StatusViewer';
//  import socket from './state/socket';
//  django에 텍스트를 보내기 위한 것
import axios from 'axios';

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

function sendCommand(command) {
  return function() {
    console.log(`Sending the Command ${command}`);
    axios
    .post("/api/flysaying/", { content: command })
    .then(res => this._renderText());
  };
}

const amount = 100;
class App extends Component {
  
  state = {
    textList: [],
  };

  componentDidMount() {
    this._renderText();
  }

  render() {
    const { textList } = this.state;
    console.log(textList);

    return (
      <ViewerTemplate
        controllSession = {(<ControllSession
                              rotate9={sendCommand('ccw 90')}
                              forward={sendCommand(`forward ${amount}`)}
                              rotate5={sendCommand('cw 15')}
                              left={sendCommand(`left ${amount}`)}
                              takeoff={sendCommand('takeoff')}
                              land={sendCommand('land')}
                              emergency={sendCommand('emergency')}
                              right={sendCommand(`right ${amount}`)}
                              up ={sendCommand(`up ${amount}`)}
                              back={sendCommand(`back ${amount}`)}
                              down={sendCommand(`down ${amount}`)}
                              flipL={sendCommand('flip l')}
                              flipR={sendCommand('flip r')}
                            />)}
        statusViewer = {<StatusViewer />}   
        />
    );
  }

  _renderText = () => {
    axios
      .get("/api/flysaying/")
      .then(res => this.setState({ textList: res.data }))
      .catch(err => console.log(err));
  };
}

export default App;
