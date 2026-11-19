---
applyTo: "frontend/**"
---

# Frontend Instructions

## UI priorities
- Optimize for a clear demo experience rather than visual complexity.
- Make weather information easy to read and understand.
- Keep the interface simple — single-page with one search interaction.

## Required UX behavior
- Provide a city search input with a submit button.
- Display weather information:
  - temperature
  - weather description
  - humidity
  - wind speed
  - short forecast
- Include loading state while fetching weather.
- Include error state for failed requests or invalid cities.
- Include empty state before first search.

## Implementation guidance
- Use Jinja2 templates served by FastAPI.
- Use vanilla JavaScript for API interactions (fetch API).
- Keep CSS minimal — use a simple CSS framework or custom styles.
- No build tools required (no webpack, no npm).
- Components should be in separate template files where practical.

## Quality
- Handle slow or failing API responses gracefully.
- Show user-friendly error messages (not raw JSON errors).
- Ensure basic accessibility (labels, alt text, semantic HTML).
- Test frontend rendering with integration tests where practical.
