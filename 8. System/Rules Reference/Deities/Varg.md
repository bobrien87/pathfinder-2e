---
type: deity
source-type: "Remaster"
domains: "Creation, Destruction, Knowledge, Toil"
favored-weapon: "Greataxe"
divine-font: "Harm"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Anticipate Peril]], Rank 4: [[Creation]], Rank 5: [[Impaling Spike]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Varg is another of the older orc deities and is said to be the first orc to learn how to forge blades. In life, Varg was a notably intelligent orc who focused exclusively on waging war. He recognized that the orcs' enemies were better equipped, better trained, and used better tactics in battle. He sought to learn these things, which allowed him to become a prestigious warlord. However, Varg's experience in combat was against other orcs. His overconfidence led him to lay "siege" to a walled city outside Belkzen. The siege didn't last long. In fact, Varg died quickly and his hold scattered.

**Title** The Iron Warrior

**Areas of Concern** Innovation, iron, tactics, technology, war

**Edicts** Use tactics rather than relying solely on brute force or overwhelming numbers, use siege engines for combat whenever possible, seek out new technology

**Anathema** Pursue technology for non-combat purposes, use machinery and other advanced technology outside of combat, keep advanced weaponry or battle tactics a secret from orcs

**Religious Symbol** crumbling, smoking tower

**Sacred Animal** wooly rhinoceros

**Sacred Colors** green, iron gray

**Source:** `= this.source` (`= this.source-type`)
