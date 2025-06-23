import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
from typing import Optional

# Full set of questions from quiz_app.py
QUESTIONS = [
    {"question": "How is a 12-bit instruction divided in the described instruction format?", "options": ["Three 4-bit components (nibbles)", "Two 6-bit halves", "Four 3-bit fields", "Six 2-bit pairs"], "answer": 0, "explanation": "A 12-bit instruction is divided into three 4-bit components, called nibbles: opcode, first operand, and second operand."},
    {"question": "What does the Program Counter (PC) do?", "options": ["Stores intermediate results", "Tracks the address of the next instruction", "Acts as a buffer for data", "Points to the last stack address used"], "answer": 1, "explanation": "The Program Counter (PC) keeps track of the memory address of the next instruction to execute."},
    {"question": "Which bus is unidirectional and sends memory addresses from the CPU to memory?", "options": ["Control Bus", "Address Bus", "Data Bus", "Instruction Bus"], "answer": 1, "explanation": "The Address Bus is unidirectional and is used to send memory addresses from the CPU to memory."},
    {"question": "Which type of RAM is used in CPU caches and does not require refreshing?", "options": ["Dynamic RAM (DRAM)", "Static RAM (SRAM)", "Synchronous DRAM (SDRAM)", "Flash Memory"], "answer": 1, "explanation": "Static RAM (SRAM) is faster, more expensive, and used in CPU caches. It does not require refreshing."},
    {"question": "What is the main advantage of Carry Lookahead Adders over Ripple Carry Adders?", "options": ["Lower cost", "Reduced propagation delay", "Simpler design", "Uses fewer gates"], "answer": 1, "explanation": "Carry Lookahead Adders reduce propagation delay by calculating carry signals in advance, making them faster than Ripple Carry Adders."},
    {"question": "Which addressing mode is the fastest?", "options": ["Immediate Addressing", "Direct Addressing", "Indirect Addressing", "Indexed Addressing"], "answer": 0},
    {"question": "What is the function of the Memory Data Register (MDR)?", "options": ["Points to the memory location being accessed", "Acts as a buffer for data fetched from or written to memory", "Tracks the next instruction", "Stores intermediate results"], "answer": 1},
    {"question": "Which instruction set architecture emphasizes simplicity and fixed-length instructions?", "options": ["CISC", "RISC", "SIMD", "VLIW"], "answer": 1},
    {"question": "What does the Arithmetic Logic Unit (ALU) do?", "options": ["Handles real numbers with decimals", "Performs integer arithmetic and logical operations", "Stores instructions", "Controls program flow"], "answer": 1},
    {"question": "Which type of ROM can be erased using ultraviolet light and reprogrammed multiple times?", "options": ["Mask ROM", "PROM", "EPROM", "EEPROM"], "answer": 2},
    {"question": "What is the main function of the BIOS during the boot process?", "options": ["Loads the operating system", "Executes a Power-On Self-Test (POST)", "Manages user input", "Controls the CPU clock speed"], "answer": 1},
    {"question": "Which bus is bidirectional and transfers actual data between the CPU and memory?", "options": ["Control Bus", "Address Bus", "Data Bus", "Instruction Bus"], "answer": 2},
    {"question": "What is the main drawback of Ripple Carry Adders?", "options": ["High cost", "Cumulative delay due to carry propagation", "Complex design", "Limited to 8 bits"], "answer": 1},
    {"question": "Which register holds the instruction currently being executed?", "options": ["Program Counter (PC)", "Current Instruction Register (CIR)", "Memory Address Register (MAR)", "Accumulator (ACC)"], "answer": 1},
    {"question": "What is the function of the Stack Pointer (SP)?", "options": ["Points to the last stack address used", "Stores intermediate results", "Tracks the next instruction", "Acts as a buffer for data"], "answer": 0},
    {"question": "Which addressing mode combines a base address with an index value?", "options": ["Immediate Addressing", "Indexed Addressing", "Relative Addressing", "Base-Displacement Addressing"], "answer": 1},
    {"question": "What is the main purpose of status registers and flag bits?", "options": ["Store instructions", "Record outcomes of previous operations", "Control program flow", "Buffer data"], "answer": 1},
    {"question": "Which logical operation is used to toggle specific bits?", "options": ["AND", "OR", "XOR", "NOT"], "answer": 2},
    {"question": "What is the main function of the Control Bus?", "options": ["Transfers data", "Sends control signals", "Sends memory addresses", "Stores instructions"], "answer": 1},
    {"question": "Which type of memory is commonly used in USB drives and SSDs?", "options": ["Mask ROM", "EPROM", "Flash Memory", "SRAM"], "answer": 2},
    {"question": "What does the Input-Process-Output (IPO) model describe?", "options": ["The boot process", "The flow of data in computing systems", "The structure of a CPU", "The function of buses"], "answer": 1},
    {"question": "Which operation multiplies a binary value by 2?", "options": ["Left Shift (<<)", "Right Shift (>>)", "XOR", "AND"], "answer": 0},
    {"question": "What is the main difference between a half adder and a full adder?", "options": ["Half adder adds two bits, full adder adds two bits and a carry-in", "Half adder is faster", "Full adder uses fewer gates", "Half adder can subtract"], "answer": 0},
    {"question": "Which addressing mode calculates the effective address relative to the program counter?", "options": ["Immediate Addressing", "Direct Addressing", "Relative Addressing", "Indexed Addressing"], "answer": 2},
    {"question": "What is the main function of the Accumulator (ACC)?", "options": ["Stores intermediate results of arithmetic and logical operations", "Points to the last stack address used", "Acts as a buffer for data", "Tracks the next instruction"], "answer": 0},
    {"question": "Which type of adder precomputes results for both carry-in scenarios?", "options": ["Ripple Carry Adder", "Carry Lookahead Adder", "Carry Skip Adder", "Carry Select Adder"], "answer": 3},
    {"question": "What is the main function of the Memory Address Register (MAR)?", "options": ["Points to the memory location being accessed", "Acts as a buffer for data", "Tracks the next instruction", "Stores intermediate results"], "answer": 0},
    {"question": "Which type of RAM is synchronized with the system clock?", "options": ["DRAM", "SRAM", "SDRAM", "EEPROM"], "answer": 2},
    {"question": "What is the main function of the Floating-Point Unit (FPU)?", "options": ["Handles real numbers with decimal points", "Performs integer arithmetic", "Stores instructions", "Controls program flow"], "answer": 0},
    {"question": "Which type of ROM is permanently encoded during manufacturing?", "options": ["Mask ROM", "PROM", "EPROM", "EEPROM"], "answer": 0},
    {"question": "What is the main function of the Update step in the instruction execution cycle?", "options": ["Interpret the instruction", "Perform the operation", "Increment the program counter", "Fetch the next instruction"], "answer": 2},
    {"question": "Which logical operation is used to clear specific bits?", "options": ["AND + NOT", "OR", "XOR", "SHIFT"], "answer": 0},
    {"question": "What is the main function of the Decode Unit implemented as a microprogram?", "options": ["Faster but less flexible", "More flexible and easier to update but slower", "Stores instructions", "Controls program flow"], "answer": 1},
    {"question": "What is the main function of SIMD extensions?", "options": ["Allow one operation to process multiple data points simultaneously", "Store instructions", "Control program flow", "Buffer data"], "answer": 0},
    {"question": "Which type of adder skips unnecessary carry calculations?", "options": ["Ripple Carry Adder", "Carry Lookahead Adder", "Carry Skip Adder", "Carry Select Adder"], "answer": 2},
    {"question": "What is the main function of the barrel shifter?", "options": ["Shifts or rotates data by any number of bits in a single operation", "Performs integer arithmetic", "Stores instructions", "Controls program flow"], "answer": 0},
    {"question": "What is the main function of the Instruction Set Architecture (ISA)?", "options": ["Defines the interface between hardware and software", "Stores instructions", "Controls program flow", "Buffers data"], "answer": 0},
    {"question": "Which type of ROM can be electrically erased and reprogrammed without removal?", "options": ["Mask ROM", "PROM", "EPROM", "EEPROM"], "answer": 3},
    {"question": "What is the main function of the ALU in hardware implementation?", "options": ["Built using combinational logic circuits such as full adders and shifters", "Stores instructions", "Controls program flow", "Buffers data"], "answer": 0},
    {"question": "Which flag indicates a carry out from addition?", "options": ["Zero Flag", "Carry Flag", "Overflow Flag", "Sign Flag"], "answer": 1},
    {"question": "What is the main function of the Accumulator (ACC)?", "options": ["Stores intermediate results of arithmetic and logical operations", "Points to the last stack address used", "Acts as a buffer for data", "Tracks the next instruction"], "answer": 0},
    {"question": "Which operation divides a binary value by 2?", "options": ["Left Shift (<<)", "Right Shift (>>)", "XOR", "AND"], "answer": 1},
    {"question": "What is the main function of the BIOS?", "options": ["Initializes hardware during the boot process", "Stores instructions", "Controls program flow", "Buffers data"], "answer": 0},
    {"question": "Which type of adder reduces propagation delay by calculating carry signals in advance?", "options": ["Ripple Carry Adder", "Carry Lookahead Adder", "Carry Skip Adder", "Carry Select Adder"], "answer": 1},
    {"question": "What is the main function of the IPO model in software development?", "options": ["Defines inputs, process, outputs, and validates the system", "Stores instructions", "Controls program flow", "Buffers data"], "answer": 0},
    {"question": "Which addressing mode combines a base register with a displacement value?", "options": ["Immediate Addressing", "Indexed Addressing", "Relative Addressing", "Base-Displacement Addressing"], "answer": 3},
    {"question": "What is the main function of the Update step in the instruction execution cycle?", "options": ["Interpret the instruction", "Perform the operation", "Increment the program counter", "Fetch the next instruction"], "answer": 2},
    {"question": "Which type of adder connects multiple full adders in series?", "options": ["Ripple Carry Adder", "Carry Lookahead Adder", "Carry Skip Adder", "Carry Select Adder"], "answer": 0},
    {"question": "What is the main function of the Current Instruction Register (CIR)?", "options": ["Holds the instruction currently being executed", "Tracks the next instruction", "Acts as a buffer for data", "Stores intermediate results"], "answer": 0},
    {"question": "Which type of memory is used in main memory and requires constant refreshing?", "options": ["DRAM", "SRAM", "SDRAM", "EEPROM"], "answer": 0},
    {"question": "What is the main function of the Program Counter (PC)?", "options": ["Tracks the address of the next instruction", "Stores intermediate results", "Acts as a buffer for data", "Points to the last stack address used"], "answer": 0},
    {"question": "Which type of ROM can be programmed once after manufacturing?", "options": ["Mask ROM", "PROM", "EPROM", "EEPROM"], "answer": 1},
    {"question": "What is the main function of the Data Bus?", "options": ["Transfers actual data between the CPU and memory", "Sends control signals", "Sends memory addresses", "Stores instructions"], "answer": 0},
    {"question": "Which operation preserves the most significant bit when shifting right?", "options": ["Arithmetic Shift Right", "Logical Shift Right", "Left Shift", "XOR"], "answer": 0},
    {"question": "What is the main function of the Accumulator (ACC)?", "options": ["Stores intermediate results of arithmetic and logical operations", "Points to the last stack address used", "Acts as a buffer for data", "Tracks the next instruction"], "answer": 0},
    {"question": "Which type of adder precomputes results for both carry-in scenarios?", "options": ["Ripple Carry Adder", "Carry Lookahead Adder", "Carry Skip Adder", "Carry Select Adder"], "answer": 3},
    {"question": "What is the main function of the Stack Pointer (SP)?", "options": ["Points to the last stack address used", "Stores intermediate results", "Tracks the next instruction", "Acts as a buffer for data"], "answer": 0}
]

class FormQuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Computer Architecture Quiz - Form Style")
        self.geometry("800x600")
        self.configure(bg="#f7f9fa")
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('TButton', font=("Segoe UI", 14), padding=10, background="#1976d2", foreground="#fff")
        self.style.configure('TLabel', font=("Segoe UI", 14), background="#f7f9fa")
        self.style.configure('Header.TLabel', font=("Segoe UI", 22, "bold"), background="#f7f9fa", foreground="#2d3a4a")
        self.style.configure('Question.TLabel', font=("Segoe UI", 16, "bold"), background="#f7f9fa", foreground="#2d3a4a")
        self.style.configure('Result.TLabel', font=("Segoe UI", 16, "bold"), background="#f7f9fa", foreground="#1976d2")
        self.current = 0
        self.user_answers: list[Optional[int]] = [None] * len(QUESTIONS)
        self.feedback = ""
        self.answered = [False] * len(QUESTIONS)
        self.show_form_question()

    def show_form_question(self):
        for widget in self.winfo_children():
            widget.destroy()
        q = QUESTIONS[self.current]
        header = ttk.Label(self, text="Computer Architecture Quiz", style='Header.TLabel')
        header.pack(pady=10)
        progress = ttk.Progressbar(self, value=self.current, maximum=len(QUESTIONS), length=700)
        progress.pack(pady=10)
        if self.feedback:
            feedback_label = ttk.Label(self, text=self.feedback, style='Result.TLabel', wraplength=700, justify="left")
            feedback_label.pack(pady=5)
        qlabel = ttk.Label(self, text=f"Q{self.current+1} of {len(QUESTIONS)}: {q['question']}", style='Question.TLabel', wraplength=700, justify="left")
        qlabel.pack(pady=18)
        self.selected = tk.IntVar(value=self.user_answers[self.current] if self.user_answers[self.current] is not None else -1)
        self.option_buttons = []
        for i, opt in enumerate(q['options']):
            btn = tk.Button(self, text=f"{chr(65+i)}. {opt}", font=("Segoe UI", 14), width=60, anchor="w",
                            bg="#e3f0fc" if self.selected.get() == i else "#fff",
                            fg="#1976d2" if self.selected.get() == i else "#333",
                            relief="solid", bd=2,
                            command=lambda idx=i: self.select_option(idx))
            btn.pack(pady=6, padx=40, fill="x")
            self.option_buttons.append(btn)
        nav_frame = tk.Frame(self, bg="#f7f9fa")
        nav_frame.pack(pady=30)
        prev_btn = ttk.Button(nav_frame, text="Previous", command=self.prev_question)
        prev_btn.grid(row=0, column=0, padx=10)
        submit_btn = ttk.Button(nav_frame, text="Submit", command=self.submit_answer)
        submit_btn.grid(row=0, column=1, padx=10)
        next_btn = ttk.Button(nav_frame, text="Next", command=self.next_question)
        next_btn.grid(row=0, column=2, padx=10)
        finish_btn = ttk.Button(nav_frame, text="Finish Exam", command=self.finish_exam)
        finish_btn.grid(row=0, column=3, padx=10)
        if self.current == 0:
            prev_btn.state(["disabled"])
        if self.current == len(QUESTIONS)-1:
            next_btn.state(["disabled"])
        # Disable Next unless answered
        if not self.answered[self.current]:
            next_btn.state(["disabled"])

    def select_option(self, idx):
        self.selected.set(idx)
        for i, btn in enumerate(self.option_buttons):
            btn.configure(bg="#e3f0fc" if i == idx else "#fff",
                          fg="#1976d2" if i == idx else "#333")

    def submit_answer(self):
        idx = self.selected.get()
        if idx == -1:
            messagebox.showinfo("No selection", "Please select an answer before submitting.")
            return
        self.user_answers[self.current] = idx
        self.answered[self.current] = True
        correct = idx == QUESTIONS[self.current]['answer']
        explanation = QUESTIONS[self.current].get('explanation', 'No explanation available.')
        if correct:
            self.feedback = "Correct! " + explanation
        else:
            correct_idx = QUESTIONS[self.current]['answer']
            self.feedback = f"Incorrect. The correct answer is {chr(65+correct_idx)}. {QUESTIONS[self.current]['options'][correct_idx]}\nExplanation: {explanation}"
        self.show_form_question()

    def prev_question(self):
        self.feedback = ""
        if self.current > 0:
            self.current -= 1
            self.show_form_question()

    def next_question(self):
        self.feedback = ""
        if self.current < len(QUESTIONS)-1 and self.answered[self.current]:
            self.current += 1
            self.show_form_question()

    def jump_to_question(self, idx):
        self.feedback = ""
        self.current = idx
        self.show_form_question()

    def finish_exam(self):
        score = sum(1 for i, q in enumerate(QUESTIONS) if self.user_answers[i] == q['answer'])
        percent = (score / len(QUESTIONS)) * 100
        summary = f"Exam Finished!\n\nYour score: {score} / {len(QUESTIONS)}\nPercentage: {percent:.1f}%\n\n"
        for i, q in enumerate(QUESTIONS):
            user = self.user_answers[i]
            correct = q['answer']
            summary += f"Q{i+1}: {q['question']}\n"
            for j, opt in enumerate(q['options']):
                mark = "[X]" if user == j else "[ ]"
                correct_mark = " (Correct)" if j == correct else ""
                summary += f"  {mark} {chr(65+j)}. {opt}{correct_mark}\n"
            summary += f"Explanation: {q.get('explanation', 'No explanation available.')}\n\n"
        messagebox.showinfo("Exam Summary", summary)
        self.destroy()

if __name__ == "__main__":
    app = FormQuizApp()
    app.mainloop() 