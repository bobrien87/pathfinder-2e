---
type: deity
source-type: "Remaster"
domains: "Cold, Darkness, Sorrow, Star"
favored-weapon: "Sling"
divine-font: "Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Dizzying Colors]], Rank 5: [[Cloak Of Colors]], Rank 6: [[Teleport]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Dancing through the northern sky, the Shimmering Maiden represents constellations, homesickness, and the northern lights. Pulura understands that the constellations are the guide with which mortals navigate their world, lighting the way so that those who travel or explore can always find their way home. The stories of the constellations not only entertain with tales of goodness and light and strength, but they are also a tool for helping others learn and remember the stars. This ensures that the map in the sky is easy to read and never forgotten. To learn this map and to guide those who are lost or otherwise in need of direction are exceptional callings, but even more so is to teach a petitioner to navigate the skies themself on the journey.

**Title** The Shimmering Maiden

**Areas of Concern** Constellations, homesickness, northern lights

**Edicts** Aid travelers, comfort the lonely, teach the constellations

**Anathema** Mock the homesick, deny warmth to others, pollute the skies with smoke or light

**Religious Symbol** face in northern lights

**Sacred Animal** firefly

**Sacred Colors** midnight blue

**Source:** `= this.source` (`= this.source-type`)
