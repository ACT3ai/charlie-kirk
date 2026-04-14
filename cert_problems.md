# Certificate Diagnostic Report — whoassassinatedcharliekirk.com

**Date:** 2026-04-14  
**Tested by:** openssl 3.6.2, curl 8.7.1, nmap 7.99  
**Target:** https://whoassassinatedcharliekirk.com/Influencers/podcasts  
**GitHub repo:** ACT3ai/charlie-kirk → deployed via GitHub Actions → GitHub Pages

---

## TL;DR — Root Cause Found

**The apex domain (no www) works perfectly.** The cert is valid, fresh (issued yesterday), and the full chain verifies.

**The www subdomain fails with a cert error.** `www.whoassassinatedcharliekirk.com` CNAME-points to `act3ai.github.io`, but GitHub Pages serves the `*.github.io` wildcard cert for it — and that wildcard does NOT cover `www.whoassassinatedcharliekirk.com`. Any browser or tool visiting `https://www.whoassassinatedcharliekirk.com` gets a cert mismatch error.

The current Let's Encrypt cert only has one SAN: `whoassassinatedcharliekirk.com`. The `www.` version is not in the cert and has no valid cert at all.

---

## DNS Records

| Record | Type | Value |
|--------|------|-------|
| whoassassinatedcharliekirk.com | A | 185.199.108.153 |
| whoassassinatedcharliekirk.com | A | 185.199.109.153 |
| whoassassinatedcharliekirk.com | A | 185.199.110.153 |
| whoassassinatedcharliekirk.com | A | 185.199.111.153 |
| www.whoassassinatedcharliekirk.com | CNAME | act3ai.github.io |
| whoassassinatedcharliekirk.com | TXT | google-site-verification=Fw1UBvx-... |
| whoassassinatedcharliekirk.com | TXT | google-site-verification=_8R_Gc5f... |
| whoassassinatedcharliekirk.com | CAA | (none — any CA may issue) |

All four A record IPs are GitHub Pages CDN nodes (`cdn-185-199-*.github.com`).

---

## Certificate Details (Parsed)

```yaml
subject: CN=whoassassinatedcharliekirk.com
issuer:
  country: US
  organization: Let's Encrypt
  common_name: R13
chain:
  - depth: 0
    subject: CN=whoassassinatedcharliekirk.com
    issuer: C=US, O=Let's Encrypt, CN=R13
  - depth: 1
    subject: C=US, O=Let's Encrypt, CN=R13
    issuer: C=US, O=Internet Security Research Group, CN=ISRG Root X1
  - depth: 2
    subject: C=US, O=Internet Security Research Group, CN=ISRG Root X1
    issuer: (self-signed root)
validity:
  not_before: "2026-04-13T11:04:27Z"
  not_after:  "2026-07-12T11:04:26Z"
  days_remaining: 88
  issued_days_ago: 1
public_key:
  algorithm: RSA
  bits: 2048
  exponent: 65537
signature_algorithm: sha256WithRSAEncryption
subject_alternative_names:
  - DNS:whoassassinatedcharliekirk.com
  # NOTE: www.whoassassinatedcharliekirk.com is NOT listed here
fingerprints:
  sha256: "10:F4:C2:A2:B7:10:CA:E6:F0:7D:BE:C7:B3:8B:74:CC:E4:3F:12:3A:C1:CE:9C:F5:45:41:26:E6:A4:CE:39:9E"
  sha1: "A9:78:6D:70:AC:8C:16:3A:D2:8B:91:59:A7:AB:48:08:3A:23:5D:50"
  md5: "E7:7D:10:BA:F4:87:5F:22:E8:99:B4:13:F3:AD:0F:17"
x509_extensions:
  key_usage: "Digital Signature, Key Encipherment"
  extended_key_usage: "TLS Web Server Authentication"
  basic_constraints: "CA:FALSE"
  subject_key_id: "58:C9:B2:AA:68:E6:A5:48:CC:D8:2B:E8:42:B2:BF:7F:BE:45:66:68"
  authority_key_id: "E7:AB:9F:0F:2C:33:A0:53:D3:5E:4F:78:C8:B2:84:0E:3B:D6:92:33"
  crl_distribution: "http://r13.c.lencr.org/12.crl"
  ocsp_stapling: false
ct_logs:
  - log_id: "94:4E:43:87:..."
    timestamp: "2026-04-13T12:02:57.320Z"
  - log_id: "46:AF:86:3D:..."
    timestamp: "2026-04-13T12:02:57.529Z"
serial_number: "06:ef:fc:49:10:2e:c7:1f:19:d3:39:0b:b7:16:bb:07:3c:0b"
version: 3
```

---

## Test Results

### PASS — Things That Work

