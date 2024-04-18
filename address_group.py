def create_firewall_config_from_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        addresses = input_file.readlines()

    # Remove leading and trailing whitespaces, and filter out empty lines
    addresses = [address.strip() for address in addresses if address.strip()]

    with open(output_file_path, 'w') as output_file:
        for address in addresses:
            output_file.write(f"    edit H-{address}\n")
            output_file.write(f"        set subnet {address} 255.255.255.255\n")
            output_file.write(f"    next\n")
            

    print(f"Configuration file '{output_file_path}' created successfully!")

# Example usage
input_file_path = 'addresses.txt'  # Path to the input text file containing addresses
output_file_path = 'firewall_config.txt'  # Path to the output configuration file
create_firewall_config_from_file(input_file_path, output_file_path)
