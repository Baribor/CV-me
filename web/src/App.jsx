import { BrowserRouter, Route, Routes } from "react-router-dom"
import HomePage from "./pages/Home"
import MainLayout from "./layouts/MainLayout"
import SignInPage from "./pages/SigninPage"
import ContactUsPage from "./pages/ContactUsPage"

function App() {

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<MainLayout />}>
            <Route index element={<HomePage />} />

            <Route element={<SignInPage />} path="signin" />
            <Route element={<ContactUsPage />} path="contact-us" />
          </Route>
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