| Test | Result |
|------|--------|
| `whoassassinatedcharliekirk.com` HTTPS connection | ✅ PASS |
| TLS handshake (apex domain) | ✅ PASS — TLS 1.3 |
| Certificate chain verification (apex) | ✅ PASS — `verify return code: 0 (ok)` |
| Let's Encrypt cert valid (apex) | ✅ PASS — 88 days remaining |
| HTTP → HTTPS redirect | ✅ PASS — 301 from GitHub.com |
| TLS 1.2 support | ✅ PASS — ECDHE-RSA-CHACHA20-POLY1305 |
| TLS 1.3 support | ✅ PASS — TLS_AES_128_GCM_SHA256 |
| All cipher suites | ✅ PASS — All rated A (nmap ssl-enum-ciphers) |
| Certificate chain complete (2 intermediates) | ✅ PASS |
| CT (Certificate Transparency) logs | ✅ PASS — 2 logs present |
| Page loads over HTTPS | ✅ PASS — HTTP/2 200 OK |
| CNAME in build output | ✅ PASS — `site/build/CNAME` = `whoassassinatedcharliekirk.com` |
| DNS A records resolve to GitHub CDN | ✅ PASS — all 4 IPs confirmed |

### FAIL — Things That Are Broken

| Test | Result |
|------|--------|
| `www.whoassassinatedcharliekirk.com` HTTPS | ❌ FAIL — cert mismatch |
| SAN covers www subdomain | ❌ FAIL — `www.` NOT in cert SAN |
| www cert valid | ❌ FAIL — GitHub serves `*.github.io` cert, which does NOT cover `www.whoassassinatedcharliekirk.com` |
| OCSP stapling | ❌ FAIL — `OCSP responses: no responses sent` (GitHub Pages limitation) |
| HSTS header | ❌ MISSING — no `Strict-Transport-Security` header served |
| CAA records | ⚠️ MISSING — any CA can issue certs for this domain (not critical but a best-practice gap) |

### www Subdomain Cert Error (exact output)

```
subject: CN=*.github.io
subjectAltName does not match host name www.whoassassinatedcharliekirk.com
SSL: no alternative certificate subject name matches target host name 'www.whoassassinatedcharliekirk.com'
```

GitHub Pages serves its own `*.github.io` wildcard cert when the custom domain cert doesn't cover the requested SNI. That wildcard covers `*.github.io` hosts, not your custom domain.

---

## Deployment Architecture (Current)

```
Browser request to www.whoassassinatedcharliekirk.com
  → DNS CNAME → act3ai.github.io
  → resolves to 185.199.x.x (GitHub Pages CDN)
  → GitHub Pages serves *.github.io cert  ← WRONG CERT, causes error
  → cert says CN=*.github.io, SAN has no www.whoassassinatedcharliekirk.com
  → Browser/client rejects with cert mismatch
```

```
Browser request to whoassassinatedcharliekirk.com (apex, no www)
  → DNS A records → 185.199.x.x (GitHub Pages CDN)
  → GitHub Pages serves correct Let's Encrypt cert
  → cert says CN=whoassassinatedcharliekirk.com, SAN matches
  → TLS 1.3 handshake succeeds, page loads
```

---

## Five Paths to Fix

### Fix 1 — Remove the www CNAME from DNS (Quickest, 5 minutes)

**What:** Delete the `CNAME www → act3ai.github.io` record from your DNS provider.

**Why it works:** If `www.whoassassinatedcharliekirk.com` doesn't resolve, browsers can't reach it, so there's no cert error. Anyone who types `www.` gets NXDOMAIN (domain not found) instead of a cert error — a much cleaner failure.

**Downside:** `www.` stops working entirely instead of redirecting to the apex.

**Steps:**
1. Log in to your DNS provider (where `whoassassinatedcharliekirk.com` is registered/hosted).
2. Delete the `www CNAME → act3ai.github.io` record.
3. Done. Propagates in minutes to hours.

---

### Fix 2 — GitHub Pages: Set Both apex + www as Custom Domain (Free, Recommended)

**What:** GitHub Pages can provision a Let's Encrypt cert that covers both `whoassassinatedcharliekirk.com` AND `www.whoassassinatedcharliekirk.com` if you configure it correctly in the repo settings.

**Why it works:** When GitHub Pages detects both apex A records and a `www CNAME → [org].github.io`, it issues a cert with both SANs.

**Steps:**
1. Go to https://github.com/ACT3ai/charlie-kirk/settings/pages
2. Under "Custom domain", ensure it's set to `whoassassinatedcharliekirk.com` (apex, no www).
3. Check "Enforce HTTPS" — GitHub will provision/renew the cert automatically.
4. In your DNS, confirm the www CNAME points to `act3ai.github.io` AND the apex has the 4 GitHub A records.
5. GitHub should automatically issue a cert covering both apex and www when both DNS records point correctly.
6. If it doesn't auto-issue, clear the custom domain field, save, re-enter it, and save again to force re-provisioning.

**Note:** The CNAME file in `site/build/CNAME` already contains `whoassassinatedcharliekirk.com` — this is correct and tells GitHub Pages which custom domain to use.

---

### Fix 3 — Cloudflare Proxy (Free, Adds DDoS Protection + HSTS)

**What:** Move DNS to Cloudflare (free tier), enable the orange-cloud proxy. Cloudflare issues its own Universal SSL cert covering both apex and www automatically, and handles the www → apex redirect with a Page Rule.

