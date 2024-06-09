// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import GoogleAuth from './components/GoogleAuth';
import MicrosoftAuth from './components/MicrosoftAuth';
function App() {
    return (
        <Router>
            <Switch>
                <Route path="/auth/google" component={GoogleAuth} />
                <Route path="/auth/microsoft" component={MicrosoftAuth} />
            </Switch>
        </Router>
    );
}
// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import GoogleAuth from './components/GoogleAuth';
import MicrosoftAuth from './components/MicrosoftAuth';
import MergedData from './components/MergedData';
function App() {
    return (
        <Router>
            <Switch>
                <Route path="/auth/google" component={GoogleAuth} />
                <Route path="/auth/microsoft" component={MicrosoftAuth} />
                <Route path="/merge" component={MergedData} />
            </Switch>
        </Router>
    );
}
export default App;
export default App;
const express = require('express');
const app = express();
app.listen(3000, () => {
  console.log('Server started on port 3000');
});