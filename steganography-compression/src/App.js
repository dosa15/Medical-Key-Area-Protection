import { React, Component } from "react";
import { Link } from 'react-router-dom';

class App extends Component {
	render () {
		return(
			<div className="App">
				<ul>
					<li><Link to="/method1">Method1</Link></li>
					<li><Link to="/method2">Method2</Link></li>
				</ul>
			</div>
		);
	}
}

export default App;
