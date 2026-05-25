---
type: deity
source-type: "Remaster"
domains: "Confidence, Might, Truth, Zeal"
favored-weapon: "Longsword"
divine-font: "Heal"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Sure Strike]], Rank 2: [[Enlarge]], Rank 4: [[Fire Shield]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Most recent of the once-mortal gods to ascend to prominence via the Starstone, Iomedae represents honor, justice, rulership, and valor. Called the Light of the Sword by some, the goddess attracts the worship of those who seek to drive back villainy, chaos, and wickedness. Iomedae focuses on supporting benevolent order for the virtuous and meting out merciful justice to the selfish, tyrannical, and destructive. While she and her followers would rather convince the errant to change their ways with words or generous deeds, they don't falter when they strike at the hearts of the unrepentant, the allies of fiends, and those who pay lip service to the "greater good" while committing despicable acts. Iomedae is the patron of choice for those who wish to take an active hand in the battle to protect the innocent and punish the guilty.

**Title** The Inheritor

**Areas of Concern** honor, justice, rulership, valor

**Edicts** be temperate, fight for justice and honor, hold valor in your heart

**Anathema** abandon a companion in need, dishonor yourself, refuse a challenge from an equal

**Religious Symbol** sword and sun

**Sacred Animal** lion

**Sacred Colors** red, white

**Source:** `= this.source` (`= this.source-type`)
