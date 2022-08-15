import os
from os import listdir
from .parserC import parser
from .CodeGeneration import cgen, function_declaration, reset_function_declaration_phase
from .SymbolTable import *
from .preloadfunctions import code_predified_functions
import sys


def get_mips_code(input_content):
    reset_function_declaration_phase()
    input_content = code_predified_functions + input_content
    parse_tree, code = parser(input_content)
    symbol_table = SymbolTable()
    symbol_table.push_scope(Scope())
    function_declaration(parse_tree, symbol_table)
    mips_code = cgen(parse_tree, symbol_table).code
    return mips_code


def run(input_content: str, complete_code: bool) -> str:
    if complete_code:
        input_content = code_predified_functions + input_content
    try:
        parse_tree, code = parser(input_content)
        try:
            symbol_table = SymbolTable()
            symbol_table.push_scope(Scope())
            function_declaration(parse_tree, symbol_table)
            mips_code = cgen(parse_tree, symbol_table).code
            return mips_code
        except:
            code = get_mips_code('''
                                int main(){
                        Print("Semantic Error");
                    }
                ''')
            return code
    except:
        return get_mips_code('''
                           int main(){
                        Print("Syntax Error");
                    }
            ''')
