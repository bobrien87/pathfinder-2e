---
type: deity
source-type: "Remaster"
domains: "Ambition, Might, Pain, Tyranny"
favored-weapon: "Flail"
divine-font: "Harm"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Fleet Step]], Rank 2: [[Shatter]], Rank 8: [[Monstrosity Form]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Hadregash, the foremost goblin creator-god, is often depicted as a barghest with muscles rippling under his smoke-colored fur. Known to be the strongest and mightiest among the four creator-gods, he instills the idea that in numbers there is strength, and strength equals power. Many goblinoids follow his creed and rulership by creating allegiances within the different tribes and paying as much respect as possible to the chain of command. Hobgoblins hold Hadregash in the highest regard, using his teachings as their founding principles: work in numbers; strategically plan your next ambush to harm enemies as little as possible, taking the greatest number of individuals as prisoners; and rule all lands with an iron fist.

The Greatest Supreme Chieftain Boss accepts many kinds of offerings from his followers (blood sacrifices being his favorite). Powerful weapons must be a close second, as he sends his most capable followers to retrieve these offerings from altars and use them in combat. Hadregash rarely sees worship among non-goblinoids, except in the case of cruel tyrants and similarly minded individuals.

**Title** Greatest Supreme Chieftain Boss

**Areas of Concern** Conquest, invasion, war

**Edicts** Conquer everything you see, rule with an iron fist, fight tactically

**Anathema** Bow before others, let others control your actions, permit insubordination

**Religious Symbol** chain and manacle

**Sacred Animal** cougar

**Sacred Colors** green, red

**Source:** `= this.source` (`= this.source-type`)
