---
type: deity
source-type: "Remaster"
domains: "Change, Creation, Glyph, Might"
favored-weapon: "Longsword"
divine-font: "Harm"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Liberating Command]], Rank 3: [[Clairaudience]], Rank 5: [[Synaptic Pulse]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Nameless is a whisper in the mind, a shadow in the corner of one's eye, or a sudden noise with no source. They despise all creatures that dare claim sovereignty over others and work to bring down all who rule. Both righteous and the wicked figures of authority are targets for Nameless and their followers. One might point out the hypocrisy of Upon an Empty Throne's own rise to power, but the tormentor's wrath is reserved for those who actively seek positions of authority, and they claim their divinity came unbidden to them.

**Title** Upon an Empty Throne

**Areas of Concern** Delusions of authority, doubt, torment

**Edicts** Crush the confident and arrogant, incite rebellion against just and unjust rulers alike, sow doubt from the shadows

**Anathema** Hold a position of authority for more than a day, seek power for any reason but destroying those in power

**Religious Symbol** broken crown on an empty stone throne

**Sacred Animal** worm

**Sacred Colors** black, gold, gray

**Source:** `= this.source` (`= this.source-type`)
