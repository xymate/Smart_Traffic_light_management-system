Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Import necessary libraries
import time
import random
import numpy as np
from sklearn.cluster import KMeans

# Define the traffic light class
class TrafficLight:
    def __init__(self, n_lights):
        self.n_lights = n_lights
        self.state = np.zeros(n_lights, dtype=int)
        self.green_duration = np.ones(n_lights, dtype=int)
    
    def __repr__(self):
        return f"TrafficLight(state={self.state}, green_duration={self.green_duration})"
    
    def update(self, intensity):
        # Cluster the intensity values
        kmeans = KMeans(n_clusters=self.n_lights, random_state=0).fit(intensity.reshape(-1, 1))
        centers = kmeans.cluster_centers_
        labels = kmeans.labels_
        
        # Update the green durations based on the cluster centers
        self.green_duration = (centers / centers.sum() * 10).astype(int)
        
        # Update the state of the traffic lights
        for i in range(self.n_lights):
            if self.state[i] == 0:
                if labels[i] == 0:
                    self.state[i] = 1
            else:
                if self.green_duration[i] == 0:
                    self.state[i] = 0
                else:
                    self.green_duration[i] -= 1

# Define the main function
def main():
    # Initialize the traffic light
    traffic_light = TrafficLight(n_lights=3)
    
    # Start the simulation loop
    for t in range(100):
        # Generate random traffic intensity values
        intensity = np.array([random.randint(0, 10) for _ in range(3)])
        
        # Update the traffic light
        traffic_light.update(intensity)
        
        # Print the traffic light state and green durations
        print(f"t={t}, {traffic_light}")
        
        # Wait for 1 second
        time.sleep(1)

if __name__ == '__main__':
    main()
