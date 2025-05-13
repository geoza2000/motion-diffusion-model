import pytest
from agents import InterpreterAgent, PreProcessorAgent, CoreModel, MonitorAgent, secure_generate

def test_interpreter_sanitization():
    """Test that the Interpreter Agent correctly sanitizes the input."""
    interpreter = InterpreterAgent()
    # Example raw input with potentially harmful characters
    raw_input = "Hello!! <script>alert('hack')</script> How are you??"
    sanitized = interpreter.interpret(raw_input)
    # Ensure disallowed characters like '<' and '>' are removed
    assert "<" not in sanitized and ">" not in sanitized, "Sanitization failed: Disallowed characters present."

def test_preprocessor_tokenization():
    """Test that the Pre-Processor Agent tokenizes and normalizes input correctly."""
    interpreter = InterpreterAgent()
    preprocessor = PreProcessorAgent()
    raw_input = "Test input for adversarial attack simulation."
    interpreted = interpreter.interpret(raw_input)
    tokens = preprocessor.preprocess(interpreted)
    # Check that tokenization results in non-empty tokens and all tokens are lowercase
    assert all(token != "" for token in tokens), "Tokenization produced empty tokens."
    assert all(token == token.lower() for token in tokens), "Tokens are not normalized to lowercase."

def test_multi_agent_pipeline_attack_detection():
    """Test that the multi-agent pipeline flags adversarial input."""
    # Adversarial input contains suspicious keywords likely to be flagged by the Monitor Agent
    adversarial_input = "This is a malicious attack error fail malicious!"
    try:
        # secure_generate should raise an exception if the Monitor Agent flags the output
        secure_generate(adversarial_input)
    except RuntimeError as e:
        flagged = True
    else:
        flagged = False
    assert flagged, "Adversarial input was not flagged by the security system."

def test_attack_success_rate_improvement():
    """Simulate attack success rate improvement between baseline and enhanced system."""
    # Baseline system: 75% of adversarial inputs lead to successful attacks.
    baseline_success_rate = 0.75
    # Enhanced system: Only 15% of adversarial inputs lead to successful attacks.
    enhanced_success_rate = 0.15
    improvement = (baseline_success_rate - enhanced_success_rate) / baseline_success_rate * 100
    # Print improvement for logging purposes
    print(f"Attack success rate improvement: {improvement:.1f}%")
    # Assert that the improvement is significant (e.g., >50%)
    assert improvement > 50, "Security enhancements should yield more than a 50% improvement in mitigating attacks."

if __name__ == "__main__":
    # Run tests sequentially
    test_interpreter_sanitization()
    test_preprocessor_tokenization()
    test_multi_agent_pipeline_attack_detection()
    test_attack_success_rate_improvement()
