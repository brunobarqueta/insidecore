const ToggleButton = ({ label, isActive, onClick }) => {
    return (
        <button
            className={`w-24 rounded-full text-xs font-light py-1 ${isActive ? 'bg-blue-900 text-white' : 'bg-white text-gray-500'}`}
            onClick={onClick}
        >
            {label}
        </button>
    );
};

export default ToggleButton;