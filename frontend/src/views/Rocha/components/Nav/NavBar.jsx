import logoRocha from '../../assets/logo-rocha.svg'

const NavBar = () => {
    return (
        <nav className="bg-orange-500 text-white p-4 flex items-center justify-between">
            <div className="flex items-center cursor-pointer">
                <img src={logoRocha} alt="Logo" className="h-12 mr-4" />
                <span className="text-lg font-bold">Simulações</span>
            </div>
            <div className="flex items-center space-x-8 font-semibold text-xs">
                <a href="#" className="hover:text-gray-200">
                    Manual de Uso
                </a>
                <a href="#" className="hover:text-gray-200">
                    Início
                </a>
                <a href="#" className="hover:text-gray-200">
                    Painel Administrativo
                </a>
            </div>
        </nav>
    )
}

export default NavBar
