# OGM Tile - Krav

## Status

Proposal drafting phase. Pair writing to create fundable project description. 

### Update 2021-10-26

[[Zapier]] has a Zoom-YouTube integration, which will watch for a new Zoom recording and post it to YouTube, unlisted.  Control of the metadata is okay but not great.  May or may not be useful.

[[Google Sites]] apparently doesn't have an API for sites created on or after November 22, 2016: [Google Sites API](https://developers.google.com/sites)

[Zoom API](https://marketplace.zoom.us/docs/api-reference/zoom-api/cloud-recording/) looks good.

[YouTube Data API](https://developers.google.com/youtube/v3) looks okay, probably a little hard to use.  Quota limits will not allow more than 6 uploads per day, perhaps fewer. (See notes below for adasq/youtube-studio, it says it works around the quota.)

Anchor.fm doesn't have an API, but someone kludged together a [Puppeteer script to do Anchor.fm uploads](https://github.com/Schrodinger-Hat/youtube-to-anchorfm/blob/main/upload-episode.js).

Need more information:

- which speech transcription service to use?
- define episode metadata
- what to do about Google Sites not having an API?
- should the script (or a separate script) move Zoom artifacts to trash?

#### Export from Descript

- Buzzsprout
- Captivate
- Castos
- eWebinar
- Headliner
- Hello Audio
- Podcast.co
- Restream
- Transistor
- VideoAsk
- Wistia

## Roles and Responsibilities

### Sponsor

Jerry

### Project Manager

TBD 

### Lead

Pete

### Team

Pete & TBD

## Goals

Automate process of turning fresh episode's raw files into more usable production artifacts. Raw files include video, audio and text. We know this project is done when it measurably improves the process of publishing calls, getting as close to full automation as practicable now.

Inputs:

- call recording artifacts (mp4, m4a, txt) in Zoom account

Outputs:

- video and episode metadata goes to YouTube Studio
- audio and episode metadata goes to Anchor.fm
- audio gets machine transcribed via one of Otter, AWS, GCP, Descript, etc. Highly desired to identify speakers by zoom name.
- transcript, zoom chat, and call metadata go to the episode web page (web hosted on Google Sites)

For parts that are not practicably automatable in this phase, create a text or markdown or Google Keep checklist for a human to finish.

## Resource Requirements

_what (people, money, things) are needed to accomplish this project? where do they come from?_

## People

_who are the people working on this project? who can I ask for more information? how can I best get in touch with them?_

## Approach

1. Define the desired workflow, including specific kinds of raw files and production artifacts.
2. Choose hypothetical solutions for each part of the workflow.
3. Test hypotheses.
4. Build system, starting with long tentpoles.
5. Integrate and create production pipeline.
6. Create user and technical documentation.
7. Document future potential enhancements and fixes.

Build and use open source components.  Built components, integration, and documentation will be made open source.

Build project in Python.  Maybe use serverless (e.g., AWS Lambda) for some/all deployments.

Interview project team afterwards for a WtW episode.

### Notes

- need/able to use https://github.com/adasq/youtube-studio ?

## Workplan and Timeline

_what are the specific tasks needed to accomplish our goals? when might they happen? who / what / when?_

## Communication Norms

_how have the project participants agreed to stay in touch? what, where and how often are regular meetings? special ceremonies?_

