import TextField from "@mui/material/TextField"

const style = {
	"& label.Mui-focused": {
		color: "#2196f3",
	},
	"& .MuiOutlinedInput-root": {
		"&.Mui-focused fieldset": {
			borderColor: "#2196f3",
		},
	},
	".MuiInputBase-input": {}
};

const CVmeTextField = ({ containerStyle, children, ...props }) => {
	return (
		<div className={containerStyle + " relative"}>
			<TextField {...props} sx={style} fullWidth />
			<div className="absolute right-0 top-[50%] -translate-y-[50%] mr-2">
				{children}
			</div>
		</div>
	)
};

export default CVmeTextField;