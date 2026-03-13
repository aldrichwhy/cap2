import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import EmotionDetectionPage from "./pages/EmotionDetectionPage";
import TherapistHomePage from "./pages/TherapistHomePage";
import PatientHomePage from "./pages/PatientHomePage";
import PatientChatBoard from "./pages/PatientChatBoard";

//These handles the URLs and where they lead to

function App() {
  return (
    <Routes>
    {/* Make page always redirect to Login.jsx page first*/}
    <Route path="/" element={<Navigate to="/login" replace />} />

    <Route path="/login" element={<Login />} />
    <Route path="/register" element={<Register />} />
    <Route path="/therapist-home" element={<TherapistHomePage />} />
    <Route path="/therapist" element={<EmotionDetectionPage />} />
    <Route path="/patient-home" element={<PatientHomePage />} />
    <Route path="/patient-chat" element={<PatientChatBoard />} />
</Routes>
  );
}

export default App;