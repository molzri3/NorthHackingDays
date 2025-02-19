import os

def compile_and_run(input_file):
    compile_command = f"gcc {input_file} -o code"
    compile_result = os.system(compile_command)

    if compile_result == 0:
        print("Compilation successful.")
        print("Running the program...")
        run_result = os.system("./code")

        if run_result == 0:
            print("Program executed successfully.")
        else:
            print("Program execution failed.")
    else:
        print("Compilation failed. Please check the source code.")

def main():
    input_code = input("Enter the input C script: ")
    
    with open("code.c", "w") as file:
        for ch in input_code:
            if ch in ['[', ']', '{', '}', '\\', '#']:
                print("Ma3endek zher abana !!")
                return  
            else:
                file.write(ch)

    compile_and_run("code.c")

if __name__ == "__main__":
    main()
