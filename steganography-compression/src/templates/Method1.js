import { React, Component } from "react";

class Method1 extends Component {
    constructor(props) {
        super(props);
        this.state = {
            image: null
        };
    
        this.onImageChange = this.onImageChange.bind(this);
    }
  
    onImageChange = event => {
        if (event.target.files && event.target.files[0]) {
            let img = event.target.files[0];
            this.setState({
                image: URL.createObjectURL(img)
            });
        }
    };
  
    render() {
        return (
            <div>
                <h1>Method1</h1>
                <div>
                    <div>
                    <img src={this.state.image} />
                    <h2>Select Image</h2>
                    <input type="file" name="myImage" onChange={this.onImageChange} />
                    </div>
                </div>
            </div>
        );
    }
}

export default Method1;