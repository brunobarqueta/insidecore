import HomeContent from '@/components/home/HomeContent';
import { Link } from 'react-router-dom';
import NavBar from '../components/NavBar';
import SideBar from '@/components/sidebar/SideBar';
import { useAuthStore } from '../store/auth';
import Login from './login';

const Home = () => {
    const [isLoggedIn, user] = useAuthStore((state) => [state.isLoggedIn, state.user]);
    return <div>{isLoggedIn() ? <LoggedInView user={user()} /> : <Login />}</div>;
};

const LoggedInView = ({ user }) => {

    return (
        <div className="flex h-full bg-gray-100">
            {/* <div>
            <h1>Welcome {user.username}</h1>
            <Link to="/private">
                <button>Private</button>
            </Link>
            <Link to="/logout">
                <button>Logout</button>
            </Link>
        </div> */}
            <NavBar />
            <SideBar />
            <HomeContent />
        </div>
    );
};

export const LoggedOutView = ({ title = 'Home' }) => {
    return (
        <div>
            <h1>{title}</h1>
            <Link to="/login">
                <button>Login</button>
            </Link>
            <Link to="/register">
                <button>Register</button>
            </Link>
        </div>
    );
};

export default Home;
