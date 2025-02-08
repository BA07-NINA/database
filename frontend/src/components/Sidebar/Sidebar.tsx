import { Link} from '@tanstack/react-router'

function Sidebar() {
  return(
    <div className="min-h-screen min-w-10 bg-gray-50">
      <nav className="w-64 bg-white">
        <div className="flex flex-col space-y-1 p-3">
          <Link to="/" className="[&.active]:font-bold">
            Overview
          </Link>{' '}
          <Link to="/about" className="[&.active]:font-bold">
            About
          </Link>
        </div>
      </nav>
    </div>
    
  )
}

export default Sidebar;