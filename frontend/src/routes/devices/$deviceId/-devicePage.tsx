import { useState } from 'react';
import DeviceNav from '@/components/pagenav/DeviceNav';
import { Route } from '.';
import DeviceAudioFilesPage from './-deviceAudioFilesPage';
import DeviceDetailPage from './-deviceDetailPage';

export default function DevicePage() {
  const { deviceId } = Route.useParams();
  const [activeTab, setActiveTab] = useState<'details' | 'audioFiles'>('details'); 

  return (
    <div>
      {/* Render the device navigation component */}
      <DeviceNav
        deviceId={deviceId}
        activeTab={activeTab}
        setActiveTab={setActiveTab}
      />

      {activeTab === 'details' && (
        <DeviceDetailPage />
      )}

      {activeTab === 'audioFiles' && (
        <DeviceAudioFilesPage />
      )}
    </div>
  );
}
