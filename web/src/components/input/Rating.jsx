import { useState } from "react"
import StarIcon from '@mui/icons-material/Star';
import StarBorderIcon from '@mui/icons-material/StarBorder';
import IconButton from "@mui/material/IconButton";

export default function Rating() {
	const [rating, setRating] = useState(0)

	const handleRatingSet = (r) => {
		setRating(r)
	}
	return (
		<div>
			<span>
				{
					rating >= 1 ? <IconButton>
						<StarIcon />
					</IconButton> : <IconButton onClick={() => handleRatingSet(1)}>
						<StarBorderIcon />
					</IconButton>
				}
			</span>
			<span>
				{
					rating >= 2 ? <IconButton>
						<StarIcon />
					</IconButton> : <IconButton onClick={() => handleRatingSet(2)}>
						<StarBorderIcon />
					</IconButton>
				}
			</span>
			<span>
				{
					rating >= 3 ? <IconButton>
						<StarIcon />
					</IconButton> : <IconButton onClick={() => handleRatingSet(3)}>
						<StarBorderIcon />
					</IconButton>
				}
			</span>
			<span>
				{
					rating >= 4 ? <IconButton>
						<StarIcon />
					</IconButton> : <IconButton onClick={() => handleRatingSet(4)}>
						<StarBorderIcon />
					</IconButton>
				}
			</span>
			<span>
				{
					rating >= 5 ? <IconButton>
						<StarIcon />
					</IconButton> : <IconButton onClick={() => handleRatingSet(5)}>
						<StarBorderIcon />
					</IconButton>
				}
			</span>
		</div>
	)
}