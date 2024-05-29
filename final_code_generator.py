import os

class FinalCodeGenerator:
    def generate(self, intermediate_code: list, input_file: str) -> str:
        """
        Generate the final code and write it to a new file.

        Args:
            intermediate_code (list): List of strings representing the intermediate code.
            input_file (str): Path to the input file.

        Returns:
            str: Path to the generated output file.
        """
        # Extract the base name of the input file
        base_name, _ = os.path.splitext(input_file)
        # Generate the output file name by appending "_output.txt" to the base name
        output_file = f"{base_name}_output.txt"
        # Write the intermediate code to the output file
        with open(output_file, 'w') as file:
            for line in intermediate_code:
                file.write(line + '\n')
        # Return the name of the generated output file
        return output_file
