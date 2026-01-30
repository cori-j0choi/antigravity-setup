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

        console.log('\n📦 Installing dependencies...');
        try {
            execSync('npm install', { cwd: targetDir, stdio: 'inherit' });
        } catch (e) {
            console.warn('⚠️ Dependency installation failed. Please run "npm install" manually.');
        }

        // Context Analysis
        const analyzeScript = path.join(targetDir, 'bin', 'analyze.js');
        if (fs.existsSync(analyzeScript)) {
            console.log('\n🔍 Starting Context Analysis...');
            try {
                const { spawnSync } = require('child_process');
                spawnSync('node', [analyzeScript], { stdio: 'inherit' });
            } catch (e) {
                console.warn('⚠️ Analysis script failed:', e.message);
            }
        }

        // Auto-Configuration (.cursorrules)
        const configScript = path.join(targetDir, 'bin', 'configure.js');
        if (fs.existsSync(configScript)) {
            try {
                const { spawnSync } = require('child_process');
                spawnSync('node', [configScript], { stdio: 'inherit' });
            } catch (e) {
                console.warn('⚠️ Configuration script failed:', e.message);
            }
        }

        console.log('\n✅ Installation Successful!');
        console.log(`\nLocation: ${targetDir}`);
        console.log('\nNext Steps:');
        console.log(`  1. cd "${targetDir}"`);
        console.log('  2. Configure mcp/mcp_config.json');
        console.log('  3. Start using the agent!');

    } catch (err) {
        console.error('\n❌ Installation Failed:', err.message);
        process.exit(1);
    }
}

main();
