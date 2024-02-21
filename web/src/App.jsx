import { BrowserRouter, Route, Routes } from "react-router-dom"
import HomePage from "./pages/Home"
import MainLayout from "./layouts/MainLayout"
import SignInPage from "./pages/SigninPage"
import ContactUsPage from "./pages/ContactUsPage"
import SignUpPage from "./pages/SignupPage"
import ForgotPasswordPage from "./pages/ForgotPasswordPage"
import DashBoard from "./pages/dashboard/DashboardPage"
import MyCVsPage from "./pages/dashboard/MyCVsPage"
import DashboardLayout from "./layouts/DashboardLayout"

function App() {

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<MainLayout />}>
            <Route index element={<HomePage />} />

            <Route element={<SignInPage />} path="signin" />
            <Route element={<SignUpPage />} path="signup" />
            <Route element={<ForgotPasswordPage />} path="forgot-password" />
            <Route element={<ContactUsPage />} path="contact-us" />
          </Route>
          <Route element={<DashboardLayout />} path="/dashboard">
            <Route element={<DashBoard />} index />
            <Route element={<MyCVsPage />} path="cv" />
          </Route>
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
