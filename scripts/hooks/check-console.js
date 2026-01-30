const fs = require('fs');

async function main() {
    // Read input from stdin (standard protocol for hooks)
    let inputData = '';
    process.stdin.on('data', chunk => inputData += chunk);

    process.stdin.on('end', () => {
        try {
            const input = JSON.parse(inputData);
            const filePath = input.tool_input?.file_path;

            if (filePath && fs.existsSync(filePath)) {
                const content = fs.readFileSync(filePath, 'utf8');
                const lines = content.split('\n');
                const matches = [];

                lines.forEach((line, index) => {
                    if (line.includes('console.log')) {
                        matches.push(`Line ${index + 1}: ${line.trim()}`);
                    }
                });

                if (matches.length > 0) {
                    console.error(`[Hook] ⚠️  console.log detected in ${filePath}:`);
                    matches.slice(0, 3).forEach(m => console.error(`  ${m}`));
                    if (matches.length > 3) console.error(`  ... and ${matches.length - 3} more`);
                }
            }
        } catch (e) {
            // Ignore parsing errors or invalid inputs
        }
    });
}

main();
