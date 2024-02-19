import Input from '../Input';
import userIcon from '../../assets/user-icon.svg';

const LoginData = ({username, setUsername, password, setPassword, password2, setPassword2}) => {
    return (
        <>
            <div>
                <div className="inline-flex mt-8 ml-4 mb-4">
                    <img className="mr-2" width="25px" height="25px" src={userIcon} />
                    <p className="text-blue-900">Dados de Login</p>
                </div>
                <Input
                    type="text"
                    name="login"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="Login"
                />
            </div>
            <div className="flex space-x-4 mt-4">
                <div className="w-1/2">
                    <Input
                        type="password"
                        name="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        placeholder="Defina a senha"
                    />
                </div>
                <div className="w-1/2">
                    <Input
                        type="password"
                        name="confirmPassword"
                        value={password2}
                        onChange={(e) => setPassword2(e.target.value)}
                        placeholder="Digite novamente"
                    />
                </div>
            </div>
        </>
    );
};

export default LoginData;
