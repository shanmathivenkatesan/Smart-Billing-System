/**
 * Smart Billing System - Frontend Logic
 * Simple vanilla JavaScript - no frameworks
 */

const API_URL = 'http://localhost:8000/api';

// Get DOM elements
const generateBtn = document.getElementById('generateBtn');
const loading = document.getElementById('loading');
const billDisplay = document.getElementById('billDisplay');

// Add click event to button
generateBtn.addEventListener('click', generateBill);

/**
 * Main function - Generate a new bill
 */
async function generateBill() {
    try {
        // Show loading
        loading.classList.remove('hidden');
        billDisplay.classList.add('hidden');
        generateBtn.disabled = true;
        
        // Call backend API
        const response = await fetch(`${API_URL}/generate-bill`, {
            method: 'POST'
        });
        
        if (!response.ok) {
            throw new Error('Failed to generate bill');
        }
        
        const data = await response.json();
        
        // Hide loading
        loading.classList.add('hidden');
        generateBtn.disabled = false;
        
        // Display the bill and agent decisions
        displayBill(data);
        
    } catch (error) {
        loading.classList.add('hidden');
        generateBtn.disabled = false;
        alert('Error: ' + error.message + '\n\nMake sure backend is running on http://localhost:8000');
        console.error('Error:', error);
    }
}

/**
 * Display bill information and agent decisions
 */
function displayBill(data) {
    const bill = data.bill;
    const decisions = data.agent_decisions;
    
    // Display bill info
    document.getElementById('billId').textContent = bill.bill_id;
    document.getElementById('timestamp').textContent = bill.timestamp;
    document.getElementById('total').textContent = bill.total;
    
    // Display items
    const itemsList = document.getElementById('itemsList');
    itemsList.innerHTML = '';
    bill.items.forEach(item => {
        const itemDiv = document.createElement('div');
        itemDiv.className = 'item';
        itemDiv.textContent = `${item.name} - Qty: ${item.qty} - ₹${item.price} each`;
        itemsList.appendChild(itemDiv);
    });
    
    // Display Print Decision
    const printDec = decisions.print_decision;
    document.getElementById('printDecision').textContent = 
        printDec.should_print ? '✅ YES - Will Print' : '❌ NO - Digital Only';
    document.getElementById('printDecision').className = 
        printDec.should_print ? 'status-yes' : 'status-no';
    document.getElementById('printReason').textContent = printDec.reason;
    
    // Display Online Status
    const onlineDec = decisions.online_decision;
    document.getElementById('onlineStatus').textContent = 
        onlineDec.is_online ? '🟢 ONLINE' : '🔴 OFFLINE';
    document.getElementById('onlineStatus').className = 
        onlineDec.is_online ? 'status-online' : 'status-offline';
    document.getElementById('onlineReason').textContent = onlineDec.reason;
    document.getElementById('features').textContent = onlineDec.features.join(', ');
    
    // Display Error Detection
    const errorDec = decisions.error_decision;
    document.getElementById('errorStatus').textContent = 
        errorDec.has_error ? '⚠️ ERROR FOUND' : '✅ NO ERRORS';
    document.getElementById('errorStatus').className = 
        errorDec.has_error ? 'status-error' : 'status-ok';
    document.getElementById('errorMessage').textContent = errorDec.message;
    
    // Display Summary
    document.getElementById('summary').textContent = decisions.summary;
    
    // Show the bill display
    billDisplay.classList.remove('hidden');
}

// Log when page loads
console.log('Smart Billing System loaded');
console.log('Make sure backend is running: python backend/main.py');
