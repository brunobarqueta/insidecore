import InputMask from "react-input-mask";
import { useRef } from "react";

const MaskInput = ({ fixedBg, className, ...restProps }) => {
  const inputRef = useRef(null);

  return (
    <InputMask
      {...restProps}
      className={`appearance-none ${
        restProps.value && !fixedBg
          ? 'bg-white border border-blue-900'
          : 'bg-zinc-100'
      } rounded-full mx-4 md:mx-0 md:w-full h-12 py-2 px-5 text-gray-700 text-xs leading-tight focus:outline-none ${className}`}
      ref={inputRef}
    />
  );
};

export default MaskInput;
