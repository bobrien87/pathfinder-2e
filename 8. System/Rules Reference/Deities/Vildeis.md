---
type: deity
source-type: "Remaster"
domains: "Duty, Pain, Sorrow, Zeal"
favored-weapon: "Dagger"
divine-font: "Harm, Heal"
divine-skill: "Medicine"
divine-spells: "Rank 1: [[Phantom Pain]], Rank 2: [[Slough Skin]], Rank 5: [[Synaptic Pulse]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The Cardinal Martyr presides over devotion, sacrifice, and scars. Vildeis is driven entirely by her abhorrence for evil. Evil should not and must not be allowed to exist. It should be fought without pause and without rest until it is completely and utterly destroyed. Not only does the fight never end, but every sacrifice that needs to be made to end evil must be made, and is worth making. There are no material rewards to be had for destroying evil—its destruction is all the reward necessary, and that reward can be enjoyed only once there is no more evil. Scars are the marks the fight leaves behind, the memory of all the sacrifices made. Vildeis expects total commitment from her followers, who leave everything behind and dedicate their lives to destroying all that is vile.

**Title** The Cardinal Martyr

**Areas of Concern** Devotion, sacrifice, scars

**Edicts** Sacrifice yourself in pursuit of good, champion noble causes, scar your body

**Anathema** Joke or laugh about injustice, sacrifice others in your place, indulge in luxury

**Religious Symbol** scarred gold breastplate

**Sacred Animal** eagle

**Sacred Colors** red, white

**Source:** `= this.source` (`= this.source-type`)
