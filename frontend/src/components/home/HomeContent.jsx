import FilterButtons from './FilterButtons/FilterButtons';
import HomeTop from './HomeTop';
import PanelList from './PanelList';

const HomeContent = () => {

    return (
        <div className="mt-28 p-12 pr-24 ml-72 font-inter">
            <HomeTop />
            <FilterButtons />
            <PanelList />
        </div>
    );
};

export default HomeContent;
