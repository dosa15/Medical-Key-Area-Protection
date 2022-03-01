import React, { Component, useState, useCallback, useEffect } from "react";
import 'bootstrap/dist/css/bootstrap.css';

import script from '../python/method1.py';
import PDFViewer from "pdf-viewer-reactjs";

// Core PDF viewer
import { Viewer } from '@react-pdf-viewer/core';

// Plugins
import { defaultLayoutPlugin } from '@react-pdf-viewer/default-layout';

// Import styles
import '@react-pdf-viewer/core/lib/styles/index.css';
import '@react-pdf-viewer/default-layout/lib/styles/index.css';

import { Worker } from '@react-pdf-viewer/core';

const runScript = async (code) => {
    const pyodide = await window.loadPyodide({
      indexURL : "https://cdn.jsdelivr.net/pyodide/v0.18.1/full/"
    });
  
    return await pyodide.runPythonAsync(code);
}

const Method1 = () => {

    const [output, setOutput] = useState("(loading...)");
    // const [image, setImageURL] = useState('');
    const [PDFFile, setPDFFile] = useState(null);
    const [PDFFileError, setPDFFileError] = useState('');
    const [viewPDFFile, setViewPDFFile] = useState(null);

    const defaultLayoutPluginInstance = defaultLayoutPlugin();

    const fileType = ['application/pdf'];
    const onPDFFileChange = (event) => {
            if (event.target.files && event.target.files[0]) {
                let pdf = event.target.files[0];
                if (fileType.includes(pdf.type)) {
                    let reader = new FileReader();
                    reader.readAsDataURL(pdf);
                        reader.onloadend = (e) => {
                            setPDFFile(e.target.result);
                            setPDFFileError('');
                        }
                }
            } else {
                    setPDFFile(null);
                    setPDFFileError("Please select a valid PDF file");
            }
    };

    const handlePDFFileSubmit = (event) => {
        event.preventDefault();
        if(PDFFile !== null) {
            setViewPDFFile(PDFFile);
        } else {
            setViewPDFFile(null);
        }
    };

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
            <div className="container ">
                <div>
                {/* <img src={image} /> */}
                    <h2>Select PDF</h2>
                    <form className="form-group" onSubmit={handlePDFFileSubmit}>
                        <input type="file" name="userDocument" className="form-control" onChange={onPDFFileChange} />
                        {PDFFileError && <div className="error-message">{PDFFileError}</div>}
                        <div className="my-3"></div>
                        <button type="submit" className="btn btn-success btn-lg">UPLOAD</button>
                    </form>
                </div>
                <br />
                {/* <div className="" style={{border: '1px solid black'}}>
                    {output}
                </div> */}
                <div className="pdf-container">
                    {
                        viewPDFFile && <>
                            <Worker workerUrl="https://unpkg.com/pdfjs-dist@2.12.313/build/pdf.worker.min.js">
                                <Viewer fileUrl={viewPDFFile} plugins={[defaultLayoutPluginInstance]} />
                            </Worker>
                        </>
                    }
                    {
                        !viewPDFFile && <>No PDF file selected.</>
                    }
                </div>
            </div>
        </div>
    );
}

export default Method1;