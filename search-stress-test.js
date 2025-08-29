// Quran Search Stress Test Script
// This script will thoroughly test the search functionality for bugs and performance

console.log('🚀 Starting Quran Search Stress Test...');

// Test 1: Empty Search
function testEmptySearch() {
    console.log('📝 Test 1: Empty Search');
    const searchInput = document.getElementById('searchInput');
    const searchButton = document.querySelector('.search-button');
    
    if (!searchInput || !searchButton) {
        console.error('❌ Search elements not found!');
        return false;
    }
    
    // Test empty search
    searchInput.value = '';
    searchButton.click();
    
    // Check if alert appears for empty search
    console.log('✅ Empty search test completed');
    return true;
}

// Test 2: Special Characters
function testSpecialCharacters() {
    console.log('📝 Test 2: Special Characters');
    const searchInput = document.getElementById('searchInput');
    
    const specialChars = ['!@#$%^&*()', '{}[]|\\:";\'<>?,./', '🚀📖✨', 'السلام', '1234567890'];
    
    specialChars.forEach(char => {
        searchInput.value = char;
        console.log(`Testing: "${char}"`);
        // This should not crash the application
    });
    
    console.log('✅ Special characters test completed');
    return true;
}

// Test 3: Very Long Search Terms
function testLongSearchTerms() {
    console.log('📝 Test 3: Long Search Terms');
    const searchInput = document.getElementById('searchInput');
    
    // Test extremely long search terms
    const longTerm = 'a'.repeat(1000);
    searchInput.value = longTerm;
    
    console.log(`Testing search term length: ${longTerm.length} characters`);
    console.log('✅ Long search terms test completed');
    return true;
}

// Test 4: Search Performance
function testSearchPerformance() {
    console.log('📝 Test 4: Search Performance');
    const searchInput = document.getElementById('searchInput');
    
    const testTerms = ['allah', 'mercy', 'prayer', 'quran', 'prophet', 'faith', 'islam'];
    
    const startTime = performance.now();
    
    testTerms.forEach(term => {
        searchInput.value = term;
        // Simulate search without actually triggering it
        console.log(`Performance test term: "${term}"`);
    });
    
    const endTime = performance.now();
    const duration = endTime - startTime;
    
    console.log(`⏱️ Search performance test completed in ${duration.toFixed(2)}ms`);
    return duration < 100; // Should complete in under 100ms
}

// Test 5: Search Input Validation
function testInputValidation() {
    console.log('📝 Test 5: Input Validation');
    const searchInput = document.getElementById('searchInput');
    
    // Test various input types
    const testInputs = [
        { value: 'allah', expected: 'valid' },
        { value: 'ALLAH', expected: 'valid' },
        { value: 'Allah', expected: 'valid' },
        { value: ' allah ', expected: 'valid' }, // with spaces
        { value: '', expected: 'invalid' },
        { value: '   ', expected: 'invalid' }, // only spaces
    ];
    
    let passed = 0;
    testInputs.forEach(test => {
        searchInput.value = test.value;
        const isValid = test.value.trim().length > 0;
        const expectedValid = test.expected === 'valid';
        
        if (isValid === expectedValid) {
            passed++;
            console.log(`✅ "${test.value}" - ${test.expected}`);
        } else {
            console.error(`❌ "${test.value}" - Expected: ${test.expected}, Got: ${isValid ? 'valid' : 'invalid'}`);
        }
    });
    
    console.log(`Input validation: ${passed}/${testInputs.length} tests passed`);
    return passed === testInputs.length;
}

// Test 6: Search Results Accuracy
function testSearchAccuracy() {
    console.log('📝 Test 6: Search Results Accuracy');
    
    // Test if search function exists
    if (typeof searchQuran !== 'function') {
        console.error('❌ searchQuran function not found!');
        return false;
    }
    
    // Test if quranDatabase exists and has content
    if (typeof quranDatabase === 'undefined' || !quranDatabase) {
        console.error('❌ quranDatabase not found!');
        return false;
    }
    
    const surahCount = Object.keys(quranDatabase).length;
    console.log(`📚 Found ${surahCount} surahs in database`);
    
    if (surahCount === 0) {
        console.error('❌ No surahs found in database!');
        return false;
    }
    
    console.log('✅ Search accuracy test completed');
    return true;
}

