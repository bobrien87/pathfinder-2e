---
type: deity
source-type: "Remaster"
domains: "Destruction, Nothingness, Star, Zeal"
favored-weapon: "Maul"
divine-font: "Harm"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Pummeling Rubble]], Rank 2: [[Acid Grip]], Rank 6: [[Disintegrate]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The Devourer is a new deity: an embodiment of ruin on a galactic scale, born from the acts of other deities in ages long past. Thanks to Gorum and Torag, a sliver of the deity Rovagug was bound inside Gorum's armor, turning the deity of war into an eternal prison for the Rough Beast. Inside Gorum, the sliver festered, changing and warping into something new. Following the events of the Godsrain and Gorum's demise, the sliver managed to escape its prison and ascend into the cosmos as its own being, the Devourer.

**Title** The Star-Eater

**Areas Of Concern** black holes, cosmic-scale destruction, supernovas

**Edicts** engage in acts of destruction, kill sentient beings, tear down civilizations

**Anathema** repair an object that won't inflict greater destruction; create new technology, magic, or life without a destructive purpose

**Religious Symbol** blood accretion (black hole tinged with red)

**Sacred Animal** none

**Sacred Colors** black, red

**Source:** `= this.source` (`= this.source-type`)
