const express = require('express');
const cors = require('cors');
const path = require('path');
const nodemailer = require('nodemailer');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json({ limit: '1mb' }));

// Serve static files (index.html at project root)
app.use(express.static(path.join(__dirname)));

let transporterPromise = (async () => {
  // Prefer explicit SMTP settings
  if (process.env.SMTP_HOST) {
    return nodemailer.createTransport({
      host: process.env.SMTP_HOST,
      port: Number(process.env.SMTP_PORT || 587),
      secure: Number(process.env.SMTP_PORT) === 465,
      auth: {
        user: process.env.SMTP_USER,
        pass: process.env.SMTP_PASS,
      },
    });
  }

  // Optional: Ethereal for testing (emails are not delivered, but previewable)
  if (String(process.env.ETHEREAL || '').toLowerCase() === 'true') {
    const testAccount = await nodemailer.createTestAccount();
    console.log('Ethereal test account created:', testAccount.user);
    return nodemailer.createTransport({
      host: 'smtp.ethereal.email',
      port: 587,
      auth: {
        user: testAccount.user,
        pass: testAccount.pass,
      },
    });
  }

  // Fallback: JSON transport (logs emails to console)
  console.warn('No SMTP configured. Using JSON transport (emails will NOT be delivered).');
  return nodemailer.createTransport({ jsonTransport: true });
})();

app.get('/api/health', (req, res) => {
  res.json({ ok: true, uptime: process.uptime() });
});

app.post('/api/lead', async (req, res) => {
  try {
    const {
      source = 'unknown',
      businessName = 'N/A',
      industry = 'N/A',
      email,
      avgValue,
      businessType,
      missedDaily,
      messageHistory = [],
    } = req.body || {};

    if (!email) {
      return res.status(400).json({ ok: false, error: 'Email is required' });
    }

    const ownerEmail = process.env.OWNER_EMAIL;
    if (!ownerEmail) {
      return res.status(500).json({ ok: false, error: 'OWNER_EMAIL not configured on server' });
    }

    const transporter = await transporterPromise;

    const subject = `New Free Demo Lead (${source}) - ${businessName || industry}`;

    const plainDetails = `New demo request\n\n` +
      `Source: ${source}\n` +
      `Business Name: ${businessName}\n` +
      `Industry: ${industry}\n` +
      `Lead Email: ${email}\n` +
      (businessType ? `Business Type: ${businessType}\n` : '') +
      (avgValue ? `Avg Value: ${avgValue}\n` : '') +
      (missedDaily ? `Missed Daily: ${missedDaily}\n` : '') +
      `\nConversation Snapshot:\n` +
      messageHistory.map(m => `${m.isUser ? 'User' : 'Bot'} @ ${m.timestamp || ''}: ${m.content}`)
        .slice(-10)
        .join('\n');

    const htmlDetails = `
      <h2>New Demo Request</h2>
      <p><strong>Source:</strong> ${source}</p>
      <p><strong>Business Name:</strong> ${businessName}</p>
      <p><strong>Industry:</strong> ${industry}</p>
      <p><strong>Lead Email:</strong> ${email}</p>
      ${businessType ? `<p><strong>Business Type:</strong> ${businessType}</p>` : ''}
      ${avgValue ? `<p><strong>Avg Value:</strong> ${avgValue}</p>` : ''}
      ${missedDaily ? `<p><strong>Missed Daily:</strong> ${missedDaily}</p>` : ''}
      <h3>Conversation Snapshot</h3>
      <div style="font-family: monospace; white-space: pre-wrap; background:#f6f6f6; padding:12px; border-radius:6px;">
        ${messageHistory.map(m => `${m.isUser ? 'User' : 'Bot'}: ${m.content}`).slice(-10).join('\n')}
      </div>
    `;

    const mail = {
      from: process.env.FROM_EMAIL || ownerEmail,
      to: ownerEmail,
      subject,
      text: plainDetails,
      html: htmlDetails,
    };

    const info = await transporter.sendMail(mail);

    let previewUrl;
    if (nodemailer.getTestMessageUrl && info) {
      previewUrl = nodemailer.getTestMessageUrl(info);
      if (previewUrl) {
        console.log('Preview URL:', previewUrl);
      }
    }

    return res.json({ ok: true, previewUrl });
  } catch (err) {
    console.error('Lead email error:', err);
    return res.status(500).json({ ok: false, error: 'Failed to send lead email' });
  }
});

app.listen(PORT, () => {
  console.log(`Server listening on http://localhost:${PORT}`);
});

