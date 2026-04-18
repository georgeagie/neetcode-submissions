class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> operands = new Stack<>();
        for (String token: tokens) {
            try {
                Integer operand = Integer.parseInt(token);
                operands.push(operand);
            } catch (NumberFormatException e) {
                int op2 = operands.pop();
                int op1 = operands.pop();
                if (token.equals("+")) operands.push(op1 + op2);
                else if (token.equals("-")) operands.push(op1 - op2);
                else if (token.equals("*")) operands.push(op1 * op2);
                else operands.push(op1 / op2);
            }
        }
        return operands.pop();
    }
}
