# Ryan Hance · Kyndryl Fit Map

An interactive view of three Kyndryl job descriptions: Senior Experience Strategist, Senior Experience Designer, and AI Enablement Specialist. Tabs switch between the roles. Underlined phrases open a side panel with notes from Ryan's career experience relevant to that part of the role.

**Live page:** https://ryanlhance.github.io/kyndryl/

## How it works

- `index.html` + `styles.css` + `app.js` are a static page, no build step, no dependencies.
- `data.json` holds all page content: the job descriptions, the highlighted phrases, and the experience notes each phrase opens. The roles share one pool of experience notes.
- `build_data.py` is a convenience generator for `data.json`. Edit it and run `python3 build_data.py`.

## Run locally

The page fetches `data.json`, so it needs http:

```
python3 serve.py 8000
```

then open http://localhost:8000/.
