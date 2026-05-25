---
type: deity
source-type: "Remaster"
domains: "Destruction, Knowledge, Magic, Wyrmkin"
favored-weapon: "Whip"
divine-font: "Harm"
divine-skill: "Arcana"
divine-spells: "Rank 1: [[Share Lore]], Rank 2: [[Ghostly Carrier]], Rank 3: [[Hypercognition]], Rank 4: [[Reflective Scales]], Rank 5: [[Slither]], Rank 6: [[Never Mind]], Rank 7: [[Contingency]], Rank 8: [[Unrelenting Observation]], Rank 9: [[Detonate Magic]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Abraxas, the Master of the Final Incantation, is the demon lord of forbidden lore, magic, and snakes. Abraxas has an encyclopedic knowledge of magical formulas and destructive secrets, favoring those that inflict suffering and destruction. His Final Incantation is a word of power that can unravel the mightiest of spells and unmake even artifacts. He takes the form of a viperlegged humanoid with a fanged, deformed bird's head. Abraxas's cults are most prevalent in the Darklands of Golarion, but small circles devoted to him can be found in most major cities on the surface as well.

**Title** Master of the Final Incantation

**Areas of Concern** Forbidden lore, magic, snakes

**Edicts** Learn and hoard forbidden magic, steal secrets from others

**Anathema** Destroy forbidden lore, reveal the entirety of a secret

**Religious Symbol** demonic face and snakes

**Sacred Animal** snake

**Sacred Colors** green, orange

**Source:** `= this.source` (`= this.source-type`)
