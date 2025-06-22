from core.config import get_config

def test_config():
    # Load configuration
    config = get_config()
    
    # Test browser config
    print(f"Browser headless: {config.browser.headless}")
    print(f"Browser timeout: {config.browser.timeout}ms")
    print(f"Viewport: {config.browser.viewport_width}x{config.browser.viewport_height}")
    
    # Test performance config
    print(f"\nMax sessions: {config.performance.max_concurrent_sessions}")
    print(f"Max retries: {config.performance.max_retries}")
    
    # Test that we can access the same instance
    config2 = get_config()
    assert config is config2, "Config should be a singleton"
    print("\n✓ Config singleton working correctly")

if __name__ == "__main__":
    test_config()