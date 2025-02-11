import { Device } from '@/types'
import { Link } from '@tanstack/react-router'

function DeviceNav(device: Device) {
  return (
    <nav className="device-nav">
      <ul>
        <li>
          <Link to="/device/deviceDashboard" className="[&.active]:font-bold">
            Device Dashboard
          </Link>
        </li>
        <li>
          <Link to="/device/deviceFiles" className="[&.active]:font-bold">
            Device Files
          </Link>
        </li>
      </ul>
    </nav>
  )
}

export default DeviceNav