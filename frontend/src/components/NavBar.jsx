import { Link } from 'react-router-dom';
import bell from '../assets/bell.svg';
import profile_img from '../assets/profile-img.svg';

const NavBar = () => {
    return (
        <div className={`w-full fixed top-0 left-0 z-10`}>
            <div className={`md:flex h-20 md:h-28 items-center justify-between px-4 md:px-10 py-4 tracking-wider font-inter bg-white`}>
                <div className="font-bold text-2xl md:mb-8 cursor-pointer flex items-center font-inter text-gray-800">
                    <Link to="/">
						{/* <img src={isDark ? logo_white : logo} alt="Logo" className="w-44 object-contain" /> */}
                        <div className="w-20 h-10"></div>
					</Link>
                </div>
                <ul
                    className={`md:flex md:items-center md:pb-0 font-normal text-blue-900 bg-white absolute md:static md:z-auto z-40 left-0 w-full md:w-auto md:pl-0 pl-9 transition-all duration-500 ease-in`}
                >
                    <li className={`mr-2 text-xs md:text-sm md:my-0 my-7 font-bold`}>
                        <Link to="/item-registration">Cadastro de Item</Link>
                    </li>
                    <div className="border-l-2 border-blue-900 h-3 mr-2"></div>
                    <li className={`mr-6 text-xs md:text-sm md:my-0 my-7`}>
                        <Link to="/editor">Editor</Link>
                    </li>
                    <div>
                        <img
                            src={profile_img}
                            alt="Foto de Perfil"
                            className="absolute md:relative right-20 md:right-0 -top-16 md:top-0 h-12 w-12 md:h-16 md:w-16 rounded-full mx-4"
                        />
                    </div>
                    <div className="absolute md:relative right-16 md:right-0 -top-12 md:top-0">
                        <img src={bell} alt="Sino" className="w-6 h-6 md:ml-4 object-scale-down" />
                        <div className={`absolute rounded-full w-3 h-3 -mt-7 ml-3 md:ml-7 cyan-400`}></div>
                    </div>
                </ul>
            </div>
        </div>
    );
};

export default NavBar;
