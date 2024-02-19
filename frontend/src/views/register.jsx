import { useEffect, useState } from 'react';

import BaseBackground from '../components/login/BaseBackground';
import LoginButton from '../components/login/LoginButton';
import LoginData from '../components/register/LoginData';
import PersonalData from '../components/register/PersonalData';
import ProfileUpload from '../components/register/ProfileUpload';
import RadioButton from '../components/RadioButton';
import guyWithRaisedHand from '../assets/guy-with-raised-hand.svg';
import { register } from '../utils/auth';
import { useAuthStore } from '../store/auth';
import { useNavigate } from 'react-router-dom';

function Register() {
    const [fullName, setFullName] = useState('');
    const [cpf, setCpf] = useState('');
    const [phone, setPhone] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [password2, setPassword2] = useState('');
    const [selectedOption, setSelectedOption] = useState(null);
    const [buttonEnabled, setButtonEnabled] = useState(false);
    const isLoggedIn = useAuthStore((state) => state.isLoggedIn);
    const navigate = useNavigate();

    useEffect(() => {
        if (isLoggedIn()) {
            navigate('/');
        }
    }, []);

    const resetForm = () => {
        setUsername('');
        setPassword('');
        setPassword2('');
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const { error } = await register(username, password, password2, fullName, cpf, phone);
        if (error) {
            alert(JSON.stringify(error));
        } else {
            navigate('/');
            resetForm();
        }
    };

    useEffect(() => {
        handleEnablingLoginButton();
    }, [username, password, password2]);

    const handleEnablingLoginButton = () => {
        setButtonEnabled(
            fullName !== '' && cpf !== '' && phone !== '' && username !== '' && password !== '' && password2 !== ''
        );
    };

    const handleImageUpload = () => {};

    const handleRadioChange = (e) => {
        setSelectedOption(e.target.value);
    };

    return (
        <>
            <BaseBackground isRegister={true}>
                <div className="md:w-1/2 flex flex-col">
                    <div className="bg-teal-300 h-full w-1/3 rounded-2xl"></div>
                </div>
                <div className="md:w-1/2 flex flex-col items-center">
                    <form className="w-full max-w-lg" onSubmit={handleSubmit}>
                        <ProfileUpload handleImageUpload={handleImageUpload}/>
                        <PersonalData fullName={fullName} setFullName={setFullName} cpf={cpf} setCpf={setCpf} phone={phone} setPhone={setPhone}/>
                        <LoginData username={username} setUsername={setUsername} password={password} setPassword={setPassword} password2={password2} setPassword2={setPassword2}/>

                        <p>{password2 !== password ? 'Passwords do not match' : ''}</p>
                        <div className="inline-flex gap-4">
                            <RadioButton
                                name="option"
                                value="true"
                                checked={selectedOption === 'true'}
                                onChange={handleRadioChange}
                                label="Sim"
                            />
                            <RadioButton
                                name="option"
                                value="false"
                                checked={selectedOption === 'false'}
                                onChange={handleRadioChange}
                                label="Não"
                            />
                            <p className="text-xs break-words w-40 mt-7 text-gray-500">
                                Você deseja receber novidades por e-mail?
                            </p>
                            <LoginButton className="mt-4 ml-40" buttonEnabled={buttonEnabled} />
                        </div>
                    </form>
                </div>
            </BaseBackground>
            <img className="absolute top-0 w-5/6 pointer-events-none" src={guyWithRaisedHand} />
        </>
    );
}

export default Register;
