import React, { useState } from 'react';
// import axios from 'axios';

function VSL() {
  const [text, setText] = useState('');
  // const [background, setBackground] = useState('office'); // Default background
  const [font, setFont] = useState('arial');
  const [videoUrl, setVideoUrl] = useState('');

  const handleTextChange = (e) => {
    setText(e.target.value);
  };

  const generateVideo = async () => {
    try {
      const response = await fetch('http://localhost:5000/generate-video', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });

      if (response.status === 200) {
        const data = response.data;
        setVideoUrl(data.video_file);
      } else {
        console.error('Failed to generate video');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };
  // const handleBackgroundChange = (e) => {
  //   setBackground(e.target.value);
  // };
  // const handleFontChange = (e) => {
  //   setFont(e.target.value);
  // };

  return (
    <div>
      <textarea
        rows="4"
        cols="50"
        value={text}
        onChange={handleTextChange}
        placeholder="Enter your text here..."
      />
      {/* <label>
        Select Background:
        <select value={background} onChange={handleBackgroundChange}>
          <option value="office">Office</option>
          <option value="field">Field</option>
        </select>
      </label> */}
      {/* <label>
        Select Font:
        <select value={font} onChange={handleFontChange}>
          <option value="arial">Arial</option>
          <option value="times_new_roman">Times New Roman</option>
        </select>
      </label> */}
      <button onClick={generateVideo}>Generate Video</button>
      {videoUrl && (
        <video width="320" height="240" controls>
          <source src={videoUrl} type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      )}
    </div>
  );
}

export default VSL;
