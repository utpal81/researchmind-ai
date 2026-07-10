import {
    BrowserRouter,
    Routes,
    Route,
} from "react-router-dom"

import AppLayout from "./components/layout/AppLayout"

import HomePage from "./pages/HomePage"

import ChatPage from "./pages/ChatPage"

import UploadPage from "./pages/UploadPage"

function App() {

    return (

        <BrowserRouter>

            <Routes>

                <Route
                    element={<AppLayout />}
                >

                    <Route
                        path="/"
                        element={<HomePage />}
                    />

                    <Route
                        path="/chat"
                        element={<ChatPage />}
                    />

                    <Route
                        path="/upload"
                        element={<UploadPage />}
                    />

                </Route>


            </Routes>

        </BrowserRouter>

    )

}

export default App