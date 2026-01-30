const { ensureDir, SESSIONS_DIR, MEMORY_DIR, log } = require('../lib/utils');
const fs = require('fs');
const path = require('path');

async function main() {
    ensureDir(SESSIONS_DIR);

    const lessonsDir = path.join(MEMORY_DIR, 'lessons');
    ensureDir(lessonsDir);

    // 1. Load Lessons
    const lessons = fs.readdirSync(lessonsDir).filter(f => f.endsWith('.md'));
    if (lessons.length > 0) {
        log(`📚 Found ${lessons.length} learned insights in memory/lessons/.`);
        console.error(`[Context] Loading ${lessons.length} lessons...`);
    } else {
        log(`ℹ️ No prior lessons found. Run /learn after this session.`);
    }

    // 2. Check Previous Session
    const sessions = fs.readdirSync(SESSIONS_DIR).filter(f => f.endsWith('.md')).sort().reverse();
    if (sessions.length > 0) {
        const lastSession = sessions[0];
        log(`Last session: ${lastSession}`);
    }

    log(`🚀 Antigravity Session Started. Use /plan to begin.`);
}

main();
