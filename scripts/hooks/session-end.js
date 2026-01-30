const { ensureDir, SESSIONS_DIR, getTodayString, log } = require('../lib/utils');
const fs = require('fs');
const path = require('path');

async function main() {
    ensureDir(SESSIONS_DIR);

    const dateStr = getTodayString();
    const sessionFile = path.join(SESSIONS_DIR, `${dateStr}.session.md`);

    const timestamp = new Date().toISOString();
    let content = `\n## Session End: ${timestamp}\n`;

    // Append to session file
    fs.appendFileSync(sessionFile, content);

    log(`💾 Session log updated: ${sessionFile}`);
    log(`💡 Don't forget to run /learn to extract insights if you haven't already.`);
}

main();
