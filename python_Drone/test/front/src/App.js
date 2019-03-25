import React, { Component } from 'react';
import ViewerTemplate from './Components/ViewerTemplate';
import ControllSession from './Components/ControllSession';
import StatusViewer from './Components/StatusViewer';
import socket from './state/socket';

function sendCommand(command) {
  return function() {
    console.log(`Sending the Command ${command}`);
    socket.emit('command', command);
  };
}
const amount = 100;
class App extends Component {
  render() {
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
}

export default App;
