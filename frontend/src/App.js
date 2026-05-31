import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>🎬 All-Lucky-ai</h1>
        <p>AI Long Video Generator</p>
        <p>Generate 30-minute videos from Text, Images, and Audio</p>
      </header>
      <main>
        <section className="features">
          <div className="feature">
            <h2>📝 Text-to-Video</h2>
            <p>Create videos from text descriptions</p>
          </div>
          <div className="feature">
            <h2>🖼️ Image-to-Video</h2>
            <p>Transform image sequences into animated videos</p>
          </div>
          <div className="feature">
            <h2>🎵 Audio-to-Video</h2>
            <p>Generate videos from audio/voice</p>
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
