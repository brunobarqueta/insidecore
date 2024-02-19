import lock from '../../assets/lock.png';
import { useNavigate } from 'react-router-dom';

const LoginOptions = () => {

    const navigate = useNavigate();

    return (
        <div className="flex items-center justify-left mt-8 gap-2">
            <img
                className="color-blue-900 cursor-pointer"
                src={lock}
                width={25}
                height={25}
                alt="lock"
            />
            <p className="text-xs font-bold text-blue-900 leading-5 cursor-pointer">
                Esqueceu a senha?
            </p>
            <div className="border-l-2 border-teal-200 h-3"></div>
            <p className="text-xs font-bold text-blue-900 leading-5 mr-4 cursor-pointer" onClick={() => navigate('/register')}>
                Criar conta
            </p>
        </div>
    );
};

export default LoginOptions;
