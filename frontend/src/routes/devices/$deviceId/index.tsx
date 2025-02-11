import { useState } from 'react';
import { deviceQueryOptions } from '@/api/query';
import DeviceNav from '@/components/pagenav/DeviceNav';
import { useSuspenseQuery } from '@tanstack/react-query';
import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/devices/$deviceId/')({
  loader: async ({ params: { deviceId }, context: { queryClient } }) => {
    await queryClient.prefetchQuery(deviceQueryOptions(deviceId));
    return { deviceId };
  },
  component: RouteComponent,
});

function RouteComponent() {
  const { deviceId } = Route.useParams();
  const { data: device } = useSuspenseQuery(deviceQueryOptions(deviceId));

  const [activeTab, setActiveTab] = useState<'details' | 'audioFiles'>('details');

  return (
    <div>
      <DeviceNav
        deviceId={device.id}
        activeTab={activeTab}
        setActiveTab={setActiveTab}
      />

      {activeTab === 'details' && (
        <div>
          <h2>Device Details</h2>
          <p>ID: {device.id}</p>
        </div>
      )}
      {activeTab === 'audioFiles' && (
        <div>
          <h2>Audio Files</h2>
          {/* Render audio files or related component here */}
          <p>List of audio files for device {device.id}...</p>
        </div>
      )}
    </div>
  );
}
