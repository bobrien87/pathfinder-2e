---
type: deity
source-type: "Remaster"
domains: "Fire, Nature, Sun, Time"
favored-weapon: "Spear"
divine-font: "Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Breathe Fire]], Rank 2: [[Floating Flame]], Rank 3: [[Threefold Aspect]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** King of the Heavens

**Areas of Concern** Creation, rulership, the sun

**Edicts** Bring order to places of chaos, kill evil monsters and fiends, encourage just laws, provide warmth where needed

**Anathema** Avoid personal change, kill a plant or a creature with cold damage, seal a building to completely block sunlight

**Religious Symbol** solar disk

**Sacred Animal** falcon

**Sacred Colors** red, gold

**Source:** `= this.source` (`= this.source-type`)
