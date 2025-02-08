import { Link } from '@tanstack/react-router';
import { CiUser } from 'react-icons/ci';

function Navbar() {
  return (
    <nav className="bg-green-900 p-3">
      <div className="flex items-center justify-between w-full">
        <Link to="/" className="text-white text-5xl">PAM</Link>
        <div className="flex items-center space-x-4">
          <Link to="/" className="text-white text-2xl hover:underline">User</Link>
          <Link to="/">
            <CiUser className="text-white text-4xl" />
          </Link>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;

