Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import { useState } from 'react'; import { ThemeProvider } from './theme/ThemeProvider'; import { PanicButtonPanel } from './components/PanicButtonPanel'; import { ThemeSelector } from './components/ThemeSelector'; import { AboutPage } from './components/AboutPage'; import { Header } from './components/Header'; import { Footer } from './components/Footer';

function App() { const [showAbout, setShowAbout] = useState(true);

if (showAbout) { return ( <AboutPage onEnter={() => setShowAbout(false)} /> ); }

return (

    <main className="flex-1 flex flex-col lg:flex-row gap-4 p-4 lg:p-6">
      <div className="flex-1 flex flex-col gap-4">
        <div className="bg-card border border-border rounded-lg p-6 shadow-sm">
          <h2 className="text-2xl font-bold mb-4 text-foreground">Vision Helper</h2>
          <p className="text-muted-foreground leading-relaxed mb-4">
            This application is designed with accessibility in mind, providing multiple visual modes
            to accommodate different vision needs.
          </p>
          
          <div className="space-y-3">
            <div className="flex items-start gap-3">
              <div className="w-2 h-2 rounded-full bg-primary mt-2 flex-shrink-0" />
              <div>
                <h3 className="font-semibold text-foreground">Normal Mode</h3>
                <p className="text-sm text-muted-foreground">Standard color palette with good contrast</p>
              </div>
            </div>
            
            <div className="flex items-start gap-3">
              <div className="w-2 h-2 rounded-full bg-primary mt-2 flex-shrink-0" />
              <div>
                <h3 className="font-semibold text-foreground">High-Contrast Mode</h3>
                <p className="text-sm text-muted-foreground">Yellow and blue palette optimized for colorblind users</p>
              </div>
            </div>
            
            <div className="flex items-start gap-3">
              <div className="w-2 h-2 rounded-full bg-primary mt-2 flex-shrink-0" />
              <div>
                <h3 className="font-semibold text-foreground">Grayscale Mode</h3>
                <p className="text-sm text-muted-foreground">No color, relies on contrast and typography</p>
              </div>
            </div>
          </div>
        </div>

        <div className="bg-card border border-border rounded-lg p-6 shadow-sm">
          <h3 className="text-lg font-semibold mb-3 text-foreground">Theme Selection</h3>
          <ThemeSelector />
        </div>
      </div>

      <div className="lg:w-[40%] flex-shrink-0">
        <PanicButtonPanel />
      </div>
    </main>

    <Footer />
  </div>
</ThemeProvider>
); }

export default App;

=== PanicButtonPanel.tsx ===

import { useState } from 'react'; import { AlertTriangle } from 'lucide-react';

export function PanicButtonPanel() { const [activated, setActivated] = useState(false);

const handleActivate = () => { setActivated(true); setTimeout(() => setActivated(false), 2000); };

return (

"This is for low-vision users who need to trigger an emergency alert by touch alone."

  <button
    onClick={handleActivate}
    className={`
      flex-1 rounded-lg border-4 transition-all
      focus-visible:outline-none focus-visible:ring-8 focus-visible:ring-ring
      ${
        activated
          ? 'bg-destructive border-destructive scale-95'
          : 'bg-destructive/90 border-destructive hover:bg-destructive hover:scale-[1.02] active:scale-95'
      }
    `}
    aria-label="Emergency panic button - press to trigger alert"
  >
    <div className="flex flex-col items-center justify-center gap-6 p-8">
      <AlertTriangle 
        className="w-24 h-24 lg:w-32 lg:h-32 text-destructive-foreground" 
        strokeWidth={2.5}
        aria-hidden="true"
      />
      <div className="text-center">
        <div className="text-4xl lg:text-5xl font-bold text-destructive-foreground mb-2">
          {activated ? 'ALERT SENT' : 'PANIC'}
        </div>
        <div className="text-xl lg:text-2xl text-destructive-foreground/90">
          {activated ? 'Help is on the way' : 'Press for Emergency'}
        </div>
      </div>
    </div>
  </button>
</div>
); }

=== ThemeSelector.tsx ===

