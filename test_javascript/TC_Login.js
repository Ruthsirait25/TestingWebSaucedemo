const { Builder, By, until } = require('selenium-webdriver');

(async function saucedemoTests() {
    const driver = await new Builder().forBrowser('chrome').build();
    const waitTime = 5000;
    const url = 'https://www.saucedemo.com/';

    async function login(username, password) {
        await driver.get(url);
        const userField = await driver.findElement(By.id('user-name'));
        const passField = await driver.findElement(By.id('password'));
        const loginBtn = await driver.findElement(By.id('login-button'));

        await userField.clear();
        await userField.sendKeys(username);
        await passField.clear();
        await passField.sendKeys(password);
        await loginBtn.click();
    }

    async function getErrorMessage() {
        try {
            const errorElement = await driver.wait(
                until.elementLocated(By.xpath("//h3[@data-test='error']")),
                waitTime
            );
            return (await errorElement.getText()).trim();
        } catch (e) {
            return null;
        }
    }

    // Test Case 1: Login dengan kredensial benar
    console.log('Test Case 1: Login dengan kredensial benar');
    await login('standard_user', 'secret_sauce');
    if ((await driver.getCurrentUrl()).includes('inventory')) {
        console.log('PASS: Login berhasil');
    } else {
        console.log('FAIL: Login gagal');
    }

    // Test Case 2: Login dengan password salah
    console.log('\nTest Case 2: Login dengan password salah');
    await login('standard_user', 'wrong_password');
    let errorMessage = await getErrorMessage();
    console.log('[DEBUG] Pesan error:', errorMessage);
    if (errorMessage && errorMessage.toLowerCase().includes('do not match any user')) {
        console.log('PASS: Error message muncul');
    } else {
        console.log('FAIL: Tidak ada atau salah error message');
    }

    // Test Case 3: Login tanpa username
    console.log('\nTest Case 3: Login tanpa username');
    await login('', 'secret_sauce');
    errorMessage = await getErrorMessage();
    console.log('[DEBUG] Pesan error:', errorMessage);
    if (errorMessage && errorMessage.toLowerCase().includes('username is required')) {
        console.log('PASS: Error message muncul');
    } else {
        console.log('FAIL: Tidak ada atau salah error message');
    }

    await driver.quit();
})();