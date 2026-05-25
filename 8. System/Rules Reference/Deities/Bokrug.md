---
type: deity
source-type: "Remaster"
domains: "Destruction, Dreams, Water, Wealth"
favored-weapon: "Ranseur"
divine-font: "Harm, Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Hydraulic Push]], Rank 5: [[Control Water]], Rank 9: [[Wrathful Storm]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Silently dwelling beneath the surface of a nameless lake within a far-flung corner of the Dreamlands, Bokrug was once the patron deity of an ancestry known only as the beings of Ib—amphibious humanoids with froglike features—but the incursion of humans upon their domain resulted in the total extermination of this shoreside civilization. Shades of these creatures still haunt that area.

**Title** The Water Lizard

**Areas of Concern** Revenge, storms, water

**Edicts** Spread Bokrug's faith into the waking world, offer blood sacrifices to Bokrug

**Anathema** None

**Religious Symbol** green lizard with a long, coiled tail

**Sacred Animal** none

**Sacred Colors** blue, green

**Source:** `= this.source` (`= this.source-type`)
