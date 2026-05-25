---
type: deity
source-type: "Remaster"
domains: "Healing, Nature, Perfection, Wood"
favored-weapon: "Scythe"
divine-font: "Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Endure]], Rank 2: [[Entangling Flora]], Rank 6: [[Tangling Creepers]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Uncorrupted wildlife was rare in the land of Sarkoris during the time of the Worldwound, found only in the most remote regions farthest from the demonic incursion. Now that the hordes of demons have been pushed back, worshippers of Immaculate Growth encourage the natural world to reclaim the once-blighted terrain. This covenant nurtures newgrowth forest springing up around the fringes of the Shudderwood and bolsters valiant farmers clearing arable land near new settlements. Scouting and raiding parties that head deep into the Sarkoris Scar often seek out followers of Immaculate Growth to join their bands, as few people are so skilled at determining whether a campsite is threatened by hostile surroundings. Though the covenant is most popular along the fringes of the Sarkoris Scar, some followers have brought the faith back into Mendev, and a small group of worshippers have traveled to the Gravelands, hoping to ally with the surviving Knights of Lastwall to reclaim the land and study the unnatural growth around the ruins of Gallowspire.

**Covenant Members** cunning spirit guides, dryads, powerful leshies, wood elementals

**Areas of Concern** cleanliness, propagation, vegetation

**Edicts** clear away dead vegetation, foster wild plant life, protect natural areas

**Anathema** allow blight to spread, enable the destruction of wilderness areas

**Religious Symbol** blossoming tree

**Source:** `= this.source` (`= this.source-type`)
