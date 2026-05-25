---
type: deity
source-type: "Remaster"
domains: "Cold, Earth, Indulgence, Water"
favored-weapon: "Spear"
divine-font: "Harm"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Shockwave]], Rank 3: [[Bottomless Stomach]], Rank 5: [[Control Water]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The first spawn to rise from the frigid, oily fluid that flows through the Land of Black Blood deep in the Darklands, Orgesh is the ravenous but cunning Great Old One of hunger and alchemy. It quickly outgrew its fellow children of the Black Blood, the charda, and departed without warning to pursue greater ambitions elsewhere in the Darklands. Nonetheless, many charda continue to worship their wayward ancestor, though just as many curse its name for what they perceive as abandonment in favor of a new kindred found deep within the darkness of the Sightless Sea. The Faceless God's true form is that of a malformed humanoid with overlong clawed legs that stretch out from a grossly swollen belly, its head completely featureless except for a maw that hangs open to reveal countless serrated teeth.

**Title** The Faceless God

**Areas of Concern** Alchemy, caverns, hunger, subterranean waterways

**Edicts** Surpass your peers in your chosen field at any cost, travel using subterranean waterways, use blood and toxic metals in alchemy

**Anathema** None

**Religious Symbol** open maw surrounding a rune

**Sacred Animal** none

**Sacred Colors** black, blue

**Source:** `= this.source` (`= this.source-type`)
