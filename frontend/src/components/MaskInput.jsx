import InputMask from "react-input-mask";

const MaskInput = ({ ...props }) => {
    return (
      <InputMask
        {...props}
        className={`appearance-none ${props.value && !props.fixedBg? "bg-white border border-blue-900" : "bg-zinc-100 "} rounded-full mx-4 md:mx-0 md:w-full h-12 py-2 px-5 text-gray-700 text-xs leading-tight focus:outline-none ${props.className}`}
      />
    );
  };
  
  export default MaskInput;