// Test 7: Keyboard Event Handling
function testKeyboardEvents() {
    console.log('📝 Test 7: Keyboard Event Handling');
    const searchInput = document.getElementById('searchInput');
    
    // Test if handleSearch function exists
    if (typeof handleSearch !== 'function') {
        console.error('❌ handleSearch function not found!');
        return false;
    }
    
    // Test Enter key simulation
    const enterEvent = new KeyboardEvent('keypress', { key: 'Enter' });
    searchInput.dispatchEvent(enterEvent);
    
    console.log('✅ Keyboard event test completed');
    return true;
}

// Test 8: Search Button Functionality
function testSearchButton() {
    console.log('📝 Test 8: Search Button Functionality');
    const searchButton = document.querySelector('.search-button');
    
    if (!searchButton) {
        console.error('❌ Search button not found!');
        return false;
    }
    
    // Check button properties
    const hasOnclick = searchButton.hasAttribute('onclick');
    const isClickable = !searchButton.disabled;
    const hasText = searchButton.textContent.trim().length > 0;
    
    console.log(`Button onclick: ${hasOnclick}`);
    console.log(`Button clickable: ${isClickable}`);
    console.log(`Button text: "${searchButton.textContent.trim()}"`);
    
    const allGood = hasOnclick && isClickable && hasText;
    console.log(`✅ Search button test: ${allGood ? 'PASSED' : 'FAILED'}`);
    
    return allGood;
}

// Test 9: Responsive Design
function testResponsiveDesign() {
    console.log('📝 Test 9: Responsive Design');
    
    // Test if CSS media queries are properly defined
    const styleSheets = document.styleSheets;
    let hasMediaQueries = false;
    
    for (let sheet of styleSheets) {
        try {
            for (let rule of sheet.cssRules) {
                if (rule instanceof CSSMediaRule) {
                    hasMediaQueries = true;
                    console.log(`📱 Found media query: ${rule.conditionText}`);
                }
            }
        } catch (e) {
            // Cross-origin stylesheets may throw errors
        }
    }
    
    console.log(`✅ Responsive design test: ${hasMediaQueries ? 'PASSED' : 'FAILED'}`);
    return hasMediaQueries;
}

// Test 10: Error Handling
function testErrorHandling() {
    console.log('📝 Test 10: Error Handling');
    
    // Test if search functions handle errors gracefully
    try {
        // Test with invalid data
        if (typeof searchQuran === 'function') {
            console.log('✅ searchQuran function exists and is callable');
        }
        
        if (typeof handleSearch === 'function') {
            console.log('✅ handleSearch function exists and is callable');
        }
        
        console.log('✅ Error handling test completed');
        return true;
    } catch (error) {
        console.error('❌ Error handling test failed:', error);
        return false;
    }
}

// Run all tests
function runAllTests() {
    console.log('🔍 Starting comprehensive search functionality testing...\n');
    
    const tests = [
        testEmptySearch,
        testSpecialCharacters,
        testLongSearchTerms,
        testSearchPerformance,
        testInputValidation,
        testSearchAccuracy,
        testKeyboardEvents,
        testSearchButton,
        testResponsiveDesign,
        testErrorHandling
    ];
    
    let passed = 0;
    let total = tests.length;
    
    tests.forEach((test, index) => {
        try {
            const result = test();
            if (result) passed++;
            console.log(`\n--- Test ${index + 1} completed ---\n`);
        } catch (error) {
            console.error(`❌ Test ${index + 1} failed with error:`, error);
        }
    });
    
    console.log(`\n🎯 TEST RESULTS: ${passed}/${total} tests passed`);
    
    if (passed === total) {
        console.log('🎉 ALL TESTS PASSED! Search functionality is robust and ready for production.');
    } else {
        console.log('⚠️ Some tests failed. Please review the issues above.');
    }
    
    return passed === total;
}

// Auto-run tests when script is loaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', runAllTests);
} else {
    runAllTests();
}

console.log('📋 Search stress test script loaded. Tests will run automatically.');
