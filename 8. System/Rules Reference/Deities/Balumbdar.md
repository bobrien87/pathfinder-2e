---
type: deity
source-type: "Remaster"
domains: "Might, Nature, Perfection, Protection"
favored-weapon: "Greatclub"
divine-font: "Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Ant Haul]], Rank 2: [[Enlarge]], Rank 4: [[Dinosaur Form]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Balumbdar, or He Who Is Massive, is the god of all huge things in the world that tower over smaller things. Creatures of great size, such as elephants and dinosaurs, are sacred to him, as are natural features that dominate the landscape like mountains and massive trees. Balumbdar is also a god of strength, but of might born of great size rather than training or skill. Balumbdar is considered brutish and dim-witted by most other gods, but the fact that he towers over them in any interaction means he always commands respect. When he bothers to manifest at all, it is as a startlingly large man with slabs of muscle and equally thick rolls of fat. He sometimes instead appears as a city-sized animal or as imposing clouds, heavy with rain and low to the ground.

**Title** The World-Shaker

**Areas of Concern** Great size, megafauna, strength

**Edicts** Grow as large as you can, shelter those smaller and weaker than you, tend large animals and megafauna

**Anathema** Accidentally injure others with your size, topple a massive natural monument, use magic to assume a form smaller than you are

**Religious Symbol** Mountain held in two hands

**Sacred Animal** megafauna

**Sacred Colors** brown, black

**Source:** `= this.source` (`= this.source-type`)
