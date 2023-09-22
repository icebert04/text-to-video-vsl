import React, { useState } from 'react';
import VideoPlayer from './videoPlayer';

function VSL() {
  const [text, setText] = useState('');
  // const [videoUrl, setVideoUrl] = useState('');

  const videoUrl = 'http://localhost:5000/VSL/voiceover_output.mp4';
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
        console.log('Video generation request successful.');
      } else {
        console.error('Failed to generate video');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };
  

  return (
   <div className="flex justify-center items-center h-screen">
    <div className="w-full max-w-xl text-center">
    <h1 className="text-4xl font-bold mb-4">Generate your Own VSL</h1>
      <textarea
        className="border rounded-md p-2 w-full"
        rows="4"
        cols="50"
        value={text}
        onChange={handleTextChange}
        placeholder="Enter your VSL script here..."
      />
      <button
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4"
        onClick={generateVideo}
      >
        Generate Video
      </button>
      {/* {videoUrl ? (
        <VideoPlayer />
      ) : (
        <div className="text-red-600 font-bold mt-8">No video found.</div>
      )} */}
    </div>
  </div>
  );
}

export default VSL;
