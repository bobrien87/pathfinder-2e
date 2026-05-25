---
type: deity
source-type: "Remaster"
domains: "Duty, Earth, Protection, Vigil"
favored-weapon: "Claw, Shield-boss"
divine-font: "Harm, Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Anticipate Peril]], Rank 3: [[Cozy Cabin]], Rank 6: [[Wall Of Force]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

As crusaders, naturalists, and descendants of Old Sarkoris struggle to reclaim the demon-haunted lands of what was the Worldwound, they turn to the Boundary of Strength for divine assistance in holding their territorial gains. The densest concentration of this covenant's worshippers resides in the town of Gundrun, the only stable settlement during the demonic occupation. Generally practical people, devotees care less about the nature of the Boundary of Strength than its effectiveness. This covenant is frequently invoked by night guards on patrol and those attempting to cleanse, salvage, or study the *wardstones* that remain scattered around the Sarkoris Scar.

**Covenant Members** Dolok Darkfur, Kagia, Stag Mother of the Forest of Stones, stone elementals

**Areas of Concern** boundaries, containment, guardianship

**Edicts** establish and protect your personal territory, punish trespassers, safeguard lawful visitors

**Anathema** abandon a guard post, cede territory to an invader

**Religious Symbol** stone wall

**Source:** `= this.source` (`= this.source-type`)
