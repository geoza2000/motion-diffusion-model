def test_malformed_data_detection():
    malformed_data = np.array([[np.inf, np.nan, 1.0]])
    with pytest.raises(ValueError, match="Invalid or malicious input"):
        dataset.process_input(malformed_data)

adv_input = generate_adversarial_example(original_input)
response = model.infer(adv_input)