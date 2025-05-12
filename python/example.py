import noc
import modest 
import re 

def parse_probabilities(output: str) -> list[tuple[int, float]]:
    """Parses the output of the Modest tool to extract probabilities.

    Args:
        output: The output string from the Modest tool.

    Returns:
        A list of floats representing the extracted probabilities along with 
        their associated clock cycle.
        [[clk, prob], [clk, prob], ...]
    """
    probabilities = []
    pattern = r"Property \w+Probability\w+RewardBounded(\d+)\s+Estimated probability:\s+([\d.]+)"
    matches = re.findall(pattern, output)
    
    # Sort matches by the number in the property name
    matches.sort(key=lambda x: int(x[0]))

    for cycle, probability in matches:
        probabilities.append((int(cycle), float(probability)))
    return probabilities

def main():
    """ Example of using the Noc and Modest libaries """    
    # Generate a 2x2 NoC to verify functional correctness
    _2x2 = noc.Noc(2)

    with open("tmp.modest", "w") as f:
        f.write(_2x2.print(noc.PropertyType.FUNCTION))
    return
    
    # Run Modest check on the file to verify it works
    _2x2_output = modest.check(_2x2.print(noc.PropertyType.FUNCTION))
    
    # Check if there were any errors
    if "False" in _2x2_output:
        print("Failed verification for 2x2")
        return 
    else:
        print("Basic 2x2 design verification succeeded")

    
    # If there were no errors, characterize the PSN with a resistive noise 
    # threshold of 5
    done: bool = False
    cycles_per_block: int = 50
    current_cycle: int = 1 
    probabilities = []
    
    while not done:
        # Set the clock bounds
        clk_low = current_cycle
        clk_high = clk_low + cycles_per_block - 1
    
        # Run the PSN characterization
        _2x2_sim_output = modest.simulate(_2x2.print(noc.PropertyType.RESISTIVE, 
                                                     clk_low=clk_low, clk_high=clk_high))
    
        # Check if we have reached a probability of 1.0 yet (with a small margin for
        # floating point error)
        probabilities += _2x2_sim_output

        max_prob = max(probabilities, key=lambda x: x[1])[1]
        if max_prob >= (1.0 - 1e-5):
            break

        # Update which cycle we are starting on 
        current_cycle += cycles_per_block

    print("PSN characterization finished.")
    print("Clk, Probability")
    for clk_cycle, prob in probabilities:
        print(f"{clk_cycle:3}, {prob:3.3f}")

if __name__ == "__main__":
    main()
