#!/usr/bin/env node

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const os = require('os');

const REPO_URL = 'https://github.com/cori-j0choi/antigravity-setup.git';
const DEFAULT_DIR = path.join(os.homedir(), '.agent', 'antigravity-setup');

function main() {
    console.log('🚀 Antigravity Setup Installer');

    // Parse args
    let targetDir = process.argv[2] || DEFAULT_DIR;

    // Resolve absolute path
    if (!path.isAbsolute(targetDir)) {
        targetDir = path.resolve(process.cwd(), targetDir);
    }

    console.log(`\n📦 Target Directory: ${targetDir}`);

    if (fs.existsSync(targetDir)) {
        console.error(`\n❌ Error: Directory already exists at ${targetDir}`);
        console.error('   Please delete it or choose a different location.');
        process.exit(1);
    }

    console.log('\n⏳ Cloning repository...');

    try {
        // Create parent dirs if they don't exist
        fs.mkdirSync(path.dirname(targetDir), { recursive: true });

        // Git clone
        execSync(`git clone ${REPO_URL} "${targetDir}"`, { stdio: 'inherit' });

        console.log('\n✅ Installation Successful!');
        console.log('\nNext Steps:');
        console.log(`  1. cd "${targetDir}"`);
        console.log('  2. npm install');
        console.log('  3. Configure mcp/mcp_config.json');
        console.log('  4. Review README.md');

    } catch (err) {
        console.error('\n❌ Installation Failed:', err.message);
        process.exit(1);
    }
}

main();
