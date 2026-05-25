---
type: deity
source-type: "Remaster"
domains: "Creation, Knowledge, Water, Wealth"
favored-weapon: "Sickle"
divine-font: "Harm"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Temporary Tool]], Rank 4: [[Creation]], Rank 5: [[Control Water]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The brains of the four goblin creator-gods, Zogmugot is a goddess with a baleful temper and obsessive temperament. Depictions of Lady Lastbreath show her as a barghest with sea-green fur. Always watching with her colorful sea-glass eyes, goblins risk much by gaining her attention. She dislikes being bothered by mortal petitioners, and if she decides that a goblin should have figured out a problem on their own, she is quick to unleash her wrath. Zogmugot is in charge of deciding whether a goblin drowns in water or is washed back ashore, and she viciously drowns her victims when she's in a bad mood. Most goblins ritually placate her for this reason, while followers desperate to get her attention go to the depths of the sea and attempt to drown themselves.

**Title** Lady Lastbreath

**Areas of Concern** Drowning, invention, self-sufficiency

**Edicts** Ply the sea, work fervently and without help, use what is given to you

**Anathema** Unnecessarily seek divine attention or guidance, disrespect the water, bury a piece of sea glass

**Religious Symbol** seaweed draped chest

**Sacred Animal** crab

**Sacred Colors** blue, brown

**Source:** `= this.source` (`= this.source-type`)
