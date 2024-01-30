import { Outlet } from "react-router-dom";
import NavBar from "../components/navigation/Navbar";
import Footer from "../components/navigation/Footer";



const MainLayout = () => {

	return (
		<>{/*  */}
			<NavBar />
			<main>
				<Outlet />
			</main>
			<Footer />
		</>
	)
}

export default MainLayout;