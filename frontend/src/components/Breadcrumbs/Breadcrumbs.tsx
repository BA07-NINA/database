import { Link, useLocation } from '@tanstack/react-router';

function Breadcrumbs() {
  const location = useLocation();

  return (
    <nav className="p-3 rounded-md w-full border-b border-gray-300">
      <ol className="list-reset flex text-black">
        <li>
          <Link 
            to="/" 
            className={`hover:underline ${location.pathname === '/' ? 'font-bold text-black' : 'text-black'}`}
          >
            Overview
          </Link>
        </li>
        {location.pathname !== '/' && (
          <>
            <li>
              <span className="mx-2">&gt;</span>
            </li>
            <li>
              <Link 
                to="/about" 
                className={`hover:underline ${location.pathname === '/about' ? 'font-bold text-black' : 'text-black'}`}
              >
                About
              </Link>
            </li>
          </>
        )}
      </ol>
    </nav>
  );
}

export default Breadcrumbs;

