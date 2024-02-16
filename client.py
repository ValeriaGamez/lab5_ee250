import numpy as np
import pandas as pd
import requests
import plotly.express as px

def get_delay(hostname: str, message_size: int) -> int:
    """Get the end-to-end delay to a host.
    
    Args:
        address: The address to check.
        message_size: The size of the message (in bytes) to send.
        
    Returns:
        The delay in milliseconds.
    """
    # create a message of the specified size
    message = ("a" * message_size).encode('utf-8')

    # send the message to the server
    response = requests.post(f"http://{hostname}:5000/delay", data=message)

    # return the delay
    return response.elapsed.total_seconds() * 1000
    
def main():
    # TODO: Choose the best and worst locations from Part 1 to sample the signal strength at
    locations = ['bedroom', 'living room']
    data_sizes = [10, 10**3, 10**6]
    samples = 5

    data = []
    
    for location in locations:
        print(f"Go to the {location} and press enter to start sampling")
        input()
        for size in data_sizes:
            delays = []
            for i in range(samples):
                print(f"[{location}] Sending {size} bytes ({i+1}/{samples})")
                delay = get_delay('172.20.10.10', size)
                delays.append(delay)

            delay_mean = np.mean(delays)
            delay_std = np.std(delays)

            data.append([size, location, delay_mean, delay_std])
        
    # TODO: create a dataframe from the data
    #       Make sure to name the columns appropriately (see the plot below)
    df = pd.DataFrame(data, columns=['size', 'location', 'delay_mean', 'delay_std'])
    
    fig = px.line(
        df,
        x="size",
        y="delay_mean",
        color="location",
        error_y="delay_std",
        title="Delay vs. Message Size",
        labels={
            "size": "Message Size (bytes)",
            "delay_mean": "Delay (ms)",
            "delay_std": "Standard Deviation (ms)",
        },
        log_x=True,
        template="plotly_white",
    )
    # write the plot to a file
    fig.write_image("delay.png")

    # Question 10: Do you notice any trends in the data?
    #              How does it differ from Part 1?
    #              What do you think is causing the differences?


if __name__ == "__main__":
    main()

    
