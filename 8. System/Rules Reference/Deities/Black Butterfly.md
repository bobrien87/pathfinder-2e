---
type: deity
source-type: "Remaster"
domains: "Freedom, Secrecy, Star, Void"
favored-weapon: "Starknife"
divine-font: "Heal"
divine-skill: "Stealth"
divine-spells: "Rank 1: [[Penumbral Shroud]], Rank 2: [[Blur]], Rank 4: [[Flicker]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The Silence Between flutters among and between the stars, representing distance, silence, and space. Often called Desna's Shadow, the Black Butterfly is sometimes believed to be an aspect of Desna that has broken off and taken on its own life; her interest in distance and space certainly reflects Desna's love of travel. The Black Butterfly finds the silence of the sea of stars useful for introspection and learning about oneself. Those who follow her take opportunities when they can to sit in silent meditation, in zones of silence and darkness when possible. Travel across large distances offers plenty to think about and contemplate, and the Black Butterfly encourages such journeys. She hates all evil, but she truly despises the powerful beings of evil that populate the Dark Tapestry, and her followers are expected to fight these beings and their followers without mercy.

**Title** The Silence Between

**Areas of Concern** Distance, silence, space

**Edicts** Study the stars, notice moments of silence, perform anonymous acts of kindness

**Anathema** Disrupt another's meditation, interrupt tranquil moments, play noisy or discordant music

**Religious Symbol** black butterfly with star

**Sacred Animal** butterfly

**Sacred Colors** black, silver

**Source:** `= this.source` (`= this.source-type`)
