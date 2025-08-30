# STRICT DESIGN POLICY - NO EXCEPTIONS

## CRITICAL: Index Page is the ONLY Template Allowed

**UNDER NO CIRCUMSTANCES IS THE DESIGN ALLOWED TO DEVIATE IN THE SLIGHTEST**

### Design Template
- **ONLY TEMPLATE**: `complete-islamic-study-guide-dark.html` (the index page)
- **NO EXCEPTIONS**: Every single page, subpage, link, and component must use this exact design
- **ZERO TOLERANCE**: Any deviation from this design is strictly forbidden

### Required Elements (Must Match Index Page Exactly)
1. **CSS Variables**: Exact same color scheme, shadows, borders
2. **Typography**: Georgia, Times New Roman, serif font family
3. **Layout**: Same container, header, content sections, spacing
4. **Colors**: `--bg-primary: #0a0f0f`, `--accent-primary: #10b981`, etc.
5. **Shadows**: `--shadow-primary: 0 8px 32px rgba(0, 0, 0, 0.3)`
6. **Borders**: `border: 2px solid var(--accent-primary)`
7. **Responsive Design**: Identical media queries and mobile behavior

### EMOJIS ARE EXPLICITLY FORBIDDEN
- **NO EMOJIS**: This is a serious Islamic research application
- **NO EMOJI CHARACTERS**: Remove all emoji symbols
- **NO EMOJI TEXT**: Remove emoji-related descriptions
- **PROFESSIONAL INTERFACE**: Maintain serious, scholarly appearance

### Implementation Rules
1. **Copy CSS**: Use exact CSS from index page
2. **Copy Structure**: Use exact HTML structure from index page
3. **Copy Layout**: Use exact grid, spacing, and positioning
4. **Copy Interactions**: Use exact hover effects and transitions
5. **Copy Responsiveness**: Use exact mobile breakpoints

### Verification Process
Before any page is considered complete:
1. Compare with index page side-by-side
2. Verify CSS variables match exactly
3. Verify layout structure matches exactly
4. Verify no emojis are present
5. Verify responsive behavior matches exactly

### Consequences of Violation
- **IMMEDIATE REJECTION**: Any page not matching will be rejected
- **MANDATORY REFIX**: Violating pages must be immediately corrected
- **NO MERGES**: Non-compliant code will not be merged
- **QUALITY STANDARD**: This is a professional Islamic research application

### Template Usage
```html
<!-- ALWAYS use this exact structure from index page -->
<style>
    :root {
        --bg-primary: #0a0f0f;
        --bg-secondary: #1a1a1a;
        --accent-primary: #10b981;
        /* ... exact same variables */
    }
    
    body {
        font-family: 'Georgia', 'Times New Roman', serif;
        /* ... exact same styles */
    }
    
    .container {
        max-width: 1400px;
        margin: 0 auto;
        padding: 1.5rem;
    }
    
    /* ... continue with exact same CSS */
</style>

<div class="container">
    <div class="header">
        <h1>{title}</h1>
        <p>{description}</p>
    </div>
    
    <div class="content-section">
        <h3>{section_title}</h3>
        <div class="links-grid">
            <!-- ... exact same structure -->
        </div>
    </div>
</div>
```

### Final Warning
**THIS IS NOT A SUGGESTION - THIS IS A MANDATORY REQUIREMENT**

Every developer, contributor, and maintainer must follow this policy without exception. The index page design is the foundation of this application's professional appearance and user experience.

**NO DEVIATIONS. NO EXCEPTIONS. NO EMOJIS.**
