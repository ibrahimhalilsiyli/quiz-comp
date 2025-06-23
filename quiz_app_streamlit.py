import streamlit as st

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

st.title("Computer Architecture Quiz")

if 'current' not in st.session_state:
    st.session_state.current = 0
    st.session_state.user_answers = [None] * len(QUESTIONS)
    st.session_state.finished = False
    st.session_state.show_feedback = False
    st.session_state.last_correct = None
    st.session_state.last_explanation = ""

def next_question():
    if st.session_state.current < len(QUESTIONS) - 1:
        st.session_state.current += 1
        st.session_state.show_feedback = False

def prev_question():
    if st.session_state.current > 0:
        st.session_state.current -= 1
        st.session_state.show_feedback = False

def finish_quiz():
    st.session_state.finished = True

def select_option(idx):
    st.session_state.user_answers[st.session_state.current] = idx
    correct = idx == QUESTIONS[st.session_state.current]["answer"]
    st.session_state.last_correct = correct
    st.session_state.last_explanation = QUESTIONS[st.session_state.current].get("explanation", "")
    st.session_state.show_feedback = True

if not st.session_state.finished:
    q = QUESTIONS[st.session_state.current]
    st.subheader(f"Question {st.session_state.current + 1} of {len(QUESTIONS)}")
    st.write(q["question"])
    options = q["options"]
    answered = st.session_state.user_answers[st.session_state.current] is not None
    # Show options as big buttons
    for i, opt in enumerate(options):
        btn_key = f"option_{st.session_state.current}_{i}"
        if answered:
            # Show which was selected, and disable all
            if st.session_state.user_answers[st.session_state.current] == i:
                st.button(f"{chr(65+i)}. {opt}", key=btn_key, disabled=True, use_container_width=True)
            else:
                st.button(f"{chr(65+i)}. {opt}", key=btn_key, disabled=True, use_container_width=True)
        else:
            if st.button(f"{chr(65+i)}. {opt}", key=btn_key, use_container_width=True):
                select_option(i)
    # Feedback
    if st.session_state.show_feedback:
        if st.session_state.last_correct:
            st.markdown("<h2 style='color:green;'>CORRECT</h2>", unsafe_allow_html=True)
        else:
            st.markdown("<h2 style='color:red;'>INCORRECT</h2>", unsafe_allow_html=True)
            st.write(f"Correct answer: {options[q['answer']]}")
        if st.session_state.last_explanation:
            st.info(st.session_state.last_explanation)
    # Navigation
    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        st.button("Previous", on_click=prev_question, disabled=st.session_state.current == 0)
    with col2:
        st.button("Finish Exam", on_click=finish_quiz)
    with col3:
        st.button("Next", on_click=next_question, disabled=st.session_state.current == len(QUESTIONS) - 1)
else:
    score = sum(1 for i, q in enumerate(QUESTIONS) if st.session_state.user_answers[i] == q["answer"])
    percent = (score / len(QUESTIONS)) * 100
    st.success(f"Exam Finished! Your score: {score} / {len(QUESTIONS)} ({percent:.1f}%)")
    if st.button("Restart"):
        st.session_state.current = 0
        st.session_state.user_answers = [None] * len(QUESTIONS)
        st.session_state.finished = False
        st.session_state.show_feedback = False
        st.session_state.last_correct = None
        st.session_state.last_explanation = "" 