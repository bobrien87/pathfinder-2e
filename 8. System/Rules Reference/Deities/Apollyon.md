---
type: deity
source-type: "Remaster"
domains: "Air, Decay, Plague, Swarm"
favored-weapon: "Scythe"
divine-font: "Harm"
divine-skill: "Medicine"
divine-spells: "Rank 1: [[Goblin Pox]], Rank 2: [[Vomit Swarm]], Rank 5: [[Toxic Cloud]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The Prince of Plagues seized power for himself after the disappearance of the previous Rider of Pestilence by obsessively eliminating all potential rivals. Apollyon commands his vast army of leukodaemons to spread oblivion like a virus. He wastes no time on trivial acts of violence and lacks the patience to wait for longterm schemes to come to fruition. Instead, his plagues carry oblivion through cities like lightning, decimating entire kingdoms in the span of a few days. His greatest creations have been diseases that corrupt the soul itself, ensuring that my Lady must send his victims to Abaddon once they've succumbed.

**Title** Prince of Plagues

**Areas of Concern** Pestilence

**Edicts** End all mortal life through disease and poison, cultivate diseased animals

**Anathema** Prevent plagues, bury or burn the dead

**Religious Symbol** diseased yellow scythe

**Sacred Animal** horse, rat

**Sacred Colors** white

**Source:** `= this.source` (`= this.source-type`)
