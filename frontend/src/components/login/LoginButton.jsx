import PlayDisabled from '../../assets/play-disabled.svg';
import PlayEnabled from '../../assets/play-enabled.svg';

const LoginButton = ({buttonEnabled, className}) => {
    return (
        <button
            type="submit"
            className={`${!buttonEnabled && 'pointer-events-none'} ${className}`}
        >
            <img
                src={buttonEnabled ? PlayEnabled : PlayDisabled}
                alt="PlayDisabled"
            />
        </button>
    );
};

export default LoginButton;
