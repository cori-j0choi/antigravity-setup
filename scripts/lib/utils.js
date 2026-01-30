const fs = require('fs');
const path = require('path');

// Common paths
const ROOT_DIR = process.cwd();
const MEMORY_DIR = path.join(ROOT_DIR, 'memory');
const SESSIONS_DIR = path.join(MEMORY_DIR, 'sessions');

function ensureDir(dirPath) {
    if (!fs.existsSync(dirPath)) {
        fs.mkdirSync(dirPath, { recursive: true });
    }
}

function log(message) {
    console.error(`[Antigravity] ${message}`);
}

function getTodayString() {
    return new Date().toISOString().split('T')[0];
}

module.exports = {
    ROOT_DIR,
    MEMORY_DIR,
    SESSIONS_DIR,
    ensureDir,
    log,
    getTodayString
};
