import './App.css'

import { BrowserRouter, Route, Routes } from 'react-router-dom'

import Home from './views/home'
import ItemRegistration from './views/itemRegistration'
import Login from './views/login'
import Logout from './views/logout'
import MainWrapper from './layouts/MainWrapper'
import Private from './views/private'
import PrivateRoute from './layouts/PrivateRoute'
import Register from './views/register'
import Simulation from './views/Rocha/components/simulation'
import { Toaster } from './components/ui/toaster'

function App() {
    return (
        <BrowserRouter>
            <MainWrapper>
                <Routes>
                    <Route
                        path="/private"
                        element={
                            <PrivateRoute>
                                <Private />
                            </PrivateRoute>
                        }
                    />
                    <Route
                        path="/"
                        element={
                            <PrivateRoute>
                                <Home />
                            </PrivateRoute>
                        }
                    />
                    <Route path="/login" element={<Login />} />
                    <Route path="/register" element={<Register />} />
                    <Route path="/logout" element={<Logout />} />
                    <Route
                        path="/item-registration"
                        element={
                            <PrivateRoute>
                                <ItemRegistration />
                            </PrivateRoute>
                        }
                    />
                    <Route
                        path="/item-registration/:id"
                        element={
                            <PrivateRoute>
                                <ItemRegistration />
                            </PrivateRoute>
                        }
                    />
                    <Route path="/simulation" element={<Simulation />} />
                </Routes>
                <Toaster />
            </MainWrapper>
        </BrowserRouter>
    )
}

export default App
