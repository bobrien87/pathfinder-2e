---
type: deity
source-type: "Remaster"
domains: "Confidence, Glyph, Knowledge, Secrecy"
favored-weapon: "Longsword"
divine-font: "Harm"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Mindlink]], Rank 3: [[Distracting Chatter]], Rank 5: [[Subconscious Suggestion]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Upon the backs of all beholden to him, Titivilus scratches the record of Hell with long claws. His is a slender form, almost like a human man stretched well beyond his typical proportions, with skin the color of the deep purples of a sunset. Nine hands, each with nine fingers, transcribe every word spoken within the rings in illustrious longhand and great detail, down to the tones and rhythms. Steel is a crude tool for change; the Scrivening Count would crumble empires with but a whisper. A spear and shield may break a body, but lies, propaganda, rhetoric, and truth manipulate the hearts and minds that drive the hands.

**Title** The Scrivener

**Areas of Concern** Lies, propaganda, rhetoric, truth

**Edicts** Quote people back to themselves, chronicle the times you live in, skew the truth to your purpose

**Anathema** Allow a rumor to go unchallenged, destroy records, trust in memory alone

**Religious Symbol** devil hand writing

**Sacred Animal** viper

**Sacred Colors** black, white

**Source:** `= this.source` (`= this.source-type`)
