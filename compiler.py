import argparse
from tokenizer import tokenize
from my_parser import Parser
from semantic_analyzer import SemanticAnalyzer
from code_generator import CodeGenerator
from final_code_generator import FinalCodeGenerator

def read_code_from_file(file_path: str) -> str:
    
    with open(file_path, 'r') as file:
        return file.read()

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="A simple compiler for a dummy language.")
    parser.add_argument('-f', '--file', type=str, required=True, help="Path to the source code file.")
    args = parser.parse_args()

    # Read source code from file
    if args.file:
        code = read_code_from_file(args.file)
    else:
        print("No input file provided. Use -f to specify a file.")
        return

    # Lexical Analysis
    tokens = tokenize(code)

    # Syntax Analysis
    parser = Parser(tokens)
    ast = parser.parse()

    # Semantic Analysis
    semantic_analyzer = SemanticAnalyzer()
    semantic_analyzer.analyze(ast)

    # Intermediate Code Generation
    code_generator = CodeGenerator()
    code_generator.generate(ast)

    # Final Code Generation
    final_code_generator = FinalCodeGenerator()
    # Generate output file name based on input file name and write generated code
    output_file = final_code_generator.generate(code_generator.code, args.file)

    # Print message indicating where the output file was written
    print(f"Generated code has been written to {output_file}")

if __name__ == "__main__":
    main()
