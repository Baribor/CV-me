import { useState } from "react"
import NewCVDialog from "../../components/dialogs/NewCVDialog";


export default function MyCVsPage() {
	const [dialog, openDialog] = useState(false);
	const cvs = [

	]

	const onDialogClose = () => {
		openDialog(false)
	}
	return (
		<div>
			<div className="text-end">
				<button className="text-white bg-primary max-sm:text-sm px-4 py-2 rounded-full shadow-md active:scale-[.99]" onClick={() => openDialog(true)}>Create new CV</button>
			</div>

			<div>
				{
					cvs.length === 0 ? (
						<div className="flex justify-center items-center min-h-[calc(100vh-200px)] flex-col">
							<img src="/emptycv.svg" alt="" className="w-[240px]" />
							<h2 className="text-xl font-bold text-center selection:bg-primary selection:text-white">Looks like you haven&apos;t unleashed your CV awesomeness onto the world just yet!</h2>
						</div>
					) : (
						<div>

						</div>
					)
				}
			</div>
			{
				dialog && <NewCVDialog handleClose={onDialogClose} />
			}
		</div>
	)
}