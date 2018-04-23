import React from 'react';
import ReactDOM from 'react-dom';
import { Header } from 'semantic-ui-react';
import registerServiceWorker from './registerServiceWorker';
import 'semantic-ui-css/semantic.min.css';

ReactDOM.render((<Header size="huge">Hello World!</Header>), document.getElementById('root'));
registerServiceWorker();
