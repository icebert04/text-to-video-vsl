// VideoPlayer.js
import React from 'react';

function VideoPlayer() {
  const videoUrl = 'http://localhost:5000/VSL/voiceover_output.mp4';

  return (
    <div className="container flex justify-center mx-auto mt-8">
        <h2 className='text-3xl font-bold mb-4'>Your Video is generated here</h2>
        <div className='mt-8'> 
          <video width="320" height="240" controls>
            <source src={videoUrl} type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        </div>
    </div>
  );
}

export default VideoPlayer;
