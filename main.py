from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Tuple
import random
import math

app = FastAPI()

class PathResponse(BaseModel):
    path: List[Tuple[int, int]]

@app.get("/simulate_golf_ball_path", response_model=PathResponse)
def simulate_golf_ball_path():
    # Parameters for the parabolic trajectory
    start_x = 720
    start_y = 850
    velocity = 125  # Initial velocity
    angle = 88  # Launch angle in degrees
    g = 9.81  # Gravity

    # Convert angle to radians
    angle_rad = math.radians(angle)

    # Time step for simulation
    time_step = 0.1

    path = []
    t = 0
    while True:
        x = start_x + (velocity * math.cos(angle_rad) * t)
        y = start_y - ((velocity * math.sin(angle_rad) * t) - (0.5 * g * t * t))

        if x >= 750 and y > 440:
            break
        if y < 0:
            y = 0
            break

        path.append({'x': int(x), 'y': int(y)})
        t += time_step
    
    return PathResponse(path=path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

