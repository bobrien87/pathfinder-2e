---
type: deity
source-type: "Remaster"
domains: "Change, Earth, Fire, Water"
favored-weapon: "Club"
divine-font: "Harm, Heal"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Thunderstrike]], Rank 4: [[Dinosaur Form]], Rank 6: [[Elemental Confluence]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Some things are constantly changing, and Valani teaches that an island is the greatest example of major changes. An island can be born from nothing, rising up from boiling waters. Over time, the hardened volcanic rock transforms into an island full of life. A powerful storm or more volcanic activity can wipe away all this life, leaving the island again bare for new change and transformation. Valani teaches embracing these changes and taking them in stride. The only way to find joy is to take each moment for what it is, and embrace all the changes that come. Valani holds great power over natural forces like storms and especially volcanoes. As such, he sees worship from druids, elementalists, and people living on islands vulnerable to major changes from such primal forces.

**Title** The Fireshaker

**Areas of Concern** Change, growth, primal forces, volcanic islands

**Edicts** Encourage change for the sake of rebirth, respect the power of the elements, focus on your own self growth

**Anathema** Refuse to accept changes in yourself or others, repress you own anger or laughter, use the forces of nature for wanton destruction

**Religious Symbol** volcano with gold lava

**Sacred Animal** dinosaur

**Sacred Colors** brown, gold

**Source:** `= this.source` (`= this.source-type`)
