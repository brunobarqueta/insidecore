import EditIcon from '../../assets/edit-icon.svg';
import EyeIcon from '../../assets/eye-icon.svg';
import TrashIcon from '../../assets/trash-icon.svg';

const ListItem = ({ title, date }) => {
    return (
        <div className="w-full h-14 rounded-full bg-white flex gap-24 items-center pl-8 pr-3">
            <p className="w-4/5 text-gray-600">{title}</p>
            <p className="text-xs text-gray-500 font-light">{date}</p>
            <div className="flex gap-2 justify-center">
                <img className="cursor-pointer" src={EyeIcon} />
                <img className="cursor-pointer" src={EditIcon} />
                <img className="cursor-pointer" src={TrashIcon} />
            </div>
            <div>
                <div className="w-6 h-6 bg-blue-900 rounded-full"></div>
            </div>
        </div>
    );
};

export default ListItem;
