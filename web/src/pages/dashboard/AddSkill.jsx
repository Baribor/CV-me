import Rating from "@mui/material/Rating";
import InputField from "../../components/input/InputField";


export default function AddSkill() {
	return (
		<div className="grid grid-cols-2 gap-2 gap-y-4">
			<InputField
				label="Skill"
				type="text"
				name="skill"
			/>
			<div className="flex items-center">
				<Rating
					size="large" />
			</div>
			<div className="col-span-2">
				<button className="font-bold text-primary text-sm hover:shadow-md px-3 py-2 active:scale-[.98]">Add another</button>
			</div>
			<div className="col-span-2 text-end">
				<button className="font-bold bg-primary text-sm rounded-full text-white hover:shadow-md px-6 py-2 active:scale-[.98]">Preview</button>
			</div>
		</div>
	)
}