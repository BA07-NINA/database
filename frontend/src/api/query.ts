import { Device } from "@/types";
import { queryOptions } from "@tanstack/react-query";

const API_URL = 'http://localhost:3001/devices';

const fetchDevices = async (): Promise<Device[]> => {
    const response = await fetch(API_URL);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  };

export const devicesQueryOptions = queryOptions<Device[]>({
    queryKey: ['devices'], // The unique key for this query
    queryFn: fetchDevices, // The function to fetch data
})

const fetchDeviceById = async (id: string): Promise<Device> => {
    const response = await fetch(`${API_URL}/${id}`);
    if (!response.ok) {
      throw new Error(`Device not found (ID: ${id})`);
    }
    return response.json();
};

export const deviceQueryOptions = (deviceId: string) => queryOptions<Device>({
    queryKey: ['device', deviceId],
    queryFn: () => fetchDeviceById(deviceId),
});