/*
**High Level*: WebDev

Category:
Accessibility

Topic:
Operable Accessibility (e.g keyboard, consistent navigation)
*/

// Accessibility Functions
function focusElement(element) {
  element.focus();
}

function activateElement(element) {
  element.click();
}

function navigateToLink(link) {
  window.location.href = link;
}

// Voice Commands Mapping
const voiceCommands = {
  'go to home': () => {
    navigateToLink('/home');
  },
  'go to courses': () => {
    navigateToLink('/courses');
  },
  'go to resources': () => {
    navigateToLink('/resources');
  },
  'go to profile': () => {
    navigateToLink('/profile');
  },
  'enroll in course': () => {
    const enrollButton = document.getElementById('enroll-button');
    activateElement(enrollButton);
  },
  'open course': () => {
    const courseLink = document.getElementById('course-link');
    navigateToLink(courseLink.href);
  },
  // Add more voice commands as needed
};

// Voice Recognition Setup
const recognition = new SpeechRecognition();
recognition.continuous = true;

recognition.onresult = (event) => {
  const { transcript } = event.results[event.results.length - 1][0];

  // Normalize and process the transcript
  const command = transcript.toLowerCase();
  if (voiceCommands.hasOwnProperty(command)) {
    voiceCommands[command]();
  }
};

// Start Voice Recognition
function startVoiceRecognition() {
  recognition.start();
  console.log('Voice recognition started...');
}

// Stop Voice Recognition
function stopVoiceRecognition() {
  recognition.stop();
  console.log('Voice recognition stopped...');
}

// Initialize the Educational Platform
function initializePlatform() {
  const voiceControlButton = document.getElementById('voice-control-button');
  const stopButton = document.getElementById('stop-button');

  // Add event listeners for voice control and stop buttons
  voiceControlButton.addEventListener('click', startVoiceRecognition);
  stopButton.addEventListener('click', stopVoiceRecognition);
}

// Entry Point
window.onload = initializePlatform;
