
document.addEventListener('DOMContentLoaded', () => {
    // --- Element References ---
    const loginSection = document.getElementById('login-section');
    const mainContent = document.getElementById('main-content');
    const loginBtn = document.getElementById('login-btn');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    const loginError = document.getElementById('login-error');
    const logOutput = document.getElementById('log-output');

    const ssidInput = document.getElementById('ssid');
    const powerLevelSelect = document.getElementById('power-level');
    const channelSelect = document.getElementById('channel');
    const saveWifiBtn = document.getElementById('save-wifi-btn');
    const rebootBtn = document.getElementById('reboot-btn');

    const transmitPowerSpan = document.getElementById('transmit-power');
    const effectiveRateSpan = document.getElementById('effective-rate');

    // --- Logging ---
    function log(message) {
        const timestamp = new Date().toLocaleTimeString();
        logOutput.textContent += `[${timestamp}] ${message}\n`;
        logOutput.scrollTop = logOutput.scrollHeight;
    }

    // --- Core Logic ---
    function updateLiveStatus() {
        const power = powerLevelSelect.value;
        const channel = channelSelect.value;

        // 1. Update Transmit Power based on Power Level
        const powerMap = {
            'low': '10 dBm',
            'medium': '15 dBm',
            'high': '20 dBm'
        };
        transmitPowerSpan.textContent = powerMap[power] || 'N/A';

        // 2. Update Effective Rate based on Power and Channel
        let baseRate = 54; // Base Mbps
        if (power === 'medium') baseRate = 72;
        if (power === 'high') baseRate = 150;

        if (channel === '1' || channel === '11') {
            baseRate *= 0.9; // Simulate interference on edge channels
        } else if (channel === '6') {
            baseRate *= 1.1; // Simulate clear channel
        }
        effectiveRateSpan.textContent = `${Math.round(baseRate)} Mbps`;
    }

    // --- Event Listeners ---
    loginBtn.addEventListener('click', () => {
        if (usernameInput.value === 'admin' && passwordInput.value === 'password123') {
            loginSection.classList.add('hidden');
            mainContent.classList.remove('hidden');
            log('Login successful.');
            updateLiveStatus(); // Initial status update
        } else {
            loginError.textContent = 'Invalid username or password.';
            log('Login attempt failed.');
        }
    });

    powerLevelSelect.addEventListener('change', updateLiveStatus);
    channelSelect.addEventListener('change', updateLiveStatus);

    saveWifiBtn.addEventListener('click', () => {
        const newSsid = ssidInput.value;
        const newPower = powerLevelSelect.options[powerLevelSelect.selectedIndex].text;
        const newChannel = channelSelect.options[channelSelect.selectedIndex].text;
        log(`WiFi settings saved: SSID=${newSsid}, Power=${newPower}, Channel=${newChannel}`);
        alert('WiFi settings have been saved!');
    });

    rebootBtn.addEventListener('click', () => {
        log('Router reboot initiated...');
        alert('Router is rebooting!');
        setTimeout(() => { log('Router reboot complete.'); }, 3000);
    });

    log('Admin panel script initialized.');

    // --- Modal Logic ---
    const modal = document.getElementById('generic-modal');
    const backdrop = document.getElementById('modal-backdrop');
    const modalOkBtn = document.getElementById('modal-ok-btn');
    const modalCancelBtn = document.getElementById('modal-cancel-btn');

    // Function to show the modal
    window.editProfile = function(param1, param2, param3, param4) {
        log(`Opening modal with params: ${param1}, ${param2}, ${param3}, ${param4}`);
        
        // Populate modal with data from the button
        document.getElementById('modal-param-1').textContent = param1;
        document.getElementById('modal-param-2').textContent = param2;
        document.getElementById('modal-param-3').textContent = param3;
        document.getElementById('modal-param-4').textContent = param4;
        
        // Show the modal and backdrop
        modal.classList.remove('hidden');
        backdrop.classList.remove('hidden');
    }

    // Function to hide the modal
    function closeModal() {
        modal.classList.add('hidden');
        backdrop.classList.add('hidden');
        log('Modal closed.');
    }

    // Event listeners for modal buttons
    modalOkBtn.addEventListener('click', () => {
        const p2 = document.getElementById('modal-param-2').textContent;
        alert(`'OK' clicked for profile ${p2}!`);
        log(`Modal confirmed for profile ${p2}.`);
        closeModal();
    });

    modalCancelBtn.addEventListener('click', closeModal);
    backdrop.addEventListener('click', closeModal); // Also close on backdrop click
});
