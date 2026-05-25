---
type: deity
source-type: "Remaster"
domains: "Destruction, Metal, Star, Sun"
favored-weapon: "Alchemical-bomb"
divine-font: "Harm, Heal"
divine-skill: "Crafting"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The building blocks of the mortal Universe were forged within suns, each element in reality created within the burning furnace of their cores. Almost all life in the Universe still depends on these suns, with both animals and plants nourished by the life-giving energy of these blazing spheres. Yet these gifts are granted by the slow death of the stars, their eons-long immolation finally ending in an explosive nova and a collapse into a black hole. Inna, the Death of Stars, is the poison that lurks in the heart of these doomed suns, the slow murder of these celestial bodies that facilitates all other life. This gift does not come without a price: the death throes of these cosmic giants offer an [[Invisible]], radioactive death to those who come too close.

**Title** The Death of Stars

**Areas of Concern** Black holes, energy, radiation, stars

**Edicts** Create using heat or fire, sacrifice yourself to achieve your goals, destroy objects when their purpose is done, rescue creatures from doomed planets

**Anathema** Douse ashes with water instead of letting them burn out, bury a body instead of cremating it, curse the sun

**Religious Symbol** blindingly bright star

**Sacred Animal** all

**Sacred Colors** red, white, yellow

**Source:** `= this.source` (`= this.source-type`)
