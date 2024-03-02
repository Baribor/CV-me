import { useRecoilValue } from "recoil"
import { user } from "../../store"


export default function DashBoard() {
	const currentUser = useRecoilValue(user);

	return (
		<div>
			<h2 className="text-3xl">Welcome <span className="text-primary font-bold">{currentUser?.first_name}</span></h2>
		</div>
	)
}