import MenuAccordion from './MenuAccordion';
import SearchField from './SearchField';

const SideBar = () => {
    
    return (
        <div className="w-1/5 fixed h-screen bg-blue-900 flex flex-col px-10">
            <div className="flex-grow flex flex-col mt-32 font-nunito text-white text-sm">
                <SearchField />
                <h1 className="text-teal-300 font-bold text-xl">Sub-menu</h1>
                <MenuAccordion />
            </div>
        </div>
    );
};

export default SideBar;
