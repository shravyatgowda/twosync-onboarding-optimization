# Onboarding teardown: partner pairing

**Scope:** a couples app where the core experience only works once both partners have accounts and are linked ("paired"). "TwoSync" is a working name for the product used in this case study.

> **Note on evidence.** The baseline flow below is a structured hypothesis, not measured data. Replace the observations in section 2 with screenshots and notes from the app you tore down before using this in an interview.

## 1. The job of this screen

Get a new user's partner into the app, because an unpaired user has nothing to do. Every drop between registration and pairing is a user who has already shown intent and then hits a wall.

## 2. Baseline flow and friction hypotheses

| Step | What the user does | Likely friction | How we would check |
|---|---|---|---|
| 1. Register | Phone number + OTP | OTP delay, wrong number | OTP success rate, time to verify |
| 2. Invite screen | Reads instructions, chooses how to invite | Too many choices, unclear value of inviting now | Screen view to channel-selected rate |
| 3. Share | Share sheet opens, picks an app | Share sheet is a context switch; many users never return | channel-selected to invite_sent rate |
| 4. Partner opens link | Partner taps a message | Weak message copy, link looks like spam | invite_sent to invite_opened rate |
| 5. Partner installs and registers | Store install, OTP, profile | Longest step, most drop-off | invite_opened to partner_registered rate |
| 6. Pairing | Accounts link automatically or via code | Code entry errors | partner_registered to pairing_completed rate |

## 3. Where I would look first

The biggest absolute loss is almost always step 2 to 3: users who reach the invite screen and leave without sending anything. It is also the step the product fully controls, with no dependency on the partner's behavior. That makes it the right place for the first test.

## 4. Why bedtime matters

Couples tend to use this kind of product late in the evening. An invite sent at 11 PM often waits until the partner next opens the phone. A fast, one-tap invite that works inside the evening window reduces the chance the invite goes stale.

## 5. Proposed change

Replace the multi-option invite page with a single screen: one dominant "Send on WhatsApp" button, two quieter alternatives, a visible pairing code, and a live status after sending ("Invite sent", "Opened", "Paired"). Working prototype: `prototype/index.html`.

## 6. Open questions

- What share of invites are sent between 9 PM and midnight, and do they convert differently?
- Does a visible status after sending reduce users sending a second invite?
- Is the share sheet the biggest leak, or is it the partner's install step?
