---
type: deity
source-type: "Remaster"
domains: "Darkness, Destruction, Earth, Fire"
favored-weapon: "Greatpick"
divine-font: "Harm"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Shockwave]], Rank 2: [[Ash Cloud]], Rank 7: [[Volcanic Eruption]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Imprisoned under the colossal peak of Mhar Massif following a botched attempt to burrow into the Universe, the World Thunder is a mysterious Great Old One commanding the elements of earth and fire. Though the primordial flames of Golarion's core suspend the god in a sleep-like trance, its cult believes that tectonic activity—both natural events and those created by Mhar's more powerful priests—will one day emancipate their destructive master, ushering in an age of fire and ash that will consume Golarion. Icons created in veneration of Mhar depict a towering mountain of jagged stone, with great falls of lava pouring from its ashwreathed summit and clawed crystalline limbs reaching out in every direction from its base. Whether this is Mhar's true form remains a mystery to mortals, however, as every world Mhar has previously manifested within was invariably destroyed once the heat of its core could no longer keep it from stirring.

**Title** The World Thunder

**Areas of Concern** Caverns, mountains, volcanoes

**Edicts** Cause tectonic disasters, destroy objects and creatures using fire

**Anathema** None

**Religious Symbol** shattered triangular rune

**Sacred Animal** none

**Sacred Colors** black, orange

**Source:** `= this.source` (`= this.source-type`)
