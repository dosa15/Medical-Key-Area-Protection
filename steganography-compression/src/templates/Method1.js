import { React, Component, useState, useCallback, useEffect } from "react";
import 'bootstrap/dist/css/bootstrap.css';

import script from '../python/method1.py';

const runScript = async (code) => {
    const pyodide = await window.loadPyodide({
      indexURL : "https://cdn.jsdelivr.net/pyodide/v0.18.1/full/"
    });
  
    return await pyodide.runPythonAsync(code);
}

const Method1 = () => {

    const [output, setOutput] = useState("(loading...)");
    const [image, setImageURL] = useState('');

    const onImageChange = useCallback(event => {
        if (event.target.files && event.target.files[0]) {
            let pdf = event.target.files[0];
            // this.setState({
            //     image: URL.createObjectURL(img)
            // });
            setImageURL(URL.createObjectURL(pdf));
        }
    }, []);

    useEffect(() => {
        const run = async () => {
            const scriptText = await (await fetch(script)).text();
            const out = await runScript(scriptText);
            setOutput(out);
        }
        run();
    }, []);
    
    return (
        <div>
            <h1>Method1</h1>
            <div>
                <div>
                <img src={image} />
                <h2>Select Image</h2>
                <input type="file" name="userDocument" onChange={onImageChange} />
                </div>
                <br />
                <div className="" style={{border: '1px solid black'}}>
                    {output}
                </div>
            </div>
        </div>
    );
}

export default Method1;