const Input = ({ value, fixedBg, ...props }) => {
  return (
    <input
      {...props}
      value={value || ""}
      className={`appearance-none ${value && !fixedBg ? "bg-white border border-blue-900" : "bg-zinc-100 "} rounded-full mx-4 md:mx-0 md:w-full h-12 py-2 px-5 text-gray-700 text-xs leading-tight focus:outline-none ${props.className}`}
    />
  );
};

  
  export default Input;
