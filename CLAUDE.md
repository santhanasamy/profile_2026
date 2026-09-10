# Profile Resume Repository

## Files
- `index.html` — Primary resume (uses external `web.css`)
- `Resume_Aug_2026_outside.html` — Self-contained resume with inline `<style>` block
- `web.css` — Shared stylesheet for `index.html`

Both HTML files must stay in sync — any content or structural change applies to both.

## CSS Architecture

All styling uses CSS classes — **never use inline `style` attributes** on HTML elements.

### Key CSS Classes
| Class | Purpose |
|-------|---------|
| `.section` | Top-level resume section (Summary, Skills, Experience, etc.) |
| `.section-title` | Blue-underlined uppercase section header |
| `.project-title` | Client or project heading (e.g. "Capital One Banking Android") |
| `.sub-section-title` | Blue sub-header within an employer (e.g. "Key Responsibilities & Initiatives") |
| `.sub-project-title` | Nested project under a client (e.g. "Connect PaySDK" under Fiserv) |
| `.project-context` | Italic context line below a project title |
| `.client-block` | Separates clients within the same employer — dashed border-top with 14px margin |
| `.employer-block` | Separates different employers — solid border-top with 14px margin |
| `.no-break` | Prevents page-break inside the block |
| `.page-break` | Forces page break before the element |

### Spacing Rules
- Sections: `margin-bottom: 12px`
- Employer blocks: `margin-top: 10px` (via `.employer-block`)
- Project titles: `margin-top: 6px; margin-bottom: 2px`
- Sub-project titles: `margin-top: 5px; margin-bottom: 2px`
- Sub-section titles: `margin-top: 8px; margin-bottom: 4px`
- Bullet items: `margin-bottom: 1px; line-height: 1.45`
- No extra margin utilities (`mt-6`, `mt-12`, etc.) — spacing is baked into class definitions

## Print / Export Rules
- Page size: US Letter (8.5 x 11in), margins 0.5in top/bottom, 0.6in left/right
- Content must fill pages properly — no wasted whitespace above or below
- After a `.page-break`, the next `.no-break` element gets `margin-top: 0` in `@media print`
- First employer block on page 2 should have no top margin
- Colors print correctly via `print-color-adjust: exact`

## When Making Changes
1. Always update both `index.html` and `Resume_Aug_2026_outside.html`
2. If adding a new CSS class, add it to both `web.css` and the `<style>` block in the self-contained file
3. Use semantic class names, not inline styles
4. Verify section hierarchy: Section > Employer > Client/Project > Sub-project
5. Keep both files structurally identical in content; only difference is CSS delivery method
