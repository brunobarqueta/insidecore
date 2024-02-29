import ConfigsPanel from '../../assets/configs-panel.svg';
import DashboardPanel from '../../assets/dashboard-panel.svg';
import { Link } from 'react-router-dom';
import QuestionIcon from '../../assets/question-icon.svg';

const HomeTop = () => {
    return (
        <div className="grid grid-cols-3 h-32 gap-12">
            <div>
                <Link to="/dashboard">
                    <img className="cursor-pointer" src={DashboardPanel} alt="dashboard-panel" />
                </Link>
            </div>
            <div>
                <Link to="/configs">
                    <img className="cursor-pointer" src={ConfigsPanel} alt="configs-panel" />
                </Link>
            </div>
            <div>
                <img className="mt-4" src={QuestionIcon} alt="question-icon" />
                <p className="mt-2 text-sm text-gray-500">Precisa de ajuda?</p>
                <button className="w-36 mt-2 py-1 text-sm text-gray-500 border border-cyan-300 rounded-full">Entre em contato</button>
            </div>
        </div>
    );
};

export default HomeTop;
