const BaseBackground = ({children}, isRegister) => {
    return (
        <section className="h-screen px-24 py-20">
            <div className={`flex flex-col md:flex-row h-full font-inter bg-white rounded-2xl overflow-hidden ${!isRegister && 'p-3'}`}>
                {children}
            </div>
        </section>
    );
};

export default BaseBackground;
