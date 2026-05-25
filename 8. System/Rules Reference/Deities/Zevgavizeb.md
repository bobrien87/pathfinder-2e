---
type: deity
source-type: "Remaster"
domains: "Destruction, Might, Nature, Wyrmkin"
favored-weapon: "Spiked-gauntlet"
divine-font: "Harm"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Pest Form]], Rank 4: [[Dinosaur Form]], Rank 8: [[Earthquake]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Zevgavizeb, the Glutton in the Dark, is the demon lord of caverns, reptiles, and xulgaths. He dwells at the center of a massive network of caverns called Gluttondark, filled with continually warring nations of reptilian creatures, along with other, more hideous subterranean creatures. He encourages these conflicts to cull the weakest of his followers and devours all life found within defeated nations as a price for failure. Largely concerned with these perpetual conflicts, Zevgavizeb seldom seeks to influence Golarion directly, though reptilian ancestries and xulgaths in particular routinely commit atrocities in his name.

**Title** The Glutton in the Dark

**Areas of Concern** Caverns, reptiles, xulgaths

**Edicts** Slaughter the cowardly, subjugate the weak

**Anathema** Favor stealth over shows of strength, eat cooked meat

**Religious Symbol** twisted, taloned tentacle

**Sacred Animal** dinosaur

**Sacred Colors** black, green

**Source:** `= this.source` (`= this.source-type`)
