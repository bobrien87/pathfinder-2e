---
type: deity
source-type: "Remaster"
domains: "Knowledge, Void, Passion, Trickery"
favored-weapon: "Spiked-chain"
divine-font: "Harm"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Charm]], Rank 3: [[Distracting Chatter]], Rank 5: [[Subconscious Suggestion]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Many an idealist with great hopes to change the world has had their dreams realized by meeting a handsome stranger on the road. Velgaas, who might be mistaken for a nagaji with his scaled skin and forked tongue, takes great care to learn their altruistic desires, then carefully plants the seeds of destruction into their kind hearts. Charities become cesspools of corruption, laboratories convert into dens of torture, and peaceful protests spiral into mob violence.

**Title** Minds in the Dark

**Areas of Concern** Emotional manipulation, emptiness, ignorance

**Edicts** Be sweet with lies and cruel with truths, corrupt the good intentions of others, master the art of manipulation

**Anathema** Be obvious with your lies, reveal the truth without benefit

**Religious Symbol** black drops of poison trickling from an ear

**Sacred Animal** snake

**Sacred Colors** purple, red

**Source:** `= this.source` (`= this.source-type`)
