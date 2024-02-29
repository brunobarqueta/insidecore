import { useEffect, useState } from 'react';

import BaseBackground from '../components/BaseBackground';
import Input from '../components/Input';
import LoginButton from '../components/login/LoginButton';
import LoginOptions from '../components/login/LoginOptions';
import User from '../assets/user.svg';
import backgroundOffice from '../assets/background-office.png';
import { login } from '../utils/auth';
import { useAuthStore } from '../store/auth';
import { useNavigate } from 'react-router-dom';
import womanWithIPad from '../assets/woman-with-ipad.png';

const Login = () => {
    const navigate = useNavigate();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [buttonEnabled, setButtonEnabled] = useState(false);
    const isLoggedIn = useAuthStore((state) => state.isLoggedIn);

    useEffect(() => {
        if (isLoggedIn()) {
            navigate('/');
        }
    }, []);

    const resetForm = () => {
        setUsername('');
        setPassword('');
    };

    const handleLogin = async (e) => {
        e.preventDefault();
        const { error } = await login(username, password);
        if (error) {
            alert(error);
        } else {
            navigate('/');
            resetForm();
        }
    };

    useEffect(() => {
        handleEnablingLoginButton();
    }, [username, password]);

    const handleEnablingLoginButton = () => {
        setButtonEnabled(username !== '' && password !== '');
    };

    return (
        <>
            <BaseBackground>
                <div className="md:w-1/2 flex flex-col justify-center items-center">
                    <img className="rounded h-full w-screen" src={backgroundOffice} />
                    {/* object-scale-down */}
                </div>
                <div className="md:w-1/2 flex flex-col items-center">
                    <form className="w-full max-w-lg mt-4" onSubmit={handleLogin}>
                        <img src={User} className="relative mt-4" alt="User" />
                        <Input
                            type="text"
                            className="mt-16"
                            name="username"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            placeholder="E-mail"
                        />
                        <Input
                            type="password"
                            className="mt-6"
                            name="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            placeholder="Senha"
                        />
                        <LoginOptions />
                        <LoginButton className="mt-24" buttonEnabled={buttonEnabled} />
                    </form>
                </div>
            </BaseBackground>
            <img className="absolute top-[-1rem] left-32 w-1/3 pointer-events-none" src={womanWithIPad} />
        </>
    );
};

export default Login;
