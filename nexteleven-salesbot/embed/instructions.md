## Web embed instructions (Botpress Cloud)

1) In Botpress Cloud, open your bot → Deploy → Webchat → Copy snippet.
2) Paste the snippet before `</body>` on your site. For local demo, use `embed/web-widget.html`.
3) Set bot name, theme, and position in the channel settings.

Example placeholder snippet (replace with your live snippet):
```html
<script src="https://cdn.botpress.cloud/webchat/v2/inject.js"></script>
<script src="https://cdn.botpress.cloud/webchat/v2/config.js"></script>
<script>
  window.botpressWebChat.init({
    botId: "nexteleven-salesbot",
    clientId: "YOUR_CLIENT_ID",
    composerPlaceholder: "Ask about pricing, features, or request a demo",
    themeName: "prism",
  });
  window.botpressWebChat.onEvent(function() {
    window.botpressWebChat.sendEvent({ type: 'proactive-trigger', channel: 'web' });
  }, ['LIFECYCLE.LOADED']);
  window.botpressWebChat.onEvent(function() {
    window.botpressWebChat.sendPayload({ type: 'proactive-message', text: 'Hi! I\'m the NextEleven SalesBot. Want pricing or a quick demo?' });
  }, ['WEBCHAT.OPEN']);
  window.botpressWebChat.renderPopup();
</script>
```

