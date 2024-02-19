import User from '../../assets/user.svg';

const ProfileUpload = ({handleImageUpload}) => {
    return (
        <div className="inline-flex items-center mt-4">
            <img src={User} className="relative mt-4" alt="User" />
            <div className="ml-6">
                <p className="text-blue-900 mt-2">Foto de perfil</p>
                <button
                    className="border rounded-full border-teal-300 text-xs py-1 px-3 text-gray-500 mt-2"
                    onClick={handleImageUpload}
                >
                    Carregar imagem
                </button>
            </div>
        </div>
    );
};

export default ProfileUpload;