**Why it works:** Cloudflare's Universal SSL covers `whoassassinatedcharliekirk.com` and `www.whoassassinatedcharliekirk.com` out of the box for free, with no GitHub Pages involvement.

**Steps:**
1. Add site to Cloudflare (free tier at cloudflare.com).
2. Import existing DNS records — Cloudflare auto-imports them.
3. Enable the orange cloud (proxy) on both the apex A records and the www CNAME.
4. In SSL/TLS settings → set mode to "Full" (since GitHub Pages handles its own cert).
5. Add a Page Rule: `www.whoassassinatedcharliekirk.com/*` → Forwarding URL (301) → `https://whoassassinatedcharliekirk.com/$1`.
6. Enable HSTS in Cloudflare's SSL → Edge Certificates → HSTS.
7. Update nameservers at your registrar to Cloudflare's nameservers.

**Bonus:** Fixes HSTS gap, adds CDN caching, DDoS protection, and analytics.

---

### Fix 4 — AWS Certificate Manager + CloudFront (Most Robust, User Has AWS Access)

**What:** Use AWS ACM to issue a cert covering both apex and www, then serve the site through CloudFront pointing to GitHub Pages as the origin. CloudFront terminates TLS with your ACM cert.

**Why it works:** ACM certs cover whatever domains you specify (wildcard or multi-SAN). CloudFront handles HTTPS termination before traffic ever hits GitHub Pages.

**Steps:**
1. Request ACM cert (must be in us-east-1 for CloudFront):
   ```bash
   aws acm request-certificate \
     --domain-name whoassassinatedcharliekirk.com \
     --subject-alternative-names www.whoassassinatedcharliekirk.com \
     --validation-method DNS \
     --region us-east-1
   ```
2. Add the CNAME validation records ACM gives you to your DNS.
3. Wait for ACM to validate (usually under 5 minutes with DNS validation).
4. Create a CloudFront distribution:
   - Origin: `whoassassinatedcharliekirk.com` (GitHub Pages) on port 443
   - Alternate domain names (CNAMEs): `whoassassinatedcharliekirk.com`, `www.whoassassinatedcharliekirk.com`
   - SSL certificate: select the ACM cert you just created
   - Redirect HTTP to HTTPS: yes
5. Add a second origin behavior to redirect www → apex (or handle with CloudFront Function).
6. Update DNS:
   - Apex: ALIAS or CNAME to `d*.cloudfront.net` (your distribution domain)
   - www: CNAME to `d*.cloudfront.net`
7. Remove the GitHub Pages A records from DNS apex (CloudFront becomes the entry point).

**Cost:** CloudFront free tier covers 1TB/month and 10M requests — likely free or near-free for this site.

---

### Fix 5 — certbot DNS Challenge + Self-Hosted Cert Upload to Cloudflare (Manual Override)

**What:** Use certbot with the DNS-01 challenge to manually generate a wildcard or multi-SAN cert, then upload it to Cloudflare (or another proxy) as a Custom Certificate. This bypasses GitHub Pages cert provisioning entirely.

**Why it works:** You control the cert and upload it wherever you want — Cloudflare accepts custom uploaded certs on Business+ plans, but you can also use this cert with any other proxy.

**Steps:**
```bash
# Install certbot
brew install certbot

# Generate cert with DNS challenge (no server needed)
sudo certbot certonly \
  --manual \
  --preferred-challenges dns \
  -d whoassassinatedcharliekirk.com \
  -d www.whoassassinatedcharliekirk.com

# certbot will prompt you to add a TXT record to your DNS
# Add _acme-challenge.whoassassinatedcharliekirk.com TXT = [provided value]
# Then press Enter to complete validation

# Cert files will be at:
# /etc/letsencrypt/live/whoassassinatedcharliekirk.com/fullchain.pem
# /etc/letsencrypt/live/whoassassinatedcharliekirk.com/privkey.pem
```

**Downside:** Cert expires every 90 days and renewal is manual unless you automate the DNS challenge (requires a DNS provider with API access and the appropriate certbot plugin).

---

## Recommended Path

**Fastest fix right now:** Fix 2 (verify GitHub Pages settings and force cert re-provisioning). This costs nothing and uses infrastructure already in place.

**If Fix 2 doesn't resolve it within 24 hours:** Fix 3 (Cloudflare) — free, permanent, and adds HSTS and CDN.

**If you want maximum control and you're already in AWS:** Fix 4 (ACM + CloudFront) — the most robust solution, gives you full cert control and doesn't depend on GitHub's cert provisioning at all.

---

## Additional Hardening Recommendations (Once Cert is Fixed)

- **Add HSTS header** — No `Strict-Transport-Security` header is currently served. GitHub Pages doesn't allow custom headers; this requires Cloudflare or CloudFront.
- **Add CAA records** — Restrict cert issuance to Let's Encrypt only:
  ```
  whoassassinatedcharliekirk.com  CAA  0 issue "letsencrypt.org"
  whoassassinatedcharliekirk.com  CAA  0 issuewild ";"
  ```
- **OCSP stapling** — Not available on GitHub Pages. Cloudflare and CloudFront both support it.