import { useTheme } from '../theme/ThemeProvider'; import { THEME_LABELS, THEME_DESCRIPTIONS, type ThemeType } from '../theme/theme'; import { Check } from 'lucide-react';

export function ThemeSelector() { const { theme, setTheme } = useTheme(); const themes: ThemeType[] = ['normal', 'high-contrast', 'grayscale'];

return (

{themes.map((t) => ( <button key={t} onClick={() => setTheme(t)} className={ w-full text-left p-4 rounded-lg border-2 transition-all focus-visible:outline-none focus-visible:ring-4 focus-visible:ring-ring ${ theme === t ? 'border-primary bg-primary/10' : 'border-border bg-card hover:border-primary/50' } } aria-pressed={theme === t} >
{THEME_LABELS[t]}
{THEME_DESCRIPTIONS[t]}
{theme === t && ( )}
))}
); }
=== AboutPage.tsx ===

import { Button } from '@/components/ui/button'; import { Eye, Palette, AlertTriangle } from 'lucide-react';

export function AboutPage({ onEnter }) { return (

Vision Helper
Accessible emergency alert system designed for all vision abilities

    <div className="bg-card border border-border rounded-lg p-8 mb-8 shadow-sm">
      <div className="space-y-6">
        <div className="flex items-start gap-4">
          <div className="w-12 h-12 rounded-lg bg-primary/10 flex items-center justify-center flex-shrink-0">
            <Palette className="w-6 h-6 text-primary" />
          </div>
          <div>
            <h3 className="text-lg font-semibold text-foreground mb-2">Three Visual Modes</h3>
            <p className="text-muted-foreground leading-relaxed">
              Choose between Normal, High-Contrast (Yellow/Blue), and Grayscale themes.
            </p>
          </div>
        </div>

        <div className="flex items-start gap-4">
          <div className="w-12 h-12 rounded-lg bg-destructive/10 flex items-center justify-center flex-shrink-0">
            <AlertTriangle className="w-6 h-6 text-destructive" />
          </div>
          <div>
            <h3 className="text-lg font-semibold text-foreground mb-2">Large Touch Target</h3>
            <p className="text-muted-foreground leading-relaxed">
              Emergency panic button occupies 40% of the screen for low-vision users.
            </p>
          </div>
        </div>
      </div>
    </div>

    <div className="text-center">
      <Button onClick={onEnter} size="lg" className="text-lg px-8 py-6 h-auto focus-visible:ring-4">
        Enter Application
      </Button>
    </div>
  </div>
</div>
); }

src/
 ├─ App.tsx
 ├─ components/
 │   ├─ PanicButtonPanel.tsx
 │   ├─ ThemeSelector.tsx
 │   ├─ AboutPage.tsx
 │   ├─ Header.tsx
 │   └─ Footer.tsx
 ├─ theme/
 │   ├─ ThemeProvider.tsx
 │   └─ theme.ts
 └─ pose/
     └─ PoseModel.tsximport { useState } from 'react';
