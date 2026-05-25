---
type: deity
source-type: "Remaster"
domains: "Ambition, Luck, Secrecy, Trickery"
favored-weapon: "Hatchet"
divine-font: "Heal"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Illusory Disguise]], Rank 4: [[Honeyed Words]], Rank 5: [[Subconscious Suggestion]]"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** Brother Guile

**Areas of Concern** Cunning, schemes, trickery

**Edicts** Participate in pranks, seek trickery as a solution to a fight, draw mazes or sketch trap schematics

**Anathema** Insult another for attempting to trick you, reveal how a feat of legerdemain is performed, rush another person's plotting

**Religious Symbol** Circular maze

**Sacred Animal** Magpie

**Sacred Colors** Orange, white

**Source:** `= this.source` (`= this.source-type`)