import { ThemeProvider } from './theme/ThemeProvider';
import { PanicButtonPanel } from './components/PanicButtonPanel';
import { ThemeSelector } from './components/ThemeSelector';
import { AboutPage } from './components/AboutPage';
... import { Header } from './components/Header';
... import { Footer } from './components/Footer';
... import { PoseModel } from './pose/PoseModel';
... 
... function App() {
...   const [showAbout, setShowAbout] = useState(true);
... 
...   if (showAbout) {
...     return <AboutPage onEnter={() => setShowAbout(false)} />;
...   }
... 
...   return (
...     <ThemeProvider>
...       <Header />
...       <main className="flex-1 flex flex-col lg:flex-row gap-4 p-4 lg:p-6">
...         <div className="flex-1 flex flex-col gap-4">
...           <div className="bg-card border border-border rounded-lg p-6 shadow-sm">
...             <h2 className="text-2xl font-bold mb-4 text-foreground">Vision Helper</h2>
...             <p className="text-muted-foreground leading-relaxed mb-4">
...               This application is designed with accessibility in mind, providing multiple visual modes
...               to accommodate different vision needs.
...             </p>
...           </div>
... 
...           <div className="bg-card border border-border rounded-lg p-6 shadow-sm">
...             <h3 className="text-lg font-semibold mb-3 text-foreground">Theme Selection</h3>
...             <ThemeSelector />
...           </div>
... 
...           <div className="bg-card border border-border rounded-lg p-6 shadow-sm">
...             <h3 className="text-lg font-semibold mb-3 text-foreground">Pose Recognition</h3>
...             <PoseModel />
...           </div>
... 
...           <div className="bg-card border border-border rounded-lg p-6 shadow-sm">
...             <h3 className="text-lg font-semibold mb-3 text-foreground">Camera Vision</h3>
...             <video id="camera" autoPlay playsInline className="border rounded-lg"></video>
...             <button onClick={capture} className="mt-4 px-4 py-2 bg-primary text-white rounded-lg">
...               Describe what I see
...             </button>
...             <canvas id="canvas" hidden></canvas>
...             <div id="vision-output" className="mt-2 text-muted-foreground"></div>
...           </div>
...         </div>
... 
...         <div className="lg:w-[40%] flex-shrink-0">
...           <PanicButtonPanel />
        </div>
      </main>
      <Footer />
    </ThemeProvider>
  );
}

// Camera capture + Vision API + Speech
function capture() {
  const video = document.getElementById("camera") as HTMLVideoElement;
  const canvas = document.getElementById("canvas") as HTMLCanvasElement;
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  canvas.getContext("2d")!.drawImage(video, 0, 0);

  const imageData = canvas.toDataURL("image/png");

  fetch("VISION_API_ENDPOINT", {
    method: "POST",
    headers: { "Authorization": "Bearer YOUR_KEY" },
    body: imageData
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById("vision-output")!.textContent = data.description;
      speak(data.description);
    });
}

function speak(text: string) {
  const msg = new SpeechSynthesisUtterance(text);
  speechSynthesis.speak(msg);
}

export default App;import { useEffect } from 'react';
import * as tmPose from '@teachablemachine/pose';

export function PoseModel() {
  useEffect(() => {
    const URL = "https://teachablemachine.withgoogle.com/models/AfyXJpuce/";
    let model, webcam, ctx, labelContainer, maxPredictions;

    async function init() {
      const modelURL = URL + "model.json";
      const metadataURL = URL + "metadata.json";
      model = await tmPose.load(modelURL, metadataURL);
      maxPredictions = model.getTotalClasses();

      const size = 200;
      const flip = true;
      webcam = new tmPose.Webcam(size, size, flip);
      await webcam.setup();
      await webcam.play();
      window.requestAnimationFrame(loop);

      const canvas = document.getElementById("canvas") as HTMLCanvasElement;
      canvas.width = size;
      canvas.height = size;
      ctx = canvas.getContext("2d")!;
      labelContainer = document.getElementById("label-container")!;
      for (let i = 0; i < maxPredictions; i++) {
        labelContainer.appendChild(document.createElement("div"));
      }
    }

    async function loop() {
      webcam.update();
      await predict();
      window.requestAnimationFrame(loop);
    }

    async function predict() {
      const { pose, posenetOutput } = await model.estimatePose(webcam.canvas);
      const prediction = await model.predict(posenetOutput);

      for (let i = 0; i < maxPredictions; i++) {
        const classPrediction =
          prediction[i].className + ": " + prediction[i].probability.toFixed(2);
        labelContainer.childNodes[i].textContent = classPrediction;
      }

      drawPose(pose);
    }

    function drawPose(pose) {
      if (webcam.canvas) {
        ctx.drawImage(webcam.canvas, 0, 0);
        if (pose) {
          const minPartConfidence = 0.5;
          tmPose.drawKeypoints(pose.keypoints, minPartConfidence, ctx);
          tmPose.drawSkeleton(pose.keypoints, minPartConfidence, ctx);
        }
      }
    }

    init();
  }, []);

  return (
    <div>
      <canvas id="canvas"></canvas>
      <div id="label-container"></div>
    </div>
  );
